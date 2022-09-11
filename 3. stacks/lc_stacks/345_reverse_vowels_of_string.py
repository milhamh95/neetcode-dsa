# https://leetcode.com/problems/reverse-vowels-of-a-string/

class Solution:
    def reverseVowels(self, s: str) -> str:
        # convert string to array string
        arrayS = list(s)

        l, r = 0, len(arrayS) - 1
        vowel = 'aiueoAIUEO'

        while l < r:
            isLeftVowel = s[l] in vowel
            isRightVowel = s[r] in vowel

            if isLeftVowel and isRightVowel:
                arrayS[l], arrayS[r] = arrayS[r], arrayS[l]
                l += 1
                r -= 1
                continue

            if not isLeftVowel:
                l += 1

            if not isRightVowel:
                r -= 1

        # join list string to string
        return "".join(arrayS)

#         stackVowel = ""
#         newS = ""

#         for ltr in s:
#             if ltr in 'aiueoAIUEO':
#                 stackVowel = stackVowel + ltr

#         for ltr in s:
#             if ltr in 'aiueoAIUEO':
#                 newS = newS + stackVowel[-1]
#                 stackVowel = stackVowel[:-1]
#                 continue

#             newS = newS + ltr

#         return newS

        # stackVowel = []
        # newS = ""

        # for ltr in s:
        #     if ltr in 'aiueoAIUEO':
        #         stackVowel.append(ltr)

        # for ltr in s:
        #     if ltr in 'aiueoAIUEO':
        #         newS = newS + stackVowel.pop()
        #         continue

        #     newS = newS + ltr

        # return newS
