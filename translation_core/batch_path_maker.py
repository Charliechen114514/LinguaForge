from dataclasses import dataclass
from typing import Callable
import os
from pathlib import Path
from documentation_io.raw_document_collector import RawDocumentCollector


MappingPolicy = Callable[[list[str]], str]

@dataclass 
class SingtonFileInfo:
    src_path:   str
    dest_path:  str


def all_in_one_policy(paths_info: list[str]) -> str:
    ROOT_DIR = paths_info[0]
    TARGET_FOR_EACH = paths_info[1]
    return os.path.join(ROOT_DIR, TARGET_FOR_EACH)

def insertive_all(paths_info: list[str]) -> str:
    doc_path = paths_info[0]
    lang_type = paths_info[1]
    return  str(Path(doc_path).parent / str(Path(doc_path).stem + \
            "_" + lang_type + Path(doc_path).suffix))


class BatchFilePathMaker:
    def __init__(self):
        self.__mapping_policy: MappingPolicy = None

    @staticmethod
    def display_lists(display: list[SingtonFileInfo]):
        result = ""
        index = 1
        for each_singlt in display:
            result += f"[bold green]{index}: [bold yellow]{each_singlt.src_path} -> [bold green]{each_singlt.dest_path}\n"
            index += 1
        return result

    def register_mapping_policy(self, policy_maker: MappingPolicy):
        self.__mapping_policy = policy_maker

    def provide_making_lists(self, srcs: list[str], policy_reqs: list[list[str]]) -> list[SingtonFileInfo]:
        if len(srcs) != len(policy_reqs):
           raise ValueError("Can not matchings size of srcs and policies")
       
        res: list[SingtonFileInfo] = []
        index = 0
        for each in srcs:
           res.append(SingtonFileInfo(
               src_path=each, 
               dest_path=self.__mapping_policy(policy_reqs[index])))
           index += 1
        return res

    @staticmethod
    def provide_insertive_policy_result(
        root_dir: str, lang_type: str, suffixs: list[str]) -> list[SingtonFileInfo]:
        maker = BatchFilePathMaker()
        maker.register_mapping_policy(insertive_all)
        files = RawDocumentCollector.collect_documents(root_dir, suffixs)
        policys = []
        for file in files:
            policys.append([file, lang_type])
        return maker.provide_making_lists(files, policys)     

    @staticmethod
    def __makeup_files(file_path: str, lang_type: str):
        return str(Path(file_path).stem + \
            "_" + lang_type + Path(file_path).suffix)

    @staticmethod
    def provide_all_in_one_policy_result(
        root_dir: str,dest_dir: str, lang_type: str, suffixs: list[str]
    ):
        maker = BatchFilePathMaker()
        maker.register_mapping_policy(all_in_one_policy)
        files = RawDocumentCollector.collect_documents(root_dir, suffixs)
        policys = []
        for file in files:
            policys.append([dest_dir, BatchFilePathMaker.__makeup_files(file, lang_type)])
        return maker.provide_making_lists(files, policys)




