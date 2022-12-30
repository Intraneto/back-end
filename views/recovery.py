import flet as ft


def main(page: ft.Page):
    return ft.Column(
        [
            ft.Text("Recovery", size=32),
            ft.Text("Username"),
            ft.TextField(
                autofocus=True,
                hint_text="example@intraneto.com",
            ),
            ft.Divider(),
            ft.Text("You also may want to...", size=16),
            ft.TextButton(
                "Access your account",
                on_click=lambda _: page.go("/signin"),
            ),
            ft.TextButton(
                "Create an account",
                on_click=lambda _: page.go("/signup"),
            ),
            ft.TextButton(
                "Recover your password",
                on_click=lambda _: page.go("/recovery"),
            ),
        ],
        width=300,
    )
