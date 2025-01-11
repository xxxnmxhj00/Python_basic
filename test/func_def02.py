def slicing(s, start = 0, end = -1): # 5번째가 -1 번째
    return s[start : end] # s[0 : -1] => s[0:5]

s = "python"
print ( slicing(s) ) 
print ( slicing(s, 2,3)) 
print ( slicing(s,start=3, end = 5)) 