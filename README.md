# QQNT-Version-History

English | [简体中文](README.zh-CN.md) | ![GitHub Release](https://img.shields.io/github/v/release/PRO-2684/qqnt-version-history?display_name=release&logo=qq&color=1EBAFC)

This repo automatically tracks public version history of [QQNT](https://im.qq.com/pcqq/index.shtml).

- For detailed changelogs, visit [this page](https://im.qq.com/pcqq/support.html).
- For versions prior to `9.9.15.28498`/`9.9.15_241009`, please refer to [this thread](https://bbs.pcbeta.com/forum.php?mod=viewthread&tid=1969561) (Chinese).
- Also, you may use `winget` to search for specific versions and install QQNT, which is the way I recommend:
    - To list all available versions: `winget search Tencent.QQ.NT --versions`
    - To install a specific version: `winget install Tencent.QQ.NT --version <version>`
    - Related packages
        - `Tencent.QQ.NT` (QQNT)
        - `Tencent.WeChat` (WeChat)
        - `Tencent.WeChat.Universal` (WeChat Test Version)

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

## Related Projects

- [WeChat4-Version-History](https://github.com/PRO-2684/WeChat4-Version-History): Automatically tracks version history of [WeChat4](https://pc.weixin.qq.com/).
- [wechat-windows-versions](https://github.com/tom-snow/wechat-windows-versions): Automatically tracks version history of [WeChat3](https://pc.weixin.qq.com/).
