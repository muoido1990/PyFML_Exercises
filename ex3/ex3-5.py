'''
Input: một số nguyên trong range(1,13).
Output: tên tương ứng của tháng đó bằng tiếng Anh, và số ngày trong tháng đó.
Tháng 2 tính 28 ngày.

Ví dụ:

- input_data: 2

- output: February 28
'''
input_data = input('Enter the number: ')
number = int(input_data)
L = ['Jan','Feb','March','April','May','June','July','Aug','Sep','Oct','Nov','Dec']
try:
	print(L[number - 1])
except IndexError:
	print('this is not a number')
	
	
