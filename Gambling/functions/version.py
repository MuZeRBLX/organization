def GetVersion():

    import requests

    owner = "neovim"
    repo = "neovim"
    url = f"https://api.github.com/repos/{owner}/{repo}/releases/latest"

    response = requests.get(url)
    data = response.json()

    version = data.get("tag_name", "No version found")
    return version
