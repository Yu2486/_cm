import math

# 為了避免 log(0) 導致的 -inf，我們加入一個極小值
EPSILON = 1e-15

def entropy(p):
    """
    計算單一機率分佈 P 的熵 (Entropy)。
    H(P) = - Σ p(x) * log2(p(x))
    
    使用純 Python 的 list comprehension 和 sum()。
    """
    # 我們只對 p(x) > 0 的項進行加總，
    # 因為 p(x) = 0 時，p(x) * log(p(x)) = 0
    return -sum(pi * math.log2(pi) for pi in p if pi > 0)

def cross_entropy(p, q):
    """
    計算 P 和 Q 的交叉熵 (Cross-Entropy)。
    H(P, Q) = - Σ p(x) * log2(q(x))
    
    使用 zip() 來同時迭代 p 和 q。
    """
    total_ce = 0.0
    for pi, qi in zip(p, q):
        # 只有當 p(x) > 0 時，該項才有貢獻
        if pi > 0:
            # 必須防止 log2(0)，使用 max(qi, EPSILON) 來"裁剪"
            qi_clipped = max(qi, EPSILON)
            total_ce += pi * math.log2(qi_clipped)
    
    return -total_ce

def kl_divergence(p, q):
    """
    計算 P || Q 的 KL 散度 (Kullback-Leibler Divergence)。
    D_KL(P || Q) = Σ p(x) * log2(p(x) / q(x))
                  = Σ p(x) * (log2(p(x)) - log2(q(x)))
    """
    total_kl = 0.0
    for pi, qi in zip(p, q):
        # KL 散度的總和只定義在 p(x) > 0 的地方
        if pi > 0:
            # 將 p(x) 和 q(x) 都進行裁剪，避免 log(0)
            pi_clipped = max(pi, EPSILON)
            qi_clipped = max(qi, EPSILON)
            
            # 使用 D = p * (log(p) - log(q))
            total_kl += pi * (math.log2(pi_clipped) - math.log2(qi_clipped))
    
    return total_kl

    # ---
    # 另一種更簡潔的寫法 (利用已有的函數):
    # return cross_entropy(p, q) - entropy(p)
    # ---

def mutual_information(p_xy):
    """
    計算 X 和 Y 的互資訊 (Mutual Information)。
    I(X; Y) = H(X) + H(Y) - H(X, Y)
    
    p_xy 是一個 2D 的 "list of lists" (列表的列表)。
    """
    
    # 1. 計算 H(X, Y) (聯合熵)
    #    首先 "攤平" 2D 列表
    p_xy_flat = [p_ij for row in p_xy for p_ij in row]
    h_xy = entropy(p_xy_flat)
    
    # 2. 計算 H(X) (邊緣熵)
    #    P(X) = Σ_y P(X, Y) -> 對 p_xy 的每一 "列" (row) 進行加總
    p_x = [sum(row) for row in p_xy]
    h_x = entropy(p_x)
    
    # 3. 計算 H(Y) (邊緣熵)
    #    P(Y) = Σ_x P(X, Y) -> 對 p_xy 的每一 "行" (column) 進行加總
    #    這裏使用一個 "zip(*p_xy)" 技巧來轉置(transpose)矩陣
    p_y = [sum(col) for col in zip(*p_xy)]
    h_y = entropy(p_y)
    
    # 4. 計算互資訊 I(X; Y) = H(X) + H(Y) - H(X, Y)
    mi = h_x + h_y - h_xy
    
    # 由於浮點數誤差，MI 可能是極小的負數，我們將其修正為 0
    return max(0.0, mi)

# --- 範例執行 (與之前完全相同，只是資料結構是 list 而非 numpy array) ---
if __name__ == "__main__":
    
    print("===== 1. 熵 (Entropy) =====")
    p_fair_coin = [0.5, 0.5]
    print(f"公平硬幣 [0.5, 0.5] 的熵: {entropy(p_fair_coin):.4f} bits")
    
    p_biased_coin = [0.9, 0.1]
    print(f"不公平硬幣 [0.9, 0.1] 的熵: {entropy(p_biased_coin):.4f} bits")
    
    p_certain_coin = [1.0, 0.0]
    print(f"確定硬幣 [1.0, 0.0] 的熵: {entropy(p_certain_coin):.4f} bits")
    print("-" * 30)

    # -----------------------------------------------
    
    print("===== 2. 交叉熵 & KL 散度 =====")
    P = [0.9, 0.1]
    Q = [0.5, 0.5]
    
    h_p = entropy(P)
    h_pq = cross_entropy(P, Q)
    kl_pq = kl_divergence(P, Q)
    
    print(f"P (真實) = {P}")
    print(f"Q (預測) = {Q}")
    print(f"P 的熵 H(P): {h_p:.4f} bits")
    print(f"交叉熵 H(P, Q): {h_pq:.4f} bits")
    print(f"KL 散度 D_KL(P || Q): {kl_pq:.4f} bits")
    
    # 驗證 KL 散度的重要特性: D_KL(P || Q) = H(P, Q) - H(P)
    print(f"H(P, Q) - H(P): {(h_pq - h_p):.4f} bits (應等於 KL 散度)")
    print("-" * 30)
    
    # -----------------------------------------------
    
    print("===== 3. 互資訊 (Mutual Information) =====")
    
    # 範例1: 兩個變數完全獨立
    p_xy_independent = [
        [0.25, 0.25],  # P(X=0, Y=0), P(X=0, Y=1)
        [0.25, 0.25]   # P(X=1, Y=0), P(X=1, Y=1)
    ]
    mi_ind = mutual_information(p_xy_independent)
    print(f"獨立變數的 P(X,Y):\n{p_xy_independent}")
    print(f"互資訊: {mi_ind:.4f} bits (應接近 0)")

    # 範例2: 兩個變數完全相關 (X=Y)
    p_xy_dependent = [
        [0.5, 0.0],
        [0.0, 0.5]
    ]
    mi_dep = mutual_information(p_xy_dependent)
    print(f"\n完全相關變數的 P(X,Y):\n{p_xy_dependent}")
    print(f"互資訊: {mi_dep:.4f} bits (應等於 H(X) = 1.0)")
