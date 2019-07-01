class QuickSort:
    @staticmethod
    def partition(arr, low, high): 
        i = ( low-1 )         # index of smaller element 
        pivot = arr[high]     # pivot 

        for j in range(low , high):
            if arr[j] <= pivot:
                i += 1
                arr[i],arr[j] = arr[j],arr[i]

        arr[i+1],arr[high] = arr[high],arr[i+1] 
        return ( i+1 )

    @staticmethod
    def quickSort(arr, low, high):
        if low < high:
            pivot = QuickSort.partition(arr,low,high)
            QuickSort.quickSort(arr, low, pivot-1)
            QuickSort.quickSort(arr, pivot+1, high)

class MergeSort:
    # Merges two subarrays of arr[]. 
    # First subarray is arr[l..m] 
    # Second subarray is arr[m+1..r] 
    @staticmethod
    def merge(a1, a2): 
        swaps, i, j, result, m, n = 0, 0, 0, [], len(a1), len(a2)
        ra = result.append
        while i < m and j < n:
            if a1[i] <= a2[j]:
                ra(a1[i])
                i += 1
            else:
                ra(a2[j])
                j += 1
                swaps += m - i
        result += a1[i:]
        result += a2[j:]    
        return swaps, result

    # l is for left index and r is right index of the 
    # sub-array of arr to be sorted
    @staticmethod
    def mergeSort(arr): 
        n = len(arr)
        mid = n // 2
        if n > 1:
            left_swaps, left_result = MergeSort.mergeSort(arr[:mid])
            right_swaps, right_result = MergeSort.mergeSort(arr[mid:])
            m_swaps, result = MergeSort.merge(left_result, right_result)
            return m_swaps + left_swaps + right_swaps, result
        return 0, arr
