price = [100,180,260,310,40,535,695]
n = len(price)
def  buyandsell(price,n):
    i =0
    if(i==n-1):
        return
    while((i<=n-1)):
        while((i<=n-1)and(price[i]<price[i-1])):
            buy=i+1
            i+=1
        while((i<n)and(price[i]>=price[i-1])):
            i+=1
            sell=i
        print("buy on ",buy,"\t","serll on",sell)

buyandsell(price,n)

