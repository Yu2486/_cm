import numpy as np
from scipy.linalg import lu

# 1. 遞迴方式計算行列式
def recursive_determinant(A):
    """
    使用遞迴的餘因子展開法計算矩陣 A 的行列式。
    A 必須是一個方陣 (n x n)。
    """
    n = A.shape[0]
    
    if A.shape[1] != n:
        raise ValueError("矩陣必須是方陣")

    # 基本情況
    if n == 1:
        return A[0, 0]
    if n == 2:
        return A[0, 0] * A[1, 1] - A[0, 1] * A[1, 0]

    det_val = 0
    for j in range(n):
        minor = np.delete(np.delete(A, 0, axis=0), j, axis=1)
        cofactor_sign = (-1) ** j
        det_val += cofactor_sign * A[0, j] * recursive_determinant(minor)

    return det_val

# 測試
A_test = np.array([[1, 2, 3], 
                   [4, 5, 6], 
                   [7, 8, 9]])
print("遞迴計算的行列式:", recursive_determinant(A_test))
print("NumPy 內建的行列式:", np.linalg.det(A_test))


# 2. LU 分解後計算行列式
def det_from_lu(A):
    """
    使用 LU 分解計算矩陣 A 的行列式。
    """
    P, L, U = lu(A)
    det_U = np.prod(np.diag(U))
    det_L = 1.0
    det_P = np.linalg.det(P)
    det_A = det_P * det_L * det_U
    return det_A

# 測試
A_test_2 = np.array([[2, 1, 1], [4, 3, 3], [8, 7, 9]])
print("\nLU 分解計算的行列式:", det_from_lu(A_test_2))
print("NumPy 內建的行列式:", np.linalg.det(A_test_2))


# 3. 驗證矩陣分解的重構
def verify_decomposition(A):
    print(f"\n--- 驗證矩陣重構 ---")
    
    # LU 分解
    P, L, U = lu(A)
    A_lu_reconstructed = P.T @ L @ U
    lu_diff = np.linalg.norm(A - A_lu_reconstructed)
    print(f"LU 重構誤差 (P.T @ L @ U): {lu_diff:.2e}")

    # 特徵值分解 (僅方陣)
    if A.shape[0] == A.shape[1]:
        eigen_values, P_eig = np.linalg.eig(A)
        Lambda = np.diag(eigen_values)
        P_inv = np.linalg.inv(P_eig)
        A_eig_reconstructed = P_eig @ Lambda @ P_inv
        eig_diff = np.linalg.norm(A - A_eig_reconstructed)
        print(f"特徵值重構誤差 (P @ Lambda @ P_inv): {eig_diff:.2e}")
    else:
        print("特徵值分解：非方陣，跳過。")

    # SVD 分解
    U, s, V_T = np.linalg.svd(A)
    Sigma = np.zeros(A.shape)
    np.fill_diagonal(Sigma, s)
    A_svd_reconstructed = U @ Sigma @ V_T
    svd_diff = np.linalg.norm(A - A_svd_reconstructed)
    print(f"SVD 重構誤差 (U @ Sigma @ V.T): {svd_diff:.2e}")

# 測試
A_square = np.array([[1, 2, 0], [2, 1, 3], [0, 3, 1]], dtype=float)
verify_decomposition(A_square)

A_rect = np.array([[1, 2, 3], [4, 5, 6]], dtype=float)
verify_decomposition(A_rect)


# 4. 使用特徵值分解計算 SVD
def svd_from_eig(A):
    """
    通過對 A.T @ A 進行特徵值分解來計算 SVD。
    """
    C = A.T @ A
    eigen_values, V = np.linalg.eigh(C)
    idx = eigen_values.argsort()[::-1]
    eigen_values = eigen_values[idx]
    V = V[:, idx]
    singular_values = np.sqrt(np.maximum(0, eigen_values))

    m, n = A.shape
    Sigma = np.zeros((m, n))
    np.fill_diagonal(Sigma, singular_values)

    U = np.zeros((m, m))
    for i in range(m):
        if i < len(singular_values) and singular_values[i] > 1e-10:
            U[:, i] = (1.0 / singular_values[i]) * (A @ V[:, i])

    return singular_values, V.T

# 測試
A_test_svd = np.array([[1, 1], [0, 1], [1, 0]], dtype=float)
s_eig, V_T_eig = svd_from_eig(A_test_svd)
s_np, V_T_np = np.linalg.svd(A_test_svd)[1:]

print("\nSVD (來自 Eig) 奇異值:", s_eig)
print("SVD (來自 NumPy) 奇異值:", s_np)
print("SVD (來自 Eig) V.T:\n", V_T_eig)
print("SVD (來自 NumPy) V.T:\n", V_T_np)


# 5. PCA 使用 SVD
def pca_svd(X, k_components):
    """
    使用 SVD 進行主成分分析 (PCA)。
    """
    # 1. 數據中心化
    X_mean = np.mean(X, axis=0)
    X_centered = X - X_mean

    # 2. SVD 分解
    U, s, V_T = np.linalg.svd(X_centered)

    # 3. 主成分
    components = V_T[:k_components, :]

    # 4. 解釋的變異量
    total_variance = np.sum(s**2)
    variance_explained = (s**2 / total_variance)[:k_components]

    # 5. 降維
    V_k = V_T[:k_components, :].T
    X_reduced = X_centered @ V_k

    return X_reduced, components, variance_explained

# 測試 PCA
X_data = np.array([[1, 2, 3], 
                   [2, 4, 6], 
                   [3, 6, 9], 
                   [10, 10, 10], 
                   [11, 11, 11]], dtype=float)

k = 1
X_reduced, components, var_exp = pca_svd(X_data, k)

print("\n--- PCA 主成分分析 (使用 SVD) ---")
print("降維後的數據 (5 樣本 x 1 維):\n", X_reduced)
print("主成分向量 (1 x 3):\n", components)
print("單一主成分解釋的總變異量百分比:", var_exp * 100, "%")
