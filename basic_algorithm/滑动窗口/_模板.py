class Template:
    def sliding_window(arr):
        """
        滑动窗口常用于解决一些涉及子串或自数组的问题
        通过维护一个可变大小的窗口来遍历字符串或数组执行特定操作
        根据题目要求，可分为：定长滑动窗口、不定长滑动窗口
        关键词：字符串、数组、正数

        滑动窗口的时间复杂度为O(n)
        """
        left = s = 0
        for right,x in enumerate(arr):
            s += x
            while case: # 判断需要收缩左窗口
                s -= arr[left]
                left += 1
        return