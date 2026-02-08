# PDF-Merger

This repository contains a single-file HTML app `pdfmerger.html`.

Build targets
- Native Windows EXE (portable) for x86 and x64 produced via GitHub Actions.

How it works
- A tiny Python wrapper (`main.py`) opens `pdfmerger.html` in a native window using `pywebview`.
- Packaging uses `PyInstaller` to create a single portable EXE that includes the HTML file.

Quick local build (Windows)
1. Install Python (x86 for 32-bit or x64 for 64-bit)
2. Install dependencies:
```
pip install -r requirements.txt
```
3. Build:
```
pyinstaller --noconsole --onefile --add-data "pdfmerger.html;." main.py
```

CI builds
- The workflow `.github/workflows/build-windows.yml` builds both x86 and x64 on `windows-latest` and uploads the resulting EXE artifacts.

Notes
- The produced EXE is a single-file bundle. Size depends on Python and `pywebview` runtime; this approach is significantly smaller than Electron but larger than native-compiled apps.
- For Windows 7 compatibility, use the Windows runners and the produced EXE; ensure the target machine has the Visual C++ runtime if needed.
