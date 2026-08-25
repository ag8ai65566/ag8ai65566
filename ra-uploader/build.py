#!/usr/bin/env python3
"""Inline the vendor library and app sources into one self-contained HTML file.

The result runs offline from the local filesystem with no install step and no
network access, which is what the people using it need.
"""
import pathlib, re, sys, datetime

HERE = pathlib.Path(__file__).parent
SRC, VENDOR, DIST = HERE / 'src', HERE / 'vendor', HERE / 'dist'
OUT = DIST / 'RA-Batch-Upload.html'

PARTS = {
    '/*__SHEETJS__*/': VENDOR / 'xlsx.full.min.js',
    '/*__CORE__*/':    SRC / 'core.js',
    '/*__BUILD__*/':   SRC / 'build.js',
    '/*__APP__*/':     SRC / 'app.js',
}


# An element id becomes a global via named element access. If one collides
# with a name a UMD wrapper sniffs for, the library attaches itself to the
# DOM node instead of the window and silently fails to load.
UMD_NAMES = {'exports', 'module', 'define', 'require', 'global', 'globalThis',
             'XLSX', 'RACore', 'RABuild'}


def check_ids(html):
    ids = set(re.findall(r'\bid="([^"]+)"', html)) | set(re.findall(r"\bname=\"([^\"]+)\"", html))
    clash = sorted(ids & UMD_NAMES)
    if clash:
        sys.exit('element id/name collides with a global a UMD wrapper looks for: '
                 + ', '.join(clash) + ' - rename it')


def main():
    html = (SRC / 'index.html').read_text(encoding='utf-8')
    check_ids(html)

    # Stamp the template BEFORE inlining. SheetJS's own source contains the
    # literal string "</body></html>", so stamping afterwards would corrupt it.
    stamp = datetime.date.today().isoformat()
    html = html.replace('</body>', f'<!-- built {stamp} -->\n</body>')

    for token, path in PARTS.items():
        if token not in html:
            sys.exit(f'placeholder {token} missing from index.html')
        code = path.read_text(encoding='utf-8')
        # A literal </script> inside JS would close the tag early.
        code = code.replace('</script>', '<\\/script>')
        html = html.replace(token, code)

    DIST.mkdir(exist_ok=True)
    OUT.write_text(html, encoding='utf-8')
    kb = OUT.stat().st_size / 1024
    print(f'{OUT}  ({kb:.0f} KB)')


if __name__ == '__main__':
    main()
