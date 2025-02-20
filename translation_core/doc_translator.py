from translation_core.doc_transdriver import DocumentDriverBase
from translation_core.doc_myerror import *
from translation_core.doc_spliter import DocumentSpliterBase
from translation_core.doc_trans_sched import DocumenTranslationSchedler
from translation_core.doc_summon_controller import DocumentSummon

class DocumentTranslator:
    def __init__(self):
        self.__driver = None
        self.__spliter = None
        

    def __check(self):
        if self.__driver is None:
            raise NoneDriverSpecified()
        if self.__spliter is None:
            raise NoneSpliterSpecified()
        return

    def set_driver(self, driver: DocumentDriverBase):
        self.__driver = driver

    def set_spliter(self, spliter: DocumentSpliterBase):
        self.__spliter = spliter

    def generate_target_translation_documentations(self, doc_path: str) -> DocumentSummon:
        self.__check()
        sched = DocumenTranslationSchedler(self.__driver, self.__spliter)
        result = sched.translate_document(doc_path)
        default_name = DocumentSummon.default_policy_name(
                doc_path, self.__driver.dest_lang_type)
        summon = DocumentSummon(default_name, result)
        return summon