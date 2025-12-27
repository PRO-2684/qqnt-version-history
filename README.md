# QQNT-Version-History

[![GitHub Release](https://img.shields.io/github/v/release/PRO-2684/qqnt-version-history?display_name=release&label=QQ&logo=qq&color=1EBAFC)](https://github.com/PRO-2684/qqnt-version-history/releases/latest)
[![GitHub Downloads (all assets, all releases)](https://img.shields.io/github/downloads/PRO-2684/qqnt-version-history/total?logo=github)](https://github.com/PRO-2684/qqnt-version-history/releases)

> [!NOTE]
> QQ is offering latest version only for China IP, so this repo might not get comprehensive updates. See [config.png](./config.png) for illustration of this problem: the upper half is what I get on my physical machine in China, while the lower half is what I get on my Azure machine not located in China. You can see that QQ is offering different versions.

This repo automatically tracks public version history of [QQNT](https://im.qq.com/pcqq/index.shtml).

## Downloads

- Kindly navigate to [Releases](https://github.com/PRO-2684/qqnt-version-history/releases) to search and **download** tracked versions.
- The **oldest** version tracked by this repo is [`9.9.15.28498`/`9.9.15_241009`](https://github.com/PRO-2684/qqnt-version-history/releases/tag/9.9.15_241009).
- For detailed **changelogs**, visit [the official support site](https://im.qq.com/pcqq/support.html).
- For versions **prior** to `9.9.15.28498`/`9.9.15_241009`, kindly refer to the [Other Sources](#other-sources) section.

## Version & Version Code

- **Version Code** is the version number used in the installer file name and download URL, and is in the format of `x.x.x_x`.
- **Version** is the version number used in all other places, and is in the format of `x.x.x.x`. For example:
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

## Other Sources

### Telegram @QQUpdates

[@QQUpdates](http://t.me/QQUpdates) on Telegram provides VERY comprehensive version history of QQ on ALL platforms. Check that out if you can't find the version you want.

### Winget

You may use [`winget`](https://github.com/microsoft/winget-cli) to search for specific versions and install QQNT, but certain versions might be missing from this source:

- To list all available versions: `winget search Tencent.QQ.NT --versions`
- To install a specific version: `winget install Tencent.QQ.NT --version <version>`
- Related packages
    - `Tencent.QQ.NT` (QQNT)
    - `Tencent.WeChat` (WeChat)
    - `Tencent.WeChat.Universal` (WeChat 4)

### Chinese Forums

> These sources are updated manually, and might not be updated in time. However, they contain versions prior to `9.9.15.28498`/`9.9.15_241009`, which acts as complementary to this repo.

- [PC Beta Forum](https://bbs.pcbeta.com/forum.php?mod=viewthread&tid=1969561) | [Archive](https://web.archive.org/web/20250314001429/https://bbs.pcbeta.com/forum.php?mod=viewthread&tid=1969561)
- [Koishi Unofficial](https://forum.itzdrli.cc/d/9) | [Archive](https://web.archive.org/web/20250526040017/https://forum.itzdrli.cc/d/9)

## Related Projects

- [WeChat4-Version-History](https://github.com/PRO-2684/WeChat4-Version-History): Automatically tracks version history of [WeChat4](https://pc.weixin.qq.com/).
- [wechat-windows-versions](https://github.com/tom-snow/wechat-windows-versions): Automatically tracks version history of [WeChat3](https://pc.weixin.qq.com/).

## Star History

<a href="https://www.star-history.com/#PRO-2684/qqnt-version-history&Date">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=PRO-2684/qqnt-version-history&type=Date&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=PRO-2684/qqnt-version-history&type=Date" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=PRO-2684/qqnt-version-history&type=Date" />
 </picture>
</a>
