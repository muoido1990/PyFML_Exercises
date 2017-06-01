'''
Cho list numbers chứa các giá trị từ -10 đến 10, trừ số 0.
In ra tuple chứa tổng (sum) và tích (product) của các phần tử trong list numbers.
Không sử dụng hàm ``sum``.

Input::

  li = range(-10, 11)
  li = list(li)
  li.remove(0)

Thêm dòng sau vào cuối bài để kiểm tra kết quả::

  from functools import reduce
  assert (mysum, myproduct) == (sum(numbers), reduce(lambda x,y: x*y, numbers))
'''
li = range(-10, 11)
li = list(li)
li.remove(0)

mysum = 0
for i in li:
    mysum += i
print(mysum)

myproduct = 1
for i in li:
    myproduct *= i
print(myproduct)

from functools import reduce
assert (0, 13168189440000) == (sum(li), reduce(lambda x,y: x*y, li))
