import flet as ft


def main(page: ft.Page):
    def check_item_clicked(e):
        e.control.checked = not e.control.checked
        page.update()

    return ft.AppBar(
        leading=ft.Icon(ft.icons.PALETTE),
        leading_width=40,
        title=ft.TextButton("Intraneto.com", on_click=lambda _: page.go("/")),
        center_title=False,
        bgcolor=ft.colors.SURFACE_VARIANT,
        actions=[
            ft.TextField(hint_text="Search", border_radius=0),
            ft.TextButton("Login", on_click=lambda _: page.go("/signin")),
            ft.TextButton("Sign Up", on_click=lambda _: page.go("/signup")),
            ft.IconButton(ft.icons.FILTER_3),
            ft.IconButton(
                icon=ft.icons.SETTINGS,
                on_click=lambda _: page.go("/settings"),
            ),
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(text="Item 1"),
                    ft.PopupMenuItem(),  # divider
                    ft.PopupMenuItem(
                        text="Checked item", checked=False, on_click=check_item_clicked
                    ),
                ],
                icon=ft.icons.MENU,
            ),
        ],
    )
