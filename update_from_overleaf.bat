@echo off
setlocal

if "%~2"=="" (
  echo Usage: %~n0 ^<zip-file^> ^<pdf-file^> [commit-message]
  exit /b 1
)

set "ZIP_FILE=%~1"
set "PDF_FILE=%~2"
set "COMMIT_MSG=%~3"
set "SRC_DIR=src"
set "RENDERED_PDF=rendered.pdf"

if not exist "%ZIP_FILE%" (
  echo "Error: ZIP file (%ZIP_FILE%) not found."
  exit /b 1
)

if not exist "%PDF_FILE%" (
  echo "Error: PDF file (%PDF_FILE%) not found."
  exit /b 1
)

echo Cleaning up old content...
rd /s /q "%SRC_DIR%"
del "%RENDERED_PDF%"

echo Unpacking ZIP file to %SRC_DIR%...
mkdir "%SRC_DIR%"
powershell -Command "Expand-Archive -Path '%ZIP_FILE%' -DestinationPath '%SRC_DIR%' -Force"

echo Moving PDF to %RENDERED_PDF%...
move "%PDF_FILE%" "%RENDERED_PDF%"

echo Adding new files to git...
git add "%SRC_DIR%\*" "%RENDERED_PDF%"

if [%COMMIT_MSG%] == [] (
  echo No commit message provided. Opening editor for git commit...
  git commit -a
) else (
  echo Committing changes with provided message...
  git commit -a -m "%COMMIT_MSG%"
)

echo Repository updated successfully.
endlocal
