class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        tmp = 1
        if num <= 1:
            return False
        for i in range(2, int(sqrt(num)) + 1):
            if num % i == 0:
                tmp += i
                if i != num // i:
                    tmp += num // i
        if tmp == num:
            return True
        return False
