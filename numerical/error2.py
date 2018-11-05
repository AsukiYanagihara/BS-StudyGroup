# _*_ coding: utf-8 _*_
"""
error2.pyプログラム
誤差計算の例題プログラム
丸め誤差の例題
"""
# メイン実行部
# 10進の0.1の値
print (0.1)

# 10進を1000000回加える
x = 0.0
for i in range (1000000):
 x = x + 0.1 # 0.1は2進数で循環小数

# 結果出力
print (x)
# end of error2.py