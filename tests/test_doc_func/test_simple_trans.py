from translation_core import Document_GoogleTransDriver
from documentation_io.raw_document_reader import RawDocumentReader

SIMPLY_TRANS_TEST_DOC = "tests\\doc_test\\simple_trans.md"

def normalize(text: str) -> str:
    return text.strip().lower()

def return_result_en() -> str:
    return "hello world!"



def test_simple_translations():
    driver = Document_GoogleTransDriver()
    driver.dest_lang_type = 'en'
    text = RawDocumentReader.read_document_buffer(SIMPLY_TRANS_TEST_DOC, encoding='utf-8')
    trans = driver.translate_text(text)
    assert normalize(trans) == normalize(return_result_en())