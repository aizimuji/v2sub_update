"""
该文件可以生成相应的升级json 文件
"""
import sys
import json


def generate_version_dict(
    version: str, file_name: str, description: str, with_exec: bool = False
) -> dict:
    version_dict = {
        "version": version,
        "update_file": file_name,
        "description": description,
        "with_exec": with_exec,
    }

    return version_dict


def get_description(version):
    """
    读取txt
    """
    file_name = f"release_{version}.txt"
    with open(file_name, encoding="utf-8") as f:
        desc = f.read()
    return desc


def get_file_url(file_name: str) -> str:
    """
    返回代理过的下载文件url
    """
    fmt_s = "https://ghproxy.com/https://raw.githubusercontent.com/aizimuji/v2sub_update/main/{file_name}"
    return fmt_s.format(file_name=file_name)


def write_json(version: str, with_exec: bool = False):
    win_file_name = f"update_win_{version}.zip"
    description = get_description(version)
    win_file_url = get_file_url(win_file_name)
    win_dict = generate_version_dict(version, win_file_url, description, with_exec)

    mac_file_name = f"update_mac_{version}.zip"
    mac_file_url = get_file_url(mac_file_name)
    mac_dict = generate_version_dict(version, mac_file_url, description, with_exec)
    json_dict = {"win": win_dict, "mac": mac_dict}
    out_file = "update.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(json_dict, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("usage: update_json version(str) with_exec(1, 0)")
        sys.exit(1)
    version = sys.argv[1]
    with_exec = bool(sys.argv[2])
    write_json(version, with_exec)
