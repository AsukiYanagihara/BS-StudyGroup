# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 21:50:32 2018
cal.プログラム
セルオートマン一次元計算プログラム
ルールと初期状態から、時間発展を計算する。
"""
# モジュールのインポート
import sys # sys.exit()の利用に必要

#定数
N = 65 #セルの最大個数
R = 8 #ルール表の大きさ
MAXT = 50 #繰り返し計算の回数

#下請け関数の定義
# setrule()関数
def setrule(rule,ruleno):
    """ルール表の初期化"""
    # ルール表読み込み
    for i in range(0, R):
        rule[i] = ruleno % 2 # // 演算子は 整数除算 を行い、(小数部を切り捨てた) 整数値を返します; 剰余は、% で求めます。:
        ruleno = ruleno // 2 #左シフト
    #ルール表の出力
    for i in range(R - 1, -1, -1):
        print(rule[i])
# setrule()関数の終わり
        
# initca()関数
def intica(ca):
    """セルオートマンへの初期値の読み込み"""
    # 初期値読み込み
    line = input("caの初期値を入力してください:")
    print()
    #内部表現への変換
    for no in range (len(line)):
        ca[no] = int(line[no])
    # intca()関数の終わり

# putca()関数
def putca(ca):
    """caの状態の出力"""
    for no in range(N - 1, -1, -1):
        print("{:1d}".format(ca[no]), end="")
    print()
# putca()関数の終わり
    
# nextt()関数
def nextt(ca,rule):
    """caの状態の更新"""
    nextca = [0 for i in range(N)] #次世代のca
    # ルールの適用
    for i in range(1, N-1):
        nextca[i] = rule[ca[i + 1] * 4 +ca[i] *2 + ca[i - 1]]
    # caの更新
    for i in range(N):
        ca[i] = nextca[i]
    # nextt()関数の終わり

#　メイン実行部
# ルール表の初期化
rule = [0 for i in range(R)] #ルール表の作成
ruleno = int(input("ルール番号を入力してください:"))
print()
if ruleno < 0 or ruleno > 255:
    print("ルール番号が正しくありませんね(´・ω・｀)")
    sys.exit()
setrule(rule, ruleno) #ルール表のセット
# セルオートマンへの初期値読み込み
ca = [0 for i in range(N)] #セルの並び
intica(ca) # 初期値読み込み
putca(ca) # caの状態出力
#時間の発展の計算
for t in range(MAXT):
    nextt(ca, rule) #次の時刻に更新
    putca(ca) # caの状態の出力
# ＼(^o^)／
