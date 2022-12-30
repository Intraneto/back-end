import flet as ft


def main(page: ft.Page):
    return ft.Column(
        [
            ft.Text("Login", size=32),
            ft.Text("Username"),
            ft.TextField(
                autofocus=True,
                hint_text="example@intraneto.com",
            ),
            ft.Text("Password"),
            ft.TextField(password=True),
            ft.Row(
                [
                    ft.FilledButton(
                        "Continue",
                        on_click=lambda e: page.go("/"),
                    ),
                    # inline, continue as guest
                    ft.OutlinedButton(
                        "Continue as guest",
                        on_click=lambda e: page.go("/"),
                    ),
                ],
            ),
            ft.Divider(),
            ft.Text("You also may want to...", size=16),
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
