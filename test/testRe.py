#-*- coding=utf-8 -*-
#@time: 2021/11/21 16:32
#@author: 陈立
#@file: testRe.py
#@Software: PyCharm

#正则表达式：字符串模式（判断字符串是否符合一定的标准

import re
#创建模式对象

# pat = re.compile("AA")   #此处的AA，是正则表达式，用来去验证其他的字符串
# m = pat.search("AACBAACBAAA")  #search字符串被检验的内容,进行比对查找


#没有模式对象
# m = re.search("asd","Aasd")   #前面的模板是规则（模板），后面的字符串是被校验的对象
# print(m)


# m = re.findall("[A-Z]+","ASDaDFGa")    #前面的模板是规则（正则表达式），后面的字符串是被校验的对象
# print(m)


#sub

# print(re.sub("a","A","abcdefg"))    #找到a,用A替换，在第三个字符串中查找

#建议在正则表达式中，被比较的字符串前面加上r 不用担心转义字符的问题
a = "\nabd\'"
print(a)