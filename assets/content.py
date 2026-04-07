import re
from pathlib import Path
from datetime import datetime
import frontmatter


def load_markdown_dir(directory: str) -> list[dict]:
    """Load all markdown files from a directory and parse frontmatter."""
    items = []
    dir_path = Path(directory)

    if not dir_path.exists():
        return items

    for file_path in dir_path.glob("*.md"):
        # frontmatter.load() parses both frontmatter and content automatically
        post = frontmatter.load(file_path)

        # Convert to dict and add content
        meta = dict(post.metadata)
        meta["content"] = post.content

        # Ensure featured is a boolean
        if "featured" in meta and isinstance(meta["featured"], str):
            meta["featured"] = meta["featured"].lower() == "true"
        meta.setdefault("featured", False)

        # Extract slug from filename (remove leading numbers if present)
        base_name = file_path.stem
        meta["slug"] = re.sub(r"^\d+-", "", base_name)

        items.append(meta)

    return items


def parse_date(date_str: str) -> datetime:
    """
    Parse various date formats into a datetime for sorting.
    Handles: "2025-03-15", "2025-03", "2025", "Oct 2025", etc.
    """
    if not date_str:
        return datetime(1900, 1, 1)

    date_str = str(date_str).strip()

    # Try ISO format first: 2025-03-15 or 2025-03 or 2025
    for fmt in ["%Y-%m-%d", "%Y-%m", "%Y"]:
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError:
            continue

    # Try "Month Year" format: "Oct 2025"
    try:
        return datetime.strptime(date_str, "%b %Y")
    except ValueError:
        pass

    # Try "Month DD, YYYY": "October 15, 2025"
    try:
        return datetime.strptime(date_str, "%B %d, %Y")
    except ValueError:
        pass

    # Fallback: if we can't parse, put it far in the past
    return datetime(1900, 1, 1)


def sort_items(items: list[dict]) -> list[dict]:
    """
    Sort items by:
    1. Featured items first
    2. Manual order (lower = higher priority)
    3. Date (newer = higher priority)
    """

    def sort_key(item):
        # For featured: False=0, True=1. We want True first, so negate
        featured_priority = 0 if item.get("featured", False) else 1

        # For order: lower numbers = higher priority
        order_priority = item.get("order", 9999)

        # For date: newer = higher priority, so negate the timestamp
        date = parse_date(item.get("date", "1900-01-01"))
        date_priority = -date.timestamp()  # Negate so newer dates sort first

        return (featured_priority, order_priority, date_priority)

    return sorted(items, key=sort_key)


PROJECTS = sort_items(load_markdown_dir("assets/projects"))
EXPERIENCES = sort_items(load_markdown_dir("assets/experiences"))
BLOGS = sort_items(load_markdown_dir("assets/blogs"))
