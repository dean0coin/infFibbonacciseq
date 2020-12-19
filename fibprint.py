stopAt = int(input("To what number in the Fibonacci Sequence do want to stop at?: "))


fSeq = [1, 1]
numNum1 = 0
numNum2 = 1

print("1")
print("1")
for i in range(stopAt - 2): # -2 To make up for the first 2 numbers printed by default ^^^ (1, 1)
    nNum = fSeq[numNum1] + fSeq[numNum2]
    fSeq.append(nNum)
    numNum1 += 1
    numNum2 += 1
    print(nNum)