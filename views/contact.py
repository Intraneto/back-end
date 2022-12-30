# Contact form view

# Path: websites/intraneto.com/app/views/contact.py

# Compare this snippet from websites/intraneto.com/app/views/auth.py:

import flet as ft
from components import navbar


def main(page: ft.Page):
    return ft.View(
        "/",
        [
            navbar.main(page),
            ft.Column(
                [
                    ft.Text("Username"),
                    ft.TextField(
                        autofocus=True,
                        hint_text="your username",
                    ),
                    ft.Text("Message"),
                    ft.TextField(
                        hint_text="your message",
                        multiline=True,
                        min_lines=10,
                        max_lines=10,
                    ),
                    ft.FilledButton(
                        "Send",
                        on_click=lambda e: page.go("/"),
                    ),
                    # go back
                    ft.TextButton(
                        "Back",
                        on_click=lambda _: page.go("/"),
                    ),
                ],
                expand=1,
                width=300,
                alignment="center",
            ),
        ],
        horizontal_alignment="center",
    )


# Contact form view

# Path: websites/intraneto.com/app/views/contact.py
