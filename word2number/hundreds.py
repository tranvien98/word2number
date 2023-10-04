from word2number.tens import process_tens
from word2number.units import process_units
from word2number.utils.hundreds import NumbersOfHundreds
from word2number.single import process_single


def pre_process_hundreds(words: list) -> NumbersOfHundreds:
    """Tiền xữ lý danh sách chữ số đầu vào.

    Giúp tiền xữ lý dữ liệu đầu vào bao gồm như định dang lại danh sách, kiểm tra tính hợp lệ
    của danh sách...

    Args:
        words (list): Danh dách chữ số dùng để tiền xữ lý.

    Returns:
        Trả về một instance sau khi đã được xữ lý
        Nếu có lỗi sẽ trả về lỗi.

    """
    numbers_of_hundreds = NumbersOfHundreds.format_words(words)

    # Kiểm tra tính hợp lệ của danh sách chữ số.
    numbers_of_hundreds.validate()

    return numbers_of_hundreds


def process_hundreds(words: list) -> str:
    """Xữ lý chữ số hàng trăm.

    Args:
        words (list): Danh sách chữ số đầu vào.

    Returns:
        Chuổi số hàng trăm.

    """
    # Tiền xữ lý danh sách chữ số đầu vào.

    numbers_of_hundreds = pre_process_hundreds(words)
    # print(numbers_of_hundreds.words_number)
    # Xữ lý chữ số hàng trăm.
    clean_words_number = numbers_of_hundreds.words_number

    value_of_hundreds = []
    value_of_tens = []

    # Lấy vị trí index của từ khóa hàng chục
    tens_index = numbers_of_hundreds.get_keyword_index['tens_index']
    hundreds_index = numbers_of_hundreds.get_keyword_index['hundreds_index']
    # print(clean_words_number)

    if hundreds_index:
        value_of_hundreds = clean_words_number[:1]

        try:
            value_of_tens = clean_words_number[hundreds_index + 1 :]
        except IndexError:
            value_of_tens = []

        # Trường hợp ['bốn', 'trăm', 'hai'] == 420
        if len(value_of_tens) == 1:
            value_of_tens.append('không')

    elif tens_index:
        # Lấy giá trị của phần chục.
        try:
            value_of_tens = clean_words_number[tens_index - 1 : tens_index + 2]
        except IndexError:
            value_of_tens = clean_words_number[tens_index - 1 :]

        # Lấy giá trị của phần còn lại.
        remaining = clean_words_number[tens_index + 2 :]
        if not remaining:
            remaining = clean_words_number[: tens_index - 1]

        # Trường hợp cho các số như ['hai','mươi', 'ba'] == 023
        if len(clean_words_number) <= 3:
            value_of_hundreds = ['không']
            value_of_tens = clean_words_number
        # print(tens_index)
        if len(clean_words_number) == 4:
            # Trường hợp đặc biệt như ['ba', 'bốn', 'mươi', 'hai'] == 342
            if tens_index == 1 and clean_words_number[0] == "một":
                remaining.insert(0, value_of_tens[-1])
                value_of_tens = value_of_tens[0:2]
                return process_tens(value_of_tens) + process_tens(remaining)

            if tens_index == 1:
                print(clean_words_number, value_of_tens, remaining)
                return process_tens(value_of_tens) + process_units(remaining)

            # Trường hợp đặc biệt như ['bốn', 'mươi', 'hai', 'ba'] == 423
            if tens_index == 2:
                return process_units(remaining) + process_tens(value_of_tens)

            # 
        if len(clean_words_number) == 5 or len(clean_words_number) == 6:
        # ['một', 'chín', 'tám', 'mươi'] -> xử lý thành  ['một', 'chín', 'tám', 'mươi', 'không]
            if tens_index == len(clean_words_number) - 2:
                tmp_number = ''
                for nb in remaining:
                    tmp_number+=process_units([nb])
                return tmp_number + process_tens(value_of_tens)
            if tens_index == 1 and clean_words_number[0] == "một" and len(clean_words_number) == 5:
                return process_tens(value_of_tens) + process_tens(remaining)
            # if tens_index == len(clean_words_number) :
            #     tmp_number = ''
            #     for nb in remaining:
            #         tmp_number+=process_units([nb])
            #     return tmp_number + process_tens(value_of_tens)
        if len(clean_words_number) == 7 or len(clean_words_number) == 8:
            if "năm" in clean_words_number:
                return process_tens(clean_words_number[0:len(clean_words_number)-5]) + process_single(clean_words_number[-5:])
    # Trường hợp ['hai', 'ba'] == 023
    elif len(clean_words_number) <= 2:
        value_of_hundreds = ['không']
        value_of_tens = clean_words_number

    # Trường hợp ['năm', 'sáu', 'hai'] == 562
    elif len(clean_words_number) == 3:
        value_of_hundreds = clean_words_number[:1]
        value_of_tens = clean_words_number[1:]
    # xử lý th đọc năm ví dụ một chín tám mươi
    return process_units(value_of_hundreds) + process_tens(value_of_tens)
