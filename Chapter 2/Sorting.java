public class Sorting {

	public static void insertionSort(int[] arr) {
		for(int i = 1; i < arr.length; i++) {
			//ASSERT: Currently, the first i-1 are already sorted               
			//insert currentElement into the sorted sequence 0...i-1            
			int currentElement = arr[i];
			int j = i-1;
			//Find the correct place for the currentElement                     
			while (j >= 0 && arr[j] > currentElement) {
				arr[j+1] = arr[j];
				j--;
			}
			arr[j+1] = currentElement;
		}
	}

	public static void selectionSort(int[] arr) {
		for(int i = 0; i < arr.length; i++) {
			//ASSERT: The array positions 0...i-1 are already sorted            
			int iMin = i;
			//Find the smallest element in i-END                                
			for(int j = i+1; j < arr.length; j++) {
				if(arr[j]<arr[iMin]) iMin = j;
			}
			int temp = arr[iMin];
			arr[iMin]=arr[i];
			arr[i]=temp;
		}
	}


	public static void binaryInsertionSort(int[] a) {
		for(int i = 1; i < a.length; i++) {
			int currentElement = a[i];
			//Binary Search                                                     
			int start = 0, end = i, middle = (start + end)/2;
			while(start < end) {
				if(currentElement > a[middle])
					start = middle + 1;
				else if(currentElement < a[middle])
					end = middle;
				else break;

				middle = (start+end)/2;
			}

			if(middle != i) {
				for(int j = i-1; j >= middle; j--)
					a[j+1] = a[j];

				a[middle] = currentElement;
			}
		}
	}

    public static void bubbleSort(int[] a) {
        boolean swapped = true;
        while(swapped) {
            swapped = false;
            for(int i = 0; i < a.length-1; i++) {
                if(a[i] > a[i+1]) {
                    int temp = a[i];
                    a[i] = a[i+1];
                    a[i+1] = temp;
                    swapped = true;
                }
            }
            
        }
    }
    
    public static void mergeSort(int[] A, int p, int r) {
        if (p < r) {
            int q = (p + r) / 2;
            mergeSort(A, p, q);
            mergeSort(A, q + 1, r);
            merge(A, p, q, r);
        }
    }
    
    public static void merge(int[] A, int p, int q, int r) {
        int n1 = q - p + 1;
        int n2 = r - q;
        int[] L = new int[n1 + 1];
        int[] R = new int[n2 + 1];
        L[n1] = Integer.MAX_VALUE;
        R[n2] = Integer.MAX_VALUE;
        for (int i = 0; i < n1; i++) {
            L[i] = A[p + i];
        }
        for (int j = 0; j < n2; j++) {
            R[j] = A[q + j + 1];
        }
        int x = 0, y = 0;
        for (int k = p; k < r; k++) {
            if (L[x] <= R[y]) {
                A[k] = L[x];
                x++;
            } else {
                A[k] = R[y];
                y++;
            }
        }
    }


	public static void main(String args[]) {
		int a[] = {10,98,-4,-12,1234,445,4,3,1234,1,566,4,9};
		mergeSort(a, 0, a.length-1);

		for(int i = 0; i < a.length; i++)
			System.out.print(a[i]+ " ");

		System.out.println();
	}
}
