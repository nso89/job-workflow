@echo off
cls

set jobworkflow=main.py
set file=job-details.txt

python %jobworkflow%

if exist "%file%" (

    for /f "delims=" %%a in (%file%) do ( 
        echo Opening %%a\cover-letter-resume.odt.
        start "" "%%a\cover-letter-resume.odt" 
    )
    echo Removing %file%.
    del /q "%file%"
)

exit /b
