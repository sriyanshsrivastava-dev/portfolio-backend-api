from abc import ABC, abstractmethod
from django.core.files.storage import default_storage


class FileUploader(ABC):
    @classmethod
    @abstractmethod
    def upload(cls,file,file_name:str)-> str:
        pass


class LocalFileUploader(FileUploader):
    @classmethod
    def upload(cls,file,file_name)-> str:
        path = default_storage.save(
            f"projects/media/{file_name}",
            file
        )
        return default_storage.url(path)