import os, shutil
from urllib import request
import wget_patch
import time

version = "1.87.2"

linkdict = {
    "Windows.x64.System-installer": "https://update.code.visualstudio.com/{version}/win32-x64/stable",
    "Windows.x64.User-installer": "https://update.code.visualstudio.com/{version}/win32-x64-user/stable",
    "Windows.x64.zip": "https://update.code.visualstudio.com/{version}/win32-x64-archive/stable",
    "Windows.Arm64.System-installer": "https://update.code.visualstudio.com/{version}/win32-arm64/stable",
    "Windows.Arm64.User-installer": "https://update.code.visualstudio.com/{version}/win32-arm64-user/stable",
    "Windows.Arm64.zip": "https://update.code.visualstudio.com/{version}/win32-arm64-archive/stable",
    # 'Windows.x86.System-installer': 'https://update.code.visualstudio.com/{version}/win32/stable',
    # 'Windows.x86.User-installer': 'https://update.code.visualstudio.com/{version}/win32-user/stable',
    # 'Windows.x86.zip': 'https://update.code.visualstudio.com/{version}/win32-archive/stable',
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


# 创建文件夹
def create_folder(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)


# 删除已存在文件
def delete_file(file_path):
    if os.path.exists(file_path):
        try:
            shutil.os.remove(file_path)

        except Exception as e:
            print("delete file error:" + str(e))
    # else:
    #     print("file not found")


def wget_download(
    url, dir_path, key=None, key_max_len=None, retry=0, delete_exists=False
):
    retry_times = retry

    redirected_url = request.urlopen(url).geturl()

    # 如果文件已经存在删除已有文件
    if delete_exists:
        filename = wget_patch.filename_from_url(redirected_url)
        delete_file(dir_path + "/" + filename)

    try:
        wget_patch.download(redirected_url, dir_path, key, key_max_len)
    except Exception as e:
        print(" error: ", e)
        if retry_times > 0:
            print(key, "retry times:", retry - retry_times + 1)
            time.sleep(2)  # 防止请求频繁
            wget_patch.download(redirected_url, dir_path, key, key_max_len)
            retry_times -= 1


def main():
    print("================ vscode version: %s ================\n" % version)

    # terminal 打印使用
    key_max_len = len(max(list(linkdict.keys()), key=len))

    for key, value in linkdict.items():
        dir_path = version + "/" + key

        create_folder(dir_path)
        url = value.replace("{version}", version)
        wget_download(url, dir_path, key, key_max_len, 3, True)
        time.sleep(2)  # 防止请求频繁


main()
