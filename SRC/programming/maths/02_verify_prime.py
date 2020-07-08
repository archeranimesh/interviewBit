import math


class Solution(object):
    def is_prime(self, A):
        if A <= 1:
            return False
        for i in range(2, (A // 2) + 1):
            if A % i == 0:
                return False
        return True

    def is_prime_sqrt(self, A):
        if A <= 1:
            return False
        for i in range(2, int(math.sqrt(A)) + 1):
            if A % i == 0:
                return False
        return True


if __name__ == "__main__":
    soln = Solution()
    print(soln.is_prime(12))
    print(soln.is_prime_sqrt(12))
