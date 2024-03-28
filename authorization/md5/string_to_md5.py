import hashlib

from config import CONFIG_MD5


def calculate_md5(string):
    for i in range(CONFIG_MD5):
        md5_hash = hashlib.md5()
        md5_hash.update(string.encode('utf-8'))
        string = md5_hash.hexdigest()
    return string