# _*_ coding: utf-8 _*_
"""
bidec.pyプログラム
2分法による方程式の解法プログラム
使い方　
"""
# グローバル変数
a = 2	# f(x)=X*X-a
LIMIT = 1e-20	#終了条件

#　下請け関数の定義
#　f()関数
def f(x):
	"""関数値の計算"""
	return x * x - a
#　f()関数の終わり

# メイン実行部
# 初期設定
xp = float(input("xpを入力してください:"))
xn = float(input("xnを入力してください:"))

# 繰り返し処理
while (xp - xn) * (xp - xn) > LIMIT: #終了条件を満たすまで繰り返す
	xmid = (xp + xn) / 2# 新たな中間地値の計算 
	if f(xmid) > 0: #中間地値が正ならば
	 xp = xmid #xpを更新
	else: #中間値が正でないならば
	 xn = xmid #xnを更新
	print("{:.15f} {:.15f}".format (xn, xp))
# bidec.pyの終わり