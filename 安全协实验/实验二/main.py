from RSA import generate_p_q_n, generate_rsa_keys,encrypt_message
e1 = 3
e2 = 5
n = 77
# 消息 M1 和 M2
M1 = 4
M2 = 7
# 计算私钥 E = e1 * e2
E = e1 * e2
e1_ni=pow(e1,-1,n)
e2_ni=pow(e2,-1,n)
print("E=",E)
M = pow(M1, E*e1_ni, n) * pow(M2, E*e2_ni, n)%n
print("M=",M)
S = pow(M1,e1_ni,n)*pow(M2,e2_ni,n)
print("S=",S)
X = 6
print("M1单个签名",pow(M1,e1_ni,n))
print("M2单个签名",pow(M2,e2_ni,n))
# 划分出每一条消息的签名
#signature_M2 = (pow(S, X, n) * pow(pow(M1, X*pow(e1,-1,n), n) * pow(M2,(X-1)*pow(e2,-1,n), n), -1,n)) %n
signature_M1 = int(S/(pow(M2,e2_ni,n))% n)
print("从批签名中划分出单个消息m1的签名:", signature_M1)
signature_M2 = (pow(S, X)/ (pow(M1,X*e1_ni,n)*pow(M2,(X-1)*e2_ni,n)%n))%n
print("从批签名中划分出单个消息m2的签名:", signature_M2)

