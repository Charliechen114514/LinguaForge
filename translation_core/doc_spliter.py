from abc import abstractmethod, ABCMeta

class TextToken:
    def __init__(self, index:int, text: str):
        self.__index = index
        self.__text = text    

    @property
    def index(self) -> int:
        return self.__index
    
    @property
    def text(self) -> int:
        return self.__text
    
    def set_text(self, text: str):
        self.__text = text


class DocumentSpliterBase(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def set_raw_text(self, text: str):
        pass

    @abstractmethod
    def set_spliter_colon(self, text: str):
        pass

    @abstractmethod
    def set_max_sentence_length(self, max_length: str):
        pass

    @abstractmethod
    def fetch_indexsive_text(self) -> list[TextToken]:
        pass