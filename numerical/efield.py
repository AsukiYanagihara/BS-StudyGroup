# _*_ coding utf-8 _*_
"""
efield.py プログラム
2次元運動のSimulationプログラム
電界中の荷電粒子のSimulation
"""
# モジュールのインポート
import math

# 定数
Q = (((0.0, 0.0), 10.0), ((5.0, -5.0), 5.0)) # 電荷の位置と値
TIMELIMIT = 20.0 # Similationうちきり時刻
RLIMIT = 0.1 # 距離rの最低値
H = 0.01 # 時刻の刻み幅

# メイン実行部
t = 0.0 # 時刻t

# 係数の入力
vx = float(input("初速度v0xを入力してください:"))
vy = float(input("初速度v0yを入力してください:"))
x = float(input("初期位置xを入力してください:"))
y = float(input("初期位置yを入力してください:"))

print("{:.7f} {:.7f} {:.7f} {:.7f} {:.7f}".format(t, x, y, vx, vy))
 # 現在時刻と現在の位置
 
# 2次元運動の計算
while t < TIMELIMIT: #打ち切り時間まで計算
 t = t + H #時刻の更新
 rmin=float("inf") #距離の最小値を初期化
 for qi in Q:
  rx = qi[0][0] - x #距離rxの計算
  ry = qi[0][1] - y #距離ryの計算
  r = math.sqrt(rx * rx + ry * ry) # 距離rの計算
  if r < rmin:
   rmin = r #距離の最小値を更新
  vx += (rx / r / r / r * qi[1]) * H # 速度vxの計算
  vy += (rx / r / r / r * qi[1]) * H # 速度vyの計算
 x += vx * H #位置xの計算
 y += vy * H #位置yの計算
 print("{:.7f} {:.7f} {:.7f} {:.7f} {:.7f}".format(t, x, y, vx, vy))
  # 現在時刻と現在の位置
 if rmin < RLIMIT:
  break # 電荷に非常に近づいたら終了
# end

