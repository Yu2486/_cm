import math
import turtle
from typing import List, Tuple, Optional

# ==================== 幾何類別定義 ====================
class Point:
    """點類別"""
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f"Point({self.x}, {self.y})"
    
    def __eq__(self, other):
        if not isinstance(other, Point):
            return False
        return math.isclose(self.x, other.x) and math.isclose(self.y, other.y)
    
    def distance_to(self, other: 'Point') -> float:
        """計算兩點之間的距離"""
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
    
    def translate(self, dx: float, dy: float) -> 'Point':
        """平移點"""
        return Point(self.x + dx, self.y + dy)
    
    def scale(self, factor: float, center: 'Point' = None) -> 'Point':
        """縮放點"""
        if center is None:
            center = Point(0, 0)
        translated = Point(self.x - center.x, self.y - center.y)
        scaled = Point(translated.x * factor, translated.y * factor)
        return Point(scaled.x + center.x, scaled.y + center.y)
    
    def rotate(self, angle: float, center: 'Point' = None) -> 'Point':
        """旋轉點（角度為弧度）"""
        if center is None:
            center = Point(0, 0)
        x_rel = self.x - center.x
        y_rel = self.y - center.y
        cos_angle = math.cos(angle)
        sin_angle = math.sin(angle)
        x_rotated = x_rel * cos_angle - y_rel * sin_angle
        y_rotated = x_rel * sin_angle + y_rel * cos_angle
        return Point(x_rotated + center.x, y_rotated + center.y)

class Line:
    """直線類別"""
    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        return f"Line({self.p1}, {self.p2})"
    
    def slope(self) -> Optional[float]:
        """計算斜率，如果是垂直線則返回None"""
        if math.isclose(self.p1.x, self.p2.x):
            return None
        return (self.p2.y - self.p1.y) / (self.p2.x - self.p1.x)
    
    def intercept(self) -> Optional[float]:
        """計算y截距，如果是垂直線則返回None"""
        slope = self.slope()
        if slope is None:
            return None
        return self.p1.y - slope * self.p1.x
    
    def is_vertical(self) -> bool:
        """判斷是否為垂直線"""
        return math.isclose(self.p1.x, self.p2.x)
    
    def is_horizontal(self) -> bool:
        """判斷是否為水平線"""
        return math.isclose(self.p1.y, self.p2.y)
    
    def equation_coefficients(self) -> Tuple[float, float, float]:
        """返回直線方程係數 Ax + By + C = 0"""
        A = self.p2.y - self.p1.y
        B = self.p1.x - self.p2.x
        C = self.p2.x * self.p1.y - self.p1.x * self.p2.y
        return A, B, C
    
    def translate(self, dx: float, dy: float) -> 'Line':
        """平移直線"""
        return Line(self.p1.translate(dx, dy), self.p2.translate(dx, dy))
    
    def scale(self, factor: float, center: Point = None) -> 'Line':
        """縮放直線"""
        return Line(self.p1.scale(factor, center), self.p2.scale(factor, center))
    
    def rotate(self, angle: float, center: Point = None) -> 'Line':
        """旋轉直線（角度為弧度）"""
        return Line(self.p1.rotate(angle, center), self.p2.rotate(angle, center))

class Circle:
    """圓類別"""
    def __init__(self, center: Point, radius: float):
        self.center = center
        self.radius = radius
    
    def __repr__(self):
        return f"Circle(center={self.center}, radius={self.radius})"
    
    def area(self) -> float:
        """計算圓面積"""
        return math.pi * self.radius ** 2
    
    def circumference(self) -> float:
        """計算圓周長"""
        return 2 * math.pi * self.radius
    
    def translate(self, dx: float, dy: float) -> 'Circle':
        """平移圓"""
        return Circle(self.center.translate(dx, dy), self.radius)
    
    def scale(self, factor: float, center: Point = None) -> 'Circle':
        """縮放圓"""
        return Circle(self.center.scale(factor, center), self.radius * factor)
    
    def rotate(self, angle: float, center: Point = None) -> 'Circle':
        """旋轉圓（角度為弧度）"""
        return Circle(self.center.rotate(angle, center), self.radius)

