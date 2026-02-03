import reflex as rx

config = rx.Config(
    app_name="dashboard",
    api_url="https://dashboard-re25.onrender.com:8000",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)