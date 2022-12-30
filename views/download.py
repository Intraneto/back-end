import flet
from components import navbar


def main(page: flet.Page):
    return flet.View(
        "/download",
        [
            navbar.main(page),
            flet.Column(
                [
                    flet.Markdown(open("content/download.md").read()),
                ],
                expand=1,
                width=800,
                alignment="center",
            ),
        ],
        horizontal_alignment="center",
    )
