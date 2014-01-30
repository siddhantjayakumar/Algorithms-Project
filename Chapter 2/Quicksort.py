def quicksort(arr,start,end): 
	if start < end:
		pivot = partition(arr,start,end)
		quicksort(arr,start,pivot-1)
		quicksort(arr,pivot,end)
		
def partition(arr,start,end):
	pivot = arr[end]
	i = start-1
	
	for j in range(start,end):
		if arr[j] <= pivot:
			i += 1
			arr[i], arr[j] = arr[j], arr[i] 
			
	arr[i+1], arr[end] = arr[end], arr[i+1]
	return i+1
			
     	