import reflex as rx


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
                rx.icon(icon, size=24, color="var(--accent-9)"),
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


def project_card(project: dict) -> rx.Component:
    """Unified, clean project card with a dialog for details."""
    is_featured = "🥇" in project["title"] or "🥉" in project["title"]

    return rx.card(
        rx.vstack(
            rx.flex(
                (
                    rx.badge("Featured", color_scheme="indigo")
                    if is_featured
                    else rx.fragment()
                ),
                rx.badge(project["date"], variant="soft", color_scheme="gray"),
                spacing="2",
            ),
            rx.heading(
                project["title"].replace("🥇", "").replace("🥉", "").strip(), size="5"
            ),
            rx.text(
                (
                    project["description"][:120] + "..."
                    if len(project["description"]) > 120
                    else project["description"]
                ),
                size="2",
                color="var(--gray-11)",
            ),
            rx.dialog.root(
                rx.dialog.trigger(
                    rx.button("Read More", variant="soft", size="2", margin_top="1em")
                ),
                rx.dialog.content(
                    rx.dialog.title(project["title"]),
                    rx.scroll_area(
                        rx.markdown(project["description"]), max_height="60vh"
                    ),
                    rx.dialog.close(
                        rx.button("Close", variant="soft", margin_top="1em")
                    ),
                ),
            ),
            spacing="3",
            align_items="start",
        ),
        width="100%",
    )


def experience_item(exp: dict) -> rx.Component:
    """Clean experience timeline item."""
    return rx.box(
        rx.vstack(
            rx.flex(
                rx.heading(exp["title"], size="4"),
                rx.spacer(),
                rx.badge(exp["date"], variant="surface", color_scheme="gray"),
                width="100%",
                align="center",
            ),
            rx.markdown(exp["description"], size="2", color="var(--gray-11)"),
            spacing="2",
            width="100%",
            padding_left="1em",
            border_left="2px solid var(--accent-6)",
        ),
        margin_bottom="2em",
    )


def blog_card(blog: dict) -> rx.Component:
    """Clean blog preview card."""
    return rx.card(
        rx.vstack(
            rx.badge(blog["date"], variant="soft"),
            rx.heading(blog["title"], size="5"),
            rx.text(
                blog["description"][:100] + "...", size="2", color="var(--gray-11)"
            ),
            rx.link("Read post →", href="#", size="2", weight="bold"),
            spacing="3",
        ),
        width="100%",
    )
