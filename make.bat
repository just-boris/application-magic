SET PATH=c:\Program Files (x86)\Inkscape;%PATH%
for /f "tokens=1,* delims=." %%i in ('dir /b img_static *.svg') do (
  inkscape -f img_static\%%i.%%j -A img\%%i.pdf
)
pdflatex -synctex=1 --output-directory=build -interaction=nonstopmode main.tex