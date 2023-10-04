import os
import sys
WORKING_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(WORKING_DIR, "../"))

from word2number import w2n
text = [
	"mùng mười tháng mười một năm một chín bốn lăm",
    "mùng mười tháng mười năm hai không hai ba", 
	"một hai ba bốn năm",
	"mùng bốn tháng mười một năm hai nghìn không trăm hai mươi ba",
	"năm một chín tám mươi"
	]
for te in text:
    print(w2n(te))
