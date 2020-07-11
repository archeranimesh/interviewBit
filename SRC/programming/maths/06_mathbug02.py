class Solution:
    # @param A : integer
    # @return a list of list of integers
    def squareSum(self, A):
        ans = []
        a = 0
        while a * a < A:
            b = a  # Started the loop with a
            print("a=", a)
            while b * b < A:
                print("\tb=", b)
                if a * a + b * b == A:
                    newEntry = [a, b]
                    print("\t\t", newEntry)
                    ans.append(newEntry)
                b += 1
            a += 1
        return ans


if __name__ == "__main__":
    soln = Solution()
    print(soln.squareSum(5))
