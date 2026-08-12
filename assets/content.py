import re
from pathlib import Path
from datetime import datetime
import frontmatter

PRESENT_KEYWORDS = {"present", "current", "now", "ongoing"}
REQUIRED_FIELDS = {"title"}


def parse_month(date_str: str) -> datetime:
    """Parse a single point in time: '2025-02', '2025', 'Feb 2025', etc."""
    if not date_str or str(date_str).strip().lower() in PRESENT_KEYWORDS:
        return datetime.max

    date_str = str(date_str).strip()

    for fmt in ["%Y-%m-%d", "%Y-%m", "%Y"]:
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError:
            continue

    for fmt in ["%b %Y", "%B %d, %Y"]:
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError:
            continue

    return datetime(1900, 1, 1)


def format_date_range(start: str, end: str | None) -> str:
    start_label = parse_month(start).strftime("%b %Y")

    if not end or str(end).strip().lower() in PRESENT_KEYWORDS:
        return f"{start_label} - Present"

    end_label = parse_month(end).strftime("%b %Y")
    return f"{start_label} - {end_label}"


def load_markdown_dir(directory: str) -> list[dict]:
    """Load all markdown files from a directory and parse frontmatter."""
    items = []
    dir_path = Path(directory)

    if not dir_path.exists():
        return items

    for file_path in dir_path.glob("*.md"):
        post = frontmatter.load(file_path)
        meta = dict(post.metadata)
        meta["content"] = post.content

        missing = REQUIRED_FIELDS - meta.keys()
        if missing:
            raise ValueError(f"{file_path} is missing required frontmatter: {missing}")

        if "featured" in meta and isinstance(meta["featured"], str):
            meta["featured"] = meta["featured"].lower() == "true"
        meta.setdefault("featured", False)

        # --- Date handling ---
        if "start_date" in meta:
            end_raw = meta.get("end_date")
            meta["date"] = format_date_range(meta["start_date"], end_raw)
            meta["_start_dt"] = parse_month(meta["start_date"])
            meta["_end_dt"] = parse_month(end_raw) if end_raw else datetime.now()
        else:
            dt = parse_month(meta.get("date", ""))
            meta["_start_dt"] = dt
            meta["_end_dt"] = dt

        base_name = file_path.stem
        meta["slug"] = re.sub(r"^\d+-", "", base_name)

        items.append(meta)

    return items


def sort_items(items: list[dict]) -> list[dict]:
    """
    Sort priority:
    1. Featured items first
    2. Manual order override (if set)
    3. Newest end date (Ongoing/Present items stay on top)
    4. Newest start date (Most recently started roles float to top)
    """

    def sort_key(item):
        featured_priority = 0 if item.get("featured", False) else 1
        order_priority = item.get("order", 9999)
        end_priority = -item["_end_dt"].timestamp()
        start_priority = -item["_start_dt"].timestamp()
        return (featured_priority, order_priority, end_priority, start_priority)

    return sorted(items, key=sort_key)


PROJECTS = sort_items(load_markdown_dir("assets/projects"))
EXPERIENCES = sort_items(load_markdown_dir("assets/experiences"))
BLOGS = sort_items(load_markdown_dir("assets/blogs"))
