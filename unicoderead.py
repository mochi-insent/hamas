import sys
import json

# JSONのUnicodeエスケープを通常文字列に変換
data = None
with open(sys.argv[1], 'r') as f:
    data = json.load(f)
with open('decode_'+sys.argv[1], 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)