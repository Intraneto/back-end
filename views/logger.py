# Have an input field then update the runtime route_view_mapping from start.py to include the new route and view module. Then, when the user clicks the button, the page will navigate to the new route and the new view will be displayed.

# route_view_mapping: Dict[str, str] = {
#     "/": "home",
#     "/about": "about",
#     "/terminal": "terminal",
#     "/console": "console",
#     "/settings": "settings",
#     "/download": "download",
# }

import os

import flet

from app.components import navbar


def main(page: flet.Page):
    # Have an input field to update the route_view_mapping and inject a custom function
    # Important to have a text field to update the route_view_mapping

    return flet.View(
        "/",
        [
            navbar.main(page),
            flet.Row(
                [
                    flet.Text("Views:"),
                    flet.Input(
                        width=100,
                        height=100,
                        on_change=lambda value: route_view_mapping.update(
                            {value: "new"}
                        ),
                    ),
                ]
                + [
                    get_app(app.strip(".py"), page)
                    for app in sorted(
                        os.listdir(
                            os.path.join(os.path.dirname(__file__), "..", "views")
                        )
                    )
                    if app not in ["__init__.py"] and app.endswith(".py")
                ],
                alignment="center",
                scroll=True,
                spacing=16,
                run_spacing=16,
                # wrap=True,
                height=100,
            ),
        ],
    )
