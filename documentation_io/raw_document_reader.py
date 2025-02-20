class RawDocumentReader:
    @staticmethod
    def __raw_read(path:str, encodings: str):
        with open(path, 'r', encoding=encodings) as f:
            return f.read()

    """
        default encoding method is gb18030, while you can also try 
    """
    @staticmethod
    def read_document_buffer(path: str, encoding='gb18030'):
        try:
            return RawDocumentReader.__raw_read(path, encoding)
        except UnicodeDecodeError:
            try:
                return RawDocumentReader.__raw_read(path, 'gb18030')
            except UnicodeDecodeError:
                return RawDocumentReader.__raw_read(path, 'utf-8')