# 1. Bài toán Two Sum

"""
Cho một mảng các số nguyên và một mục tiêu số nguyên, trả về các chỉ số của hai số sao cho chúng cộng lại thành mục tiêu.

Bạn có thể giả định rằng mỗi đầu vào sẽ có chính xác một giải pháp và bạn không thể sử dụng cùng một phần tử hai lần.

Bạn có thể gửi lại câu trả lời theo bất kỳ thứ tự nào.

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        self.nums = []
        self.target = int
                                    # vidu: nums = [2,3,4,5,8,2,1]
        for i in range(len(nums)): # len(nums): 0,1,2,3,4,5,6
            for j in range(i + 1, len(nums)): # j: 1,2,3,4,5,6,2,3,4,5,6,3,4,5,6,6
                if nums[i] + nums[j] == target:
                    return i, j
if __name__ == "__main__":
    a = Solution()
    print(a.twoSum([2,7,11,15], 9))


# 20. Bài toán Valid Parentheses
"""
Cho một chuỗi s chỉ chứa các ký tự '(', ')', '{', '}', '[' và ']', hãy xác định xem chuỗi đầu vào có hợp lệ hay không.

Chuỗi đầu vào hợp lệ nếu:

Các dấu ngoặc mở phải được đóng bằng cùng một loại dấu ngoặc.
Dấu ngoặc mở phải được đóng theo đúng thứ tự.
Mọi dấu ngoặc đóng đều có một dấu ngoặc mở tương ứng cùng loại.

Input: s = "()[]{}"
Output: true
"""

class Solution:
    def isValid(self, sequence):
        """
        Function to check if sequence contains valid parenthesis
        :param sequence: Dãy dấu ngoặc
        :return:True is sequence is valid else False
        """
        # Thay thế các cặp thích hợp cho đến khi dãy trống hoặc không có cặp nào
        while True:
            if '()' in sequence:
                sequence = sequence.replace('()', '')
            elif '{}' in sequence:
                sequence = sequence.replace('{}', '')
            elif '[]' in sequence:
                sequence = sequence.replace('[]','')
            else:
                return not sequence
if __name__ == '__main__':
    sequence = '{[()]}'
    print(f'Is {sequence} valid ? : {Solution().isValid(sequence)}')
    sequence1 = '{[()]}{]{}}'
    print(f'Is {sequence1} valid ? : {Solution().isValid(sequence1)}')