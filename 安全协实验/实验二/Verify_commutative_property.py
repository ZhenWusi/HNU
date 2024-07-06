from RSA import generate_p_q_n,generate_rsa_keys,encrypt_message,decrypt_message
bits = int(input("请输入 p, q 的长度（例如：512 或 1024）: "))
p,q,n =generate_p_q_n(bits)
print("参数 p:", p)
print("参数 q:", q)
print("参数 n:", n)
public_key1, private_key1 = generate_rsa_keys(p,q,n)
e1, n = public_key1
print("公钥 e1:", e1)
d1, n = private_key1
print("私钥 d1:", d1)
public_key2, private_key2 = generate_rsa_keys(p,q,n)
e2, n = public_key2
print("公钥 e1:", e2)
d2, n = private_key2
print("私钥 d1:", d2)
m1=int(input("请输入明文m1:"))
e2e1m1=encrypt_message(public_key2,encrypt_message(public_key1, m1))
d2d1c1=decrypt_message(private_key2,decrypt_message(private_key1, e2e1m1))
print("先用e1再用e2加密结果为",e2e1m1)
print("先用d1再用d2解密结果为",d2d1c1)
m2=int(input("请输入明文m2:"))
e1e2m2=encrypt_message(public_key1,encrypt_message(public_key2, m2))
d1d2c2=decrypt_message(private_key1,decrypt_message(private_key2, e1e2m2))
print("先用e2再用e1加密结果为",e1e2m2)
print("先用d2再用d1解密结果为",d1d2c2)
if m1==d2d1c1 and m2==d1d2c2:
    print("具有相同模数的RSA密码算法满足交换律!")
