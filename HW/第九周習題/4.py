import math

# 為了避免 log(0) 導致的 -inf，我們加入一個極小值
EPSILON = 1e-15

def entropy(p):
    """
    計算單一機率分佈 P 的熵 (Entropy)。
    H(P) = - Σ p(x) * log2(p(x))
    """
    return -sum(pi * math.log2(pi) for pi in p if pi > 0)

def cross_entropy(p, q):
    """
    計算 P 和 Q 的交叉熵 (Cross-Entropy)。
    H(P, Q) = - Σ p(x) * log2(q(x))
    """
    total_ce = 0.0
    for pi, qi in zip(p, q):
        if pi > 0:
            qi_clipped = max(qi, EPSILON)
            total_ce += pi * math.log2(qi_clipped)
    
    return -total_ce

# --- 驗證程式 ---

print("程式驗證：H(P, Q) >= H(P, P)\n")

# 1. 定義 P (真實分佈)
#    (假設一個三分類問題，真實答案是第 2 類)
P_true = [0.0, 1.0, 0.0]

# 2. 定義 Q_perfect (完美的預測, Q = P)
Q_perfect = [0.0, 1.0, 0.0]

# 3. 定義 Q_imperfect (不完美的預測, Q != P)
#    模型預測 "第 2 類" 的機率是 0.7，但猜錯為 "第 1 類" 的機率是 0.3
Q_imperfect = [0.3, 0.7, 0.0]

# 4. 定義 Q_imperfect_2 (另一個不完美的預測)
#    模型預測 "第 2 類" 的機率是 0.9，猜得比較準
Q_imperfect_2 = [0.1, 0.9, 0.0]

# --- 計算 ---

# 情況 1: 完美預測 (Q = P)
# H(P, P) 應該等於 H(P)
h_p = entropy(P_true)
ce_p_p = cross_entropy(P_true, Q_perfect)

print(f"P (真實)   = {P_true}")
print(f"P 的熵 H(P) = {h_p:.4f} bits")
print(f"交叉熵 H(P, P) = {ce_p_p:.4f} bits (最小值)")
print("-" * 30)

# 情況 2: 不完美預測 1 (Q != P)
ce_p_q1 = cross_entropy(P_true, Q_imperfect)
print(f"Q1 (預測 1) = {Q_imperfect}")
print(f"交叉熵 H(P, Q1) = {ce_p_q1:.4f} bits")
print(f"驗證 H(P, Q1) > H(P, P)?")
print(f"   {ce_p_q1:.4f} > {ce_p_p:.4f}  -->  {ce_p_q1 > ce_p_p}")
print("-" * 30)

# 情況 3: 不完美預測 2 (Q != P, 但猜得比較準)
ce_p_q2 = cross_entropy(P_true, Q_imperfect_2)
print(f"Q2 (預測 2) = {Q_imperfect_2}")
print(f"交叉熵 H(P, Q2) = {ce_p_q2:.4f} bits")
print(f"驗證 H(P, Q2) > H(P, P)?")
print(f"   {ce_p_q2:.4f} > {ce_p_p:.4f}  -->  {ce_p_q2 > ce_p_p}")
print("-" * 30)

# 比較兩個不完美的預測
print("比較 H(P, Q1) 和 H(P, Q2):")
print(f"Q2 (0.9) 比 Q1 (0.7) 更接近 P (1.0)")
print(f"因此 Q2 的交叉熵 ({ce_p_q2:.4f}) 應該低於 Q1 ({ce_p_q1:.4f})")
print(f"驗證: {ce_p_q2 < ce_p_q1}")
