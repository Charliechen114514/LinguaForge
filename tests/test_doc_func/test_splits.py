from translation_core import DefaultSpliter, TextToken
from documentation_io.raw_document_reader import RawDocumentReader

test_doc = "tests\\doc_test\\splitive_test.md"

def test_split_length():
    raw_text = RawDocumentReader.read_document_buffer(test_doc, encoding='utf-8')
    default_spliter = DefaultSpliter()
    default_spliter.set_spliter_colon('。')
    default_spliter.set_raw_text(raw_text)
    result: list[TextToken] = default_spliter.fetch_indexsive_text()
    for each in result:
        assert len(each.text) <= DefaultSpliter.MAX_LENGTH

