## Convert text to number (vietnamese)

### 1. Thêm các trường hợp đặc biệt

<strong> Thêm các dấu đặc biệt </strong>

ví dụ: năm phẩy hai -> 5,2  ta sẽ thêm vào `special_char` dòng 30 file data.py `"phẩy: ","`


<strong> Thêm các đơn vị đặc biệt </strong>

ví dụ: năm đô -> 5\$  ta sẽ thêm vào `units_acronyms` dòng 34 file data.py `"đô": "$"`

<strong> Thêm các từ ngoại lệ </strong>

Các từ ngoại lệ sẽ không chuyển sang số trong quá trình convert

Dòng 44 file data.py `excecpt_word = ["phong ba, cơm chín"]`

Chạy file test/convert_number.py

`python test/convert_number.py`

kết quả sẽ là:

```
902
12963324425
30,5
125,64
52021
tháng 8
ngày 12
ngày 24 tháng 11
tháng 5 năm 1945
ngày 13 tháng 2 năm 1992
đơn vị đo
20km
20kg
38C
hiệu điện thế 220V
80dB
1000000đ
1526000$
```
