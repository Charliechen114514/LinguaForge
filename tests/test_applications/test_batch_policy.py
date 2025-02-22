from translation_core.batch_path_maker import \
    BatchFilePathMaker, all_in_one_policy, insertive_all
from linguaforge.translator_cli_interface import SingleDocumentTranslatorCLI
from documentation_io.raw_document_collector import RawDocumentCollector
import os
from pathlib import Path

def makeup_files(file_path: str, lang_type: str):
    return str(Path(file_path).stem + \
            "_" + lang_type + Path(file_path).suffix)

def test_maker():
    maker = BatchFilePathMaker()
    maker.register_mapping_policy(all_in_one_policy)
    files = RawDocumentCollector.collect_documents("tests/doc_test", ["md"])
    lang_type = "en"
    root_path = "tests/demo_contain"
    policys = []
    for file in files:
        policys.append([root_path, makeup_files(file, lang_type)])
    result = maker.provide_making_lists(files, policys)
    res = BatchFilePathMaker.display_lists(result)
    print(res)

    maker.register_mapping_policy(insertive_all)
    for file in files:
        policys.append([file, lang_type])
    result = maker.provide_making_lists(files, policys)
    res = BatchFilePathMaker.display_lists(result)
    print(res)

    assert 1