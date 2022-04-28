from importlib.resources import contents
import os 
import sys
WORKING_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(WORKING_DIR, "../"))
from word2number import w2n
import re


text = ["chín trăm linh hai",
"mười hai tỷ chín trăm sáu ba triệu ba trăm hai mươi tư nghìn bốn trăm hai mươi lăm",
"ba mươi phẩy năm",
"một trăm hai lăm phẩy sáu tư",
"năm hai nghìn không trăm hai mốt",
"tháng tám",
"ngày mười hai",
"ngày hai mươi tư tháng mười một",
"tháng năm năm một nghìn chín trăm bốn lăm",
"ngày mười ba tháng hai năm một nghìn chín trăm chín hai",
"Đơn vị đo",
"hai mươi ki lô mét",
"hai mươi cân",
"ba mươi tám độ xê",
"hiệu điện thế hai trăm hai mươi vôn",
"tám mươi đề xi ben",
"một triệu đồng",
"một triệu năm trăm hai mươi sáu nghìn đô"]

for tx in text:
    print(w2n(tx))

# print((convert))