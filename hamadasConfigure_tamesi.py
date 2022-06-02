class hamasconf():
    def __init__(self) -> None:
        pass

    # 監視対象ディレクトリ
    target_dir = '\\\\192.168.24.27\\disk1\\New共通\\生産部\\品質保証\\05_生産\\02_生産管理\\02_工程管理\\測定値記録自動化\\試し\\ハートビート\\ロギング\\'

    # 参照ファイル名
    f = open(target_dir + 'BG\\' + 'センサ基本測定データ判定ファイル名.txt', 'r', encoding='UTF-8')

    #   出力ファイル名
    dst_file = '★基本測定データの判定.xlsm'

    #   出力シート名、貼付け開始位置
    h_sheet_name = 'データ貼付け用'
    start_row_prt = 1
    start_col_prt = 17
    start_row_abs = 1
    start_col_abs = 2

    path = '\\\\192.168.24.27\\disk1\\New共通\\生産部\\品質保証\\05_生産\\02_生産管理\\02_工程管理\\測定値記録自動化\\試し\\ハートビート\\BG\\htbt.txt'
