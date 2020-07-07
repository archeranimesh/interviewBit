class Solution(object):
    def is_prime(self, A):
        if A <= 1:
            return False
        for i in range(2, A):
            if A % i == 0:
                return False
        return True


if __name__ == "__main__":
    soln = Solution()
    print(soln.is_prime(2))
