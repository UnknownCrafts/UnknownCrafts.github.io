# surya_website.py
import reflex as rx
from assets.config import SITE, NAV_ITEMS
from assets.sections import SECTIONS, register_sections
from assets.utils import nav_card


@rx.page(route="/", title=f"{SITE['name']}'s Website")
def index() -> rx.Component:
    return rx.center(
        rx.vstack(
            # Hero Section
            rx.vstack(
                rx.heading(f"Hello, I'm {SITE['name']}", size="9", weight="bold"),
                rx.text(SITE["tagline"], size="5", color="var(--gray-11)"),
                rx.text(SITE["subtitle"], size="3", color="var(--gray-10)"),
                spacing="3",
                align_items="start",
                padding_y="3em",
            ),
            rx.divider(),
            # Quick Navigation
            rx.heading("Explore", size="6", margin_top="1.5em"),
            rx.grid(
                *[nav_card(n.icon, n.title, n.description, n.href) for n in NAV_ITEMS],
                columns="2",
                spacing="4",
                width="100%",
            ),
            # Footer
            rx.flex(
                rx.text(f"© 2026 {SITE['name']}", size="1", color="var(--gray-9)"),
                margin_top="4em",
                width="100%",
                justify="center",
            ),
            width="100%",
            max_width="800px",
            padding="2em",
        ),
        width="100%",
        min_height="100vh",
    )


app = rx.App(
    stylesheets=["/styles.css"],
    enable_state=False,
)

register_sections(app, SECTIONS)
