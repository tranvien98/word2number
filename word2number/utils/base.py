import math
from word2number.data import (
    billion_words,
    hundreds_words,
    million_words,
    special_word,
    tens_special,
    tens_words,
    thousand_words,
    units,
    word_multiplier,
    excecpt_word
)
import re
class Numbers(object):
    """Class xữ lý chữ số đầu vào."""

    def __init__(self, words_number: list):
        """Khởi tạo instance của lớp Numbers.

        Args:
            words_number (list): Danh sách chữ số đầu vào.
        """
        self.words_number = words_number

    @property
    def get_keyword_index(self):
        """Lấy vị trí index của các từ khóa như mười, trăm, nghìn, triệu, tỷ.

        Returns:
            Trả về một dic gồm các keyword và vị trí index của nó.

        """
        keyword_index = {
            'tens_index': None,
            'hundreds_index': None,
            'thousand_index': None,
            'million_index': None,
            'billion_index': None,
            'special_index': None,
        }

        for word in self.words_number:
            if word in tens_words:
                keyword_index['tens_index'] = self.words_number.index(word)

            if word in hundreds_words:
                keyword_index['hundreds_index'] = self.words_number.index(word)

            if word in thousand_words:
                keyword_index['thousand_index'] = self.words_number.index(word)

            if word in million_words:
                keyword_index['million_index'] = self.words_number.index(word)

            if word in billion_words:
                keyword_index['billion_index'] = self.words_number.index(word)

            if word in special_word:
                keyword_index['special_index'] = self.words_number.index(word)

        return keyword_index


def convert_to_tens_word(words: list):
    """Chuyển các từ mười, chục thành ['một,'mươi']

    Returns:
        Danh sách mới sau khi chuyển đổi
    """
    # Chuyển các từ mười, chục thành ['một,'mươi']
    for word in words:
        if word in tens_special:
            tens_index = words.index(word)
            words[tens_index] = 'mươi'
            words.insert(tens_index, 'một')

    return words


def pre_process_w2n(words: str):
    """Tiền xữ lý chuỗi số đầu vào.

    Giúp tiền xữ lý dữ liệu đầu vào bao gồm như định dang lại chuỗi số, kiểm tra tính hợp lệ
    của chuỗi số...

    Args:
        words (str): Chuỗi số đầu vào.

    Returns:
        Trả về một instance sau khi đã được xữ lý
        Nếu có lỗi sẽ trả về lỗi.

    Raises:
        ValueError: Nếu đầu vào không phải là một chuỗi.
        ValueError: Nếu đầu vào là chuỗi rỗng.

    """
    clean_numbers = []
    number_list = []
    index_number = []
    words = words.replace('-', ' ')  # replace ký tự đặt biệt "-" sang khoản trắng
    words = words.lower()  # converting chuổi đầu vào thành chuổi viết thường

    origin_list = words.strip().split()  # xóa khoảng trắng thừa và chia câu thành các từ
    origin_word = ' '.join(origin_list)
    except_remem = []
    # xử lý trường hợp 3,6 tỷ
    fin_comma = [m.start() for m in re.finditer("phẩy", origin_word)]
    for fin_c in fin_comma:
        index_comma = check_index(origin_list, fin_c, "phẩy")
        fin_billion = [k.start() for k in re.finditer("tỷ", origin_word)]
        for fin_b in fin_billion:
            index_billion = check_index(origin_list, fin_b, "tỷ")
            if int(index_billion[0]) - int(index_comma[0]) < 3 and int(index_billion[0]) - int(index_comma[0]) > 0:
                except_remem.extend(index_billion)
    # nhớ các vị trí ngoại lệ trong câu để bỏ qua khi phân biệt
    for ex_word in excecpt_word:
        fin_all = [m.start() for m in re.finditer(ex_word,origin_word)]
        for  fin in fin_all:
            except_remem.extend(check_index(origin_list, fin, ex_word))
    # print(except_remem)
    if len(except_remem) == 0:
        for idx, word in enumerate(origin_list):
            if word in units or word in word_multiplier :
                clean_numbers.append(word)
                index_number.append(idx)
            else:
                if len(clean_numbers) > 0:
                    number_list.append(convert_to_tens_word(clean_numbers))
                clean_numbers = []
    else:
        # print(except_remem)
        for idx, word in enumerate(origin_list):
            if (word in units or word in word_multiplier) and (idx not in except_remem):
                # print(idx, word)
                clean_numbers.append(word)
                index_number.append(idx)
            else:
                if len(clean_numbers) > 0:
                    number_list.append(convert_to_tens_word(clean_numbers))
                clean_numbers = []        
    # print("--------------",number_list)
    if len(clean_numbers) > 0:
        number_list.append(convert_to_tens_word(clean_numbers))
    return number_list, index_number, origin_list

def check_index(words, pos, ex_word):
    res = []
    index1 = 0
    for idx, word in enumerate(words):
        if index1 >= pos and index1 <= pos + len(ex_word):
            res.append(idx)
        index1 += len(word) + 1
    return res