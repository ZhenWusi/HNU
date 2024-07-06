from RSA import generate_p_q_n, generate_rsa_keys,encrypt_message
# 扩展欧几里得
def chinese_remainder_theorem(moduli, remainders):
    if len(moduli) != len(remainders):
        raise ValueError("模数和余数数量不一致")
    n = 1
    for modulus in moduli:
        n *= modulus
    result = 0
    for modulus, remainder in zip(moduli, remainders):
        n_i = n // modulus
        inverse = pow(n_i, -1, modulus)  # 计算模数的乘法逆元
        result += remainder * n_i * inverse
    return result % n
# 生成512位的 p, q, n
bits = 512
p, q, n = generate_p_q_n(bits)
# 生成两对随机的公私钥对
public_key1, private_key1 = generate_rsa_keys(p, q, n)
e1, n = public_key1
d1, n = private_key1
public_key2, private_key2 = generate_rsa_keys(p, q, n)
e2, n = public_key2
d2, n = private_key2
# 消息 M1 和 M2
M1 = 4
M2 = 7
# 计算私钥 E = e1 * e2
E = e1 * e2
print("e1=",e1)
print("e2=",e2)
print("d1=",d1)
print("d2=",d2)
print("E=",E)
# 合并消息 M
# print(pow(e1,-1,n))
M = (pow(M1, (E*pow(e1,-1,n))%n, n) * pow(M2, (E*pow(e2,-1,n))%n, n)) % n
# 对消息 M 进行签名
S = pow(M, pow(E,-1,n), n)
# 求 X 满足 X = 0 mod e1 和 X = 1 mod e2
moduli = [e1, e2]  # 模数 e1 和 e2
remainders = [0, 1]  # 对应的余数
X = chinese_remainder_theorem(moduli, remainders)
print("X =", X)
# 划分出每一条消息的签名
signature_M2 = (pow(S, X, n) * pow(pow(M1, X*pow(e1,-1,n), n) * pow(M2,(X-1)*pow(e2,-1,n), n), -1,n)) %n
signature_M1 = (S*pow(pow(M2,(pow(e2,-1,n)),n),-1,n)) % n
print("消息 M 的合并结果:", M)
print("批签名 S:", S)
print("从批签名中划分出单个消息m1的签名:", signature_M1)
print("M1单个签名",pow(M1,pow(e1,-1,n),n))
print("从批签名中划分出单个消息m2的签名:", signature_M2)
print("M2单个签名",pow(M2,pow(e2,-1,n),n))