class Triangle:
    """三角形類別"""
    def __init__(self, p1: Point, p2: Point, p3: Point):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
    
    def __repr__(self):
        return f"Triangle({self.p1}, {self.p2}, {self.p3})"
    
    def area(self) -> float:
        """計算三角形面積（使用海龍公式）"""
        a = self.p1.distance_to(self.p2)
        b = self.p2.distance_to(self.p3)
        c = self.p3.distance_to(self.p1)
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))
    
    def perimeter(self) -> float:
        """計算三角形周長"""
        return (self.p1.distance_to(self.p2) + 
                self.p2.distance_to(self.p3) + 
                self.p3.distance_to(self.p1))
    
    def translate(self, dx: float, dy: float) -> 'Triangle':
        """平移三角形"""
        return Triangle(self.p1.translate(dx, dy), 
                       self.p2.translate(dx, dy), 
                       self.p3.translate(dx, dy))
    
    def scale(self, factor: float, center: Point = None) -> 'Triangle':
        """縮放三角形"""
        return Triangle(self.p1.scale(factor, center), 
                       self.p2.scale(factor, center), 
                       self.p3.scale(factor, center))
    
    def rotate(self, angle: float, center: Point = None) -> 'Triangle':
        """旋轉三角形（角度為弧度）"""
        return Triangle(self.p1.rotate(angle, center), 
                       self.p2.rotate(angle, center), 
                       self.p3.rotate(angle, center))

# ==================== 幾何運算函數 ====================
def line_intersection(line1: Line, line2: Line) -> Optional[Point]:
    """計算兩直線交點"""
    A1, B1, C1 = line1.equation_coefficients()
    A2, B2, C2 = line2.equation_coefficients()
    
    determinant = A1 * B2 - A2 * B1
    
    if math.isclose(determinant, 0):
        return None  # 平行或重合
    
    x = (B1 * C2 - B2 * C1) / determinant
    y = (A2 * C1 - A1 * C2) / determinant
    
    return Point(x, y)

def circle_intersection(circle1: Circle, circle2: Circle) -> List[Point]:
    """計算兩個圓的交點"""
    d = circle1.center.distance_to(circle2.center)
    r1, r2 = circle1.radius, circle2.radius
    
    # 檢查是否有交點
    if d > r1 + r2 or d < abs(r1 - r2) or (math.isclose(d, 0) and math.isclose(r1, r2)):
        return []
    
    # 計算交點
    a = (r1**2 - r2**2 + d**2) / (2 * d)
    h = math.sqrt(r1**2 - a**2)
    
    # 中間點
    x0 = circle1.center.x + a * (circle2.center.x - circle1.center.x) / d
    y0 = circle1.center.y + a * (circle2.center.y - circle1.center.y) / d
    
    # 交點
    x1 = x0 + h * (circle2.center.y - circle1.center.y) / d
    y1 = y0 - h * (circle2.center.x - circle1.center.x) / d
    
    x2 = x0 - h * (circle2.center.y - circle1.center.y) / d
    y2 = y0 + h * (circle2.center.x - circle1.center.x) / d
    
    point1 = Point(x1, y1)
    point2 = Point(x2, y2)
    
    if math.isclose(h, 0):  # 相切，只有一個交點
        return [point1]
    
    return [point1, point2]

def line_circle_intersection(line: Line, circle: Circle) -> List[Point]:
    """計算直線與圓的交點"""
    A, B, C = line.equation_coefficients()
    h, k = circle.center.x, circle.center.y
    r = circle.radius
    
    # 將直線方程轉換為參數形式
    if math.isclose(B, 0):  # 垂直線
        x = -C / A
        discriminant = r**2 - (x - h)**2
        
        if discriminant < 0:
            return []
        elif math.isclose(discriminant, 0):
            return [Point(x, k)]
        else:
            sqrt_disc = math.sqrt(discriminant)
            return [Point(x, k + sqrt_disc), Point(x, k - sqrt_disc)]
    else:
        # 一般情況：將直線方程代入圓方程
        m = -A / B
        b = -C / B
        
        # 二次方程係數
        a_coeff = 1 + m**2
        b_coeff = 2 * (m * b - m * k - h)
        c_coeff = h**2 + (b - k)**2 - r**2
        
        discriminant = b_coeff**2 - 4 * a_coeff * c_coeff
        
        if discriminant < 0:
            return []
        
        sqrt_disc = math.sqrt(discriminant)
        x1 = (-b_coeff + sqrt_disc) / (2 * a_coeff)
        x2 = (-b_coeff - sqrt_disc) / (2 * a_coeff)
        
        y1 = m * x1 + b
        y2 = m * x2 + b
        
        if math.isclose(discriminant, 0):
            return [Point(x1, y1)]
        else:
            return [Point(x1, y1), Point(x2, y2)]

