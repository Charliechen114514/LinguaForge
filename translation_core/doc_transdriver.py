from abc import abstractmethod, ABCMeta

class DocumentDriverBase(metaclass=ABCMeta):
    def __init__(self):
        self.__src_langtype = "auto" 
        self.__dest_langtype = "zh-cn" 

    @property
    def src_lang_type(self):
        return self.__src_langtype

    @src_lang_type.setter
    def src_lang_type(self, value):
        self.__src_langtype = value

    @property
    def dest_lang_type(self):
        return self.__dest_langtype

    @dest_lang_type.setter
    def dest_lang_type(self, value):
        self.__dest_langtype = value

    """
        set the translation source text if possible
        this can be null typically
    """
        
    @abstractmethod
    def translate_text(self, text: str) -> str:
        pass
