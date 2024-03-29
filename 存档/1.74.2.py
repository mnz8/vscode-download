import os, shutil
from urllib import request
import wget_patch

version = "1.76.0"
retry_times = 3

linkdict = {
    "Windows.x64.System-installer": "https://update.code.visualstudio.com/{version}/win32-x64/stable",
    "Windows.x64.User-installer": "https://update.code.visualstudio.com/{version}/win32-x64-user/stable",
    "Windows.x64.zip": "https://update.code.visualstudio.com/{version}/win32-x64-archive/stable",
    "Windows.Arm64.System-installer": "https://update.code.visualstudio.com/{version}/win32-arm64/stable",
    "Windows.Arm64.User-installer": "https://update.code.visualstudio.com/{version}/win32-arm64-user/stable",
    "Windows.Arm64.zip": "https://update.code.visualstudio.com/{version}/win32-arm64-archive/stable",
    "Windows.x86.System-installer": "https://update.code.visualstudio.com/{version}/win32/stable",
    "Windows.x86.User-installer": "https://update.code.visualstudio.com/{version}/win32-user/stable",
    "Windows.x86.zip": "https://update.code.visualstudio.com/{version}/win32-archive/stable",
    "macOS.Universal": "https://update.code.visualstudio.com/{version}/darwin-universal/stable",
    "macOS.Intel-chip": "https://update.code.visualstudio.com/{version}/darwin/stable",
    "macOS.Apple-silicon": "https://update.code.visualstudio.com/{version}/darwin-arm64/stable",
    "Linux.x64": "https://update.code.visualstudio.com/{version}/linux-x64/stable",
    "Linux.x64.debian": "https://update.code.visualstudio.com/{version}/linux-deb-x64/stable",
    "Linux.x64.rpm": "https://update.code.visualstudio.com/{version}/linux-rpm-x64/stable",
    "Linux.x64.snap": "https://update.code.visualstudio.com/{version}/linux-snap-x64/stable",
    "Linux.Arm32": "https://update.code.visualstudio.com/{version}/linux-armhf/stable",
    "Linux.Arm32.debian": "https://update.code.visualstudio.com/{version}/linux-deb-armhf/stable",
    "Linux.Arm32.rpm": "https://update.code.visualstudio.com/{version}/linux-rpm-armhf/stable",
    "Linux.Arm64": "https://update.code.visualstudio.com/{version}/linux-arm64/stable",
    "Linux.Arm64.debian": "https://update.code.visualstudio.com/{version}/linux-deb-arm64/stable",
    "Linux.Arm64.rpm": "https://update.code.visualstudio.com/{version}/linux-rpm-arm64/stable",
}


def wget_download(url, dir_path, key=None, key_max_len=None):
    redirected_url = request.urlopen(url).geturl()
    wget_patch.download(redirected_url, dir_path, key, key_max_len)


def main():
    print("================ version: %s ================" % version)
    if not os.path.exists(version):
        os.makedirs(version)

    # terminal 打印使用
    key_max_len = len(max(list(linkdict.keys()), key=len))

    for key, value in linkdict.items():
        dir_path = version + "/" + key

        if os.path.exists(dir_path):
            # 已有目录情况，删除，重新下载
            shutil.rmtree(dir_path)
        os.makedirs(dir_path)

        url = value.replace("{version}", version)

        for _ in range(0, retry_times):
            try:
                wget_download(url, dir_path, key, key_max_len)
                break
            except Exception as e:
                print("\ndownload error: %s" % e)
                continue


main()
