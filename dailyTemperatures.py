# https://leetcode.com/problems/daily-temperatures/submissions/

class mySolution():
    def dailyTemperatures(self, temperatures: list) -> list:
        arr = []
        t = temperatures
        for i in range(len(t) - 1):
            for j in range(i + 1, len(t)):
                if t[j] > t[i]:
                    arr.append(j - i)
                    break
            if t[j] <= t[i]:
                arr.append(0)
        arr.append(0)
        return arr


myTemperatures = mySolution()


class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        result = [0] * len(temperatures)
        stk = []

        for i in range(len(temperatures)):
            while stk and temperatures[stk[-1]] < temperatures[i]:  # in the first iteration stk is False
                print(temperatures[stk[-1]], stk[-1], temperatures[i])
                idx = stk.pop()
                result[idx] = i - idx
            stk.append(i)
            # print(stk)
        return result

        arr_ans = []
        t = temperatures
        next_t = t[1]
        arr_t = []
        if t[0] < t[1]:
            arr_ans.append(1)
        for i, value in enumerate(t):
            if next_t < value:
                idx = t.index(value)
                arr_ans.append(idx - i)
            else:
                next_t = value
        arr_ans.append(0)
        return arr_ans


temperatures = Solution()

if __name__ == "__main__":
    temps1 = [73, 74, 75, 71, 69, 72, 74, 74]  # expected: [1,1,0,2,1,1,0,0]
    temps2 = [75, 74, 75, 71, 69, 72, 73, 74]  # expected: [0,1,0,2,1,1,1,0]
    temps3 = [74, 74, 75, 71, 69, 72, 74, 73]  # expected: [2,1,0,2,1,1,0,0]

    print(temperatures.dailyTemperatures(temps1))
    print(temperatures.dailyTemperatures(temps2))
    print(temperatures.dailyTemperatures(temps3))