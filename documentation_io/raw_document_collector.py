import os
class RawDocumentCollector:
    @staticmethod
    def collect_documents(dir:str, suffixs_check: list[str]) -> list[str]:
        if not os.path.exists(dir):
            raise FileNotFoundError(
                f"Can not collect documents at a non-exsit dirent: {dir}")
        
        if not os.path.isdir(dir):
            raise ValueError(
                f"Provide a dirent instead of a file path!"
            )

        matched_files = []
        for root, dirs, files in os.walk(dir):  # 使用os.walk递归遍历文件夹
            for file in files:
                if file.endswith(tuple(suffixs_check)):  # 将列表转换为元组传递给endswith
                    matched_files.append(os.path.join(root, file))  # 添加符合条件的文件路径
        return matched_files
