@echo off
setlocal EnableExtensions EnableDelayedExpansion
goto :main

:fizzbuzz
set /a "r15=%1 %% 15, r3=%1 %% 3, r5=%1 %% 5"
if !r15! equ 0 (
    echo FizzBuzz
) else if !r3! equ 0 (
    echo Fizz
) else if !r5! equ 0 (
    echo Buzz
) else (
    echo %1
)
exit /b 0

:main
for /l %%i in (1,1,100) do call :fizzbuzz %%i
exit /b 0
