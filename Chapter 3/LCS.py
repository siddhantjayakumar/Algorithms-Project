'''
Longest Common Subsequence
Dynamic Programming
30/01/2013
Siddhant M. Jayakumar 
'''
#This is top-down recursive; but memoized

#Meat of the program
def lcs(i, j, memo):
    
    #Base case - if empty; subseqeuence is empty; add that to the memo array and return ""
    if i == "" or j == "":
        memo[len(i)][len(j)] = "" 
		return ""
	#If last char is same; find substring upto last and add the last	
    elif i[-1] == j[-1]:                                            
		#First check the array to see if you've already calculated it, else do so
        val = memo[len(i)-1][len(j)-1] 
        if val == 0:
            val = lcs(i[:-1], j[:-1], memo)
            memo[len(i)-1][len(j)-1] = val 

        val = val + i[-1]    
		#Add your result to the array and return
        memo[len(i)][len(j)] = val 
        return val 
    else:  
		#last char is not the same, so find the LCS of i and j upto last, and find LCS of j and i upto last
       val_1 = memo[len(i)][len(j)-1]
       val_2 = memo[len(i)-1][len(j)]    
	   #Find the longer of these two are store it as the LCS of i and j 
       if val_1 == 0:
           val_1 = lcs(i, j[:-1], memo)
           memo[len(i)][len(j)-1] = val_1
       if val_2 == 0:
           val_2 = lcs(i[:-1], j, memo)
           memo[len(i)-1][len(j)] = val_2
           
       if len(val_1) > len(val_2):
           val = val_1
       else:
           val = val_2             
	   #Store value and return
       memo[len(i)][len(j)] = val
       return val
        

#Main - take two words, set up an empty 2D array - length i+1 into length j+1 - extra space for the empty string    
i = str(raw_input("Word 1: "))
j = str(raw_input("Word 2: "))
memo = [[0 for _ in xrange(len(j)+1)] for _ in xrange(len(i)+1)]  
#Call LCS
lcs(i,j,memo)
#Return the last entry, i.e. LCS of i and j  
print memo[-1][-1]