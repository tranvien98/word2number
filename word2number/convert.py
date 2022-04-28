import re


# xử lý phần trăm dấu chấm dấu phẩy trong số
_point_number_re = re.compile(r'([0-9][0-9\.]+[0-9])')
_comma_number_re = re.compile(r'([0-9]+\,[0-9]+)')
_percent_number_re = re.compile(r'([0-9]+(%))')
_den_number_re = re.compile(r'([0-9]+(-)[0-9]+)')
_dolar_number_re = re.compile(r'([0-9]+(\$))')
_euro_number_re = re.compile(r'([0-9]+(\€))')
_link_number_re = re.compile(r'([a-zA-Z0-9]+(@)+[a-zA-Z0-9])')
_hours_number_re = re.compile(r'([0-9]+(h)+[0-9])')

def expand_commas(m):
    return m.group(1).replace(',', ' phẩy ')

def remove_point(m):
    return m.group(1).replace('.', '')

def expand_percent(m):
    return m.group(1).replace('%', ' phần trăm ')

def expand_den(m):
    return m.group(1).replace('-', ' đến ')

def expand_dolar(m):
    return m.group(1).replace('$', ' đô la ')

def expand_euro(m):
    return m.group(1).replace('!', ' ơ rô ')

def expand_link(m):
    return m.group(1).replace('@', ' a còng ')

def expand_hours(m):
    return m.group(1).replace('h', ' giờ ')

def acronyms(text):
    """
    Hàm xử lý các từ viết tắt
    """
    for i,j in _acronyms:
        text = re.sub(i,j,text)
    return text


def clear_text(text):
    """
    Hàm loại bỏ các khoảng trắng vd: 'aa    ss' ->  'aa ss'
    chuyển các từ sang dang chữ thường
    """
    text = re.sub(r'\s+', ' ', text)
    text = text.lower()
    return text

def  read_number(word):
    nu = NumberProcessing()
    check = True
    # print(word)
    for i in word:
        if not i.isdigit():
            check = False
    if check:
        return ' '.join(nu.read(word))
    else:
        return word


def split_symbol(text):
    """
    xử lý kí tự đặc biệt
    """
    return ' '.join([t.strip() for t in re.findall(r'\b.*?\S.*?(?:\b|$)',text)])
def expand(text):
    """
    Hàm xử  lý text
    """
    text = clear_text(text)
    text = acronyms(text)
    text = re.sub(_comma_number_re, expand_commas, text)
    text = re.sub(_percent_number_re, expand_percent, text)
    text = re.sub(_den_number_re, expand_den, text)
    text = re.sub(_dolar_number_re, expand_dolar, text)
    text = re.sub(_euro_number_re, expand_euro, text)
    text = re.sub(_link_number_re, expand_link, text)
    text = re.sub(_hours_number_re, expand_hours, text)
    text = read_text(text)
    # print(text)
    text = split_symbol(text)
    text = expand_number(text)
    text = clear_text(text)
    return text

