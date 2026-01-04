import cmath

def root_n(coeffs, x0=1.0 + 0j, n_iter=100):
    """
    使用牛頓法求多項式的其中一個根。
    coeffs: 多項式係數列表，例如 [a, b, c, d] 代表 ax^3 + bx^2 + cx + d
    x0: 初始猜測值 (支援複數)
    n_iter: 迭代次數
    """
    
    # 定義 f(x)：計算多項式在 x 的值 (使用秦九韶算法/Horner's method 較有效率)
    def f(x):
        res = 0
        for c in coeffs:
            res = res * x + c
        return res

    # 定義 f'(x)：計算導函數在 x 的值
    def df(x):
        res = 0
        # 導函數係數：原本 [a, b, c, d] 變為 [3a, 2b, c]
        deriv_coeffs = [(len(coeffs) - 1 - i) * coeffs[i] for i in range(len(coeffs) - 1)]
        for c in deriv_coeffs:
            res = res * x + c
        return res

    # 開始迭代
    x = x0
    for _ in range(n_iter):
        fx = f(x)
        dfx = df(x)
        
        if dfx == 0: # 避免除以零
            break
            
        x = x - fx / dfx
        
    return x

# --- 驗證邏輯 ---

# 測試一個 5 次方程式：x^5 - x - 1 = 0
# 係數為 [1, 0, 0, 0, -1, -1]
coeffs_test = [1, 0, 0, 0, -1, -1]
found_root = root_n(coeffs_test)

print(f"對於 5 次方程式 x^5 - x - 1 = 0")
print(f"求得的一個根為: {found_root}")

# 驗證 f(root) 是否接近 0
def verify(coeffs, x):
    res = 0
    for c in coeffs:
        res = res * x + c
    return res

f_val = verify(coeffs_test, found_root)
is_correct = cmath.isclose(f_val, 0, abs_tol=1e-9)

print(f"驗證 f(root) ≈ 0: {is_correct} (實際值: {f_val})")
