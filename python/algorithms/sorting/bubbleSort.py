class Sort:
      def bubble_sort(self,arr):
            for i in range(len(arr)):
                  for j in range(len(arr) - 1 ): #Last n elements are in place
                        if arr[j] > arr[j + 1]:
                              arr[j],arr[j+1] = arr[j+1],arr[j]
      def better_method(self, arr):
            swapped = True
            i = 0
            while swapped:
                  swapped = False
                  for j in range(len(arr) - i - 1):
                        if arr[j] > arr[j+1]:
                              arr[j] , arr[j + 1] =  arr[j + 1], arr[j]
                              swapped = True
            i+=1            
sort_this = Sort()
arr = [1,3,5,6,2,8,4,1,6,9]
arr2 = [8,6,5,34,2,1,1]
sort_this.bubble_sort(arr)
sort_this.better_method(arr2)
print("Arr1 after sorting",arr)
print("Arr2 After sorting", arr2)


