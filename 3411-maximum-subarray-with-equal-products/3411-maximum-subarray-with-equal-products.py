class Solution(object):
    def maxLength(self, nums):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        def lcm(a, b):
            return (a * b) // gcd(a, b)

        n = len(nums)
        ans = 0

        for i in range(n):
            product = 1
            gcd_val = 0
            lcm_val = 1

            for j in range(i, n):
                product *= nums[j]

                gcd_val = gcd(gcd_val, nums[j])
                lcm_val = lcm(lcm_val, nums[j])

                if product == gcd_val * lcm_val:
                    ans = max(ans, j - i + 1)

        return ans