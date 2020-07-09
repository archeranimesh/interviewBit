class Solution:
    # @param A : integer
    # @return a strings
    def findDigitsInBinary(self, A):
        return bin(A)[2:]

    def findDigitInBinary_div(self, A, divisor):
        return_list = []
        while A > 0:
            remainder = A % divisor
            return_list.append(remainder)
            A = A // divisor
        return_list.reverse()
        return "".join([str(elem) for elem in return_list])


if __name__ == "__main__":
    soln = Solution()
    print(soln.findDigitsInBinary(12))
    print(soln.findDigitInBinary_div(15, 2))
