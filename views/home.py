import os
import textwrap

import flet as ft
from components import navbar, sidebar

# def get_app(name: str, page: ft.Page):
#     return ft.FilledButton(
#         name.capitalize(),
#         on_click=lambda _: page.go(f"/{name}"),
#         height=100,
#         width=100,
#     )


def main(page: ft.Page):
    page.title = "GridView Example"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 50
    page.update()

    # images = ft.GridView(
    #     expand=0,
    #     runs_count=5,
    #     max_extent=150,
    #     child_aspect_ratio=1.0,
    # )

    # page.add(images)
    # for app in sorted(os.listdir("views")):
    #     if app.endswith(".py") and not app in ["__init__.py", "home.py", "error404.py"]:
    #         images.controls.append(get_app(app.strip(".py$"), page))
    # page.update()

    return ft.Markdown(
        open(os.path.join(os.path.dirname(__file__), "..", "README.md")).read(),
        width=800,
        expand=1,
    )
