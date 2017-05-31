input_data = 80
index = bin(80).rfind('1')
output_data = bin(80)[index:]
print('input_data là {}, output_data là {}'.format(input_data, output_data))

# Result
# input_data là 80, output_data là 10000
