import reflex as rx
from assets.blogs import BLOGS
from assets.projects import PROJECTS
from assets.experiences import EXPERIENCES
from assets.utils import page_layout, nav_card, project_card, experience_item, blog_card


@rx.page(route="/", title="Surya's Website")
def index() -> rx.Component:
    return rx.center(
        rx.vstack(
            # Hero Section
            rx.vstack(
                rx.heading("Hello, I'm Surya Vasudev", size="9", weight="bold"),
                rx.text(
                    "Computer Engineering Student & Full-Stack Developer",
                    size="5",
                    color="var(--gray-11)",
                ),
                rx.text(
                    "Living on the bleeding edge of tech, building robust systems, and competing in hackathons.",
                    size="3",
                    color="var(--gray-10)",
                ),
                rx.flex(
                    rx.button(
                        "View Projects", on_click=rx.redirect("/projects"), size="3"
                    ),
                    rx.button(
                        "My Experience",
                        on_click=rx.redirect("/experience"),
                        variant="soft",
                        size="3",
                    ),
                    spacing="4",
                    margin_top="1em",
                ),
                spacing="4",
                align_items="start",
                padding_y="4em",
            ),
            rx.divider(),
            # Quick Navigation
            rx.heading("Explore", size="6", margin_top="2em"),
            rx.grid(
                nav_card(
                    "briefcase", "Experiences", "My professional journey", "/experience"
                ),
                nav_card("folder-git-2", "Projects", "Things I've built", "/projects"),
                nav_card("pen-tool", "Blog", "Thoughts and writings", "/blogs"),
                nav_card(
                    "github",
                    "GitHub",
                    "Code repositories",
                    "https://github.com/UnknownCrafts",
                ),
                nav_card(
                    "linkedin",
                    "LinkedIn",
                    "Professional network",
                    "https://linkedin.com/in/surya-vasudev-b12547239/",
                ),
                columns="2",
                spacing="4",
                width="100%",
            ),
            # Footer
            rx.flex(
                rx.text(
                    "© 2026 Surya Vasudev",
                    size="1",
                    color="var(--gray-9)",
                ),
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


@rx.page(route="/projects", title="Projects")
def projects() -> rx.Component:
    return page_layout(
        rx.text(
            "Building, competing, and learning at the bleeding edge.",
            color="var(--gray-11)",
            margin_bottom="2em",
        ),
        rx.grid(
            *[project_card(p) for p in PROJECTS],
            columns="2",
            spacing="4",
            width="100%",
        ),
        title="Projects & Achievements",
    )


@rx.page(route="/experience", title="Experience")
def experience() -> rx.Component:
    return page_layout(
        rx.text(
            "Where I've contributed and grown professionally.",
            color="var(--gray-11)",
            margin_bottom="2em",
        ),
        rx.vstack(
            *[experience_item(exp) for exp in EXPERIENCES],
            width="100%",
            spacing="6",
        ),
        title="Experience",
    )


@rx.page(route="/blogs", title="Blogs")
def blogs() -> rx.Component:
    return page_layout(
        rx.cond(
            len(BLOGS) > 0,
            rx.grid(
                *[blog_card(b) for b in BLOGS],
                columns="2",
                spacing="4",
                width="100%",
            ),
            rx.center(
                rx.vstack(
                    rx.icon("pen-tool", size=40, color="var(--gray-9)"),
                    rx.heading("No Blogs Yet", size="4"),
                    rx.text("Check back soon!", color="var(--gray-11)"),
                    align="center",
                    padding="4em",
                ),
                width="100%",
            ),
        ),
        title="My Blogs",
    )


app = rx.App(
    stylesheets=["/styles.css"],
    theme=rx.theme(
        appearance="dark",
        has_background=True,
        radius="medium",
        accent_color="indigo",
        gray_color="slate",
    ),
    enable_state=False,
)
