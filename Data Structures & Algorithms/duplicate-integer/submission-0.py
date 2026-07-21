class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        self.lis=[];
        for i in range (len(nums)):
            if nums[i] not in self.lis:
                self.lis.append(nums[i]);
        return len(self.lis) != len(nums);


            
        