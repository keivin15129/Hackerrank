# Enter your code here. Read input from STDIN. Print output to STDOUT
a=raw_input()
b=a.split()
n=int(b[0])
k=int(b[1])
list0=[]
for i in range (k):
        list0.append(raw_input().split())
        
list1=zip(*list0)
for m in range (n):
    sum=0
    for d in list1[m]:
            sum=sum+float(d)
        
    print sum/k


    
