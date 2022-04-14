 
rem 				(1.0)2022.4.14, T.Mochida

rem イベントログの説明欄に表示するメッセージを定義
rem set I_TEST=sensor test result check(Hama's excel)  // ユーザモード　イベントログ書き出しはコメントアウト
 
rem イベントログに書き出し
rem eventcreate /id 999 /l application /t information /d "%I_TEST%"　// ユーザモード　イベントログ書き出しはコメントアウト

set dt=%date%
set dtnm=%dt:~0,4%%dt:~5,2%%dt:~8,2%-%COMPUTERNAME%-
set tm=%time: =0%
set tmnm=%tm:~0,2%%tm:~3,2%%tm:~6,2%.log
set FName=C:\Users\Mochida.Tetsuya\Documents\CMD\LOG\%dtnm%%tmnm%

rem -----------------------------------------------------------------
rem 「センサチェックデータ貼付プログラム」を実行します
rem -----------------------------------------------------------------

python \\192.168.24.27\disk1\New共通\生産部\品質保証\05_生産\02_生産管理\02_工程管理\測定値記録自動化\濱田さんEXCEL\BG\hamadas.py > %FName%


