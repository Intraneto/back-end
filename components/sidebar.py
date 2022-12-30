import os

import flet as ft


def main(page: ft.Page):
    def get_app(name: str):
        return ft.NavigationRailDestination(
            icon=ft.icons.FAVORITE_BORDER,
            selected_icon=ft.icons.FAVORITE,
            label=name.capitalize(),
        )

    destinations = []

    for app in sorted(
        os.listdir(os.path.join(os.path.dirname(__file__), "..", "views"))
    ):
        if app not in ["__init__.py"] and app.endswith(".py"):
            destinations.append(get_app(app.strip(".py")))

    return ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        extended=True,
        # group_alignment=-0.9,
        # on_change=lambda e: print("Selected destination:", e.control.selected_index),
        on_change=lambda e: page.go(
            f"/{destinations[e.control.selected_index].label.lower()}"
        ),
        destinations=destinations,
    )
