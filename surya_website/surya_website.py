import reflex as rx
from assets.blogs import BLOGS
from assets.projects import PROJECTS
from assets.experiences import EXPERIENCES
from assets.utils import (
    card_item,
    timeline_item,
    project_card_large,
    project_card_small,
    experience_item,
    get_featured_projects,
    get_other_projects,
    blog_card,
)


@rx.page(route="/", title="Surya's Website")
def index() -> rx.Component:
    return rx.box(
        # Hero Section
        rx.box(
            # Animated background elements
            rx.box(class_name="gradient-orb orb-1"),
            rx.box(class_name="gradient-orb orb-2"),
            rx.box(class_name="gradient-orb orb-3"),
            rx.container(
                rx.vstack(
                    # Main heading with typewriter effect
                    rx.vstack(
                        rx.text(
                            "👋",
                            size="9",
                            class_name="wave-emoji",
                        ),
                        rx.heading(
                            "Hello, I'm Surya Vasudev",
                            size="9",
                            class_name="hero-title",
                        ),
                        rx.text(
                            "Computer Engineering Student",
                            size="6",
                            class_name="hero-subtitle",
                        ),
                        rx.text(
                            "Living on the Bleeding Edge of Tech",
                            size="4",
                            class_name="hero-tagline",
                        ),
                        spacing="3",
                        align_items="center",
                        text_align="center",
                    ),
                    # CTA Buttons
                    rx.hstack(
                        rx.link(
                            rx.button(
                                "View Projects",
                                size="4",
                                class_name="cta-primary",
                            ),
                            href="/projects",
                        ),
                        rx.link(
                            rx.button(
                                "My Experience",
                                size="4",
                                variant="outline",
                                class_name="cta-secondary",
                            ),
                            href="/experience",
                        ),
                        spacing="4",
                        class_name="cta-buttons",
                    ),
                    # Scroll indicator
                    rx.vstack(
                        rx.text(
                            "Scroll to explore", size="2", class_name="scroll-text"
                        ),
                        rx.text("↓", size="6", class_name="scroll-arrow"),
                        spacing="1",
                        class_name="scroll-indicator",
                    ),
                    spacing="6",
                    align_items="center",
                    justify="center",
                    min_height="100vh",
                    padding="2em",
                ),
                max_width="1200px",
            ),
            class_name="hero-section",
            position="relative",
            overflow="hidden",
        ),
        # Stats Section
        rx.box(
            rx.container(
                rx.vstack(
                    rx.heading(
                        "Achievements & Impact",
                        size="8",
                        class_name="section-title",
                        text_align="center",
                    ),
                    rx.grid(
                        # Stat 1
                        rx.box(
                            rx.vstack(
                                rx.text("🏆", size="8"),
                                rx.heading("7+", size="8", class_name="stat-number"),
                                rx.text("Competition Wins", class_name="stat-label"),
                                spacing="2",
                                align_items="center",
                            ),
                            class_name="stat-card",
                        ),
                        # Stat 2
                        rx.box(
                            rx.vstack(
                                rx.text("💻", size="8"),
                                rx.heading("25+", size="8", class_name="stat-number"),
                                rx.text("Projects Built", class_name="stat-label"),
                                spacing="2",
                                align_items="center",
                            ),
                            class_name="stat-card",
                        ),
                        # Stat 3
                        rx.box(
                            rx.vstack(
                                rx.text("🚀", size="8"),
                                rx.heading("4", size="8", class_name="stat-number"),
                                rx.text("Professional Roles", class_name="stat-label"),
                                spacing="2",
                                align_items="center",
                            ),
                            class_name="stat-card",
                        ),
                        # Stat 4
                        rx.box(
                            rx.vstack(
                                rx.text("⚡", size="8"),
                                rx.heading("∞", size="8", class_name="stat-number"),
                                rx.text("Learning & Growing", class_name="stat-label"),
                                spacing="2",
                                align_items="center",
                            ),
                            class_name="stat-card",
                        ),
                        columns="4",
                        spacing="4",
                        width="100%",
                        class_name="stats-grid",
                    ),
                    spacing="5",
                    padding="4em 2em",
                ),
                max_width="1200px",
            ),
            class_name="stats-section",
        ),
        # Featured Highlights
        rx.box(
            rx.container(
                rx.vstack(
                    rx.heading(
                        "Recent Highlights",
                        size="8",
                        class_name="section-title",
                        text_align="center",
                    ),
                    rx.grid(
                        # Highlight 1
                        rx.box(
                            rx.vstack(
                                rx.badge(
                                    "🥇 1st Place",
                                    class_name="highlight-badge",
                                    size="3",
                                ),
                                rx.heading(
                                    "Route Optimization Champion",
                                    size="5",
                                    class_name="highlight-title",
                                ),
                                rx.text(
                                    "Won 1st place solving Vehicle Routing Problem with sub-5 second optimization for 100+ nodes",
                                    class_name="highlight-text",
                                ),
                                rx.link(
                                    rx.text(
                                        "Learn more →", class_name="highlight-link"
                                    ),
                                    href="/projects",
                                ),
                                spacing="2",
                                align_items="start",
                            ),
                            class_name="highlight-card",
                        ),
                        # Highlight 2
                        rx.box(
                            rx.vstack(
                                rx.badge(
                                    "🤖 Quantum", class_name="highlight-badge", size="3"
                                ),
                                rx.heading(
                                    "Quantum Music Generator",
                                    size="5",
                                    class_name="highlight-title",
                                ),
                                rx.text(
                                    "3rd place at IBM Qiskit Fall Fest - Translating quantum algorithms into musical compositions",
                                    class_name="highlight-text",
                                ),
                                rx.link(
                                    rx.text(
                                        "Learn more →", class_name="highlight-link"
                                    ),
                                    href="/projects",
                                ),
                                spacing="2",
                                align_items="start",
                            ),
                            class_name="highlight-card",
                        ),
                        # Highlight 3
                        rx.box(
                            rx.vstack(
                                rx.badge(
                                    "🚀 Full-Stack",
                                    class_name="highlight-badge",
                                    size="3",
                                ),
                                rx.heading(
                                    "Real-Time Collaboration",
                                    size="5",
                                    class_name="highlight-title",
                                ),
                                rx.text(
                                    "Built Code With Me - Live collaborative coding platform with WebSockets and CRDTs",
                                    class_name="highlight-text",
                                ),
                                rx.link(
                                    rx.text(
                                        "Learn more →", class_name="highlight-link"
                                    ),
                                    href="/projects",
                                ),
                                spacing="2",
                                align_items="start",
                            ),
                            class_name="highlight-card",
                        ),
                        columns="3",
                        spacing="4",
                        width="100%",
                        class_name="highlights-grid",
                    ),
                    spacing="5",
                    padding="4em 2em",
                ),
                max_width="1200px",
            ),
            class_name="highlights-section",
        ),
        # Main Navigation Cards
        rx.box(
            rx.container(
                rx.vstack(
                    rx.heading(
                        "Explore My Journey",
                        size="8",
                        class_name="section-title",
                        text_align="center",
                        margin_bottom="2em",
                    ),
                    rx.flex(
                        card_item(
                            "/briefcase.svg",
                            "Experiences",
                            "My Contributions to Society!",
                            "/experience",
                            0,
                        ),
                        card_item(
                            "/folder-open.png",
                            "Projects",
                            "Explore My Learning Journey!",
                            "/projects",
                            1,
                        ),
                        card_item(
                            "/blogger.png",
                            "Blog",
                            "Something Was Written!",
                            "/blogs",
                            2,
                        ),
                        card_item(
                            "/github.png",
                            "Github",
                            "Look At My Work!",
                            "https://github.com/UnknownCrafts",
                            3,
                        ),
                        card_item(
                            "/gitlab.png",
                            "Gitlab",
                            "Look At My Work Somewhere Else!",
                            "https://gitlab.com/suryavasudev005",
                            4,
                        ),
                        card_item(
                            "/linkedin.png",
                            "Linkedin",
                            "Connect With Me!",
                            "https://www.linkedin.com/in/surya-vasudev-b12547239/",
                            5,
                        ),
                        spacing="4",
                        width="100%",
                        direction="column",
                        wrap="wrap",
                        class_name="cards-grid",
                    ),
                    spacing="2",
                    padding="4em 2em",
                ),
                max_width="1200px",
            ),
            class_name="navigation-section",
        ),
        # Footer
        rx.box(
            rx.container(
                rx.vstack(
                    rx.text(
                        "Built with Reflex • Designed with passion",
                        class_name="footer-text",
                        size="2",
                    ),
                    rx.text(
                        "© 2025 Surya Vasudev",
                        class_name="footer-text",
                        size="1",
                    ),
                    spacing="2",
                    align_items="center",
                    padding="2em",
                ),
                max_width="1200px",
            ),
            class_name="footer-section",
        ),
        width="100%",
        class_name="home-container",
    )


