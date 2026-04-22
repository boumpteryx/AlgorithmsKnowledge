@echo off
REM Render all Mermaid diagrams to PNG
echo Rendering Mermaid diagrams to PNG...
echo.

setlocal enabledelayedexpansion
set count=0
set success=0

for /r .. %%f in (*.mmd) do (
    set /a count+=1
    set "input=%%f"
    set "output=%%~dpnf.png"
    
    echo [!count!] Rendering: %%~nxf
    npx -y @mermaid-js/mermaid-cli -i "!input!" -o "!output!" -b transparent 2>nul
    
    if !errorlevel! equ 0 (
        set /a success+=1
        echo     ^> Success: !output!
    ) else (
        echo     ^> Failed: %%f
    )
    echo.
)

echo.
echo ========================================
echo Rendering complete: !success!/!count! diagrams
echo ========================================
pause

@REM Made with Bob
