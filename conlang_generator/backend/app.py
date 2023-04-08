from pathlib import Path

from project import Project

class ConlangCreator:
    def __init__(self) -> None:
        self.current_project_dir = None
        self.current_project = None

    def load_project_from_file_path(self, file_path: Path) -> None:
        self.current_project_dir = file_path
        with open(file_path, "r") as file:
            self.__load_project(self.__parse_project_file(file))

    def __load_project(self, project: Project) -> None:
        self.current_project = project

    def __parse_project_file(self, file: str) -> Project:
        pass

    def save_project_to_file_path(self, file_path: Path) -> None:
        with open(file_path, "w") as file:
            file.write(self.__write_project_file(self.current_project))

    def __write_project_file(self, project: Project) -> str:
        pass
