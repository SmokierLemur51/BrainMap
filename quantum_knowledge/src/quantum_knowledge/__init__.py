"""

"""


from quart import Quart

"""
"""
from pathlib import Path

from quart import Quart, current_app, render_template, redirect, url_for

from .blueprints.public.routes import public



# App Factory
def create_app() -> Quart:
    app = Quart(__name__, static_url_path="/static")

    app.config.update({
        "DATABASE": Path(app.root_path) / "testing.db",
    })

    app.register_blueprint(public)
        
    return app


"""

"""
def run(app: Quart) -> None:
    app.run(debug=True)
