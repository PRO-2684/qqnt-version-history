from requests import Session
from json import load, dump
from subprocess import check_output
from os import environ
from os.path import getsize
from hashlib import md5
from argparse import ArgumentParser

x = Session()
ARCHITECTURES = ["x64", "x86", "arm"]

parser = ArgumentParser()
# Accept 5 arguments: `version`, `version-code`, `x64`, `x86`, and `arm`
parser.add_argument("version", type=str, help="The version of the QQ installation package.")
parser.add_argument("version-code", type=str, help="The version code of the QQ installation package.")
parser.add_argument("x64", type=str, help="The URL of the x64 installation package.")
parser.add_argument("x86", type=str, help="The URL of the x86 installation package.")
parser.add_argument("arm", type=str, help="The URL of the ARM installation package.")
args = parser.parse_args()
newData = {arch: {
    "url": getattr(args, arch),
    "size": -1,
    "md5": "<unknown>"
} for arch in ARCHITECTURES}
newData["version"] = args.version

def getStat(url, file, directory = "./downloads"):
    """Get and validate the stat of the file at the specified URL."""
    r = x.head(url)
    # Using `X-COS-META-MD5` header
    expectedHash = r.headers.get("X-COS-META-MD5") or "<unknown>"
    # Calculate MD5 hash of the file
    path = f"{directory}/{file}"
    with open(path, "rb") as f: # https://stackoverflow.com/a/59056837/16468609
        hash = md5()
        while chunk := f.read(8192):
            hash.update(chunk)
    actualHash = hash.hexdigest()
    expectedSize = int(r.headers.get("Content-Length")) or -1
    actualSize = getsize(path)
    if actualHash != expectedHash:
        print(f"Hash mismatch! Expected: {expectedHash}, Got: {actualHash}")
    if actualSize != expectedSize:
        print(f"Size mismatch! Expected: {expectedSize}, Got: {actualSize}")
    if actualHash == expectedHash and actualSize == expectedSize:
        return actualHash, actualSize
    return None, None

def getVersion():
    """Determines the version of the QQ installation package."""
    fileName = args.x86.split("/")[-1]
    output = check_output(f"peres -v {fileName} | grep 'Product Version:' | awk '{{print $3}}'", shell=True)
    return output.decode("utf-8").strip()

def getStats():
    """Get and validate the stats of downloaded files under `./downloads`."""
    for info in newData.values():
        url = info["url"]
        fileName = url.split("/")[-1]
        hash, size = getStat(url, fileName)
        if not hash:
            return False
        info["md5"] = hash
        info["size"] = size
    newData["version"] = getVersion()
    return True

def updateJson():
    """Updates `versions.json` if update detected, appending the new version information."""
    versionCode = args.version_code
    with open("versions.json", "r") as f:
        data = load(f)
    print(f"Update detected.")
    data[versionCode] = newData
    with open("versions.json", "w") as f:
        dump(data, f, indent=4)

def generateReleaseNotes():
    """Generate release notes based on the changes."""
    with open("release-notes.md", "w") as f:
        f.write("## Version Info\n")
        f.write(f"- Version: `{args.version}`\n")
        f.write(f"- Version code: `{args.version_code}`\n")
        f.write("## Assets\n")
        for arch, info in newData.items():
            f.write(f"- {arch.capitalize()}\n")
            f.write(f"    - Official link: [{info['url'].split('/')[-1]}]({info['url']})\n")
            f.write(f"    - Size: {info['size']} bytes\n")
            f.write(f"    - MD5: `{info['md5']}`\n")

def main():
    if not getStats():
        raise RuntimeError("Failed to get and validate the stats of downloaded files.")
    updateJson()

if __name__ == "__main__":
    main()
