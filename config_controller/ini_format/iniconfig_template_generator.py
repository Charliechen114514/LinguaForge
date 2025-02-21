from config_controller.config_template_generator import TemplateConfigFormat
from linguaforge.translator_cli_interface import \
    SingleFileCLICommandArgPasser, BatchFileCLICommandArgPasser, ALL_IN_ONE, INSERT_IN
import configparser, os
config = configparser.ConfigParser()

config_content = \
"""
# This is the configuration file for single documentations
# The thing you must specify is the src_doc, dest_lang, split_colon
# others will use the default!
"""

STR_TYPE_SIN_FILE = "single-file"
STR_TYPE_DOC_TREE = "doc-tree"

BATCH_SUMMON_TYPE_ALL_IN_ONE = "all-in-one"
BATCH_SUMMON_TYPE_INSERT_DIR = "insert-in"

class IniFormatFile(TemplateConfigFormat):
    def __init__(self):
        super().__init__()

    @staticmethod
    def __set_as_single_type():
        config["type"] = {
            "anatype": STR_TYPE_SIN_FILE
        }
        config["document_path"] = {
            "src_doc": "",
            "dest_doc": ""
        }

        config["langs_settings"] = {
            "dest_lang": "",
            "split_colon":""
        }

    @staticmethod
    def __handle_process_as_single_doc() -> SingleFileCLICommandArgPasser:
            src_doc = config["document_path"].get("src_doc", "").strip('"').strip("'") or ""
            dest_doc = config["document_path"].get("dest_doc", "").strip('"').strip("'") or ""
            dest_lang = config["langs_settings"].get("dest_lang", "").strip('"').strip("'") or ""
            split_col = config["langs_settings"].get("split_colon", "").strip('"').strip("'")

            if not os.path.exists(src_doc):
                raise FileNotFoundError(f"Can not find waiting trans file: \n" \
                                    f"{os.path.abspath(src_doc)}!\n"\
                                    "Specify the path carefully!") 

            if dest_lang == "":
                raise ValueError("You must specify the dest language for translation!")

            if split_col == "":
                raise ValueError("Can not accept empty splits")
            
            return SingleFileCLICommandArgPasser(src_doc_path=src_doc,
                                   dest_doc_path=dest_doc,
                                   dest_lang=dest_lang,
                                   split_colon=split_col)

    def __set_as_doc_tree_type():
        config["type"] = {
            "anatype": STR_TYPE_DOC_TREE
        }
        config["document_path"] = {
            "src_dir": "",
            "dest_type": "",
            "dest_dir": ""
        }        
        config["langs_settings"] = {
            "dest_lang": "",
            "split_colon":""
        }

    @staticmethod
    def __handle_process_as_batch() -> BatchFileCLICommandArgPasser:  
        src_dir = config["document_path"].get("src_dir", "").strip('"').strip("'") or ""
        dest_type = config["document_path"].get("dest_type", "").strip('"').strip("'") or ""
        dest_dir =  config["document_path"].get("dest_dir", ".").strip('"').strip("'") or "."
        dest_lang = config["langs_settings"].get("dest_lang", "").strip('"').strip("'") or ""
        split_colon = config["langs_settings"].get("split_colon", "").strip('"').strip("'") or ""
  
        if not os.path.exists(src_dir):
            raise FileNotFoundError(f"Can not find waiting trans file: \n" \
                                    f"{os.path.abspath(src_dir)}!\n"\
                                    "Specify the path carefully!") 

        if dest_type.strip().lower() == BATCH_SUMMON_TYPE_ALL_IN_ONE:
            batch_type = ALL_IN_ONE
        elif dest_type.strip().lower() == BATCH_SUMMON_TYPE_INSERT_DIR:
            batch_type = INSERT_IN
        else:
            raise ValueError(f"{dest_type} is not a valid batch process method!")
        
        if dest_lang == "":
            raise ValueError("You must specify the dest language for translation!")

        if split_colon == "":
            raise ValueError("Can not accept empty splits")        

        return BatchFileCLICommandArgPasser(
            src_dir_path=src_dir, dest_type=batch_type,
            dest_dirent=dest_dir, dest_lang=dest_lang, split_colon=split_colon
        )

    def gen_empty_template(self, path: str, type_create: int):
        if type_create == TemplateConfigFormat.SINGLE_TYPE:
            IniFormatFile.__set_as_single_type()
        else:
            IniFormatFile.__set_as_doc_tree_type()
        with open(path, "w") as configfile:
            configfile.write(config_content)
            config.write(configfile)


    def createSingleFilePasser(self, path: str) -> SingleFileCLICommandArgPasser:
        if not os.path.exists(path):
            raise FileNotFoundError(f"Can not find file: \n" \
                                    f"{os.path.abspath(path)}!\n"\
                                    "Specify the path carefully!")        
        config.read(path, encoding="utf-8")
        type_create = config["type"].get("type", "").strip('"').strip("'")
        if type_create != STR_TYPE_SIN_FILE:
            raise ValueError("Wrong use of ini file, this is not a single file ini")    
        
        return IniFormatFile.__handle_process_as_single_doc()

    def createBatchFilePasser(self, path: str) -> BatchFileCLICommandArgPasser:
        if not os.path.exists(path):
            raise FileNotFoundError(f"Can not find file: \n" \
                                    f"{os.path.abspath(path)}!\n"\
                                    "Specify the path carefully!")        
        config.read(path, encoding="utf-8")
        type_create = config["type"].get("anatype", "").strip('"').strip("'")
        if type_create != STR_TYPE_DOC_TREE:
            raise ValueError("Wrong use of ini file, this is not a doc file ini")    
        
        return IniFormatFile.__handle_process_as_batch()        


    
