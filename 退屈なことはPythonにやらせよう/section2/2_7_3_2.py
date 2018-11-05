# coding: utf-8

"""
退屈なことはPythonにやらせよう
2.7.3_2　elif文の連結
"""

# パラメータ入力部
print('あなたはだれ?')
name = input()
print('何歳？')
age = input(str())

# フロー図
if name == 'alice':
    print('やあalice')
elif age < 12:
    print('aliceじゃないね、くそがきが')
else:
    print('あなたはAliceでも子供でもないですね')
    