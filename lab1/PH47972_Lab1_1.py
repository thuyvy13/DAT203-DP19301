# Khởi tạo mảng NumPy từ mảng Python gồm 10 năm sinh tùy ý từ 2000 - 2005, tính:
import numpy as np
from scipy import stats

my_array = np.array([2000, 2001, 2002, 2002, 2003, 2003, 2004, 2004, 2004, 2005])
age = 2024 - my_array

# - Tổng số tuổi
total_age = np.sum(age)
print(f"Tổng số tuổi: {total_age}")

# - Tuổi trung bình
average_age = np.mean(age)
print(f"Tuổi trung bình: {average_age}")

# - Tuổi trung vị
median_age = np.median(age)
print(f"Tuổi trung vị: {age}")

# - Tuổi nhỏ nhất
min_age = np.min(age)
print(f"Tuổi nhỏ nhất: {min_age}")

# - Tuổi lớn nhất
max_age = np.max(age)
print(f"Tuổi nhỏ nhất: {max_age}")

# - Tuổi yếu vị
mode_age = stats.mode(age)
print(f"Tuổi yếu vị:")
print("Mode:", mode_age.mode)
print("Frequency:", mode_age.count)