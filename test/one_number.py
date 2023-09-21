import os 
import sys
WORKING_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(WORKING_DIR, "../"))
from word2number import w2n

text = "chín tỷ đồng"
print(w2n(text))