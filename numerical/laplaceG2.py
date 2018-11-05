# -*- coding: utf-8 -*-
"""
LaplaceG.pyプログラム
ラプラス方程式の解法プログラム
反復法によりラプラス方程式を解く
グラフ描写機能追加！！！！

"""
# モジュールのインポート
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import math

# 定数
LIMIT = 1000 # 反復回数の上限
N = 101 # x軸方向の分割数
M = 101 # y軸方向の分割数

#下請け関数の定義
# iteration()関数
def iteration(u):
    """1回分の反復計算, 
    D2領域の計算用"""
    u_next = [[0 for i in range(N)] for j in range(M)] #次ステップのuij
    # 次のステップの値を計算
    # 下1/4の計算
    for i in range(int(N / 4), int((N - 1) * 3 / 4)):
        for j in range(1, int((M - 1) / 4)):
            u_next[i][j] = (u[i][j - 1] + u[i - 1][j] + u[i + 1][j] + u[i][j + 1]) / 4
    # 中央1/2の計算
    for i in range(1, N-1):
        for j in range(int((M - 1) / 4), int((M - 1) * 3 / 4)):
            u_next[i][j] = (u[i][j - 1] + u[i - 1][j] + u[i + 1][j] + u[i][j + 1]) / 4
    # 上1/4の計算
    for i in range(int(N / 4), int((N - 1) * 3 / 4)):
        for j in range(int((M - 1) * 3 / 4), M - 1):
            u_next[i][j] = (u[i][j - 1] + u[i - 1][j] + u[i + 1][j] + u[i][j + 1]) / 4
  
    
    
    # uijの更新
    for i in range(1, N - 1):
        for j in range(1, M - 1):
            u[i][j] = u_next[i][j]
# iteration()関数の終わり＼(^o^)／

# メイン実行部
u = [[0 for i in range(N)] for j in range(M)] #uijの初期化
for i in range(M):
    u[0][i] = math.sin(2 * math.pi * i / (M - 1))

#反復法の計算
for i in range(LIMIT):
    iteration(u)

print(u) #結果の出力

# グラフ描写
x = np.arange(0, N)
y = np.arange(0, M)
X,Y = np.meshgrid(x, y)
fig = plt.figure()
ax = Axes3D(fig)
# ax.plot_wireframe(X, Y, u) #wireframe形式
ax.plot_surface(X, Y, u, cmap = cm.coolwarm) #surface形式
plt.show()
#＼(^o^)／     