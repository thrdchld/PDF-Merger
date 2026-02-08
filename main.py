import webview
import os
import sys

def resource_path(relative_path):
    if getattr(sys, 'frozen', False):
        base = sys._MEIPASS
    else:
        base = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base, relative_path)


def main():
    html = resource_path('pdfmerger.html')
    url = 'file://' + html
    webview.create_window('PDF Merger', url, width=1000, height=700, resizable=True)
    webview.start()


if __name__ == '__main__':
    main()
