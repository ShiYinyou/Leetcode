class Template:
    def opposite_two_pointers(arr):
        """
        相向双指针是指在一个有序数组中，使用两个指针从两端向中间移动，通过调整指针的位置来解决问题。
        相向双指针一般用于处理需要同时考虑数组两端元素的问题，如回文检测、两数之和。
        关键词：有序、求和与目标
        """
        left, right = 0, len(arr)-1
        while left < right:
            if case1:
                left += 1
            elif case2:
                right -= 1
            else:
                return ans