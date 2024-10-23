from requests import Session
from re import search
from json import loads, load, dump

x = Session()
MAPPING = {
    "x64": "ntDownloadX64Url",
    "x86": "ntDownloadUrl",
    "arm": "ntDownloadARMUrl",
}

def determineConfigUrl():
    """Determine the URL of the configuration file."""
    r = x.get("https://im.qq.com/pcqq/index.shtml")
    r.encoding = r.apparent_encoding
    # var rainbowConfigUrl = "https://qq-web.cdn-go.cn/im.qq.com_new/f0ba2273/202410222121/windowsDownloadUrl.js?t=1729603316568";
    regex = r'var rainbowConfigUrl = "(https://qq-web.cdn-go.cn/im.qq.com_new/[^/]+/[^/]+/windowsDownloadUrl.js\?t=\d+)";'
    m = search(regex, r.text)
    if m:
        return m.group(1)
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

def getSizeAndHash(url):
    """Get the size and hash of the file at the specified URL."""
    r = x.head(url)
    # Using `Content-Length` and `X-COS-META-MD5` headers
    return int(r.headers.get("Content-Length")) or -1, r.headers.get("X-COS-META-MD5") or "<unknown>"

def getVersion(url):
    """Extract the version from the URL."""
    # https://dldir1.qq.com/qqfile/qq/QQNT/Windows/QQ_9.9.15_241009_x86_01.exe
    # Match version code (`9.9.15_241009`)
    regex = r'QQ_(\d+\.\d+\.\d+_\d+)'
    m = search(regex, url)
    if m:
        return m.group(1)
    return None

def generateInfo(config):
    """Generate required information based on the configuration."""
    urlForTest = config.get(MAPPING["x86"])
    if not urlForTest:
        return None
    info = {}
    for arch, key in MAPPING.items():
        url = config.get(key)
        size, hash = getSizeAndHash(url)
        info[arch] = {"url": url, "size": size, "md5": hash}
    return info

def updateJsonIfNeeded(config):
    """Updates `versions.json` if update detected, appending the new version information."""
    version = getVersion(config[MAPPING["x86"]])
    if not version:
        raise RuntimeError("Failed to extract version from the configuration.")
    with open("versions.json", "r") as f:
        data = load(f)
    if version in data:
        print(f"No update - Version {version} already exists.")
        return
    print(f"Update detected.")
    info = generateInfo(config)
    if not info:
        raise RuntimeError("Failed to generate required information based on the configuration.")
    data[version] = info
    with open("versions.json", "w") as f:
        dump(data, f, indent=4)

def main():
    url = determineConfigUrl()
    if not url:
        raise RuntimeError("Failed to determine the URL of the configuration file.")
    print(f"Configuration URL: {url}")
    config = getConfig(url)
    if not config:
        raise RuntimeError("Failed to extract JSON content from the configuration URL.")
    print(f"Configuration: {config}")
    updateJsonIfNeeded(config)

if __name__ == "__main__":
    main()
