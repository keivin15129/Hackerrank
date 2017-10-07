def merge_the_tools(string, k):
    # your code goes here
    list=[]
    length=len(string)
    for i in range(length/k):
        list.append(string[k*i:k*(i+1)]
    for r in range(length/k):
        for l in range (k-1,0,-1):
            if list[r][l] in list[r][:l] :
                list[r]= list[r][:l]+list[r][l+1:]
    for d in range (len(list)):
        print list[d]
                
