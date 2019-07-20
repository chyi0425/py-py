class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        max_len = 0
        sub_s = set()
        while right<len(s):
            if s[right] in sub_s:
                sub_s.remove(s[left])
                left +=1
            else:
                sub_s.add(s[right])
                right+=1
                max_len = max(max_len,right-left)
        return max_len

if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLongestSubstring('pwwkew'))