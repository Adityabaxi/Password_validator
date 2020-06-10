import re


pattern2=re.compile(r"[a-zA-z0-9#$%@]{7,}[0-9]")
password='Aditya@$91'

check=pattern2.fullmatch(password)
print(check)
