import json

# JSONファイルを作成するための辞書を作成します
# (Rolesの部分に日本語の文字列が含まれています)
dict = {}
dict["Email"] = "taro@example.com"
dict["Active"] = True
dict["CreatedDate"] = "2013-01-20T00:00:00Z"
dict["Roles"] = ["ユーザー", "管理者", "\\\\192.168.24.27\\disk1\\New共通\\生産部\\品質保証\\05_生産\\02_生産管理\\02_工程管理\\測定値記録自動化\\試し\\ハートビート\\BG\\log_.txt"]

# ensure_ascii "なし" で出力します
with open("output_uniEscape.json", "w", encoding="utf-8" ) as outputFile:
    json.dump(dict, outputFile, indent=2 )

# ensure_ascii "あり" で出力します
with open("output_jp.json", "w", encoding="utf-8") as outputFile:
    json.dump(dict, outputFile, indent=2, ensure_ascii=False )