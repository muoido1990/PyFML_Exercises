'''
Biết 0o644 là biểu diễn của giá trị 420 (hệ 10) trên hệ bát phân (8-Octal).
Phải cộng 0o644 thêm bao nhiêu (ở dạng Octal) để thu được 0o777 ? In ra màn
hình giá trị đó.
Với người dùng Unix, mode của một file được biểu diễn ở dạng Octal, VD:
644, 400, 777.
'''
x = 0o777 - 0o644
print(oct(x))
