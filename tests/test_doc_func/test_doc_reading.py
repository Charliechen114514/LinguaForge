
from translation_core.doc_translator import *
from translation_core import Document_GoogleTransDriver, DefaultSpliter
from translation_core import DocumentSummon
def test_translations_1():
    translator = DocumentTranslator()
    spliter = DefaultSpliter()
    spliter.set_spliter_colon('。')
    driver = Document_GoogleTransDriver()
    driver.dest_lang_type = 'en'
    translator.set_spliter(spliter)
    translator.set_driver(driver)
    result = translator.generate_target_translation_documentations("tests\\doc_test\\splitive_test.md")
    result.summon_document()
    assert 1

def test_translations_2():
    translator = DocumentTranslator()
    spliter = DefaultSpliter()
    spliter.set_spliter_colon('.')
    driver = Document_GoogleTransDriver()
    driver.dest_lang_type = 'zh-CN'
    translator.set_spliter(spliter)
    translator.set_driver(driver)
    result = translator.generate_target_translation_documentations("tests\\doc_test\\splitive_test_en.md")
    result.summon_document()
    assert 1