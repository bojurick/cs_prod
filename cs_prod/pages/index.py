"""The overview page of the app."""

import reflex as rx
from .. import styles
from ..templates import template


@template(route="/", title="index")
def index() -> rx.Component:
    """The overview page.

    Returns:
        The UI for the overview page.
    """
    return rx.text("Welcome to the overview page!")
