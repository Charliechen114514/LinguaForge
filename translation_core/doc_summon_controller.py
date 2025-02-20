from pathlib import Path
from documentation_io.raw_documnet_writer import RawDocumentWriter

class DocumentSummon:
    def __init__(self,default_path: str, ready_write: str):
        self.__ready_write = ready_write
        self.__path_write = default_path
    
    @staticmethod
    def default_policy_name(doc_path: str, suffix: str) -> str:
        return Path(doc_path).parent / str(Path(doc_path).stem + "_" + suffix + Path(doc_path).suffix)

    def redirect_path(self, path: str):
        self.__path_write = path

    def summon_document(self):
        RawDocumentWriter.write_document_buffer(self.__path_write, self.__ready_write)