'''
In ra 10 số nguyên tố đầu tiên trên cùng một dòng.

- Output: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29

Gợi ý: dùng print(2, end=', ')
'''

L =[]
for n in range(100):
	if n > 1: # start from 2
		for i in range(2, n):
			if n % i == 0:
				break
		else:
		  L.append(n)
print(L[:10])
			
