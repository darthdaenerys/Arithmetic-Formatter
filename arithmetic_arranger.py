def numdigits(x):
    ans=0
    x=abs(x)
    while(x>0):
        ans+=1
        x//=10
    return ans

def arithmetic_arranger(problems,param=False):
    arranged_problems=""
    numbers=[]

    # check for error conditions
    if len(problems)>5:
        return "Error: Too many problems."
    for i,obj in enumerate(problems):
        number=obj.split(' ')
        if number[1] not in '+-':
            return "Error: Operator must be '+' or '-'."
        if len(number[0])>4 or len(number[2])>4:
            return "Error: Numbers cannot be more than four digits."
        try:
            _=int(number[0])
            _=int(number[2])
        except ValueError:
            return "Error: Numbers must only contain digits."
    
    # construct the arranged_problems

    for obj in problems:
        numbers.append(obj.split(' '))

    # the first row
    for i in range(len(numbers)-1):
        dashes=max(len(numbers[i][0]),len(numbers[i][2]))+2
        for j in range(dashes-len(numbers[i][0])):
            arranged_problems+=' '
        arranged_problems+=numbers[i][0]
        arranged_problems+='    '
    dashes=max(len(numbers[-1][0]),len(numbers[-1][2]))+2
    for j in range(dashes-len(numbers[-1][0])):
        arranged_problems+=' '
    arranged_problems+=numbers[-1][0]
    arranged_problems+='\n'

    # the second row
    for i in range(len(numbers)-1):
        dashes=max(len(numbers[i][0]),len(numbers[i][2]))+1
        arranged_problems+=numbers[i][1]
        for j in range(dashes-len(numbers[i][2])):
            arranged_problems+=' '
        arranged_problems+=numbers[i][2]
        arranged_problems+='    '
    dashes=max(len(numbers[-1][0]),len(numbers[-1][2]))+1
    arranged_problems+=numbers[-1][1]
    for j in range(dashes-len(numbers[-1][2])):
        arranged_problems+=' '
    arranged_problems+=numbers[-1][2]
    arranged_problems+='\n'

    # the third row
    for i in range(len(numbers)-1):
        dashes=max(len(numbers[i][0]),len(numbers[i][2]))+2
        for j in range(dashes):
            arranged_problems+='-'
        arranged_problems+='    '
    dashes=max(len(numbers[-1][0]),len(numbers[-1][2]))+2
    for i in range(dashes):
        arranged_problems+='-'

    # if param is True
    ans=[]
    if param:
        arranged_problems+='\n'
        for i in numbers:
            tempnum=0
            if i[1]=='+':
                tempnum=int(i[0])+int(i[2])
            else:
                tempnum=int(i[0])-int(i[2])
            ans.append(tempnum)
        for i in range(len(numbers)-1):
            dashes=max(len(numbers[i][0]),len(numbers[i][2]))+2
            if ans[i]<0:
                dashes-=1
            for j in range(dashes-numdigits(ans[i])):
                arranged_problems+=' '
            arranged_problems+=str(ans[i])
            arranged_problems+='    '
        dashes=max(len(numbers[-1][0]),len(numbers[-1][2]))+2
        if ans[-1]<0:
            dashes-=1
        for i in range(dashes-numdigits(ans[-1])):
            arranged_problems+=' '
        arranged_problems+=str(ans[-1])

    return arranged_problems
