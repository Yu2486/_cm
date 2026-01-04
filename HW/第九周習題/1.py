from decimal import Decimal, getcontext

# 1. 設定我們想要的精確度 (例如 50 位有效數字)
#    這足以顯示開頭的數字和指數
getcontext().prec = 50

# 2. 定義我們的變數
n_tosses = 10000
probability_per_toss = Decimal(0.5)

# 3. 使用 Decimal 物件進行高精度計算
final_probability = probability_per_toss ** n_tosses

# 4. 輸出結果
print(f"一個公平銅板，連續投擲 {n_tosses} 次，")
print("全部得到正面的機率（使用高精度計算）為：")
print(final_probability)

print("\n--- (對比) ---")

# 5. 對比：使用標準浮點數的結果
standard_float_prob = 0.5 ** n_tosses
print("如果使用標準的浮點數計算：")
print(standard_float_prob)
