'''
测试 lstrip、rstrip、strip函数
'''

testStr='     left5space   mid3space   right8space        '
print(f"source str[{testStr}]")
print(f"lstrip:[{testStr.lstrip()}]")
print(f"rstrip:[{testStr.rstrip()}]")
print(f"strip:[{testStr.strip()}]")

print(testStr.strip().capitalize())