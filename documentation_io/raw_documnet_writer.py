class RawDocumentWriter:
    """
        default encoding method is gb18030, while you can also try 
    """
    @staticmethod
    def write_document_buffer(path: str, buffers: str):
        with open(path, 'w', encoding='utf-8') as f:
            f.write(buffers)
