 
rem 				(1.0)2022.4.14, T.Mochida

rem �C�x���g���O�̐������ɕ\�����郁�b�Z�[�W���`
rem set I_TEST=sensor test result check(Hama's excel)  // ���[�U���[�h�@�C�x���g���O�����o���̓R�����g�A�E�g
 
rem �C�x���g���O�ɏ����o��
rem eventcreate /id 999 /l application /t information /d "%I_TEST%"�@// ���[�U���[�h�@�C�x���g���O�����o���̓R�����g�A�E�g

set dt=%date%
set dtnm=%dt:~0,4%%dt:~5,2%%dt:~8,2%-%COMPUTERNAME%-
set tm=%time: =0%
set tmnm=%tm:~0,2%%tm:~3,2%%tm:~6,2%.log
set FName=C:\Users\Mochida.Tetsuya\Documents\CMD\LOG\%dtnm%%tmnm%

rem -----------------------------------------------------------------
rem �u�Z���T�`�F�b�N�f�[�^�\�t�v���O�����v�����s���܂�
rem -----------------------------------------------------------------

python \\192.168.24.27\disk1\New����\���Y��\�i���ۏ�\05_���Y\02_���Y�Ǘ�\02_�H���Ǘ�\����l�L�^������\�_�c����EXCEL\BG\hamadas.py > %FName%


