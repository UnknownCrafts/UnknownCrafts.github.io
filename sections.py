from dataclasses import dataclass
from typing import Callable, Optional
import reflex as rx
from assets.utils import page_layout, project_card, experience_item, blog_card
from assets.content import PROJECTS, EXPERIENCES, BLOGS


@dataclass
class ContentSection:
    route: str
    title: str
    description: str
    items: list[dict]
    card_renderer: Callable[[dict], rx.Component]
    columns: str = "2"
    empty_icon: str = "inbox"
    empty_message: str = "Nothing here yet."
    detail_route_prefix: Optional[str] = None  # e.g. "/blog" enables /blog/<slug> pages
    detail_renderer: Optional[Callable[[dict], rx.Component]] = None


def make_list_page(section: ContentSection):
    def _page() -> rx.Component:
        if section.items:
            body = rx.grid(
                *[section.card_renderer(i) for i in section.items],
                columns=section.columns,
                spacing="4",
                width="100%",
            )
        else:
            body = rx.center(
                rx.vstack(
                    rx.icon(section.empty_icon, size=40, color="var(--gray-9)"),
                    rx.heading("No Content Yet", size="4"),
                    rx.text(section.empty_message, color="var(--gray-11)"),
                    align="center",
                    padding="4em",
                ),
                width="100%",
            )

        children = [body]
        if section.description:
            children.insert(
                0,
                rx.text(
                    section.description,
                    color="var(--gray-11)",
                    margin_bottom="2em",
                ),
            )

        return page_layout(*children, title=section.title)

    return _page


def register_sections(app: rx.App, sections: list[ContentSection]) -> None:
    for section in sections:
        app.add_page(make_list_page(section), route=section.route, title=section.title)

        if section.detail_renderer and section.detail_route_prefix:
            for item in section.items:
                app.add_page(
                    lambda i=item: section.detail_renderer(i),
                    route=f"{section.detail_route_prefix}/{item['slug']}",
                    title=f"{item.get('title', '')}",
                )


SECTIONS = [
    ContentSection(
        route="/projects",
        title="Projects & Achievements",
        description="Building, competing, and learning at the bleeding edge.",
        items=PROJECTS,
        card_renderer=project_card,
    ),
    ContentSection(
        route="/experience",
        title="Experience",
        description="Where I've contributed and grown professionally.",
        items=EXPERIENCES,
        card_renderer=experience_item,
        columns="1",
    ),
    ContentSection(
        route="/blogs",
        title="My Blogs",
        description="",
        items=BLOGS,
        card_renderer=blog_card,
        empty_icon="pen-tool",
        empty_message="Check back soon!",
        detail_route_prefix="/blog",
        detail_renderer=lambda b: blog_post_page(b),
    ),
]


def blog_post_page(blog: dict) -> rx.Component:
    """Template for individual blog pages."""
    return page_layout(
        rx.vstack(
            rx.badge(
                blog.get("date", ""), color_scheme="indigo", variant="surface", size="2"
            ),
            rx.divider(margin_y="1em"),
            rx.markdown(blog["content"]),
            spacing="4",
            align_items="start",
            width="100%",
        ),
        title=blog.get("title", ""),
        show_back=True,
    )
