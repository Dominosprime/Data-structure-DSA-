array = [ 1, 1, 2, 34, 4]                  
def findMax(arr):                           
  max = arr[0]
  for i in arr:
    if i > max:
      max = i
  return max

print(findMax(array))

 
"""Time complexity: 0(n)
  Reason: The time complexity for the for loop is O(n) and that for the if statement and the assignment of i to max is constant time 
          Hence the total time complexity is the addition of O(n) + O(1) + O(1) = O(n)
  """



def countTarget(arr, target):
  count = 0
  for i in arr:
    if i == target:
      count += 1
  return count 

print(countTarget(array, 1))

"""Time complexity: 0(n)
  Reason: The time complexity for assigning 0 to count is O(1) and that of the for loop is O(n) and that for the if statement and the increment of count is constant time 
          Hence the total time complexity is the addition of O(1) + O(n) + O(1) + O(1) = O(n)
  """


def is_sorted(arr):
  for i in range(len(arr)-1):
    if arr[i] > arr[i + 1]:
      return False
  return True


"""Time complexity: 0(n)
  Reason: The time complexity for the for loop is O(n) in the worst case since it iterates through the loop n-1 times. that for the if statement is constant time. Return statements are both constant time operations
          Hence the total time complexity is the addition of  O(n) + O(1) + O(1) = O(n)
  """