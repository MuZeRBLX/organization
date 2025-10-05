import os
import shutil
import zipfile
import requests

def Update():

    # GitHub repo info
    owner = "your-username"
    repo = "your-repo"
    branch = "main"  # or "master"

    # Paths
    HOMEDIR = os.path.dirname(os.path.abspath(__file__))
    TARGET_DIR = os.path.join(HOMEDIR, "functions")
    ZIP_URL = f"https://github.com/{owner}/{repo}/archive/refs/heads/{branch}.zip"
    TEMP_ZIP = os.path.join(HOMEDIR, "repo.zip")
    EXTRACT_DIR = os.path.join(HOMEDIR, "repo_extract")

    # Download ZIP
    response = requests.get(ZIP_URL)
    with open(TEMP_ZIP, 'wb') as f:
        f.write(response.content)

    # Extract ZIP
    with zipfile.ZipFile(TEMP_ZIP, 'r') as zip_ref:
        zip_ref.extractall(EXTRACT_DIR)

    # Locate the functions folder inside the extracted repo
    extracted_root = os.path.join(EXTRACT_DIR, f"{repo}-{branch}")
    new_functions = os.path.join(extracted_root, "functions")

    # Replace old folder
    if os.path.exists(TARGET_DIR):
        shutil.rmtree(TARGET_DIR)
    shutil.copytree(new_functions, TARGET_DIR)

    # Cleanup
    os.remove(TEMP_ZIP)
    shutil.rmtree(EXTRACT_DIR)

    print("✅ Functions folder updated from GitHub.")