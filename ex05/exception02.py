nums = [1,2,3]

try :
    n = nums[5]
    print(n)
except Exception as e:
    print('error:', e)

nums2 = []
for i in range(100):
    try:
        div = i - 50 # 50 - 50
        print(i, div)

        nums += [100/div] # 100/50 예외 발생
    except Exception as e :
        print("예외발생 코드:", e)

print("정상 종료!!!")