import os
import shutil

def delete_folders(root_dir):
    for dirpath, dirnames, filenames in os.walk(root_dir, topdown=False):
        # delete __pycache__ and subs...
        if '__pycache__' in dirnames:
            pycache_dir = os.path.join(dirpath, '__pycache__')
            print(f"Deleting {pycache_dir}...")
            shutil.rmtree(pycache_dir)
        
        # delete runtimes_middlewares and subs...
        if 'runtimes_middlewares' in dirnames:
            runtime_dir = os.path.join(dirpath, 'runtimes_middlewares')
            print(f"Deleting {runtime_dir}...")
            shutil.rmtree(runtime_dir)

delete_folders(".")