import json
from pathlib import Path
import yaml
from jsonschema import Draft202012Validator

def validate_project(project_path: str, schema_path: str) -> list[str]:
    project = yaml.safe_load(Path(project_path).read_text(encoding="utf-8"))
    schema = json.loads(Path(schema_path).read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema)
    return [error.message for error in sorted(validator.iter_errors(project), key=lambda e: list(e.path))]
