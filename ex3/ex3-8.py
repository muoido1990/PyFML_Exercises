'''
Tạo 1 list chứa các số nguyên dương nhỏ hơn 1000 là bội của 3 hoặc 5.

Tính tổng của các số đó.

Gợi ý: dùng hàm sum()

https://docs.python.org/3/library/functions.html#sum
'''

L = [i for i in range(1000) if i % 3 == 0 or i % 5 == 0]
print(sum(L))

