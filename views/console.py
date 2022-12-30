import flet
from components import navbar
from flet import View


def main(page: flet.Page):
    # Create the REPL component
    # repl = Repl(language="python")

    # Add the REPL component to the view
    return View(
        "/",
        [
            navbar.main(page),
            # repl,
        ],
    )
