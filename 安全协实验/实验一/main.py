import math
import numpy as np
def is_prime(num):
    """判断一个数是否为素数"""
    if num <= 1:
        return False
    if num == 2:
        return True  # 2 是素数
    if num % 2 == 0:
        return False  # 排除所有偶数
    max_divisor = int(math.sqrt(num)) + 1
    for divisor in range(3, max_divisor, 2):
        if num % divisor == 0:
            return False
    return True
def construct_polynomial(t, q, a, k):
    """
    构造并输出多项式 F(x) = a[0]*x^(t-1) + a[1]*x^(t-2) + ... + a[t-2]*x + k (mod q)
    """
    polynomial_terms = []
    # 构造多项式项
    for i in range(t - 1):
        coefficient = a[i]
        exponent = t - 1 - i
        if coefficient != 0:
            if exponent == 0:
                term = f"{coefficient}"
            elif exponent == 1:
                term = f"{coefficient}*x"
            else:
                term = f"{coefficient}*x^{exponent}"
            polynomial_terms.append(term)
    # 添加常数项 k
    if k != 0:
        polynomial_terms.append(f"{k}")
    # 组合所有项，形成多项式字符串
    polynomial_str = " + ".join(polynomial_terms) + f" (mod {q})"
    return polynomial_str
def F(x,t,q,a,k):
    # 计算多项式 F(x) = a[0]*x^(t-1) + a[1]*x^(t-2) + ... + a[t-2]*x + k (mod q)
    result = 0
    for i in range(t-1):
        result = (result + a[i] * pow(x, t - 1 - i, q)) % q
    result = (result+k)%q
    return result
def matrix(x_t,x_values,Fx,q,t):
        '''矩阵求解法'''
        '''
        x_t 选择的影子编号
        x_values，x的取值矩阵，x_values[x_t-1]则为选择编号对应x取值
        Fx为对应同余方程fx的取值，Fx[x_t-1]为选择x对应fx取值
        t为门限值，t-1为最高次次数
        q为同余方程组的模长
        '''
        x_t = np.array([x - 1 for x in x_t])
        V = np.vander([x_values[i] for i in x_t], t, increasing=True)
        V_inv = np.linalg.inv(V)
        coefficients = np.dot(V_inv, [Fx[i] for i in x_t]) % q
        return coefficients[::-1]  # 反转系数数组
def lagrange_interpolation(x_t, x_values,Fx, q):
    """
    使用拉格朗日插值法恢复秘密消息。
    """
    t = len(x_t)
    result = 0
    for i in range(t):
        term = Fx[x_t[i]-1]
        for j in range(t):
            if i != j:
                term *= x_values[x_t[j]-1] * pow(x_values[x_t[j]-1] - x_values[x_t[i]-1], -1, q)%q
                term %= q
        result += term
        result %= q
    return result
if __name__ == "__main__":
    # (t,n)Shamir秘密共享方案
    q = int(input("输入素数:"))
    while not(is_prime(q)):
        print("输入错误，请输入素数！")
        q = int(input("输入素数:"))
    Field =list(range(q))
    print("域:", Field)
    n = int(input("输入参与者数量 n (小于域的阶)："))
    t = int(input("输入门限值t (小于参与者数量)："))
    k =int(input("请输入秘密k:"))
    a = [0] * t
    print(f"请输入选取多项式系数,从{t-1}次到1次:")
    for i in range(t-1):
        temp = int(input(f"请输入 {t-1-i} 次项系数:"))
        a[i] = temp
    print("多项式为：",construct_polynomial(t, q, a, k))
    # 计算多项式在不同影子值处的结果
    x_values = []
    print(f"请输入 {n} 个影子的取值 x:")
    while len(x_values) < n:
        x = int(input(f"请输入第 {len(x_values) + 1} 个 x 值: "))
        if x in x_values:
            print(f"值 {x} 已存在，请输入不同的值。")
        else:
            x_values.append(x)
    print(f"{n}个影子为：")
    Fx=[]
    for x in x_values:
        fx = F(x, t, q, a,k)
        Fx.append(fx)
        print(f"F({x}) = {fx}")

    x_t = []
    print(f"请输入 {t} 个影子的编号:")
    while len(x_t) < t:
        x = int(input(f"请输入第 {len(x_t) + 1} 个编号: "))
        if x in x_t:
            print(f"编号{x} 已存在，请输入不同的编号。")
        else:
            x_t.append(x)
    print("得到{t}个点对：")
    for i in range(t):
        print(f"{x_values[x_t[i]-1],Fx[x_t[i]-1]}")
    # 恢复出秘密消息
    msg1 = matrix(x_t,x_values,Fx,q,t)
    print("范德蒙行列式矩阵求解得到秘密消息",int(msg1[t-1]))
    msg2 = lagrange_interpolation(x_t,x_values,Fx,q)
    print("拉格朗日插值法得到秘密消息:",msg2)

