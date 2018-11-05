# _*_ coding: utf-8 _*_
"""
LanderG.pyのプログラム
落下運動のsimulation
逆噴射をする着陸船のsimulation
matplotlibによってグラフ描写機能付き
"""
# モジュールのインポート
import numpy as np
import matplotlib.pyplot as plt

# 定数
F = 1.5 #逆噴射の加速度を決定する係数
G = 9.80665 # 重力加速度

# 下請け関数の定義
# retrofire関数()関数
def retrofire(t, tf):
 """逆噴射の制御を担当する関数"""
 if t >= tf:
  return -F * G # 逆噴射
 else:
    return 0.0; #逆噴射の終わり

# メイン実行部
t = 0.0 #時刻t
h = 0.01 #時刻の刻み幅

# 係数の入力
v = float(input("初速度v0を入力してください:"))
x0 = float(input("初期高度x0を入力してください:"))
tf = float(input("逆噴射開始時刻を入力してください:"))
x = x0 #初期高度の設定
print ("{:.7f} {:.7f} {:.7f} ".format(t, x, v)) #現時刻と現在の位置

# グラフデータに現在地を追加
tlist = [t]
xlist = [x]

# 自由落下の計算
while (x >= 0) and (x <= x0): #地面に到達するまで計算
 t += h #時刻の更新
 v += (G + retrofire(t, tf)) * h #速度の計算
 x -= v * h #速度の更新
 print ("{:.7f} {:.7f} {:.7f}". format(t, x, v)) #現在時刻と現在の位置・速度
 # graphdataに現在位置を追加
 tlist.append(t)
 xlist.append(x)
# graphの表示
plt.plot(tlist, xlist) #グラフをプロット
plt.show()
# end