# _*_ coding: utf-8 _*_
"""
orderfreefall.pyプログラム
自由落下Simulation
自由落下の運動方程式を数値的に解く
Scipyのモジュールを利用する
"""
# モジュールのインポート
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# 定数
G = 9.80665 # 重力加速度

# 下請け関数の定義
# f()関数
def f(x,t):
 """微分方程式の右辺を与える"""
 return [x[1], -G]
# f()関数の終わり＼(^o^)／

# メイン実行部
# 係数の入力
v = float(input("初速度v0を入力してください"))
x = float(input("初期高度x0を入力してください"))

#自由落下の計算
x0 = [x, v] #初期条件の設定
t = np.arange(0, 4.53, 0.01) # 0～4.53secまでを0.01で計算
x = odeint(f, x0, t) #計算の本体
print(x) #結果出力

plt.plot(t, x)
plt.show()

# end

