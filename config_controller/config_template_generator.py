from abc import abstractmethod, ABCMeta
from linguaforge.translator_cli_interface import \
    SingleFileCLICommandArgPasser, BatchFileCLICommandArgPasser
from pathlib import Path

class TemplateConfigFormat(metaclass=ABCMeta):
    SINGLE_TYPE = 1
    DOC_TREE_TYPE = 2
    def __init__(self):
        pass

    @staticmethod
    def supportive_format() -> list[str]:
        return ['ini']
    
    @staticmethod
    def display_support_format_string() -> str:
        lists = TemplateConfigFormat.supportive_format()
        contains = 5
        return "\n".join(" ".join(\
            lists[i:i+contains]) for i in range(0, len(lists), contains))

    @staticmethod
    def generate_file_accord_type(type: str, path: str, type_create: int):
        if type.lower() == "ini":
            from config_controller.ini_format.iniconfig_template_generator import IniFormatFile
            IniFormatFile().gen_empty_template(path=path, type_create=type_create)

    @staticmethod
    def do_singlefile_parse_config(path: str) -> SingleFileCLICommandArgPasser:
        suffix = Path(path).suffix.lstrip(".").lower()
        if suffix == "ini":
            from config_controller.ini_format.iniconfig_template_generator import IniFormatFile
            return IniFormatFile().createSingleFilePasser(path)
        else:
            raise ValueError("Unrecognize format!")

    @staticmethod
    def do_batchfile_parse_config(path: str) -> BatchFileCLICommandArgPasser:
        suffix = Path(path).suffix.lstrip(".").lower()
        if suffix == "ini":
            from config_controller.ini_format.iniconfig_template_generator import IniFormatFile
            return IniFormatFile().createBatchFilePasser(path)
        else:
            raise ValueError("Unrecognize format!")


    @abstractmethod
    def gen_empty_template(self, path: str, type_create: int):
        pass

    @abstractmethod
    def createSingleFilePasser(self, path: str) -> SingleFileCLICommandArgPasser:
        pass

    @abstractmethod
    def createBatchFilePasser(self, path: str) -> SingleFileCLICommandArgPasser:
        pass    
