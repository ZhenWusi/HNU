import random
def is_prime(n, k=5):  # Miller-Rabin素性检测
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def generate_prime(bits):  # 生成指定比特长度的素数
    while True:
        p = random.getrandbits(bits)
        p |= (1 << bits - 1) | 1
        if is_prime(p):
            return p

def generate_p_q_n(bits):  # 生成 RSA 的 p, q, n
    p = generate_prime(bits // 2)
    q = generate_prime(bits // 2)
    while p == q:
        q = generate_prime(bits // 2)
    n = p * q
    return p, q, n

def gcd(a, b):  # 计算最大公约数
    while b:
        a, b = b, a % b
    return a

def modinv(a, m):  # 计算模逆
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1

def generate_e_d(phi):  # 生成 RSA 的 e, d
    e = random.randrange(2, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(2, phi)
    d = modinv(e, phi)
    return e, d
def generate_rsa_keys(p,q,n,):  # 生成 RSA 密钥对
    phi = (p - 1) * (q - 1)
    e, d = generate_e_d(phi)
    return (e, n), (d, n)

def encrypt_message(public_key, message):  # 使用公钥加密消息
    e, n = public_key
    ciphertext = pow(message, e, n)
    return ciphertext

def decrypt_message(private_key, ciphertext):  # 使用私钥解密消息
    d, n = private_key
    plaintext = pow(ciphertext, d, n)
    return plaintext
if __name__ == "__main__":
    # 生成密钥对（p, q 均为 512 位）
    bits = int(input("请输入 p, q 的长度（例如：512 或 1024）: "))
    p, q, n = generate_p_q_n(bits)
    print("参数 p:", p)
    print("参数 q:", q)
    print("参数 n:", n)
    public_key, private_key = generate_rsa_keys(p, q, n)
    e, n = public_key
    print("公钥 e:", e)
    d, n = private_key
    print("私钥 d:", d)
    print("模数 n:", n)
    # 加密和解密消息
    message = int(input("请输入消息（整数）: "))
    ciphertext = encrypt_message(public_key, message)
    print("密文:", ciphertext)
    plaintext = decrypt_message(private_key, ciphertext)
    print("解密消息:", plaintext)
