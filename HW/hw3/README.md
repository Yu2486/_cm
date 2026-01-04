# 幾何幾何學：（點，線，圓）世界的建構

## 一、 點、線、面基本數學表示

### 1. 點

- **數學表示：** 

$P(x, y)$ 

- **距離公式：

$d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$**


### 2. 線

- **兩點式：$P(x_1, x_2)$, $P(y_1, y_2)$**

**$$\frac{y-y_1}{y_1-y_2} = \frac{x-x_1}{x_1-x_2}$$**

- **一般式：**

$Ax + By + C = 0$

**$$A = y_2 - y_1$$**

**$$B = x_1 - x_2$$**

**$$C = x_2y_1 - x_1y_2$$**

- **斜率**

$$m = \frac{y_2 - y_1}{x_2 - x_1}$$

### 3. 圓  

- **圓心：**

$(h, k)$  

- **半徑：$r$**  

- **標準式：**

$(x -h)^2 + (y - k)^2 = r^2$


## 二、交點計算

### 1. 兩直線交點

兩直線 
$A_1x + B_1y = C_1$、

$A_2x + B_2y = C_2$

克拉瑪公式，當


$\Delta=0$


時兩直線平行或重合線


$
\Delta = 

\begin{vmatrix}

A_1 & B_1 \\

A_2 & B_2

\end{vmatrix}

$，


$
\Delta_1 = 
\begin{vmatrix}
C_1 & B_1 \\
C_2 & B_2
\end{vmatrix}
$，

$
\Delta_2 = 
\begin{vmatrix}
A_1 & C_1 \\
A_2 & C_2
\end{vmatrix}
$

$x=\frac{\Delta_1}{\Delta}$，$y=\frac{\Delta_2}{\Delta}$,

### 2. 兩圓交點計算過程

- **計算圓心距**：

$d = \sqrt{(h_2-h_1)^2 + (k_2-k_1)^2}$

- **交點參數**：

   $$
   a = \frac{r_1^2 - r_2^2 + d^2}{2d}, \quad
   h = \sqrt{r_1^2 - a^2}
   $$

- **中點座標**：

   $$
   x_0 = h_1 + a \cdot \frac{h_2 - h_1}{d}, \quad
   y_0 = k_1 + a \cdot \frac{k_2 - k_1}{d}
   $$

- **交點座標**：

   $$
   \begin{aligned}
   x_1 &= x_0 + h \cdot \frac{k_2 - k_1}{d} \\
   y_1 &= y_0 - h \cdot \frac{h_2 - h_1}{d} \\
   x_2 &= x_0 - h \cdot \frac{k_2 - k_1}{d} \\
   y_2 &= y_0 + h \cdot \frac{h_2 - h_1}{d}
   \end{aligned}
   $$

### 3. 直線與圓交點

將直線方程代入圓方程得到二次方程：

$$
(1+m^2)x^2 + 2(mb - mk - h)x + (h^2 + (b-k)^2 - r^2) = 0
$$

## 三、 垂直線與垂足數學

### 從點到直線的垂直線

給定直線 

$Ax + By + C = 0$ 

和點

 $P(x_0,y_0)$：

- **垂直線方程**：

$Bx - Ay + (Ay_0 - Bx_0) = 0$

### 垂足座標

$$
x = \frac{B^2x_0 - ABy_0 - AC}{A^2 + B^2}, \quad
y = \frac{A^2y_0 - ABx_0 - BC}{A^2 + B^2}
$$

## 四、 畢氏定理驗證

對於直角三角形：

- 垂直邊：

$a = \text{distance}(P, \text{垂足})$

- 底邊：

$b = \text{distance}(\text{垂足}, P_1)$ 

- 斜邊：

$c = \text{distance}(P, P_1)$

**畢氏定理**：

$a^2 + b^2 = c^2$

## 五、幾何變換數學

### 平移 (Translation)

$$
\begin{aligned}
x' &= x + dx \\
y' &= y + dy
\end{aligned}
$$

### 縮放 (Scaling)

以點 $(c_x, c_y)$ 為中心：

$$
\begin{aligned}
x' &= c_x + (x - c_x) \times \text{factor} \\
y' &= c_y + (y - c_y) \times \text{factor}
\end{aligned}
$$

### 旋轉 (Rotation)

以點 $(c_x, c_y)$ 為中心旋轉角度 $\theta$：

$$
\begin{aligned}
x_{\text{rel}} &= x - c_x \\
y_{\text{rel}} &= y - c_y \\
x_{\text{rotated}} &= x_{\text{rel}}\cos\theta - y_{\text{rel}}\sin\theta \\
y_{\text{rotated}} &= x_{\text{rel}}\sin\theta + y_{\text{rel}}\cos\theta \\
x' &= x_{\text{rotated}} + c_x \\
y' &= y_{\text{rotated}} + c_y
\end{aligned}
$$
