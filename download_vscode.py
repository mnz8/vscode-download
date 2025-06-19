import os, shutil
from urllib import request
import wget_patch
import time
import sys

PY3K = sys.version_info >= (3, 0)

version = "1.100.3"

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


def write_log(log_filename, message):
    """安全的日志写入函数"""
    try:
        # Python 2 和 3 的兼容写法
        if PY3K:
            log_file = open(log_filename, "a", encoding="utf-8")
        else:
            log_file = open(log_filename, "a")

        log_message = "[{0}] {1}\n".format(
            time.strftime("%Y-%m-%d %H:%M:%S"), message.rstrip("\n")
        )
        # Python 2 中处理 unicode
        if not PY3K and isinstance(log_message, unicode):  # type: ignore
            log_message = log_message.encode("utf-8")

        with log_file:
            log_file.write(log_message)
            log_file.flush()  # 立即刷新缓冲区
            os.fsync(log_file.fileno())  # 确保写入磁盘
    except Exception as e:
        print("写入日志失败: {0}".format(str(e)))


def wget_download(key, value, key_max_len=None, delete_exists=False, log_filename=None):
    try:
        dir_path = version + "/" + key
        create_folder(dir_path)
        url = value.replace("{version}", version)
        try:
            redirected_url = request.urlopen(url).geturl()
        except Exception as e:
            if log_filename:
                write_log(log_filename, "{0} 获取 URL 失败: {1}".format(key, str(e)))
            # 返回 key 表示下载失败
            return key

        # 如果文件已经存在删除已有文件
        if delete_exists:
            try:
                filename = wget_patch.filename_from_url(redirected_url)
                delete_file(dir_path + "/" + filename)
            except Exception as e:
                write_log(log_filename, "redirected_url: {0}".format(redirected_url))
                write_log(log_filename, "filename_from_url 失败: {0}".format(str(e)))

        try:
            downloaded_path, progress_info = wget_patch.download(
                redirected_url, dir_path, key, key_max_len
            )
            if log_filename:
                write_log(log_filename, downloaded_path)
                write_log(log_filename, progress_info)
        except Exception as e:
            print("\n error: ", e)
            if log_filename:
                write_log(log_filename, e)
            return key
    except Exception as e:
        if log_filename:
            write_log(log_filename, "{0} 未知错误: {1}".format(key, str(e)))
        return key


def main():
    print("================ vscode version: %s ================\n" % version)
    # 创建日志文件名
    log_filename = f"vscode_download_{version}_{time.strftime('%Y%m%d_%H%M%S')}.log"
    write_log(log_filename, "vscode version: {}".format(version))

    linkKeys = list(linkdict.keys())
    # terminal 打印使用
    key_max_len = len(max(linkKeys, key=len))

    whileKeys = linkKeys

    while len(whileKeys) > 0:
        key = whileKeys[0]
        value = linkdict[key]
        r = wget_download(key, value, key_max_len, True, log_filename)
        if r:
            whileKeys.append(key)
        whileKeys.remove(key)
        time.sleep(2)  # 防止请求频繁

    write_log(log_filename, "")
    write_log(log_filename, "success")


main()


# Python 3 的写法
# def write_log(log_filename, message):
#     """安全的日志写入函数"""
#     try:
#         with open(log_filename, "a", encoding="utf-8") as f:
#             f.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {message}\n")
#             f.flush()  # 立即刷新缓冲区
#             os.fsync(f.fileno())  # 确保写入磁盘
#     except Exception as e:
#         print(f"写入日志失败: {str(e)}")
