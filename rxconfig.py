import reflex as rx

config = rx.Config(
    app_name="dashboard",
    backend_port=4000,
    frontend_port=3000,
    show_built_with_reflex=False,
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)