 
rem イベントログの説明欄に表示するメッセージを定義
set I_TEST=sensor test result check(Hama's excel)
 
rem イベントログに書き出し
eventcreate /id 999 /l application /t information /d "%I_TEST%"

set dt=%date%
set dtnm=%dt:~0,4%%dt:~5,2%%dt:~8,2%-%COMPUTERNAME%-
set tm=%time%
set tmnm=%tm:~0,2%%tm:~3,2%%tm:~6,2%.log
set FName=C:\Users\Mochida.Tetsuya\Documents\CMD\LOG\%dtnm%%tmnm%

python C:\Users\Mochida.Tetsuya\source\repos\hamas\hamadas.py > %FName%


