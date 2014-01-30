def counting_sort(arr,k): 
	c = [0]*(k+1)
	b = [0]*(len(arr))
	    
	for i in range(0,len(arr)):
		c[arr[i]] += 1
	
	for i in range(1,k+1):
		c[i] += c[i-1]
		
	for i in range(len(arr)-1,-1,-1):
		b[c[arr[i]]-1] = arr[i]
		c[arr[i]] -= 1   
		         	
	return b
		
