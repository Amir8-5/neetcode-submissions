class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index1 = 0;
        index2 = 1
        for i in range(len(numbers)):
            for j in range(i+1, len(numbers)):
                sum = numbers[i] + numbers[j]
                if i != j and sum > target:
                    break
                elif i != j and sum == target:
                    return [i+1,j+1]
        