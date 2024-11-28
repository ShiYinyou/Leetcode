class Template:
    def binary_search(arr):
        """
        二分查找主要用于在有序数组中查找特定元素
        基本思想是不断将待查找的区间分为两半
        二分查找有三种写法（闭区间、半闭半开区间、开区间）和四种类型（>=、>、<、<=）
        关键词：有序数组、答案具有单调性

        二分查找的时间复杂度为O(lgn)
        """
        ### 所有模板均直接对应 >= 问题
        ## 下面是三种写法（闭区间、半闭半开区间、开区间）的模板
        ## 对于任意一种写法，注意区间都是还没有确定结论的范围
        ## if成立时更新的是哪个边界，最终的返回的就是哪个值

        # 闭区间
        def lower_bound1(nums, target):
            left, right = 0, len(nums) - 1 # 闭区间[left, right]
            while left <= right: # 区间不为空
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1 # 未确定区间为[mid+1, right]
                else:
                    right = mid - 1 # 未确定区间为[left, mid-1]
            return left
        
        # 左闭右开区间
        def lower_bound2(nums, target):
            left, right = 0, len(nums) # 左闭右开区间[left, right)
            while left < right: # 区间不为空
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1 # 未确定区间为[mid+1, right)
                else:
                    right = mid # 未确定区间为[left, mid)
            return left # right也可以
        
        # 开区间
        def lower_bound3(nums, target):
            left, right = -1, len(nums) # 开区间(left, right)
            while left + 1 < right: # 区间不为空
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid # 未确定区间为(mid, right)
                else:
                    right = mid # 未确定区间为(left, mid)
            return right
        

        ### 解决四种类型问题（>=、>、<、<=）
        # >=x : 直接调用lower_bound(nums,x)
        # >x  : 转化为>=(x+1)，调用lower_bound(nums,x+1)
        # <x  : 转化为>=(x)-1，调用lower_bound(nums,x)-1
        # <=x : 转化为>=(x+1)-1，调用lower_bound(nums,x+1)-1

        ### python bisect第三方库
        # bisect.bisect 和 bisect.bisect_right 返回大于x的第一个下标
        # bisect.bisect_left 返回大于等于x的第一个下标，即lower_bound