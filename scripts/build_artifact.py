"""Build the claude.ai Artifact version of index.html.

The artifact host wraps the page in its own <!doctype>/<html>/<head>/<body>
skeleton, so this strips those wrappers (and the charset/viewport metas the
skeleton already provides) and keeps everything else unchanged.

Usage: python3 scripts/build_artifact.py [output_path]
"""
import re, sys, pathlib

src = pathlib.Path(__file__).resolve().parent.parent / 'index.html'
out = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else 'dist/lvli-artifact.html')
s = src.read_text(encoding='utf-8')
for pat in [r'<!doctype html>\s*', r'<html[^>]*>\s*', r'<head>\s*', r'<meta charset="utf-8">\s*',
            r'<meta name="viewport"[^>]*>\s*', r'</head>\s*', r'<body>\s*', r'</body>\s*', r'</html>\s*']:
    s, n = re.subn(pat, '', s, count=1, flags=re.I)
    assert n == 1, pat
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(s, encoding='utf-8')
print(out)
