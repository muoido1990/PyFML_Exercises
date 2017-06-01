'''

Cho string s::

  s = 'Em ơi có bao nhiêu, 60năm cuộc đời, 20 năm đầu, sung sướng0bao lâu'

Tạo ra list numbers chứa tất cả các số trong string này theo thứ tự chúng xuất hiện trong ``s``.

Output::

  assert numbers == [60, 20, 0]
'''
# Bài thầy chữa trên lớp, chưa tìm được cách giải nào hay hơn 
s = 'Em ơi có bao nhiêu, 60năm cuộc đời, 20 năm đầu, sung sướng0bao lâu'
numbers = []
a_number = []

for c in s:
    if c.isdigit():
        a_number.append(c)
    else:
        s = ''.join(a_number)
        if s:
            n = int(s)
            numbers.append(n)
            a_number = []

print(numbers)
