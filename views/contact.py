import flet


def main(page: flet.Page):
    return flet.Column(
        [
            flet.Text("Username"),
            flet.TextField(
                autofocus=True,
                hint_text="your username",
            ),
            flet.Text("Message"),
            flet.TextField(
                hint_text="your message",
                multiline=True,
                min_lines=10,
                max_lines=10,
            ),
            flet.FilledButton(
                "Send",
                on_click=lambda e: page.go("/"),
            ),
            # go back
            flet.TextButton(
                "Back",
                on_click=lambda _: page.go("/"),
            ),
        ],
        expand=1,
    )
