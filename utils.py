import reflex as rx


def card_item(imagesrc, heading, text, href, index=0):
    return rx.card(
        rx.link(
            rx.flex(
                rx.avatar(
                    src=imagesrc,
                    class_name="card-avatar",
                    style={
                        "filter": rx.color_mode_cond(
                            dark="invert(1) brightness(0.8)", light="invert(0)"
                        )
                    },
                ),
                rx.box(
                    rx.heading(heading, class_name="card-heading"),
                    rx.text(text, class_name="card-text"),
                ),
                spacing="2",
            ),
            href=href,
            underline="none",
            is_external=href.startswith("http"),
        ),
        class_name=f"hover-card fade-in-up stagger-{index}",
    )


def timeline_item(project):
    component_map = {
        "a": lambda text, **props: rx.link(text, **props, is_external=True),
    }

    return rx.box(
        rx.vstack(
            rx.box(
                rx.box(class_name="timeline-dot"),
                width="20px",
                height="20px",
                margin_right="15px",
                flex_shrink="0",
            ),
            rx.vstack(
                rx.text(
                    project["date"],
                    font_size="0.9em",
                    color="#6c757d",
                    margin_bottom="4px",
                    class_name="timeline-date",
                ),
                rx.heading(
                    project["title"],
                    font_size="1.2em",
                    font_weight="bold",
                    color="#343a40",
                    margin_bottom="6px",
                    class_name="timeline-title",
                ),
                rx.markdown(
                    project["description"],
                    font_size="1em",
                    color="#495057",
                    component_map=component_map,
                    class_name="timeline-description",
                ),
                rx.dialog.root(
                    rx.dialog.trigger(
                        rx.button("View More →", class_name="view-more-btn")
                    ),
                    rx.dialog.content(
                        rx.dialog.title(project["title"]),
                        rx.markdown(
                            project["description"],
                            margin_bottom="10px",
                        ),
                        rx.dialog.close(
                            rx.button("Close", size="2", class_name="close-btn"),
                        ),
                    ),
                ),
                spacing="2",
                align_items="start",
                flex="1",
            ),
            spacing="0",
            direction="row",
            align_items="start",
            width="100%",
        ),
        class_name="timeline-item slide-in-right",
        padding="20px",
        background_color="#f8f9fa",
        border="1px solid #dee2e6",
        border_radius="12px",
        box_shadow="0 4px 6px rgba(0, 0, 0, 0.1)",
        margin_bottom="20px",
    )


def extract_award_badge(title):
    """Extract award emoji and text from title"""
    if "🥇" in title:
        return "🥇", "1st Place"
    elif "🥈" in title:
        return "🥈", "2nd Place"
    elif "🥉" in title:
        return "🥉", "3rd Place"
    elif "First Place" in title or "1st place" in title.lower():
        return "🏆", "1st Place"
    elif "Second Place" in title or "2nd place" in title.lower():
        return "🥈", "2nd Place"
    elif "Third Place" in title or "3rd place" in title.lower():
        return "🥉", "3rd Place"
    return None, None


def get_clean_title(title):
    """Remove award emojis and parentheses from title"""
    # Remove emojis
    clean = title.replace("🥇", "").replace("🥈", "").replace("🥉", "")
    # Remove content in parentheses at the end
    if "(" in clean:
        clean = clean.split("(")[0].strip()
    return clean


def project_card_large(project, index=0):
    """Large featured card for award-winning projects"""
    emoji, award_text = extract_award_badge(project["title"])
    clean_title = get_clean_title(project["title"])

    return rx.box(
        rx.box(
            # Award badge
            rx.cond(
                emoji is not None,
                rx.badge(
                    f"{emoji} {award_text}" if emoji else "Featured",
                    class_name="award-badge",
                    position="absolute",
                    top="1em",
                    right="1em",
                    size="3",
                    z_index="10",
                ),
            ),
            rx.vstack(
                rx.heading(
                    clean_title,
                    size="7",
                    class_name="project-title-large",
                ),
                rx.text(
                    project["date"],
                    class_name="project-date-large",
                    font_weight="600",
                    size="3",
                ),
                rx.text(
                    (
                        project["description"][:250] + "..."
                        if len(project["description"]) > 250
                        else project["description"]
                    ),
                    class_name="project-preview-large",
                    size="3",
                    line_height="1.6",
                ),
                rx.dialog.root(
                    rx.dialog.trigger(
                        rx.button(
                            "Read Full Story →",
                            class_name="read-more-btn",
                            size="3",
                        )
                    ),
                    rx.dialog.content(
                        rx.dialog.title(clean_title),
                        rx.text(
                            project["date"],
                            class_name="dialog-date",
                            margin_bottom="1em",
                        ),
                        rx.box(
                            rx.markdown(project["description"]),
                            max_height="60vh",
                            overflow_y="auto",
                            padding_right="1em",
                            class_name="dialog-description",
                        ),
                        rx.dialog.close(
                            rx.button("Close", size="3", class_name="dialog-close-btn"),
                        ),
                        max_width="900px",
                        class_name="project-dialog",
                    ),
                ),
                spacing="3",
                align_items="start",
            ),
            class_name=f"project-card-large fade-in-scale stagger-{index}",
        ),
        grid_column="span 2" if index == 0 else "span 1",
    )


