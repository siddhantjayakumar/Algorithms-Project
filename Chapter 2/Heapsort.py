'''
Heapsort Implementation
'''

#Start with the heapify function that 'fixes' a max-heap from index of root

def heapify(heap,root,end):
	left = 2*root + 1
	right = left + 1
	
	largest = root

	#Find the largest of the root, left and right, if not 
	#at the end of the array
	if left <= end and heap[left] > heap[root]:
		largest = left
	if right <= end and heap[right] > heap[largest]:
		largest = right
	
	#If not a heap then swap root with max child and call heapify on child
	if largest != root:
		heap[largest], heap[root] = heap[root], heap[largest] #cool Python swap
		heapify(heap,largest,end)  
		              	
def heapsort(arr):
	#First, make the array/list into a heap  
	
	#Loop from len/2 to 0 - heapify with i as root and last element as end
	for i in range(len(arr)/2,-1,-1):  
		heapify(arr,i,len(arr)-1)
	
	#Now, have a heap
	for i in range(len(arr)-1, 0, -1):    
		arr[0], arr[i] = arr[i], arr[0]
		heapify(arr, 0, i-1)
		

