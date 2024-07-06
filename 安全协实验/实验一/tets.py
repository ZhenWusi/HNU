import numpy as np

def vandermonde_inverse(x_t, x_values, Fx, q, t):
    x_t = np.array([x-1 for x in x_t])
    V = np.vander([x_values[i] for i in x_t], t, increasing=True)
    V_inv = np.linalg.inv(V)
    coefficients = np.dot(V_inv, [Fx[i] for i in x_t]) % q
    return coefficients[::-1]  # 反转系数数组

# 测试数据
x_t = [2, 3, 4]
x_values = [1, 2, 3, 4, 5]
Fx = [9, 4, 13, 2, 5]
q = 17
t = 3

# 调用函数
coefficients = vandermonde_inverse(x_t, x_values, Fx, q, t)

print('系数 (K, b, a):', coefficients)
