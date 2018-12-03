import hashlib

def gen_md5_token(str):
    m = hashlib.md5()
    m.update(str.encode("utf-8"))
    token = m.hexdigest()
    return token
