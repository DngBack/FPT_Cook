import re

text = "peJulia and Cecilia visited peAustralia and Somalia."

# Mẫu regex tìm từ kết thúc bằng 'lia'
pattern = r'pe\w+'

# Tìm tất cả các từ khớp với mẫu
matches = re.findall(pattern, text)

# In ra kết quả
print("Các từ kết thúc bằng 'lia':", matches)
