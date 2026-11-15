@echo off
setlocal EnableExtensions EnableDelayedExpansion
goto :main

:fizzbuzz
set "result="
set /a "r3=%1 %% 3, r5=%1 %% 5"
if !r3! equ 0 set "result=Fizz"
if !r5! equ 0 set "result=!result!Buzz"
if not defined result set "result=%1"
echo !result!
exit /b 0

:main
for /l %%i in (1,1,100) do call :fizzbuzz %%i
exit /b 0