def project_card_small(project, index=0):
    """Compact card for other projects"""
    clean_title = get_clean_title(project["title"])

    return rx.box(
        rx.vstack(
            rx.heading(
                clean_title,
                size="4",
                class_name="project-title-small",
                line_height="1.3",
            ),
            rx.text(
                project["date"],
                class_name="project-date-small",
                font_weight="600",
                size="1",
            ),
            rx.text(
                (
                    project["description"][:100] + "..."
                    if len(project["description"]) > 100
                    else project["description"]
                ),
                class_name="project-preview-small",
                size="2",
                line_height="1.5",
            ),
            rx.dialog.root(
                rx.dialog.trigger(
                    rx.button(
                        "View Details",
                        class_name="view-details-btn",
                        size="2",
                        variant="soft",
                    )
                ),
                rx.dialog.content(
                    rx.dialog.title(clean_title),
                    rx.text(
                        project["date"], class_name="dialog-date", margin_bottom="1em"
                    ),
                    rx.box(
                        rx.markdown(project["description"]),
                        max_height="60vh",
                        overflow_y="auto",
                        padding_right="1em",
                        class_name="dialog-description",
                    ),
                    rx.dialog.close(
                        rx.button("Close", size="3", class_name="dialog-close-btn"),
                    ),
                    max_width="900px",
                    class_name="project-dialog",
                ),
            ),
            spacing="2",
            align_items="start",
        ),
        class_name=f"project-card-small fade-in-scale stagger-{index % 6}",
    )


def experience_item(exp, index=0):
    """Modern experience card - responsive design"""
    return rx.box(
        rx.vstack(
            # Header with company and date
            rx.hstack(
                rx.vstack(
                    rx.heading(
                        exp["title"],
                        size="6",
                        class_name="company-name",
                    ),
                    rx.badge(
                        exp["date"],
                        size="2",
                        class_name="date-badge-inline",
                    ),
                    spacing="2",
                    align_items="start",
                    width="100%",
                ),
                width="100%",
                justify="between",
                align_items="start",
                class_name="experience-header",
            ),
            # Description
            rx.markdown(
                exp["description"],
                class_name="experience-description",
            ),
            spacing="3",
            align_items="start",
            width="100%",
        ),
        class_name=f"experience-card-modern slide-in-left stagger-{index}",
    )


def get_featured_projects(projects):
    """Get top 6 projects with awards/achievements"""
    # Indices of your award-winning projects
    featured_indices = [
        0,
        1,
        2,
        3,
        4,
        5,
    ]  # Route Optimization, Quotify, Code With Me, uOCTF, QNX, Sweatris
    return [projects[i] for i in featured_indices if i < len(projects)]


def get_other_projects(projects):
    """Get remaining projects"""
    return projects[6:]  # Everything after the first 6


def blog_card(blog, index=0):
    """Modern blog card - responsive design"""
    component_map = {
        "a": lambda text, **props: rx.link(text, **props, is_external=True),
    }

    return rx.box(
        rx.vstack(
            # Date badge
            rx.badge(
                blog["date"],
                class_name="blog-date-badge",
                size="2",
            ),
            # Title
            rx.heading(
                blog["title"],
                size="6",
                class_name="blog-title",
            ),
            # Preview
            rx.text(
                (
                    blog["description"][:150] + "..."
                    if len(blog["description"]) > 150
                    else blog["description"]
                ),
                class_name="blog-preview",
                size="3",
            ),
            # Read more button
            rx.dialog.root(
                rx.dialog.trigger(
                    rx.button(
                        "Read More →",
                        class_name="blog-read-btn",
                        size="2",
                        variant="soft",
                    )
                ),
                rx.dialog.content(
                    rx.dialog.title(blog["title"]),
                    rx.text(
                        blog["date"], class_name="dialog-date", margin_bottom="1em"
                    ),
                    rx.box(
                        rx.markdown(
                            blog["description"],
                            component_map=component_map,
                        ),
                        max_height="60vh",
                        overflow_y="auto",
                        padding_right="1em",
                        class_name="dialog-description",
                    ),
                    rx.dialog.close(
                        rx.button("Close", size="3", class_name="dialog-close-btn"),
                    ),
                    max_width="900px",
                    class_name="project-dialog",
                ),
            ),
            spacing="3",
            align_items="start",
            width="100%",
        ),
        class_name=f"blog-card fade-in-scale stagger-{index % 6}",
    )
