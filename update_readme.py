"""
update_readme.py
================
Automatically scans all .py solution files and updates README.md
Run locally or via GitHub Actions on every push.
"""

import os
import re

# ── Config ────────────────────────────────────────────────────────────────────

REPO_ROOT   = os.path.dirname(os.path.abspath(__file__))
README_PATH = os.path.join(REPO_ROOT, "README.md")

DIFFICULTY_DIRS = {
    "Easy":   "Easy Problem",
    "Medium": "Medium Problem",
    "Hard":   "Hard Problem",
}

CATEGORY_EMOJI = {
    "array":         "📦 Array",
    "binary search": "🔍 Binary Search",
    "linked list":   "🔗 Linked List",
    "math":          "🔢 Math",
    "stack":         "📚 Stack",
    "string":        "🔤 String",
    "tree":          "🌳 Tree",
    "graph":         "🕸️ Graph",
    "dp":            "🧩 Dynamic Programming",
    "greedy":        "💡 Greedy",
    "two pointers":  "👆 Two Pointers",
    "hash table":    "🗂️ Hash Table",
}

def get_emoji(category_folder: str) -> str:
    key = category_folder.lower()
    return CATEGORY_EMOJI.get(key, f"📂 {category_folder}")

def parse_file(filepath: str) -> dict:
    meta = {
        "number":   None,
        "title":    None,
        "approach": "—",
        "time":     "—",
        "space":    "—",
        "filepath": filepath,
    }
    filename = os.path.basename(filepath)
    match = re.match(r"^(\d+)\.\s+(.+)\.py$", filename)
    if match:
        meta["number"] = int(match.group(1))
        meta["title"]  = match.group(2)
    try:
        with open(filepath, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line.startswith("#"):
                    break
                if m := re.search(r"Approach\s*:\s*(.+)", line, re.I):
                    meta["approach"] = m.group(1).strip()
                elif m := re.search(r"Time\s*:\s*(.+)", line, re.I):
                    meta["time"] = m.group(1).strip()
                elif m := re.search(r"Space\s*:\s*(.+)", line, re.I):
                    meta["space"] = m.group(1).strip()
    except Exception:
        pass
    return meta

def scan_solutions() -> dict:
    results = {d: {} for d in DIFFICULTY_DIRS}
    for difficulty, folder in DIFFICULTY_DIRS.items():
        base = os.path.join(REPO_ROOT, folder)
        if not os.path.isdir(base):
            continue
        for category in sorted(os.listdir(base)):
            cat_path = os.path.join(base, category)
            if not os.path.isdir(cat_path):
                continue
            problems = []
            for fname in sorted(os.listdir(cat_path)):
                if not fname.endswith(".py"):
                    continue
                meta = parse_file(os.path.join(cat_path, fname))
                if meta["number"] is not None:
                    problems.append(meta)
            if problems:
                problems.sort(key=lambda x: x["number"])
                results[difficulty][category] = problems
    return results

def make_github_link(meta, difficulty_folder, category):
    rel     = f"{difficulty_folder}/{category}/{os.path.basename(meta['filepath'])}"
    encoded = rel.replace(" ", "%20")
    return f"[{meta['title']}]({encoded})"

def build_progress_bar(current, total, width=30):
    filled = int(width * current / total) if total else 0
    bar    = "█" * filled + "░" * (width - filled)
    pct    = int(100 * current / total) if total else 0
    return f"[{bar}]  {pct}%   ({current:>3} / {total})"

def build_sections(solutions):
    counts = {d: sum(len(v) for v in cats.values()) for d, cats in solutions.items()}
    total  = sum(counts.values())
    lines  = []

    lines.append("## `$ cat progress.log`\n")
    lines.append("<div align=\"center\">\n")
    lines.append("| 🟢 Easy | 🟡 Medium | 🔴 Hard | 📦 Total |")
    lines.append("|:-------:|:---------:|:-------:|:--------:|")
    lines.append(f"| **{counts['Easy']}** | **{counts['Medium']}** | **{counts['Hard']}** | **{total}** |")
    lines.append("\n</div>\n")
    lines.append("```bash")
    lines.append("[SYSTEM] Problem Tracker — maahfuzdev/LeetCode-Solutions\n")
    lines.append(f"> Total Progress  {build_progress_bar(total, 100)}")
    lines.append(f"> Easy            {build_progress_bar(counts['Easy'], 100)}")
    lines.append(f"> Medium          {build_progress_bar(counts['Medium'], 50)}")
    lines.append(f"> Hard            {build_progress_bar(counts['Hard'], 25)}")
    lines.append("")
    lines.append("[INFO]  Next milestone → 50 Easy problems")
    lines.append("[INFO]  Keep grinding. Consistency beats talent. 🔥")
    lines.append("```\n")

    lines.append("## `$ ls ./solutions --detail`\n")
    diff_icons = {"Easy": "🟢", "Medium": "🟡", "Hard": "🔴"}

    for difficulty, cats in solutions.items():
        count = counts[difficulty]
        icon  = diff_icons[difficulty]
        lines.append(f"### {icon} {difficulty} — {count} Solved\n")
        folder = DIFFICULTY_DIRS[difficulty]
        for category, problems in cats.items():
            emoji = get_emoji(category)
            lines.append(f"<details>\n<summary><code>{emoji} — {len(problems)} problem{'s' if len(problems) != 1 else ''}</code></summary>\n")
            lines.append("| # | Problem | Approach | Time | Space |")
            lines.append("|---|---------|----------|:----:|:-----:|")
            for p in problems:
                link = make_github_link(p, folder, category)
                lines.append(f"| {p['number']} | {link} | {p['approach']} | `{p['time']}` | `{p['space']}` |")
            lines.append("\n</details>\n")

    return "\n".join(lines)

START_MARKER = "<!-- AUTO-UPDATE:START -->"
END_MARKER   = "<!-- AUTO-UPDATE:END -->"

def update_readme(new_content):
    with open(README_PATH, encoding="utf-8") as f:
        readme = f.read()
    if START_MARKER not in readme or END_MARKER not in readme:
        print("❌ Markers not found in README.md")
        return False
    pattern = re.compile(re.escape(START_MARKER) + r".*?" + re.escape(END_MARKER), re.DOTALL)
    updated = pattern.sub(f"{START_MARKER}\n{new_content}\n{END_MARKER}", readme)
    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(updated)
    print("✅ README.md updated successfully!")
    return True

if __name__ == "__main__":
    print("🔍 Scanning solution files...")
    solutions = scan_solutions()
    total = sum(len(p) for cats in solutions.values() for p in cats.values())
    print(f"   Found {total} solutions.")
    print("📝 Building sections...")
    content = build_sections(solutions)
    print("💾 Writing to README.md...")
    update_readme(content)
