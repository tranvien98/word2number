## Convert text to number (vietnamese)

### 1. Thêm các trường hợp đặc biệt

<strong> Thêm các dấu đặc biệt </strong>

ví dụ: năm phẩy hai -> 5,2  ta sẽ thêm vào `special_char` dòng 30 file data.py `"phẩy: ","`


<strong> Thêm các đơn vị đặc biệt </strong>

ví dụ: năm đô -> 5\$  ta sẽ thêm vào `units_acronyms` dòng 34 file data.py `"đô": "$"`

<strong> Thêm các từ ngoại lệ </strong>

Các từ ngoại lệ sẽ không chuyển sang số trong quá trình convert

[excecpt_word](https://github.com/tranvien98/word2number/blob/main/word2number/data.py#L44)

Dòng 44 file data.py `excecpt_word = ["phong ba, cơm chín"]`

Chạy file test/convert_number.py

<strong> Thêm các từ ngoại lệ đúng </strong>
[exact_excecpt_words](https://github.com/tranvien98/word2number/blob/main/word2number/data.py#L47)
Các từ ngoại lệ đúng là các từ hoặc số sau khi được tìm kiếm đúng bằng từ đó ví dụ từ "trăm năm" trăm năm -> trăm năm,  sáu trăm năm mươi -> 650

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
