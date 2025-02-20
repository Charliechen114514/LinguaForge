from translation_core.doc_transdriver import DocumentDriverBase
from translation_core.doc_spliter import DocumentSpliterBase, TextToken
from documentation_io.raw_document_reader import RawDocumentReader
import concurrent.futures

class DocumenTranslationSchedler():
    MAX_THREAD_NUM = 5
    def __init__(self, driver: DocumentDriverBase, spliter: DocumentSpliterBase):
        self.max_thread_num = DocumenTranslationSchedler.MAX_THREAD_NUM
        self.__spliter = spliter
        self.__driver = driver
        self.__waitings: list[TextToken] = []

    def __sorted_result(self):
        self.__waitings.sort(key=lambda item: item.index)
    
    def __translation_single_text(self, textToken: TextToken):
        result = self.__driver.translate_text(text=textToken.text)
        textToken.set_text(result)

    def __read_doc(self, path: str) -> str:
        return RawDocumentReader.read_document_buffer(path=path)

    def translate_document(self, path: str) -> str:
        raw = self.__read_doc(path)
        self.__spliter.set_raw_text(raw)
        self.__waitings = self.__spliter.fetch_indexsive_text()
        with concurrent.futures.ThreadPoolExecutor(
                max_workers=DocumenTranslationSchedler.MAX_THREAD_NUM) as executor:
            future_to_text = {executor.submit(self.__translation_single_text, token): token for token in self.__waitings}
            for _ in concurrent.futures.as_completed(future_to_text):
                continue
        self.__sorted_result()
        result = ""
        for each in self.__waitings:
            result += each.text
        return result