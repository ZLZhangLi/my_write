class Solution2(object):
    def consecutiveNumbersSum(self, N):
        while N & 1 == 0:
            N >>= 1

        ans = 1    
        d = 3
        while d * d <= N:
            e = 0
            while N % d == 0:
                N /= d
                e += 1
            ans *= e + 1
            d += 2

        if N > 1: ans *= 2
        return ans
    def consecutiveNumbersSum2(self, N):
        K = 2 * N
        res = 0
        b = 1
        while b ** 2 < K:
            if not K % b and (K // b - b) % 2:  ## 判断b是否整除2N，并且b和c奇偶性不同
                res += 1
            b += 1
        return res

class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        import copy
        import collections
        prime_factors = collections.defaultdict(int)
        K = 2 * N
        b = 2
        while b ** 2 <= K:
            if not K % b:
                prime_factors[b] += 1
                K //= b
            else:
                b += 1
        prime_factors[K] += 1

        factors = []
        def traceback(component, prime_factors):
            if not prime_factors:
                factors.append(component)
            else:
                dic = copy.deepcopy(prime_factors)
                item = dic.popitem()
                for i in range(item[1] + 1):
                    traceback(component * item[0] ** i, dic)

        traceback(1, prime_factors)

        res = 0
        for factor in factors:
            if factor ** 2 < 2 * N and ((2 * N) // factor - factor) % 2:
                res += 1
        return res

n = int(input())
a = Solution()
print(a.consecutiveNumbersSum(n))