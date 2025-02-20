from translation_core.doc_spliter import DocumentSpliterBase, TextToken

class DefaultSpliter(DocumentSpliterBase):
    MAX_LENGTH = 3000
    def __init__(self):
        self.__splitings: list[str] = []
        self.__max_length = DefaultSpliter.MAX_LENGTH
        self.__split_colon = ""

    def __split_text(self, text: str):
        sentences = text.split(self.__split_colon)  # 按句号分割文本
        self.__splitings = []
        current_paragraph = ""

        for i, sentence in enumerate(sentences):
            # add colon
            if i < len(sentences) - 1:
                sentence += self.__split_colon 

            # check if overflow the max length
            if len(current_paragraph) + len(sentence) <= self.__max_length:
                if current_paragraph:
                    current_paragraph += sentence  # then append
                else:
                    current_paragraph = sentence  # else init
            else:
                self.__splitings.append(current_paragraph) 
                current_paragraph = sentence  

        if current_paragraph: 
            self.__splitings.append(current_paragraph)

    def set_spliter_colon(self, text: str):
        self.__split_colon = text

    def set_max_sentence_length(self, max_length: str):
        self.__max_length = max_length
        
    def set_raw_text(self, text):
        self.__split_text(text)

    def fetch_indexsive_text(self) -> list[TextToken]:
        i = 0
        results: list[TextToken] = []
        for each in self.__splitings:
            results.append(TextToken(i, each))
            i += 1
        return results