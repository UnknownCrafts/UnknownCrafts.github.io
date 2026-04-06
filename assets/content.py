import re
from pathlib import Path


def load_markdown_dir(directory: str) -> list[dict]:
    items = []
    dir_path = Path(directory)

    if not dir_path.exists():
        return items

    for file_path in dir_path.glob("*.md"):
        with open(file_path, "r", encoding="utf-8") as f:
            raw_text = f.read()

        meta = {"content": raw_text}
        if raw_text.startswith("---"):
            parts = raw_text.split("---", 2)
            if len(parts) >= 3:
                frontmatter, body = parts[1], parts[2]
                meta["content"] = body.strip()

                for line in frontmatter.strip().split("\n"):
                    if ":" in line:
                        key, value = line.split(":", 1)
                        meta[key.strip()] = value.strip().strip('"').strip("'")

        meta["featured"] = meta.get("featured", "false").lower() == "true"
        meta["order"] = int(meta.get("order", 999))

        base_name = file_path.stem
        meta["slug"] = re.sub(r"^\d+-", "", base_name)

        items.append(meta)

    return sorted(items, key=lambda x: x["order"])


PROJECTS = load_markdown_dir("assets/projects")
EXPERIENCES = load_markdown_dir("assets/experiences")
BLOGS = load_markdown_dir("assets/blogs")
