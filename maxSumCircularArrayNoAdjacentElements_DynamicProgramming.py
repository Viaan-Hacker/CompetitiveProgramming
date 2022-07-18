"""
Dynamic Programming Solution to the Maxium Sum of a Circular Array problem such that no adjacent elements contribute to the sum.

Note that for all i, if array[i] contributes to the sum, then array[i + 1] and array[i - 1] may not contribute to the sum.
Further, we have that the array is circular, i.e array[0] and array[N - 1] are adjacent. 


"""

def maxSumCircularArrayNoAdjacentElements(array, N):   #O(n) solution.  
    dp = [[0 for i in range(2)] for j in range(N)]
    if N == 1:
        return array[0]
    
    dp[0][0] = 0
    dp[0][1] = array[0]

    for i in range(1, N):
         dp[i][1] = dp[i - 1][0] + array[i]
         dp[i][0] = max(dp[i -1][0], dp[i - 1][1])

    if N % 2 == 1:
        return max(dp[N - 1][0], dp[N - 1][1]) - min(array[N - 1], jewels[0])
    else:
        return max(dp[N - 1][0], dp[N - 1][1])


def main():
    test_array = [1, 2, 3, 4] #Clearly the max sum in this case is 6 because of 4 + 2
    print(maxSumCircularArrayNoAdjacentElements(test_array, len(test_array)))




main()
