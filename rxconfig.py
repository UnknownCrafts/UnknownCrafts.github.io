import reflex as rx

config = rx.Config(
    app_name="surya_website",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.RadixThemesPlugin(
            theme=rx.theme(
                appearance="dark",
                has_background=True,
                radius="medium",
                accent_color="indigo",
                gray_color="slate",
            )
        ),
    ],
    show_built_with_reflex=False,
)
