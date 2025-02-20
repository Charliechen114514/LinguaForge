from documentation_io.raw_document_reader import RawDocumentReader

testing_gbk_path = 'tests\\doc_test\\gbk_read.md'

def simple_read() -> str:
    with open(testing_gbk_path, 'r', encoding='gb18030') as f:
        return f.read()

def test_read_gbk_document():
    assert simple_read() == \
        RawDocumentReader.read_document_buffer(testing_gbk_path)