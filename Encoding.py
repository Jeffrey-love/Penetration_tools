import base64
# 下面两个要安装pycryptodome
from Crypto.Cipher import DES
from Crypto.Cipher import AES
from hashlib import md5
import binascii


# def Base64encode(s):
#     bs = base64.b64encode(s.encode('utf-8'))
#     print(bs.decode('utf-8'))
# def Base64decode(s):
#     bs = str(base64.b64decode(s), "utf-8")
#     print(bs)
def Base64(s):
    # 如果输入的不是base64加密的东西(无法解密)，就进行加密
    try:
        bs = str(base64.b64decode(s), "utf-8")
        print(bs)
    except:
        print("无法解密，进行Base64加密后的字符串为:")
        bs = base64.b64encode(s.encode('utf-8'))
        print(bs.decode('utf-8'))


def DES_encode():
    key = b'abcdefgh'   # 必须八个字符
    des = DES.new(key, DES.MODE_ECB)
    text = "haha123 nihao"
    text = text+(8-(len(text)%8))*'='   # 不足八位用等号补全
    # print(text)
    encrypt_text = des.encrypt(text.encode())
    encrypt_res = binascii.b2a_hex(encrypt_text)
    print(encrypt_res)
def DES_decode():
    key = b'abcdefgh'
    des = DES.new(key, DES.MODE_ECB)
    encrypto_res = b'9725dfd2878761585c8a05ab571f5927'
    encryt_text = binascii.a2b_hex(encrypto_res)
    decrypt_res = des.decrypt(encryt_text)
    print(decrypt_res)


# 需要pycryptodome
def AES_encode():
    key = b'abcdefghabcdefgh'
    text = 'haha123 wocao'
    text = text+(16-(len(text)%16))*'='
    # print(text)
    aes = AES.new(key, AES.MODE_ECB)
    encrypt_text = aes.encrypt(text.encode())
    encrypt_res = binascii.b2a_hex(encrypt_text)
    print(encrypt_res)
def AES_decode():
    key = b'abcdefghabcdefgh'
    encrypt_res = b'5ff27bccfc1aa3c0335f2f21bb9f17db'
    aes = AES.new(key, AES.MODE_ECB)
    encrypt_text = binascii.a2b_hex(encrypt_res)
    decrypt_text = aes.decrypt(encrypt_text)
    print(decrypt_text)


def MD5_encode():
    s = 'admin'
    new_md5 = md5()
    new_md5.update(s.encode(encoding='utf-8'))
    print(new_md5.hexdigest())


def main():
    # s = input('输入字符串：')
    # Base64(s)
    # DES_decode()
    # AES_decode()
    MD5_encode()


if __name__ == '__main__':
    main()
