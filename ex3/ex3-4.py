'''
- input_data = ["I", "Love", "You", "Chiu", "Chiu"]

- output: in ra thành cặp

Ví dụ::

  1 I
  2 Love
  3 You
  ... cho đến hết

Gợi ý: có thể dùng enumerate()
https://docs.python.org/2/library/functions.html#enumerate
'''

input_data = ['I', 'Love', 'You', 'Chiu', 'Chiu']
L = list(enumerate(input_data, start = 1))
for i in L:
	print(i[0],i[1])
	

	
	
	
	

