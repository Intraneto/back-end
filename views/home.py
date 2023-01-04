import os
import textwrap

import flet as ft
from components import navbar, sidebar


def main(page: ft.Page):
    page.title = "Welcome to Intraneto.com"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 50

    images = ft.GridView(
        expand=0,
        runs_count=5,
        max_extent=150,
        child_aspect_ratio=1.0,
    )

    page.add(images)
    for app in sorted(os.listdir("views")):
        if app.endswith(".py") and not app in [
            "__init__.py",
            "home.py",
            "error404.py",
            "error500.py",
        ]:
            images.controls.append(
                ft.FilledButton(
                    text=app.strip(".py").capitalize(),
                    icon=ft.icons.FAVORITE_BORDER,
                    on_click=lambda e: page.go(f"/{e.control.text.lower()}"),
                )
            )

    return ft.Column(
        [
            ft.Markdown(
                textwrap.dedent(
                    """
                    # Welcome to Intraneto.com

                    This is a collection of apps that I have created for my own use. I hope you find them useful.

                    ## Apps

                    """
                )
            ),
            images,
        ],
        expand=1,
        width=800,
        alignment="center",
    )
