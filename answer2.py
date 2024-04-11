def handleBrackets(str):
    #left记录左括号出现的下标
    left = []
    res_str = [' ']*len(str)
    index = 0
    while index < len(str):
        ch = str[index]
        if ch == '(':
            #左括号直接加入left中
            left.append(index)
        elif ch == ')':
            #如果是右括号的话，
            #如果所有左括号已经匹配则该右括号一定不匹配，设置为？
            #如果还有左括号没匹配，则pop出该左括号
            if len(left) == 0 :
                res_str[index]='?'
            else:
                left.pop()
        index += 1
    #最后未匹配的左括号设置为x
    for left_index in left:
        res_str[left_index]='x'
   
    return ''.join(res_str)

#strs存储原字符串数组
strs = []
#res_strs存储结果字符串数组
res_strs = []
while True:
    str = input()
    if not str:
        break
    res_strs.append(handleBrackets(str))
    strs.append(str)
#打印结果
index=0
while index<len(strs):
    print(strs[index])
    print(res_strs[index])
    index+=1