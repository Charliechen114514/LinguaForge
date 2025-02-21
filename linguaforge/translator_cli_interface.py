from translation_core import DocumentTranslator, Document_GoogleTransDriver, DefaultSpliter
from translation_core.doc_summon_controller import DocumentSummon
from dataclasses import dataclass
ALL_IN_ONE:int = 1
INSERT_IN: int = 2


@dataclass
class SingleFileCLICommandArgPasser:
    src_doc_path: str
    dest_doc_path: str
    split_colon: str
    dest_lang: str = "en"
    def __str__(self):
        return  f"source_document_path: {self.src_doc_path}\n"\
                f"The splition colon is: {self.split_colon}\n"\
                f"destination lang: {self.dest_lang}\n"\
                f"destination summon document path: {self.dest_doc_path}"

@dataclass
class BatchFileCLICommandArgPasser:
    src_dir_path: str
    dest_type: int
    dest_dirent: str
    split_colon: str
    dest_lang: str = "en"
    def __str__(self):
        src =   f"source_document_path: {self.src_dir_path}\n"\
                f"The splition colon is: {self.split_colon}\n"\
                f"destination lang: {self.dest_lang}\n"
        if self.dest_type == ALL_IN_ONE:
            src += "destination summon method: summon in one_dirent: {}".format(self.dest_dirent)
        else:  
            src += f"destination summon method: inside the doc tree"    
        return src


class DocumentTranslatorCLI:
    def __init__(self):
        self.__hoding_config = None

    def fetch_default_summon_path(self) -> str:
        return DocumentSummon.default_policy_name(
            self.__hoding_config.src_doc_path, 
            self.__hoding_config.dest_lang)

    def register_singledocument_args(self, args: SingleFileCLICommandArgPasser):
        self.__hoding_config = args
        if args.dest_doc_path == "":
            self.__hoding_config.dest_doc_path = self.fetch_default_summon_path()
        return

    def register_batchdocument_args(self, args: BatchFileCLICommandArgPasser):
        self.__hoding_config = args    

    @staticmethod
    def def_engine_lang_supports() -> str:
        lists = Document_GoogleTransDriver.supportive_dest_lang()
        contains = 5
        return "\n".join(" ".join(\
            lists[i:i+contains]) for i in range(0, len(lists), contains))


    def config_info(self) -> str:
        return str(self.__hoding_config)
    
    def process_translations(self) -> str:
        translator = DocumentTranslator()
        spliter = DefaultSpliter()
        spliter.set_spliter_colon(self.__hoding_config.split_colon)
        driver = Document_GoogleTransDriver()
        driver.dest_lang_type = self.__hoding_config.dest_lang
        translator.set_spliter(spliter)
        translator.set_driver(driver)
        result = translator.generate_target_translation_documentations(self.__hoding_config.src_doc_path)
        return result.summon_document()