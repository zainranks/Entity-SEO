from pathlib import Path
import typer
from .validator import validate_project

app = typer.Typer(no_args_is_help=True)

@app.command()
def validate(project: str, schema: str = "schemas/project-input.schema.json") -> None:
    errors = validate_project(project, schema)
    if errors:
        for error in errors:
            typer.echo(f"ERROR: {error}")
        raise typer.Exit(code=1)
    typer.echo("Project configuration is valid.")

@app.command()
def init(destination: str = ".") -> None:
    path = Path(destination)
    path.mkdir(parents=True, exist_ok=True)
    typer.echo(f"Initialize from examples/project.example.yaml in {path.resolve()}")

if __name__ == "__main__":
    app()