def perpendicular_from_point(line: Line, point: Point) -> Line:
    """從點向直線做垂直線"""
    A, B, C = line.equation_coefficients()
    
    if math.isclose(B, 0):  # 垂直線
        # 垂直線的垂線是水平線
        return Line(point, Point(point.x + 1, point.y))
    elif math.isclose(A, 0):  # 水平線
        # 水平線的垂線是垂直線
        return Line(point, Point(point.x, point.y + 1))
    else:
        # 一般情況：垂直線的斜率是原斜率的負倒數
        original_slope = -A / B
        perpendicular_slope = -1 / original_slope
        
        # 通過給定點的垂直線方程
        p2 = Point(point.x + 1, point.y + perpendicular_slope)
        return Line(point, p2)

def perpendicular_foot(line: Line, point: Point) -> Point:
    """計算點到直線的垂足"""
    perpendicular_line = perpendicular_from_point(line, point)
    return line_intersection(line, perpendicular_line)

# ==================== 繪圖類別 ====================
class GeometryPlotter:
    """幾何繪圖器"""
    def __init__(self, width=800, height=600):
        self.screen = turtle.Screen()
        self.screen.setup(width, height)
        self.screen.title("幾何系統視覺化")
        self.screen.bgcolor("white")
        
        # 創建多個烏龜用於繪製不同元素
        self.main_turtle = turtle.Turtle()
        self.main_turtle.speed(0)
        
        self.point_turtle = turtle.Turtle()
        self.point_turtle.speed(0)
        self.point_turtle.hideturtle()
        
        self.text_turtle = turtle.Turtle()
        self.text_turtle.speed(0)
        self.text_turtle.hideturtle()
        
        self.setup_coordinate_system()
    
    def setup_coordinate_system(self):
        """設置座標系"""
        self.main_turtle.penup()
        self.main_turtle.goto(-400, 0)
        self.main_turtle.pendown()
        self.main_turtle.goto(400, 0)  # x軸
        self.main_turtle.penup()
        self.main_turtle.goto(0, -300)
        self.main_turtle.pendown()
        self.main_turtle.goto(0, 300)  # y軸
        
        # 繪製刻度
        for i in range(-400, 401, 50):
            self.main_turtle.penup()
            self.main_turtle.goto(i, -5)
            self.main_turtle.pendown()
            self.main_turtle.goto(i, 5)
            
        for i in range(-300, 301, 50):
            self.main_turtle.penup()
            self.main_turtle.goto(-5, i)
            self.main_turtle.pendown()
            self.main_turtle.goto(5, i)
    
    def draw_point(self, point: Point, color="red", size=3, label=None):
        """繪製點"""
        self.point_turtle.penup()
        self.point_turtle.goto(point.x, point.y)
        self.point_turtle.pendown()
        self.point_turtle.dot(size, color)
        
        if label:
            self.text_turtle.penup()
            self.text_turtle.goto(point.x + 5, point.y + 5)
            self.text_turtle.pendown()
            self.text_turtle.write(label, font=("Arial", 8, "normal"))
    
    def draw_line(self, line: Line, color="blue", width=2, label=None):
        """繪製直線"""
        self.main_turtle.penup()
        self.main_turtle.goto(line.p1.x, line.p1.y)
        self.main_turtle.pendown()
        self.main_turtle.pencolor(color)
        self.main_turtle.width(width)
        self.main_turtle.goto(line.p2.x, line.p2.y)
        self.main_turtle.pencolor("black")
        self.main_turtle.width(1)
        
        if label:
            mid_x = (line.p1.x + line.p2.x) / 2
            mid_y = (line.p1.y + line.p2.y) / 2
            self.text_turtle.penup()
            self.text_turtle.goto(mid_x + 5, mid_y + 5)
            self.text_turtle.pendown()
            self.text_turtle.write(label, font=("Arial", 8, "normal"))
    
    def draw_circle(self, circle: Circle, color="green", width=2, label=None):
        """繪製圓"""
        self.main_turtle.penup()
        self.main_turtle.goto(circle.center.x, circle.center.y - circle.radius)
        self.main_turtle.pendown()
        self.main_turtle.pencolor(color)
        self.main_turtle.width(width)
        self.main_turtle.circle(circle.radius)
        self.main_turtle.pencolor("black")
        self.main_turtle.width(1)
        
        # 繪製圓心
        self.draw_point(circle.center, color="darkgreen", size=2)
        
        if label:
            self.text_turtle.penup()
            self.text_turtle.goto(circle.center.x + 5, circle.center.y + 5)
            self.text_turtle.pendown()
            self.text_turtle.write(label, font=("Arial", 8, "normal"))
    
    def draw_triangle(self, triangle: Triangle, color="purple", width=2, label=None):
        """繪製三角形"""
        self.main_turtle.penup()
        self.main_turtle.goto(triangle.p1.x, triangle.p1.y)
        self.main_turtle.pendown()
        self.main_turtle.pencolor(color)
        self.main_turtle.width(width)
        self.main_turtle.goto(triangle.p2.x, triangle.p2.y)
        self.main_turtle.goto(triangle.p3.x, triangle.p3.y)
        self.main_turtle.goto(triangle.p1.x, triangle.p1.y)
        self.main_turtle.pencolor("black")
        self.main_turtle.width(1)
        
        if label:
            centroid_x = (triangle.p1.x + triangle.p2.x + triangle.p3.x) / 3
            centroid_y = (triangle.p1.y + triangle.p2.y + triangle.p3.y) / 3
            self.text_turtle.penup()
            self.text_turtle.goto(centroid_x + 5, centroid_y + 5)
            self.text_turtle.pendown()
            self.text_turtle.write(label, font=("Arial", 8, "normal"))
    
    def draw_intersection_points(self, points: List[Point], color="orange", size=5):
        """繪製交點"""
        for i, point in enumerate(points):
            self.draw_point(point, color=color, size=size, label=f"I{i+1}")
    
    def clear_drawing(self):
        """清除繪圖"""
        self.main_turtle.clear()
        self.point_turtle.clear()
        self.text_turtle.clear()
        self.setup_coordinate_system()
    
    def keep_open(self):
        """保持視窗開啟"""
        self.screen.exitonclick()

