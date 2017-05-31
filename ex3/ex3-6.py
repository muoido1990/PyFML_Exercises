'''
Viết chương trình nhận đầu vào là string "cho meo ga chuot vit ngan" và
in ra list chứa tất cả các chữ cái chỉ xuất hiện một lần trong string trên.

- input: names = "cho meo ga chuot vit ngan"

- output: ['m', 'e', 'u', 'v', 'i']
'''

input_data = 'cho meo ga chuot vit ngan'
L = []
for i in input_data:
	if input_data.count(i) == 1:
		L.append(i)
print(L)

