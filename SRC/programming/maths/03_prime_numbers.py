import math


class Solution(object):
    def is_prime_sqrt(self, A):
        if A <= 1:
            return False
        for i in range(2, int(math.sqrt(A)) + 1):
            if A % i == 0:
                return False
        return True

    def find_prime(self, A):
        result = []
        for i in range(2, A):
            if self.is_prime_sqrt(i):
                result.append(i)
        return result

    def sieve_prime(self, A):
        result = [True] * A
        return_result = []
        p = 2
        while p * p <= A:
            if result[p]:
                for i in range(p * 2, A, p):
                    result[i] = False
            p += 1
        result[0] = False
        result[1] = False
        for p in range(A):
            if result[p]:
                return_result.append(p)
        return return_result

    def prime_eratosthenes(self, n):
        prime_list = []
        return_list = []
        for i in range(2, n + 1):
            if i not in prime_list:
                return_list.append(i)
                for j in range(i * i, n + 1, i):
                    prime_list.append(j)
        return return_list


if __name__ == "__main__":
    soln = Solution()
    print(soln.find_prime(12))
    print(soln.sieve_prime(12))
    print(soln.prime_eratosthenes(12))
