from typing import List;

class Solution:
    def calPoints(self, ops: List[str]) -> int:
        rec = []

        for ltr in ops:
            if ltr == '+' and len(rec) >= 2:
                newScore = rec[-1] + rec[-2]
                rec.append(newScore)
                continue

            if ltr == 'D' and len(rec) >= 1:
                doubleRes = rec[-1] * 2
                rec.append(doubleRes)
                continue

            if ltr == 'C':
                rec.pop()
                continue

            rec.append(int(ltr))
        # sum = 0
        # for x in rec:
        #     sum += x
        # return sum

        return sum(rec)