# ==================== 示範函數 ====================
def demo_intersections():
    """示範交點計算並繪圖"""
    plotter = GeometryPlotter()
    
    print("=== 幾何交點視覺化示範 ===\n")
    
    # 1. 兩直線交點
    print("1. 繪製兩直線交點...")
    line1 = Line(Point(-100, -100), Point(100, 100))
    line2 = Line(Point(-100, 100), Point(100, -100))
    
    plotter.draw_line(line1, color="blue", label="L1")
    plotter.draw_line(line2, color="red", label="L2")
    
    intersection = line_intersection(line1, line2)
    if intersection:
        plotter.draw_point(intersection, color="orange", size=6, label="交點")
        print(f"直線交點: {intersection}")
    
    # 2. 兩圓交點
    print("\n2. 繪製兩圓交點...")
    circle1 = Circle(Point(-50, 0), 80)
    circle2 = Circle(Point(50, 0), 80)
    
    plotter.draw_circle(circle1, color="lightblue", label="C1")
    plotter.draw_circle(circle2, color="lightgreen", label="C2")
    
    circle_intersections = circle_intersection(circle1, circle2)
    plotter.draw_intersection_points(circle_intersections)
    print(f"圓交點: {circle_intersections}")
    
    # 3. 直線與圓交點
    print("\n3. 繪製直線與圓交點...")
    line3 = Line(Point(-150, 50), Point(150, -50))
    circle3 = Circle(Point(0, 0), 70)
    
    plotter.draw_line(line3, color="purple", label="L3")
    plotter.draw_circle(circle3, color="pink", label="C3")
    
    line_circle_intersections = line_circle_intersection(line3, circle3)
    plotter.draw_intersection_points(line_circle_intersections, color="brown")
    print(f"直線圓交點: {line_circle_intersections}")
    
    plotter.keep_open()

