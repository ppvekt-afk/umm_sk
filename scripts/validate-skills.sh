#!/usr/bin/env bash
# Validate the whole repo: skill structure, frontmatter, evals, cross-references,
# pack manifest, and banned claim patterns. Run before every commit/PR; CI runs it too.
# Usage: ./scripts/validate-skills.sh
set -uo pipefail
cd "$(dirname "$0")/.."

FAIL=0
err() { echo "  ✗ $1"; FAIL=1; }

echo "1/7 Skill structure (SKILL.md + references/ + evals/evals.json per skill)"
for d in skills/*/; do
  n=$(basename "$d")
  [ -f "$d/SKILL.md" ] || err "$n: missing SKILL.md"
  [ -d "$d/references" ] || err "$n: missing references/"
  [ -f "$d/evals/evals.json" ] || err "$n: missing evals/evals.json"
done

echo "2/7 Frontmatter (name matches directory, description present)"
for d in skills/*/; do
  n=$(basename "$d")
  fm=$(awk '/^name:/{print $2; exit}' "$d/SKILL.md" 2>/dev/null)
  [ "$fm" = "$n" ] || err "$n: frontmatter name '$fm' != directory name"
  grep -q '^description:' "$d/SKILL.md" || err "$n: missing description"
done

echo "3/7 Evals are valid JSON"
for f in skills/*/evals/evals.json; do
  python3 -c "import json,sys; json.load(open(sys.argv[1]))" "$f" 2>/dev/null \
    || err "$f: invalid JSON"
done

echo "4/7 Cross-references resolve (every \`skill-name\` mention is a real skill)"
python3 - <<'EOF' || FAIL=1
import os, re, sys
# Backticked kebab-case terms that are NOT skill names (API fields, model ids, regions, packages).
ALLOW = {"platform-inputs", "gemini-3-pro-image", "lumaai-python", "x-goog-api-key",
         "asia-northeast1", "europe-west4", "us-central1", "us-east4"}
skills = {d for d in os.listdir("skills") if os.path.isdir(f"skills/{d}")}
pat = re.compile(r"`([a-z0-9]+(?:-[a-z0-9]+)+)`")
bad = []
roots = ["skills", "tools"]
for root in roots:
    for dirpath, _, files in os.walk(root):
        for f in files:
            if not f.endswith(".md"): continue
            p = os.path.join(dirpath, f)
            for m in pat.findall(open(p, encoding="utf-8").read()):
                if m not in skills and m not in ALLOW and not m.endswith(".md"):
                    bad.append(f"  ✗ {p}: unresolved reference `{m}`")
if bad:
    print("\n".join(sorted(set(bad)))); sys.exit(1)
EOF

echo "5/7 Plugin manifests (valid JSON, versions in sync)"
python3 - <<'EOF' || FAIL=1
import json, sys
try:
    p = json.load(open(".claude-plugin/plugin.json"))
    m = json.load(open(".claude-plugin/marketplace.json"))
except Exception as e:
    print(f"  ✗ plugin manifest invalid: {e}"); sys.exit(1)
if p["version"] != m["plugins"][0]["version"]:
    print(f"  ✗ version mismatch: plugin.json={p['version']} marketplace.json={m['plugins'][0]['version']}"
          " — plugin users won't see updates until these match"); sys.exit(1)
EOF

echo "6/7 Pack manifest (every pack skill exists; JSON valid)"
python3 - <<'EOF' || FAIL=1
import json, os, sys
m = json.load(open("scripts/packs.json"))
bad = [f"  ✗ pack '{p['name']}': missing skill '{s}'"
       for p in m["packs"] for s in p["skills"] if not os.path.isdir(f"skills/{s}")]
for p in m["packs"]:
    for key in ("name", "title", "description", "skills"):
        if key not in p: bad.append(f"  ✗ pack '{p.get('name','?')}': missing '{key}'")
if bad: print("\n".join(bad)); sys.exit(1)
EOF

echo "7/7 Banned patterns (claims the repo must never make)"
# WoopSocial has no analytics surface; skills must not AFFIRM it does.
# Negations ("no/not/without/never ... WoopSocial analytics") are the correct house phrasing.
# Whitespace is collapsed first so negations split across wrapped lines are still recognized.
python3 - <<'EOF' || FAIL=1
import os, re, sys
bad = []
for root in ("skills", "tools"):
    for dirpath, _, files in os.walk(root):
        for f in files:
            if not f.endswith(".md"): continue
            p = os.path.join(dirpath, f)
            text = re.sub(r"\s+", " ", open(p, encoding="utf-8").read())
            for m in re.finditer(r"WoopSocial analytics", text):
                ctx = text[max(0, m.start()-60):m.start()].lower()
                if not re.search(r"\b(no|not|never|without|nor)\b[^.]*$", ctx):
                    bad.append(f"  ✗ {p}: affirmative 'WoopSocial analytics' claim")
            if re.search(r"WoopSocial (publishes[^.]{0,80})?\+? ?(and )?reads native analytics", text):
                if "WoopSocial has none" not in text:
                    bad.append(f"  ✗ {p}: 'WoopSocial ... reads native analytics' phrasing")
if bad:
    print("\n".join(sorted(set(bad)))); sys.exit(1)
EOF
# No stale "(forthcoming)" markers for skills that ship in this repo.
hits=$(grep -rn "(forthcoming)" skills/ tools/ --include='*.md' 2>/dev/null | grep -v suno || true)
[ -z "$hits" ] || { echo "$hits"; err "found a stale (forthcoming) marker"; }

echo ""
if [ "$FAIL" -eq 0 ]; then
  echo "OK — $(ls -d skills/*/ | wc -l | tr -d ' ') skills validated."
else
  echo "FAILED — fix the issues above."
  exit 1
fi
