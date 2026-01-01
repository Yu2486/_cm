h=0.00001 # 趨近於0的△x

def df(f, x):
    return (f(x+h)-f(x))/h
    # (f(x+△x)-f(x))/△x = f'(x)
    # 代入h

def integral(f, a, b):
    x=a #從a開始
    area=0 #初始化
    while x<b:
        area+=f(x)*h
        x+=h
    return area
    # 使用黎曼和的方式由a積分到b
    # a     ._.b  每格間距h,高度為f(x),面積為f(x)*h,累加即是積分結果
    #    ._.| |
    # ._.| || |
    # | || || |
    # |h||h||h|
def theorem1(f, x):
    r = df(lambda x:integral(f, 0, x), x) # 將x的積分結果代入做微分得到r lambda是直接不記名的傳入一個函式
    print('r=', r, 'f(x)=', f(x))
    print('abs(r-f(x))<0.01 = ', abs(r-f(x))<0.01) #abs()為取絕對值
    assert abs(r-f(x))<0.01 # 驗證結果r與原函式f(x)的差是否夠小,不超過0.01 

def f(x):
    return x**3 # 宣告一個f(x)=x**3函數做測試

print('df(f, 2)=', df(f, 2)) # 代入x=2做測試的微分結果
print('integral(f, 0, 2)=', integral(f, 0, 2)) # 由0積到2的積分結果

theorem1(f, 2) # 代入驗證理論是否正確
