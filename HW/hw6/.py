import math

# 1. 定義「點，線，圓」與 5. 定義「三角形」
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f"Point({self.x:.2f}, {self.y:.2f})"

class Line:
    """以一般式 ax + by + c = 0 定義直線"""
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

class Circle:
    def __init__(self, center, radius):
        self.center = center  # Point 物件
        self.radius = radius

class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

# 2. 寫程式計算交點
def intersect_lines(l1, l2):
    """兩直線交點 (克拉瑪公式)"""
    det = l1.a * l2.b - l1.b * l2.a
    if det == 0: return None # 平行
    x = (l1.b * l2.c - l2.b * l1.c) / det
    y = (l2.a * l1.c - l1.a * l2.c) / det
    return Point(x, y)

def intersect_line_circle(line, circle):
    """直線與圓交點"""
    # 將圓心平移至原點簡化計算，最後再平移回去
    h, k = circle.center.x, circle.center.y
    r = circle.radius
    # 修正 c 以配合平移後的圓心：a(x+h) + b(y+k) + c = 0 -> ax + by + (ah+bk+c) = 0
    new_c = line.a * h + line.b * k + line.c
    
    a, b, c = line.a, line.b, new_c
    dist_sq = c**2 / (a**2 + b**2)
    if dist_sq > r**2: return [] # 無交點
    
    # 計算投影點與弦長
    x0 = -a*c / (a**2 + b**2)
    y0 = -b*c / (a**2 + b**2)
    d = math.sqrt(r**2 - dist_sq)
    mult = math.sqrt(d**2 / (a**2 + b**2))
    
    p1 = Point(x0 + b*mult + h, y0 - a*mult + k)
    p2 = Point(x0 - b*mult + h, y0 + a*mult + k)
    return [p1, p2] if dist_sq < r**2 else [Point(x0+h, y0+k)]

# 3. 給定一直線和線外一點，做一條垂直線
def get_perpendicular_line(line, point):
    """通過 point 且垂直於 line 的直線"""
    # 原線 ax + bY + c = 0, 垂直線為 bx - ay + c' = 0
    new_a = line.b
    new_b = -line.a
    new_c = -(new_a * point.x + new_b * point.y)
    return Line(new_a, new_b, new_c)

# 4. 驗證畢氏定理
def verify_pythagorean(l1, p_outside):
    # 垂足
    l_perp = get_perpendicular_line(l1, p_outside)
    p_foot = intersect_lines(l1, l_perp)
    
    # 隨取直線上另一點
    p_on_line = Point(p_foot.x + 10, (-l1.c - l1.a*(p_foot.x + 10))/l1.b)
    
    # 計算邊長
    a = math.dist((p_outside.x, p_outside.y), (p_foot.x, p_foot.y))
    b = math.dist((p_foot.x, p_foot.y), (p_on_line.x, p_on_line.y))
    c = math.dist((p_outside.x, p_outside.y), (p_on_line.x, p_on_line.y))
    
    print(f"驗證畢氏定理: a²({a**2:.2f}) + b²({b**2:.2f}) = c²({c**2:.2f})")
    return math.isclose(a**2 + b**2, c**2)

# 6. 平移、縮放、旋轉 (以 Point 為例)
def transform_point(p, dx=0, dy=0, scale=1, angle_deg=0):
    # 縮放
    nx, ny = p.x * scale, p.y * scale
    # 旋轉
    rad = math.radians(angle_deg)
    rx = nx * math.cos(rad) - ny * math.sin(rad)
    ry = nx * math.sin(rad) + ny * math.cos(rad)
    # 平移
    return Point(rx + dx, ry + dy)

# --- 測試執行 ---
p_ext = Point(0, 10)
line_base = Line(0, 1, 0) # y = 0 (X軸)
verify_pythagorean(line_base, p_ext)
