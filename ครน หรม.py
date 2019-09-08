askOp = 'What operation do you want?(+,-,*,/,**,etc)'
askNums = 'How many numbers do you want to use with operation?'
def checkStringNum(string):
    strList = list(string)
    ans = string.isdigit()
    
        
    
    return ans
            
def checkAskNums():
    Nums = input(askNums)
    if checkStringNum(Nums) == False:
            PrintNonValue()  
            while checkStringNum(Nums) == False:
                PrintNonValue()
                Nums = input(askNums)
    Nums = int(Nums)
    return Nums
    
def askHowNums(Nums):
    numList = []
    for i in range(Nums):
        x = False
        x = input('What is the #' + str(i + 1) + ' number') 
        if checkStringNum(x) == False:
            print("You typed a non-number value. This is unacceptable")
            while checkStringNum(x) == False:
                print("You typed a non-number value. This is unacceptable")
                x = input('What is the #' + str(i + 1) + ' number')
        x = int(x)
        numList.append(x)
    return numList

def PrintNonValue():
    print("You typed a non-number value. This is unacceptable")


    
def ansModu(Numlist):
    ans = 0
    x = 0
    high = 0
    for i in Numlist:
        x +=1
        num = i
        if x == 1:
            high = num
        else:
            if num > high:
                num = high
    x = 0
    y = 0
    f = True
    while True:
        x -= 1
        if x == -1:
            y = high
        else:
            y = abs(high)-1
        f = True
        for i in Numlist:
            if i % high > 0:
                f = False
                break
        if f:
            break
    ans = y
    return ans

while True:
    Op = input(askOp)
    if Op == 'หรม':      
        ans = ansPlus(askHowNums(checkAskNums()))
        print('Your answer is ' + str(ans))
    elif Op == 'ครน':
        ans = ansModu(askHowNums(checkAskNums()))
        print('Your answer is ' + str(ans))
    else:
        print('Do not understand input.Please try again')

