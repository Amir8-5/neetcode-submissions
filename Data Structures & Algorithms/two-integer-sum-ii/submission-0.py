class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index1 = 0;
        index2 = 1
        for i in range(len(numbers)):
            for j in range(i+1, len(numbers)):
                if i != j and numbers[i] + numbers[j] == target:
                    return [i+1,j+1]
        