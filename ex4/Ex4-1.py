'''
Biết function input('Bạn tên gì?') sẽ in ra màn hình dòng chữ "Bạn tên gì?"
và chờ bạn nhập câu trả lời. Sau khi bạn gõ câu trả lời rồi enter,
nội dung bạn vừa gõ sẽ được function trả về:
In [4]: name = input('Bạn tên gì? ')
Bạn tên gì? Hưng

In [5]: print(name)
Hưng

Viết chương trình nhận đầu vào là một địa chỉ IP (VD: 192.168.1.1),
in ra màn hình dạng binary của từng số tương ứng.
Input:
192.168.1.1

Output:
11000000.10101000.1.1

Note:
Trên Python2, function tương ứng tên là `raw_input`
'''
IP = input('Enter IP adress: ')
nums_in_IP = IP.split('.')
L =[]
for i in nums_in_IP:
    binary = bin(int(i))
    nums_binary = binary[2:]
    L.append(nums_binary)
L2 = '.'.join(L)
print(L2)