import sympy as sp

def solve_ode_general(coefficients):
    """
    求解常係數齊次常微分方程 (ODE)。
    
    參數:
    coefficients (list): 係數列表 [an, an-1, ..., a1, a0]
                         對應方程: an*y^(n) + ... + a1*y' + a0*y = 0
    
    返回:
    sympy.Expr: 通解的符號表達式
    """
    
    # 1. 定義符號
    t = sp.Symbol('t', real=True)  # 自變數 (時間)
    r = sp.Symbol('r')             # 特徵方程式的變數
    
    # 2. 建構特徵方程式 (Characteristic Equation)
    # 輸入 [1, -5, 6] 對應 r^2 - 5r + 6 = 0
    degree = len(coefficients) - 1
    char_poly = 0
    for i, coeff in enumerate(coefficients):
        char_poly += coeff * r**(degree - i)
        
    # 3. 求解特徵根 (Roots)
    # sp.roots 返回一個字典: {根: 重數}
    roots_dict = sp.roots(char_poly, r)
    
    solution_terms = []
    c_index = 1  # 用於生成 C1, C2, C3...
    
    # 4. 根據根的類型建構通解
    # 我們需要追蹤已經處理過的共軛複數根，避免重複計算
    processed_complex_roots = set()

    for root, multiplicity in roots_dict.items():
        # 分離實部與虛部
        real_part = sp.re(root)
        imag_part = sp.im(root)
        
        # --- 情況 A: 實根 (Real Roots) ---
        if imag_part == 0:
            for k in range(multiplicity):
                C = sp.Symbol(f'C{c_index}')
                # 重根時乘以 t^k
                term = C * (t**k) * sp.exp(real_part * t)
                solution_terms.append(term)
                c_index += 1
                
        # --- 情況 B: 複數根 (Complex Roots) ---
        # 形式為 alpha +/- beta*i
        # 我們只需要處理共軛對中的其中一個 (通常取虛部為正的那個)
        elif root not in processed_complex_roots and sp.conjugate(root) not in processed_complex_roots:
            # 標記這對共軛根已處理
            processed_complex_roots.add(root)
            processed_complex_roots.add(sp.conjugate(root))
            
            alpha = real_part
            beta = abs(imag_part) # 取正值以用於 cos/sin
            
            for k in range(multiplicity):
                C_A = sp.Symbol(f'C{c_index}')
                C_B = sp.Symbol(f'C{c_index + 1}')
                
                # 複數根通解公式: e^(alpha*t) * (C1*cos(beta*t) + C2*sin(beta*t))
                # 若有重根，同樣乘以 t^k
                term = (t**k) * sp.exp(alpha * t) * (C_A * sp.cos(beta * t) + C_B * sp.sin(beta * t))
                
                solution_terms.append(term)
                c_index += 2

    # 5. 線性疊加所有解
    general_solution = sum(solution_terms)
    
    return general_solution

# --- 測試範例 ---

# 範例 1: y'' - 5y' + 6y = 0 (實根: 2, 3)
coefs1 = [1, -5, 6]
sol1 = solve_ode_general(coefs1)
print(f"範例 1 係數 {coefs1} 的通解:\n y(t) = {sol1}\n")

# 範例 2: y'' + 4y = 0 (純虛根: +/- 2i) -> 震盪
coefs2 = [1, 0, 4]
sol2 = solve_ode_general(coefs2)
print(f"範例 2 係數 {coefs2} 的通解:\n y(t) = {sol2}\n")

# 範例 3: y'' + 2y' + y = 0 (重根: -1, -1) -> 臨界阻尼
coefs3 = [1, 2, 1]
sol3 = solve_ode_general(coefs3)
print(f"範例 3 係數 {coefs3} 的通解:\n y(t) = {sol3}\n")
