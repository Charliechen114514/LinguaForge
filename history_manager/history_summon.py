from config_controller.config_template_generator import TemplateConfigFormat
from translation_core.batch_path_maker import SingtonFileInfo
import configparser, os
config = configparser.ConfigParser()

class HistoryManager:
    def __init__(self):
        pass
    @staticmethod
    def __create_section_name(index: int):
        return f"hist{index}"

    @staticmethod
    def write_history_file(path:str, infos: list[SingtonFileInfo]):
        index = 0
        for each_info in infos:
            config[HistoryManager.__create_section_name(index)] = {
                "src_path": each_info.src_path,
                "dest_path": each_info.dest_path
            }
            index += 1
        with open(path, 'w') as configfile:
            config.write(configfile)
        
    @staticmethod
    def review_back(path:str) -> list[SingtonFileInfo]:
        if not os.path.exists(path):
            raise FileNotFoundError(f"Can not find the history file, see the path {path} for details")
        config.read(path)
        res: list[SingtonFileInfo] = []
        for section in config.sections():
            src_path    = config.get(section, "src_path")
            dest_path   = config.get(section, "dest_path")
            res.append(SingtonFileInfo(src_path=src_path, dest_path=dest_path))
        return res