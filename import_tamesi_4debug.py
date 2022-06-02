#   ###### センサ基本測定データ判定ファイル名.txt　で読み込み元ファイル名を指定する　#######
# #   ラベルプリンタPC から

import sys
import linecache

def exception_info():
    exc_type, exc_obj, tb = sys.exc_info()
    f = tb.tb_frame
    lineno = tb.tb_lineno
    filename = f.f_code.co_filename
    linecache.checkcache(filename)
    line = linecache.getline(filename, lineno, f.f_globals)
    return 'EXCEPTION IN ({}, LINE {} "{}"): {}'.format(filename, lineno, line.strip(), exc_obj)


try:
    #   インポートサーチパス追加
    import sys
    scrpath = __file__
    scrpath_dir = scrpath[:(scrpath.rfind('\\')+1)]
    print(scrpath_dir)
    sys.path.append(scrpath)


    #   ロギングの設定（jsonファイルから）
    import json
    from logging import getLogger, config
    from this import d

    with open(scrpath_dir + 'log_config_tamesi.json', 'r') as f:
        log_conf = json.load(f)

    config.dictConfig(log_conf)

    logger = getLogger(__name__)

    #   設定ファイルから読込
    from hamadasConfigure import hamasconf

    # ファイル変更イベント検出のため、watchdogをインポート
    import re
    from watchdog.events import FileSystemEventHandler
    from watchdog.observers import Observer

    # ファイルアクセスとスリープのため、osとtimeをインポート
    import os
    import time
    import openpyxl
    import csv

except Exception as ex:
    print(exception_info())
