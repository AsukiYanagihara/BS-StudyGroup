# _*_ coding: utf-8 _*_
"""
solve.pyプログラム
sympyモジュールを利用して方程式を解く
少し複雑な方程式の例
"""
# モジュールのインポート
from sympy import *

# メイン実行部
var("x") # 変数xの設定
equation = Eq(x**3 + 2 * x**2 - 5 * x - 6, 0) #方程式の設定
answer = solve(equation) #方程式を解く
print(answer) #結果出力
# solve.pyの終わり