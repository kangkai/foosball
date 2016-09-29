# foosball
some foosball scripts etc.

# Background
北京这边一些朋友，小米俱乐部都是采用rankade记录日常的交流比赛成绩。
https://rankade.com/bjfoosball/
https://rankade.com/mifoosball/

大家经常使用kickertool记录每次比赛。这里的脚本用于把kickertool的结果json文件导入到rankade。

kickertool在这里：
https://kickertool.com/

# Usage
'''
$ .miimport.py 
Usage: miimport.py xxx.ktool username passwd <skip>
         xxx.ktool: file exported from kickertool
         username/passwd: your rankade user/pass
'''