@rx.page(route="/projects", title="Projects")
def projects() -> rx.Component:
    featured = get_featured_projects(PROJECTS)
    other = get_other_projects(PROJECTS)

    featured_cards = [project_card_large(featured[i], i) for i in range(len(featured))]
    other_cards = [project_card_small(other[i], i) for i in range(len(other))]

    return rx.box(
        [rx.box(class_name="cube") for x in range(6)],
        rx.box(
            # Header
            rx.box(
                rx.hstack(
                    rx.vstack(
                        rx.heading(
                            "Projects & Achievements",
                            size="9",
                            class_name="page-header",
                        ),
                        rx.text(
                            "Building, competing, and learning at the bleeding edge",
                            size="4",
                            class_name="page-subheader",
                        ),
                        spacing="2",
                        align_items="start",
                    ),
                    rx.spacer(),
                    rx.button(
                        "← Home",
                        on_click=rx.redirect("/"),
                        class_name="back-button-modern",
                        size="3",
                    ),
                    width="100%",
                    align_items="start",
                ),
                margin_bottom="3em",
                class_name="fade-in-down",
            ),
            # Featured Projects Section
            rx.box(
                rx.heading(
                    "🏆 Competition Wins & Featured Projects",
                    size="6",
                    class_name="section-heading",
                ),
                rx.box(
                    *featured_cards,
                    class_name="featured-grid",
                    display="grid",
                    width="100%",
                ),
                margin_bottom="3em",
            ),
            # All Projects Section
            rx.box(
                rx.heading(
                    "💻 Other Projects & Learning Journey",
                    size="6",
                    class_name="section-heading",
                ),
                rx.box(
                    *other_cards,
                    class_name="projects-grid",
                    display="grid",
                    width="100%",
                ),
            ),
            max_width="1400px",
            width="100%",
            padding="2em",
            margin="0 auto",
        ),
        background="linear-gradient(135deg, #0f0f23 0%, #1a1a2e 100%)",
        min_height="100vh",
        position="relative",
        overflow_x="hidden",
        overflow_y="auto",
        color="white",
        width="100%",
    )


