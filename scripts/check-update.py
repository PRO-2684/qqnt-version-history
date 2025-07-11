from requests import Session
from re import search
from json import load, loads
from os import environ

x = Session()
MAPPING = {
    "x64": "ntDownloadX64Url",
    "x86": "ntDownloadUrl",
    "arm": "ntDownloadARMUrl",
}

def setOutput(key, value):
    """Set the output for GitHub Actions."""
    with open(environ["GITHUB_OUTPUT"], "a") as f:
        f.write(f"{key}={value}\n")
        print(f"{key}={value}") # Print the output

def determineConfigUrl():
    """Determine the URL of the configuration file."""
    r = x.get("https://im.qq.com/pcqq/index.shtml")
    r.encoding = r.apparent_encoding
    # var rainbowConfigUrl = "//cdn-go.cn/qq-web/im.qq.com_new/latest/rainbow/windowsConfig.js";
    regex = r'var rainbowConfigUrl = "(.+)";'
    m = search(regex, r.text)
    if m:
        url = m.group(1)
        if url.startswith("//"):
            return "https:" + url
        elif url.startswith("http://") or url.startswith("https://"):
            return url
        else:
            return None
    else:
        return None

def getConfig(url):
    """Extract JSON content from the configuration URL."""
    r = x.get(url)
    r.encoding = r.apparent_encoding
    # ;(function(){var params= {...};
    regex = r';\(function\(\)\{var params= ({.*});'
    m = search(regex, r.text)
    if m:
        return loads(m.group(1))
    return None

def getVersionCode(url):
    """Extract the version code from the URL. (Not the actual version)"""
    # https://dldir1.qq.com/qqfile/qq/QQNT/Windows/QQ_9.9.15_241009_x86_01.exe
    # Match version code (`9.9.15_241009`)
    regex = r'QQ_(\d+\.\d+\.\d+_\d+)'
    m = search(regex, url)
    if m:
        return m.group(1)
    return None

def main():
    url = determineConfigUrl()
    if not url:
        raise RuntimeError("Failed to determine the URL of the configuration file.")
    print(f"Configuration URL: {url}")
    config = getConfig(url)
    if not config:
        raise RuntimeError("Failed to extract JSON content from the configuration URL.")
    versionCode = getVersionCode(config.get(MAPPING["x86"])) or "none"
    with open("versions.json", "r") as f:
        data = load(f)
    if versionCode in data:
        print(f"No update - Version code {versionCode} already exists.")
        setOutput("version-code", "none")
        return
    setOutput("version-code", versionCode)
    if versionCode != "none":
        for arch, key in MAPPING.items():
            url = config.get(key)
            setOutput(arch, url)

    # Output be like:
    # version-code=9.9.15_241009
    # x64=https://dldir1.qq.com/qqfile/qq/QQNT/Windows/QQ_9.9.15_241009_x64_01.exe
    # x86=https://dldir1.qq.com/qqfile/qq/QQNT/Windows/QQ_9.9.15_241009_x86_01.exe
    # arm=https://dldir1.qq.com/qqfile/qq/QQNT/Windows/QQ_9.9.15_241009_arm64_01.exe

if __name__ == "__main__":
    main()
