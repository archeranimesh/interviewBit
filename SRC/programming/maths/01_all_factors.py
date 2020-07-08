# https://www.interviewbit.com/problems/all-factors/
import math


class Solution:
    # @param A : integer
    # @return a list of integers
    def allFactors(self, a):
        result = []
        for i in range(1, a + 1):
            # print(i)
            if a % i == 0:
                result.append(i)
        return result

    def all_factors(self, a):
        result = [1]
        for i in range(2, a // 2 + 1):
            print(i)
            if a % i == 0:
                result.append(i)
        if a != 1:
            result.append(a)
        return result

    def all_factor_sqrt(self, A):
        result = [1]
        for i in range(1, int(math.sqrt(A)) + 1):
            if A % i == 0:
                if i not in result:
                    result.append(i)
                if i != math.sqrt(A):
                    result.append(A // i)
        return sorted(result)


if __name__ == "__main__":
    soln = Solution()
    A = 82944
    # factors = soln.allFactors(A)
    # print(factors)
    # factors = soln.all_factors(A)
    # print(factors)
    factors = soln.all_factor_sqrt(A)
    print(factors)
