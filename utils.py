import reflex as rx
from assets.content import format_date_range


def render_icon(icon_name: str) -> rx.Component:
    """Render Lucide icons or custom SVG fallbacks for deprecated brand logos."""
    if icon_name == "github":
        return rx.html(
            """<svg width="24" height="24" viewBox="0 0 24 24" fill="var(--accent-9)"><path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z"/></svg>"""
        )
    if icon_name == "gitlab":
        return rx.html(
            """<svg width="24" height="24" viewBox="0 0 24 24" fill="var(--accent-9)"><path d="M22.65 14.39L12 22.13 1.35 14.39a.84.84 0 0 1-.3-.94l1.22-3.78 2.44-7.51A.42.44 0 0 1 5.5 2a.43.43 0 0 1 .41.3l2.07 6.37h8.04l2.07-6.37a.43.43 0 0 1 .41-.3.42.44 0 0 1 .39.16l2.44 7.51 1.22 3.78a.84.84 0 0 1-.3.94z"/></svg>"""
        )
    if icon_name == "linkedin":
        return rx.html(
            """<svg width="24" height="24" viewBox="0 0 24 24" fill="var(--accent-9)"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/></svg>"""
        )
    return rx.icon(icon_name, size=24, color="var(--accent-9)")


def page_layout(*children, title: str, show_back: bool = True) -> rx.Component:
    """A standard layout wrapper for all pages to ensure consistency."""
    return rx.center(
        rx.vstack(
            rx.flex(
                rx.heading(title, size="8", weight="bold"),
                rx.spacer(),
                rx.cond(
                    show_back,
                    rx.button(
                        rx.icon("arrow-left"),
                        "Home",
                        variant="soft",
                        on_click=rx.redirect("/"),
                    ),
                ),
                width="100%",
                align="center",
                margin_bottom="2em",
            ),
            *children,
            width="100%",
            max_width="800px",
            padding="2em",
            spacing="6",
        ),
        width="100%",
        min_height="100vh",
        align_items="flex-start",
    )


def nav_card(icon: str, heading: str, text: str, href: str) -> rx.Component:
    """Simplified navigation card."""
    return rx.link(
        rx.card(
            rx.flex(
                render_icon(icon),
                rx.box(
                    rx.heading(heading, size="4"),
                    rx.text(text, size="2", color="var(--gray-11)"),
                ),
                spacing="3",
                align="center",
            ),
            _hover={
                "transform": "translateY(-2px)",
                "cursor": "pointer",
                "box_shadow": "var(--shadow-3)",
            },
            transition="all 0.2s ease",
        ),
        href=href,
        is_external=href.startswith("http"),
        text_decoration="none",
    )


def _preview_card(item: dict, footer: rx.Component) -> rx.Component:
    """Shared base for project_card and blog_card."""
    is_featured = item.get("featured", False)
    text = item.get("description") or item.get("content", "")

    return rx.card(
        rx.vstack(
            rx.flex(
                (
                    rx.badge("Featured", color_scheme="indigo")
                    if is_featured
                    else rx.fragment()
                ),
                rx.badge(item.get("date", ""), variant="soft", color_scheme="gray"),
                spacing="2",
            ),
            rx.heading(item.get("title", ""), size="5"),
            rx.text(
                text[:120] + "..." if len(text) > 120 else text,
                size="2",
                color="var(--gray-11)",
            ),
            footer,
            spacing="3",
            align_items="start",
        ),
        width="100%",
        class_name="scroll-animate",
    )


def project_card(project: dict) -> rx.Component:
    footer = rx.dialog.root(
        rx.dialog.trigger(
            rx.button("Read More", variant="soft", size="2", margin_top="1em")
        ),
        rx.dialog.content(
            rx.dialog.title(project.get("title", "")),
            rx.scroll_area(rx.markdown(project["content"]), max_height="60vh"),
            rx.dialog.close(rx.button("Close", variant="soft", margin_top="1em")),
        ),
    )
    return _preview_card(project, footer)


def blog_card(blog: dict) -> rx.Component:
    footer = rx.link(
        "Read post →",
        href=f"/blog/{blog['slug']}",
        size="2",
        weight="bold",
        color="var(--accent-11)",
    )
    return _preview_card(blog, footer)


def _position_row(pos: dict) -> rx.Component:
    """A single position/promotion row inside an experience item."""
    start = pos.get("start_date", "")
    end = pos.get("end_date", "")
    date_str = format_date_range(start, end)

    return rx.flex(
        rx.icon("chevron-right", size=14, color="var(--accent-9)"),
        rx.text(pos.get("title", ""), size="2", weight="medium"),
        rx.spacer(),
        rx.text(date_str, size="1", color="var(--gray-10)"),
        width="100%",
        align="center",
        spacing="2",
    )


# assets/utils.py


def experience_item(exp: dict) -> rx.Component:
    """Clean experience timeline item with expandable promotion roles and optional title link."""
    positions = exp.get("positions", [])

    # Wrap title in a link if URL is provided
    title_heading = rx.heading(exp["title"], size="5", weight="bold")
    title_element = (
        rx.link(
            title_heading,
            href=exp["url"],
            is_external=True,
            underline="hover",
            color="inherit",
            _hover={"color": "var(--accent-11)"},
        )
        if exp.get("url")
        else title_heading
    )

    position_accordion = (
        rx.accordion.root(
            *[
                rx.accordion.item(
                    header=rx.flex(
                        rx.vstack(
                            rx.text(pos.get("title", ""), size="3", weight="bold"),
                            rx.text(
                                format_date_range(
                                    pos.get("start_date", ""), pos.get("end_date", "")
                                ),
                                size="1",
                                color="var(--accent-11)",
                            ),
                            align_items="start",
                            spacing="1",
                        ),
                        rx.spacer(),
                        width="100%",
                        align="center",
                    ),
                    content=rx.markdown(
                        pos.get("description", ""),
                        size="2",
                        color="var(--gray-11)",
                    ),
                    value=f"position-{idx}",
                )
                for idx, pos in enumerate(positions)
            ],
            collapsible=True,
            type="multiple",
            width="100%",
            variant="ghost",
        )
        if positions
        else rx.fragment()
    )

    general_content = (
        rx.markdown(exp["content"], size="2", color="var(--gray-11)")
        if exp.get("content", "").strip()
        else rx.fragment()
    )

    return rx.box(
        rx.vstack(
            rx.flex(
                title_element,
                rx.spacer(),
                rx.badge(exp.get("date", ""), variant="surface", color_scheme="indigo"),
                width="100%",
                align="center",
            ),
            position_accordion,
            general_content,
            spacing="3",
            width="100%",
            padding_left="1em",
            border_left="2px solid var(--accent-6)",
        ),
        margin_bottom="2em",
        width="100%",
    )
