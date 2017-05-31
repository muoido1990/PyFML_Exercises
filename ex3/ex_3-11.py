'''
a) Viết 1 chương trình tìm kí tự xuất hiện nhiều nhất trong 1 chuỗi


  b) Viết 1 chương trình đếm số tần xuất hiện của các ki tự trong 1 chuỗi


  Ví dụ::


'toi la aia' -->> t: 1, o: 1, i: 2, l: 1, a: 3
'''

str = 'toi la aia'
count_char = 0
for char in str:
	if str.count(char) > count_char:
		count_char = str.count(char)
print('{} is appeared {} times'.format(
