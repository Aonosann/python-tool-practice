import sys

# sys.argv は「コマンドの後ろに書いた言葉」のリストです
# 例: python hello.py Aono
# sys.argv は ["hello.py", "Aono"] になります

if len(sys.argv) >= 2:
    name = sys.argv[1]
else:
    name = "world"

print(f"Hello, {name}!")