'''
name:Hello.py
auth:Zhangxiaojian
date:20230701
'''
import sys
print(sys.argv,len(sys.argv))
if(len(sys.argv)>=2):
    print(f"hello,world {' '.join(sys.argv[1:])}!!!")
else:
    print("hello,world!!!")
