'''
Xét các số nguyên dương < 100, in ra các số chia hết cho 5 theo dạng::

    5  == 1 * 5
    10 == 2 * 5
    15 == 3 * 5
    ...
'''

for i in range(1,101):
	if i % 5 == 0:
		print('{} == {} * 5'.format(i, i//5))
		
		
		
