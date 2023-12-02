import os

list = [
    "Windows.x64.System-installer",
    "Windows.x64.User-installer  ",
    "Windows.x64.zip",
    "Windows.Arm64.System-installer",
    "Windows.Arm64.User-installer",
    "Windows.Arm64.zip",
    "Windows.x86.System-installer",
    "Windows.x86.User-installer  ",
    "Windows.x86.zip",
    "macOS.Universal",
    "macOS.Intel-chip",
    "macOS.Apple-silicon",
    "Linux.x64",
    "Linux.x64.debian",
    "Linux.x64.rpm",
    "Linux.x64.snap",
    "Linux.Arm32",
    "Linux.Arm32.debian",
    "Linux.Arm32.rpm",
    "Linux.Arm64",
    "Linux.Arm64.debian",
    "Linux.Arm64.rpm",
]

for ele in list:
    os.mkdir(ele)

"""
https://update.code.visualstudio.com/1.73.1/linux-armhf/stable
https://update.code.visualstudio.com/1.73.1/linux-deb-armhf/stable
https://update.code.visualstudio.com/1.73.1/linux-rpm-armhf/stable
https://update.code.visualstudio.com/1.73.1/linux-arm64/stable
https://update.code.visualstudio.com/1.73.1/linux-deb-arm64/stable
https://update.code.visualstudio.com/1.73.1/linux-rpm-arm64/stable
https://update.code.visualstudio.com/1.73.1/linux-x64/stable
https://update.code.visualstudio.com/1.73.1/linux-deb-x64/stable
https://update.code.visualstudio.com/1.73.1/linux-rpm-x64/stable
https://update.code.visualstudio.com/1.73.1/linux-snap-x64/stable
https://update.code.visualstudio.com/1.73.1/darwin-arm64/stable
https://update.code.visualstudio.com/1.73.1/darwin/stable
https://update.code.visualstudio.com/1.73.1/darwin-universal/stable
https://update.code.visualstudio.com/1.73.1/win32-arm64/stable
https://update.code.visualstudio.com/1.73.1/win32-arm64-user/stable
https://update.code.visualstudio.com/1.73.1/win32-arm64-archive/stable
https://update.code.visualstudio.com/1.73.1/win32-x64/stable
https://update.code.visualstudio.com/1.73.1/win32-x64-user/stable
https://update.code.visualstudio.com/1.73.1/win32-x64-archive/stable
https://update.code.visualstudio.com/1.73.1/win32/stable
https://update.code.visualstudio.com/1.73.1/win32-user/stable
https://update.code.visualstudio.com/1.73.1/win32-archive/stable
"""
