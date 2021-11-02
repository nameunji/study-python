"""
leetcode 15. 3Sum
문제 링크 https://leetcode.com/problems/3sum/

주어진 리스트에서 3개의 숫자를 더했을 때 0이 되는 숫자들의 리스트를 리턴하라.
"""

"""
방법 1.
combination 활용해서 3개인자씩 묶어준 후 계산.  
Time Limit Exceeded
"""
from typing import List
from itertools import combinations

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        check_list = set()
        for el in combinations(nums, 3):
            if el not in check_list and sum(el) == 0:
                result.append([el[0], el[1], el[2]])
                check_list.add(el)
        return result

"""
방법 2.
먼저 nums를 for문을 돌렸을 때 nums[i+1:] 리스트에 대하여 양 끝(왼쪽(start)과 오른쪽(end))에서 좁혀오는 걸로 체크하는 방법이다.  
Runtime: 736 ms  
Memory Usage: 17.5 MB

아래 코드에 print문이 하나 들어가 있었는데 Output Limit Exceeded이 떴었다. 지우니까 통과됨.
혹시 코드가 잘 이해되지 않는다면 이 동영상 참고 : https://www.youtube.com/watch?v=GABOlWxXpfU
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)):
            fix = nums[i]
            if fix > 0:  # 만약 가장 작은 값이 0보다 크다면 뒤에는 훑어볼 필요도 없기 때문에
                break
            if i > 0 and fix == nums[i-1]:  # 현재의 값과 이전의 값이 같다면 같은 결과가 나올테니 굳이 아래 while문을 돌 필요 없으므로
                continue

            start = i + 1
            end = len(nums) - 1

            while start < end:
                if fix + nums[start] + nums[end] < 0:  # 0보다 작다는 것은 start의 위치가 더 커져야하므로 start+1
                    start += 1
                elif fix + nums[start] + nums[end] > 0:  # 0보다 크다는 것은 end의 위치가 더 작아져야하므로 end-1
                    end -= 1
                else:
                    while start < end and nums[start] == nums[start+1]:  # 만약 같은 숫자가 연속적으로 있을 경우(start)
                        start += 1
                    while start < end and nums[end] == nums[end-1]:  # 만약 같은 숫자가 연속적으로 있을 경우(end)
                        end -= 1
                    result.append([fix, nums[start], nums[end]])
                    start += 1

        return result