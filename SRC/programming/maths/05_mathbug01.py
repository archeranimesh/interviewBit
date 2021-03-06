class Solution:
    # @param A : integer
    # @return an integer
    def isPrime(self, A):
        upperLimit = int(A ** 0.5)
        for i in range(2, upperLimit + 1):
            if i < A and A % i == 0:
                return 0
        return 1


if __name__ == "__main__":
    soln = Solution()
    print(soln.isPrime(2))
