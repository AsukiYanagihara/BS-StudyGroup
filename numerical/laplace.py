# -*- coding: utf-8 -*-
"""
Laplace.pyプログラム
ラプラス方程式の解法プログラム
反復法によりラプラス方程式を解く
"""
# モジュールのインポート
import math

# 定数
LIMIT = 1000 # 反復回数の上限
N = 101 # x軸方向の分割数
M = 101 # y軸方向の分割数

#下請け関数の定義
# iteration()関数
def iteration(u):
 """1回分の反復計算"""
 u_next = [[0 for i in range(N)] for j in range(M)] #次ステップのuij
 # 次のステップの値を計算
 for i in range(1, N - 1):
  for j in range(1, M - 1):
   u_next[i][j] = (u[i][j-1] + u[i-1][j] + u[i][j+1] + u[i+1][j] ) / 4
  
 # uijの更新
 for i in range(1, N - 1):
  for j in range(1, M - 1):
   u[i][j] = u_next[i][j]
# iteration()関数の終わり＼(^o^)／

# メイン実行部
u =  [[0 for i in range(N)] for j in range(M)] #uijの初期化
for i in range(M) :
 u[0][i] = math.sin(2 * math.pi * i / (M-1))

#反復法の計算
for i in range(LIMIT):
 iteration(u)

print(u) #結果の出力
#＼(^o^)／     