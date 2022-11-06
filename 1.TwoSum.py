"""Đề bài:
Cho một mảng các số nguyên và một mục tiêu số nguyên, trả về các chỉ số của hai số sao cho chúng cộng lại thành mục tiêu.

Bạn có thể giả định rằng mỗi đầu vào sẽ có chính xác một giải pháp và bạn không thể sử dụng cùng một phần tử hai lần.

Bạn có thể gửi lại câu trả lời theo bất kỳ thứ tự nào.
"""

"""
Class cùng với object là những thành phần lõi của Python.
Class cung cấp một cách tổ chức các attributes(data) và methods (behaviors).
Một khái niệm vô cùng quan trọng của OOP(Object Oriented Programming)
là class inheritance (dịch đại ý là kế thừa class).
"""
# Tạo class Solution
class Solution:
    def twoSum(self, nums, target):
        self.nums = [] # truyền vào dạng nums là một list rỗng
        self.target = int # truyền vào định dạng target là số nguyên interger

        for i in range(len(nums)): # tạo vòng lặp cho i bắt đầu từ 0 đến độ dài của list nums khởi tạo ban đầu
            for j in range(i + 1, len(nums)): # tạo vòng lặp cho j bắt đầu từ số i + 1 đến độ dài của nums
                if nums[i] + nums[j] == target: # cộng hai list này lại tại vị trí thứ i và j: Ví dụ i = 1 thì j = 2
                    return i, j # trả về kết quả i và j


"""
Trong Python, "if__name __ ==" __main__ " 
cho phép bạn chạy các tệp chứa mã nguồn Python dưới dạng các mô-đun có thể tái sử dụng 
hoặc các chương trình độc lập.
"""
if __name__ == "__main__":
    a = Solution() # triệu hồi bé Solution ở đây nè
    print(a.twoSum([2, 7, 11, 15], 9)) # bây giờ hãy chạy phép tính và in ra màn hình kết quả nhé.

"""
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Bởi vì nums[0] + nums[1] == 9, we return [0, 1].
Ở đây hãy quan sát nhé, 2 + 7 = 9 đó nên return kết quả [0,1] là vị trí thứ 0 và 1 theo định nghĩa list của python
"""