import os

from server import App



def register_components_for_app(p_app: App) -> None:

    @p_app.component("image")
    def render_image(p_args: dict) -> str:
        return f"<img src={ "/public/" + p_args.get("path").lstrip("/") }>"