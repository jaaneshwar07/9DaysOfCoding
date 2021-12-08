def getPairsCount(arr, n, sum):
 
    count = 0  
 
    
    for i in range(0, n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == sum:
                count += 1
 
    return count
 
 

arr = [2, 5, 2, 5, 5]
n = len(arr)
sum = 7
print("Count of pairs is",
      getPairsCount(arr, n, sum))
 