@rx.page(route="/experience", title="Experience")
def experience() -> rx.Component:
    experience_items = [
        experience_item(EXPERIENCES[i], i) for i in range(len(EXPERIENCES))
    ]

    return rx.box(
        [rx.box(class_name="cube") for x in range(6)],
        rx.box(
            # Header
            rx.box(
                rx.vstack(
                    rx.heading(
                        "Experience",
                        size="9",
                        class_name="page-header",
                    ),
                    rx.text(
                        "Where I've contributed and grown",
                        size="4",
                        class_name="page-subheader",
                    ),
                    spacing="2",
                    align_items="start",
                    width="100%",
                ),
                margin_bottom="3em",
                class_name="fade-in-down",
            ),
            # Experience Cards
            rx.vstack(
                *experience_items,
                spacing="4",
                width="100%",
                class_name="experience-list",
            ),
            # Back button - desktop only
            rx.box(
                rx.button(
                    "← Home",
                    on_click=rx.redirect("/"),
                    class_name="back-button-modern back-button-desktop",
                    size="3",
                ),
                position="fixed",
                top="2em",
                right="2em",
                class_name="desktop-only",
            ),
            max_width="1000px",
            width="100%",
            padding="2em",
            margin="0 auto",
        ),
        # Floating back button - mobile only
        rx.button(
            "← Back",
            on_click=rx.redirect("/"),
            class_name="back-button-modern back-button-mobile",
            size="3",
        ),
        background="linear-gradient(135deg, #1a1a2e 0%, #16213e 100%)",
        min_height="100vh",
        position="relative",
        overflow_x="hidden",
        overflow_y="auto",
        color="white",
        width="100%",
        padding_bottom="5rem",
    )


@rx.page(route="/blogs", title="Blogs")
def blogs() -> rx.Component:
    from assets.utils import blog_card

    blog_cards = [blog_card(BLOGS[i], i) for i in range(len(BLOGS))]

    return rx.box(
        [rx.box(class_name="cube") for x in range(6)],
        rx.box(
            # Header
            rx.box(
                rx.vstack(
                    rx.heading(
                        "My Blogs",
                        size="9",
                        class_name="page-header",
                    ),
                    rx.text(
                        "Thoughts, learnings, and stories from my journey",
                        size="4",
                        class_name="page-subheader",
                    ),
                    spacing="2",
                    align_items="start",
                    width="100%",
                ),
                margin_bottom="3em",
                class_name="fade-in-down",
            ),
            # Blog Cards Grid
            rx.cond(
                len(BLOGS) > 0,
                rx.box(
                    *blog_cards,
                    class_name="blogs-grid",
                    display="grid",
                    width="100%",
                ),
                rx.box(
                    rx.vstack(
                        rx.text("📝", size="9"),
                        rx.heading("No Blogs Yet", size="6"),
                        rx.text(
                            "Check back soon for updates!",
                            color="#a0aec0",
                        ),
                        spacing="3",
                        align_items="center",
                        padding="4em",
                    ),
                    class_name="empty-state",
                ),
            ),
            # Back button - desktop only
            rx.box(
                rx.button(
                    "← Home",
                    on_click=rx.redirect("/"),
                    class_name="back-button-modern back-button-desktop",
                    size="3",
                ),
                position="fixed",
                top="2em",
                right="2em",
                class_name="desktop-only",
            ),
            max_width="1200px",
            width="100%",
            padding="2em",
            margin="0 auto",
        ),
        # Floating back button - mobile only
        rx.button(
            "← Back",
            on_click=rx.redirect("/"),
            class_name="back-button-modern back-button-mobile",
            size="3",
        ),
        background="linear-gradient(135deg, #0f0f23 0%, #1a1a2e 100%)",
        min_height="100vh",
        position="relative",
        overflow_x="hidden",
        overflow_y="auto",
        color="white",
        width="100%",
        padding_bottom="5rem",
    )


app = rx.App(stylesheets=["/styles.css"], enable_state=False)