def demo_perpendicular_and_pythagoras():
    """示範垂直線和畢氏定理"""
    plotter = GeometryPlotter()
    
    print("=== 垂直線與畢氏定理視覺化 ===")
    
    # 創建水平線和線外點
    base_line = Line(Point(-150, 0), Point(150, 0))
    external_point = Point(50, 120)
    
    # 繪製基本元素
    plotter.draw_line(base_line, color="black", width=3, label="基線")
    plotter.draw_point(external_point, color="red", size=5, label="外部點")
    
    # 計算垂直線和垂足
    perpendicular_line = perpendicular_from_point(base_line, external_point)
    foot = perpendicular_foot(base_line, external_point)
    
    if foot:
        # 繪製垂直線和垂足
        plotter.draw_line(perpendicular_line, color="green", label="垂直線")
        plotter.draw_point(foot, color="blue", size=5, label="垂足")
        
        # 繪製直角三角形
        plotter.main_turtle.penup()
        plotter.main_turtle.goto(external_point.x, external_point.y)
        plotter.main_turtle.pendown()
        plotter.main_turtle.pencolor("orange")
        plotter.main_turtle.goto(foot.x, foot.y)
        plotter.main_turtle.goto(base_line.p1.x, base_line.p1.y)
        plotter.main_turtle.goto(external_point.x, external_point.y)
        plotter.main_turtle.pencolor("black")
        
        # 計算並顯示距離
        a = external_point.distance_to(foot)
        b = foot.distance_to(base_line.p1)
        c = external_point.distance_to(base_line.p1)
        
        # 顯示距離標籤
        plotter.text_turtle.penup()
        plotter.text_turtle.goto((external_point.x + foot.x)/2, (external_point.y + foot.y)/2)
        plotter.text_turtle.write(f"a={a:.1f}", font=("Arial", 10, "normal"))
        
        plotter.text_turtle.goto((foot.x + base_line.p1.x)/2, (foot.y + base_line.p1.y)/2)
        plotter.text_turtle.write(f"b={b:.1f}", font=("Arial", 10, "normal"))
        
        plotter.text_turtle.goto((external_point.x + base_line.p1.x)/2, (external_point.y + base_line.p1.y)/2)
        plotter.text_turtle.write(f"c={c:.1f}", font=("Arial", 10, "normal"))
        
        # 驗證畢氏定理
        print(f"垂直邊 a = {a:.2f}")
        print(f"底邊 b = {b:.2f}")
        print(f"斜邊 c = {c:.2f}")
        print(f"a² + b² = {a**2 + b**2:.2f}")
        print(f"c² = {c**2:.2f}")
        print(f"畢氏定理驗證: {math.isclose(a**2 + b**2, c**2)}")
    
    plotter.keep_open()

def demo_transformations():
    """示範幾何變換"""
    plotter = GeometryPlotter()
    
    print("=== 幾何變換視覺化 ===")
    
    # 原始三角形
    original_triangle = Triangle(Point(-100, -50), Point(0, 100), Point(100, -50))
    plotter.draw_triangle(original_triangle, color="gray", label="原始")
    
    # 平移
    translated_triangle = original_triangle.translate(50, 30)
    plotter.draw_triangle(translated_triangle, color="blue", label="平移")
    
    # 縮放
    scaled_triangle = original_triangle.scale(1.5, Point(0, 0))
    plotter.draw_triangle(scaled_triangle, color="red", label="縮放")
    
    # 旋轉
    rotated_triangle = original_triangle.rotate(math.pi/4, Point(0, 0))  # 45度
    plotter.draw_triangle(rotated_triangle, color="green", label="旋轉")
    
    # 繪製變換中心
    plotter.draw_point(Point(0, 0), color="black", size=4, label="中心")
    
    print("繪製了：原始三角形（灰）、平移後（藍）、縮放後（紅）、旋轉後（綠）")
    
    plotter.keep_open()

# ==================== 主程式 ====================
if __name__ == "__main__":
    print("請選擇要運行的示範：")
    print("1. 交點計算示範")
    print("2. 垂直線與畢氏定理")
    print("3. 幾何變換示範")
    
    choice = input("請輸入選擇 (1-3): ").strip()
    
    if choice == "1":
        demo_intersections()
    elif choice == "2":
        demo_perpendicular_and_pythagoras()
    elif choice == "3":
        demo_transformations()
    else:
        print("無效選擇，運行交點計算示範")
        demo_intersections()
