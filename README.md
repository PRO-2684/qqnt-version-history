# qqnt-version-history

This repo automatically tracks public version history of [QQNT](https://im.qq.com/pcqq/index.shtml).

- For detailed changelogs, visit [this page](https://im.qq.com/pcqq/support.html).
- For versions prior to `9.9.15.28498`/`9.9.15_241009`, please refer to [this thread](https://bbs.pcbeta.com/forum.php?mod=viewthread&tid=1969561) (Chinese).

## Version & Version Code

- **Version Code** is the version number used in the installer file name and download URL.
- **Version** is the version number used in all other places. For example:
    - It is displayed in the about page of QQ.
    - It is present in various json files like `package.json`
    - It is used as the name of directory under `resources\app\versions` in the installation directory.

## [`versions.json`](./versions.json)

This file contains the version history of QQNT since `9.9.15.28498`/`9.9.15_241009`. It is structured as follows:

```json
{
    "<version code>": {
        "version": "<version>",
        "x64": {
            "url": "<x64 installer URL>",
            "size": <x64 installer size in bytes>,
            "md5": "<x64 installer MD5>"
        },
        "x86": {
            "url": "<x86 installer URL>",
            "size": <x86 installer size in bytes>,
            "md5": "<x86 installer MD5>"
        },
        "arm": {
            "url": "<arm installer URL>",
            "size": <arm installer size in bytes>,
            "md5": "<arm installer MD5>"
        }
    },
    ...
}
```


