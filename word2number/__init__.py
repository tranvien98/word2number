import re
from word2number.large_number import process_large_number
from word2number.data import units_acronyms, special_char, word_multiplier
from word2number.utils.base import pre_process_w2n
from word2number.single import process_single

def w2n(number_sentence):
    """Chuyển đổi chữ số sang số.

    Args:
        number_sentence (str): Chuổi chữ số đầu vào.

    Returns:
        Số đầu ra

    """
    # Kiểm tra tính hợp lệ của đầu vào
    if isinstance(number_sentence, int) or number_sentence.isdigit():
        return number_sentence

    if not isinstance(number_sentence, str):
        raise ValueError('Đầu vào không phải là dạng chuỗi (str)! Vui lòng truyền vào chuỗi các chữ số.')

    # Tiền xữ lý dữ liệu chuỗi số đầu vào
    number_list, index_number, origin_list = pre_process_w2n(number_sentence)
    new_string_numbers = []
    for str_num in number_list:
        # print(str_num)
        check_single = False
        for nu in str_num:
            if nu in word_multiplier:   
                check_single = True
                break
        if check_single:
            # print(str_num) 
            try:
                new_string_numbers.append(str(process_large_number(str_num)))
            except:
                # print("----")
                new_string_numbers.append(' '.join(str_num))
        else:
            new_string_numbers.append(str(process_single(str_num)))
    return merge_string(origin_list, new_string_numbers, index_number)

def merge_string(origin_list, number_list, index):
    """
        Hàm nối chuỗi
        list1: chuỗi ban đầu
        list2: chuỗi là số
        index: index các chuỗi ko là số trong cụm từ ban đầu
        return: chuỗi
    """
    idx2 = 0
    new_arr = []
    for idx1, ch in enumerate(origin_list):
        if idx1 in index:
            # if index + 1
            if idx1 + 1 not in index:
                if idx2 < len(number_list):
                    new_arr.append(number_list[idx2])
                    idx2 += 1
        else:
            new_arr.append(ch)
    text =  ' '.join(new_arr)
    text = acronyms(text)
    text = convert_special_char(text)
    text = convert_year(text)
    return text
        
def acronyms(text):
    """
    Hàm xử lý các từ viết tắt
    """
    _acronyms = [(re.compile('[0-9][ ]?%s[ ]?' % i, re.IGNORECASE), re.compile('[ ]?%s' % i, re.IGNORECASE), c) for i,c in units_acronyms.items()]
    for i,j, k in _acronyms:
        m = re.search(i, text)
        if m:
            text = re.sub(j,k,text)
    return text
    
def convert_year(text):
    _date_re = re.compile(r'\btháng[ ][1-9]{0,2}[5][1-2][0-9]{3}[ ]{0,1}')
    text = re.sub(_date_re, expand_date, text)
    _date_re = re.compile(r'\b[5][1-2][0-9]{3}[ ]{0,1}')
    text = re.sub(_date_re, expand_date, text)
    return text

def expand_date(m):
    # print( m.group(0))
    arr = m.group(0).strip().split(' ')
    if len(arr) > 1:
        pre = arr[0] + " "
    else:
        pre = ""
    # print(number)
    number = arr[-1]
    # print(number)
    if len(number) == 5:
        return pre + "năm " + number[1:] + ' '
    if len(number) == 6:
        return pre + number[0:1] + " năm " + number[2:] + ' '
    if len(number) == 7:
        return pre + number[0:2] + " năm " + number[3:] + ' '

    return m

def convert_special_char(text):
    """
    Hàm xử lý các từ viết tắt
    """
    _special_char = [(re.compile('[0-9][ ]?%s[ ]?' % i, re.IGNORECASE), re.compile('[ ]?%s[ ]?' % i, re.IGNORECASE), c) for i,c in special_char.items()]
    for i,j, k in _special_char:
        m = re.search(i, text)
        if m:
            text = re.sub(j,k,text)
    return text
