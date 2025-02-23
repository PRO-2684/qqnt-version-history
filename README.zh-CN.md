# QQNT-Version-History

[English](README.md) | 简体中文 | [![GitHub Release](https://img.shields.io/github/v/release/PRO-2684/qqnt-version-history?display_name=release&label=QQ&logo=qq&color=1EBAFC)](https://github.com/PRO-2684/qqnt-version-history/releases/latest)

此仓库自动跟踪 [QQNT](https://im.qq.com/pcqq/index.shtml) 的公开版本历史。

- 访问 [此页面](https://im.qq.com/pcqq/support.html) 以获取详细的更新日志。
- 对于 `9.9.15.28498`/`9.9.15_241009` 之前的版本，请参考 [此帖](https://bbs.pcbeta.com/forum.php?mod=viewthread&tid=1969561)。
- 另外，你也可以使用 `winget` 来搜索并安装特定版本的 QQNT，并且这是我个人推荐的方法：
    - 列举所有版本：`winget search Tencent.QQ.NT --versions`
    - 安装指定版本：`winget install Tencent.QQ.NT --version <version>`
    - 相关的软件包
        - `Tencent.QQ.NT` (QQNT)
        - `Tencent.WeChat` (WeChat)
        - `Tencent.WeChat.Universal` (WeChat Test Version)

## Version & Version Code

- **Version Code** 是安装器名称以及下载链接中用到的版本号
- **Version** 是其它所有地方用到的版本号，例如：
    - QQ 关于界面中展示的版本号
    - 若干 JSON 文件中包含的版本号，例如 `package.json`
    - 安装目录下 `resources\app\versions` 中包含的目录名

## [`versions.json`](./versions.json)

此文件包含 QQNT 自从 `9.9.15.28498`/`9.9.15_241009` 以来的版本历史。其结构如下：

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

## 相关项目

- [WeChat4-Version-History](https://github.com/PRO-2684/WeChat4-Version-History): 自动跟踪 [WeChat4](https://pc.weixin.qq.com/) 的版本历史。
- [wechat-windows-versions](https://github.com/tom-snow/wechat-windows-versions): 自动跟踪 [WeChat3](https://pc.weixin.qq.com/) 的版本历史。
