def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n):
        check_swap = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                check_swap = True
                
        if check_swap == False:
            break
    
    
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]

    bubble_sort(arr)

    print("Sorted array:")
    for i in range(len(arr)):
        print("%d" % arr[i], end=" ")