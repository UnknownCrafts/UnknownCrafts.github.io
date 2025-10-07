import reflex as rx


def card_item(imagesrc, heading, text, href):
    return (
        rx.card(
            rx.link(
                rx.flex(
                    rx.avatar(
                        src=imagesrc,
                        style={
                            "filter": rx.color_mode_cond(
                                dark="invert(1) brightness(0.8)", light="invert(0)"
                            )
                        },
                    ),
                    rx.box(
                        rx.heading(heading),
                        rx.text(text),
                    ),
                    spacing="2",
                ),
                href=href,
                underline="none",
                is_external=True,
            ),
        ),
    )


def timeline_item(project):
    component_map = {
        "a": lambda text, **props: rx.link(text, **props, is_external=True),
    }
    return rx.vstack(
        rx.text(
            project["date"],
            font_size="0.9em",
            color="#6c757d",  # Muted gray for subtlety
            margin_bottom="4px",
        ),
        rx.heading(
            project["title"],
            font_size="1.2em",
            font_weight="bold",
            color="#343a40",  # Darker color for emphasis
            margin_bottom="6px",
        ),
        rx.markdown(
            project["description"],
            font_size="1em",
            color="#495057",  # Standard text color for readability
            component_map=component_map,
        ),
        rx.dialog.root(
            rx.dialog.trigger(rx.button("View More")),
            rx.dialog.content(
                rx.dialog.title(project["title"]),
                rx.markdown(
                    project["description"],
                    margin_bottom="10px",
                ),
                rx.dialog.close(
                    rx.button("Close", size="2"),
                ),
            ),
        ),
        spacing="2",  # Space between elements in the vertical stack
        padding="5px",  # Internal padding for better spacing
        background_color="#f8f9fa",  # Light background for contrast
        border="1px solid #dee2e6",  # Soft border for structure
        border_radius="12px",  # Slightly rounded corners
        box_shadow="0 4px 6px rgba(0, 0, 0, 0.1)",  # Subtle shadow for depth
        margin_bottom="16px",  # Consistent bottom margin for stacking
    )
