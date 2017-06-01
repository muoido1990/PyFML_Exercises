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

sum_li = 0
for i in li:
    sum_li += i
print(sum_li)

product = 1
for i in li:
    product *= i
print(product)

from functools import reduce
assert (mysum, myproduct) == (sum(numbers), reduce(lambda x,y: x*y, numbers))
