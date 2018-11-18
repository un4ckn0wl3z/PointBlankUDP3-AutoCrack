@echo off

@setlocal enableextensions
@cd /d "%~dp0"

python utils\hosterz.py
start cmd.exe /k python utils\kill_time_sync.py
python utils\license_refresher.py
timeout 1 > NUL
start pbserver_auth.exe #MoMzGames
start pbserver_battle.exe #yGigaSeet
start pbserver_game.exe #FumaPraQue

timeout 2 > NUL 

python utils\patch_key.py

timeout 2 > NUL

pause
taskkill /IM "python.exe" /F
python utils\restore_point.py
pause