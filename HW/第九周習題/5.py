# --- 輔助函式 ---
def bits_to_str(bits):
    """ 將 [1, 0, 1, 1] 轉換為 "1011" """
    return "".join(map(str, bits))

def str_to_bits(s):
    """ 將 "1011" 轉換為 [1, 0, 1, 1] """
    return [int(b) for b in s]

# --- (7,4) 漢明碼編碼器 ---
def hamming_encode(data_bits):
    """
    將 4 位元的資料 (list) 編碼為 7 位元的漢明碼 (list)。
    資料位元 D = [d1, d2, d3, d4]
    """
    if len(data_bits) != 4:
        raise ValueError("資料必須是 4 位元。")
        
    d1, d2, d3, d4 = data_bits
    
    # 根據偶同位計算 P
    p1 = d1 ^ d2 ^ d4
    p2 = d1 ^ d3 ^ d4
    p3 = d2 ^ d3 ^ d4
    
    # 按照 (P1, P2, D1, P3, D2, D3, D4) 的順序組合碼字
    codeword = [p1, p2, d1, p3, d2, d3, d4]
    return codeword

# --- (7,4) 漢明碼解碼器 ---
def hamming_decode(codeword):
    """
    解碼 7 位元的漢明碼 (list)。
    返回一個 tuple: (修正後的 4 位元資料, 偵測到的錯誤位置)
    錯誤位置 0 代表沒有錯誤。
    """
    if len(codeword) != 7:
        raise ValueError("碼字必須是 7 位元。")

    # 從 codeword 中分離 P 和 D
    # 索引 (0-based): [0, 1, 2, 3, 4, 5, 6]
    # 位置 (1-based):  1, 2, 3, 4, 5, 6, 7
    # 內容:           P1,P2,D1,P3,D2,D3,D4
    
    p1_rec = codeword[0]
    p2_rec = codeword[1]
    d1_rec = codeword[2]
    p3_rec = codeword[3]
    d2_rec = codeword[4]
    d3_rec = codeword[5]
    d4_rec = codeword[6]
    
    # 計算校正子 (Syndrome bits)
    s1 = p1_rec ^ d1_rec ^ d2_rec ^ d4_rec
    s2 = p2_rec ^ d1_rec ^ d3_rec ^ d4_rec
    s3 = p3_rec ^ d2_rec ^ d3_rec ^ d4_rec
    
    # 將 S3, S2, S1 組合成錯誤位置
    # error_pos 是 1-based 的
    error_pos = (s3 * 4) + (s2 * 2) + (s1 * 1)
    
    # 複製一份原始碼字以進行修正
    corrected_codeword = list(codeword)
    
    if error_pos > 0:
        print(f"    [偵測] 錯誤發生在位置 {error_pos}")
        
        # 修正錯誤：將該位置的位元反轉 (0->1, 1->0)
        # error_pos 是 1-based, list 索引是 0-based
        error_index = error_pos - 1
        
        # 1-x 是 0/1 反轉的技巧
        corrected_codeword[error_index] = 1 - corrected_codeword[error_index] 
        print(f"    [修正] 已將位置 {error_pos} 的位元反轉。")
        
    else:
        print("    [偵測] 未偵測到錯誤。")

    # 從 "已修正" 的碼字中提取資料
    # D1 (位置 3, 索引 2)
    # D2 (位置 5, 索引 4)
    # D3 (位置 6, 索引 5)
    # D4 (位置 7, 索引 6)
    corrected_data = [
        corrected_codeword[2],
        corrected_codeword[4],
        corrected_codeword[5],
        corrected_codeword[6]
    ]
    
    return corrected_data, error_pos

# --- 主程式：執行範例 ---
if __name__ == "__main__":
    
    # 1. 原始資料
    original_data = str_to_bits("1011")
    print(f"原始資料 (D1,D2,D3,D4): {bits_to_str(original_data)}")
    print("-" * 30)

    # 2. 編碼
    encoded_word = hamming_encode(original_data)
    print(f"編碼後的漢明碼 (7位): {bits_to_str(encoded_word)}")
    print("-" * 30)

    # 3. 模擬錯誤 (情境 1: 沒有錯誤)
    print("情境 1: 模擬無錯誤傳輸")
    received_word_ok = list(encoded_word) # 複製一份
    print(f"  接收到的碼字: {bits_to_str(received_word_ok)}")
    
    decoded_data_ok, err_pos_ok = hamming_decode(received_word_ok)
    print(f"  解碼後的資料: {bits_to_str(decoded_data_ok)}")
    
    assert original_data == decoded_data_ok
    print("  結果: 資料正確！")
    print("-" * 30)

    # 4. 模擬錯誤 (情境 2: 1 位元錯誤)
    print("情境 2: 模擬 1 位元錯誤")
    
    # 複製一份，並手動製造一個錯誤
    # 假設位置 5 (索引 4) 發生錯誤
    received_word_err = list(encoded_word)
    error_sim_pos = 5 # 1-based
    error_sim_idx = error_sim_pos - 1
    
    received_word_err[error_sim_idx] = 1 - received_word_err[error_sim_idx] # 反轉
    
    print(f"  原始碼字: {bits_to_str(encoded_word)}")
    print(f"  (模擬錯誤，將位置 {error_sim_pos} 反轉)")
    print(f"  接收到的碼字: {bits_to_str(received_word_err)}")
    
    # 5. 解碼與修正
    decoded_data_err, err_pos_detected = hamming_decode(received_word_err)
    print(f"  解碼並修正後的資料: {bits_to_str(decoded_data_err)}")
    
    # 驗證
    assert err_pos_detected == error_sim_pos
    assert original_data == decoded_data_err
    print("  結果: 錯誤被成功偵測並修正，資料恢復！")
    print("-" * 30)
