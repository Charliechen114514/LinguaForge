from deep_translator import GoogleTranslator
from translation_core.doc_transdriver import DocumentDriverBase

class Document_GoogleTransDriver(DocumentDriverBase):
    def __init__(self):
        super().__init__()
        self.__translator_pvt = None
        pass

    def translate_text(self, text: str) -> str:
        if self.src_lang_type == "":
            self.src_lang_type = "auto"
        self.__translator_pvt = GoogleTranslator(
            self.src_lang_type, self.dest_lang_type)
        return self.__translator_pvt.translate(text)