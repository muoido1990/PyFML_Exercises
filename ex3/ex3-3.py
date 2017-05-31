'''
bài tập ex3

Viết chương trình loại bỏ phần mở rộng của một tên file bất kỳ.
Ví dụ::

  input_data = '....slsslslsls...sls'
  output = '....slsslslsls..'

  input_data = 'maria.data.mp9'
  output = 'maria.data'
  
'''

input_data = 'maria.data.mp3'
number = len(input_data)
for i in range(number):
	if input_data[-i] == '.':
		print('the extension of file is {}'.format(input_data[-i:]))
		print(input_data[-number:-i])
		break
		
		
		
