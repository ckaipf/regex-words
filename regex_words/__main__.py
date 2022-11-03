import typer
from typing import Optional

from .regify import app as app_regify

app = typer.Typer()
app.add_typer(app_regify, name="regify")

@app.callback()
def main():
    """
    Derive regular expressions from target strings.
    """

if __name__ == "__main__":
    app()