from RSA import generate_p_q_n, generate_rsa_keys, encrypt_message
# 生成 p、q、n
bits = 512
p, q, n = generate_p_q_n(bits)
print("参数 p:", p)
print("参数 q:", q)
print("参数 n:", n)
# 随机选择一对公私钥
public_key, private_key = generate_rsa_keys(p, q, n)
e, n = public_key
d, n = private_key
print("公钥 e:", e)
print("私钥 d:", d)
# 消息 m1=4
m1 = 4
# 计算签名,相当于拿私钥d对m1进行RSA加密
signature = encrypt_message(private_key, m1)
print("签名:", signature)
