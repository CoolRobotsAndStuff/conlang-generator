from pathlib import Path
import json

from conlang_generator.backend.project.templates.project_template import ProjectTemplate, ProjectTemplateManager

class ConlangCreator:
    def __init__(self) -> None:
        self.current_project_dir: Path = None
        self.project_manager = ProjectTemplateManager()

    def load_project_from_file_path(self, file_path: Path) -> None:
        self.current_project_dir = file_path
        with open(file_path, "r") as file:
            project_dict = json.loads(file)
            self.project_manager.from_data(project_dict)

    def save_project_to_file_path(self, file_path: Path) -> None:
        with open(file_path, "w") as file:
            project_dict = self.project_manager.to_data()
            file.write(json.dumps(project_dict))
