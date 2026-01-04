import math

# --- 我們的參數 ---
P = 0.5
N = 10000

# --- 套用公式 log(P^N) = N * log(P) ---

print(f"計算 log(P^N) 其中 P={P}, N={N}\n")

# 1. 使用自然對數 (log_e 或 ln)
#    這是 math.log() 的預設值
log_e_p = math.log(P)
result_log_e = N * log_e_p
print(f"自然對數 (log_e):")
print(f"{N} * log_e({P}) = {result_log_e:.4f}")
print("---")


# 2. 使用常用對數 (log_10)
#    這有助於我們理解 10 的次方
log_10_p = math.log10(P)
result_log_10 = N * log_10_p
print(f"常用對數 (log_10):")
print(f"{N} * log_10({P}) = {result_log_10:.4f}")
print("---")


# 3. 使用二進位對數 (log_2)
#    因為 P = 0.5 = 2^(-1)，這個計算會很漂亮
log_2_p = math.log2(P)
result_log_2 = N * log_2_p
print(f"二進位對數 (log_2):")
print(f"{N} * log_2({P}) = {result_log_2:.1f}")
print("---")
