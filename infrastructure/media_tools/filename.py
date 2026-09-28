from abc import ABC, abstractmethod
from pathlib import Path
import secrets


class FileNameGenerator(ABC):
    @classmethod
    @abstractmethod
    def generate(cls,extension:str)-> str:
        pass


class HexFileNameGenerator(FileNameGenerator):

    @classmethod
    def generate(cls, extension: str) -> str:
        return f"{secrets.token_hex(16)}.{extension.lstrip('.')}"