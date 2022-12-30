import flet as ft


def main(page: ft.Page):

    t = ft.Tabs(
        selected_index=1,
        animation_duration=300,
        tabs=[
            ft.Tab(
                text="Tab 1",
                content=ft.Container(
                    content=ft.Text("This is Tab 1"), alignment=ft.alignment.center
                ),
            ),
            ft.Tab(
                tab_content=ft.Icon(ft.icons.SEARCH),
                content=ft.Text("This is Tab 2"),
            ),
            ft.Tab(
                text="Tab 3",
                icon=ft.icons.SETTINGS,
                content=ft.Text("This is Tab 3"),
            ),
        ],
        expand=1,
    )

    page.add(t)

    return ft.Column(
        [
            t,
        ],
        expand=1,
    )
