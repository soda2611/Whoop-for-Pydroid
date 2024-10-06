import os
import zipfile
import io
import shutil
import sys
print(f"Python {sys.version_info.major}.{sys.version_info.minor}")
if True:
    try:
        os.system(f"pip install kivymd==1.2.0 googletrans==4.0.0rc1 eng-to-ipa requests")
        
        import requests

        repo_url = "https://github.com/soda2611/Whoop/archive/refs/heads/main.zip"

        repo_dir = "Whoop-main"

        sod_dir = "Whoop"

        response = requests.get(repo_url)

        zip_file = zipfile.ZipFile(io.BytesIO(response.content))

        zip_file.extractall()

        os.system(f"rmdir {sod_dir}")

        shutil.move(os.path.join(repo_dir, sod_dir), sod_dir)
        
        os.system(f"rm {repo_dir}/LICENSE.txt")
        os.system(f"rm {repo_dir}/README.md")
        os.system(f"rm {repo_dir}/setup.py")
        os.system(f"rmdir {repo_dir}")
        
    except Exception as ex:
        print(ex)

