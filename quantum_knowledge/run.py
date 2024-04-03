from src.quantum_knowledge import create_app
from quart import Quart

app = create_app()


def run(app: Quart) -> None:
    app.run(debug=True)

if __name__ == "__main__":
    run(app)