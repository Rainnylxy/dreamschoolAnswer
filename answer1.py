#使用贪心算法
def minSubsequences(source,target):
    source_index=0
    target_index=0
    subsequences_count = 0
    found_subsequence = False
    while target_index < len(target) :
        #每次都找到target中能匹配到的最大长度的子序列
        if source[source_index] == target[target_index]:
            found_subsequence = True
            target_index+=1
        source_index+=1    
        #子序列已经匹配完
        if source_index == len(source):
            #未匹配到子序列直接返回-1
            if not found_subsequence :
                return -1
            #子序列已经匹配到，匹配下一个子序列
            found_subsequence = False
            source_index = 0
            subsequences_count += 1
    return subsequences_count

source = input()
target = input()
print(source+" "+target)
print(minSubsequences(source,target))
print(minSubsequences("abc","abcbc"))
print(minSubsequences("abc","acdbc"))
print(minSubsequences("xyz","xzyxz"))



