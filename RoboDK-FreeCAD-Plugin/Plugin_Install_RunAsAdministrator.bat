@echo off

setlocal enabledelayedexpansion 

set path_from=%~dp0
set path_freecad_mod=C:\Program Files\FreeCAD 1.0\Mod

echo\
echo --------------------------
echo Installing RoboDK FreeCAD Workbench


if EXIST "!path_freecad_mod!\." (
echo\
echo Installing RoboDK for FreeCAD in:
echo !path_freecad_mod!
robocopy "%path_from%RoboDK" "!path_freecad_mod!\RoboDK" /E
)


if "%~1"=="" (
echo\
echo Done
echo ----------------------------------------------------------
echo IMPORTANT: 
echo If errors arise, make sure you run the BAT file as administrator.
echo 
echo\
pause
)



