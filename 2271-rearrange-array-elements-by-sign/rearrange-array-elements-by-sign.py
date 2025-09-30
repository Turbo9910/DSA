class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos_num = list()
        neg_num = list()
        r = list()
        for i in nums:
            if i < 0:
                neg_num.append(i)
            else:
                pos_num.append(i)
        flag = True
        i = 0
        j = 0
        k = 0

        while k < len(nums):
            if flag:
                r.append(pos_num[i])
                i+=1
                flag = False
            else:
                r.append(neg_num[j])
                j+=1
                flag = True
            k+=1
        return r


        
        
        