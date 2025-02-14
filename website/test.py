t=int(input("Number of words: "))
words=[]
def length(x):
            c=0
            for i in x:
                c=c+1
            return c


for i in range(t):
            a=input()
            words.append(a)
            
for i in words:
            if length(i)<=10:
                print(i)
            else:
                for q in i:
                    print(q,end='')
                    break
                print((length(i)-2), end='')
                print(i[length(i)-1])
            
n=int(input())
def factorial(x):
    if x==0:
        return 1
    if x==1:
        return 1
    else:
        return (factorial(x-1)*x)
    
delicious_score_list=[]
for i in range(n):
    score=int(input())
    delicious_score_list.append(score)

delicious_score_list.sort()
x=len(delicious_score_list)
chaotic_pair=((0.5)*factorial(x))/(factorial(x-2))
print(chaotic_pair/x)
              

N=int(input())
scores=input()
scoreList=scores.split()
DifferentScoreList=set(scoreList)
x=len(DifferentScoreList)
print(x)
              