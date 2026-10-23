#!/usr/bin/env python3
"""Build the OpenAI (ChatGPT/Codex) plugin ZIP from this repo's shared skills.

Usage: python3 openai/build-zip.py --category "<dashboard category>" --demo-url <https url>
Writes dist/instabids-openai.zip. Refuses to build while any placeholder is unfilled,
so a ZIP can never ship with a fake video URL or category.
"""
import argparse, json, pathlib, sys, zipfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
OPENAI = ROOT / "openai"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--category", required=True)
    ap.add_argument("--demo-url", required=True)
    a = ap.parse_args()
    if not a.demo_url.startswith("https://"):
        sys.exit("demo url must be https")

    manifest = json.loads((OPENAI / "codex-plugin.json").read_text())
    cases = json.loads((OPENAI / "test-cases.json").read_text())
    if len(cases["positive"]) != 5 or len(cases["negative"]) != 3:
        sys.exit("OpenAI requires exactly 5 positive and 3 negative test cases")
    if "__" in json.dumps(cases):
        sys.exit("test-cases.json still has a placeholder")
    manifest["interface"]["category"] = a.category
    review = manifest["extensions"]["com.openai"]["review"]
    review["test_cases"] = cases
    review["demo_recording_url"] = a.demo_url
    text = json.dumps(manifest, indent=2) + "\n"
    if "__" in text:
        sys.exit("manifest still has a placeholder")

    dist = ROOT / "dist"
    dist.mkdir(exist_ok=True)
    out = dist / "instabids-openai.zip"
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr(".codex-plugin/plugin.json", text)
        z.write(OPENAI / "mcp.json", ".mcp.json")
        z.write(ROOT / "icon.png", "assets/icon.png")
        z.write(ROOT / "icon.png", "assets/logo.png")
        z.write(OPENAI / "README.md", "README.md")
        z.write(ROOT / "LICENSE", "LICENSE")
        for skill in sorted((ROOT / "skills").glob("*/SKILL.md")):
            z.write(skill, str(skill.relative_to(ROOT)))
    print(out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
