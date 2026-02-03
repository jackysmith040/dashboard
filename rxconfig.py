import reflex as rx

config = rx.Config(
    app_name="dashboard",
    api_url="https://dashboard-ygop.onrender.com",
    show_built_with_reflex=False,
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)