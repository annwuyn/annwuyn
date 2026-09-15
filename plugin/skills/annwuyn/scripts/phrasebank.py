#!/usr/bin/env python3
"""Runtime access to the user's own copy of Morley's Academic Phrasebank.

The plugin does not ship the Phrasebank (it is (c) The University of Manchester).
This script reads the user's PDF, caches its text outside the plugin, and serves it
to the `annwuyn` skills on demand. See ../references/12-phrasebank.md.

  phrasebank.py setup [PDF]        register a copy and build the cache
  phrasebank.py status             what is registered, which edition
  phrasebank.py show PAGES         print printed pages, e.g. 32 | 8-9 | 7,32,59
  phrasebank.py search REGEX       find frames, with printed page numbers
  phrasebank.py audit FILE         sentence-by-sentence frame coverage (.docx/.md/.txt, - for stdin)

Page numbers are always the PRINTED page numbers (the "N | Page" footer), never PDF indices.
Standard library only; needs `pdftotext` (poppler) or the `pypdf` package for `setup`.
"""
import argparse, glob, hashlib, json, os, re, shutil, subprocess, sys, zipfile
from xml.etree import ElementTree as ET

HOME = os.path.expanduser(os.environ.get('ANNWUYN_HOME', '~/.annwuyn'))
CACHE_DIR = os.path.join(HOME, 'phrasebank')
CACHE = os.path.join(CACHE_DIR, 'cache.json')
ENV_PDF = 'ANNWUYN_PHRASEBANK_PDF'

# Fingerprint of the edition the page map in 12-phrasebank.md was built against.
MAPPED_EDITION = {'label': '2015 enhanced edition (PDF)', 'pdf_pages': 107, 'marker': '2015 enhanced edition'}
PHRASE_PAGES = range(7, 92)  # printed pages that hold phrase material (sections + general functions)

FOOTER = re.compile(r'(\d{1,3})\s*\|\s*P\s*a\s*g\s*e\s*$')
STOP = set('a an the of in on at to for from by with and or but as is are was were be been being '
           'this that these those it its their there which who whom what when where how than then '
           'has have had not no into about over such can may might could would should will'.split())


# ---------- locating and extracting ----------

def find_candidates():
    pats = ['~/Downloads/*hrasebank*.pdf', '~/Documents/*hrasebank*.pdf', '~/Desktop/*hrasebank*.pdf',
            '~/Documents/*/*hrasebank*.pdf', '~/Documents/*/*/*hrasebank*.pdf']
    seen = []
    for p in pats:
        for f in sorted(glob.glob(os.path.expanduser(p))):
            if f not in seen:
                seen.append(f)
    return seen


def extract_pages(pdf):
    """Return a list of page texts in PDF order, layout preserved where possible."""
    if shutil.which('pdftotext'):
        out = subprocess.run(['pdftotext', '-layout', '-enc', 'UTF-8', pdf, '-'],
                             capture_output=True, text=True, check=True).stdout
        pages = out.split('\f')
        return pages[:-1] if pages and not pages[-1].strip() else pages
    try:
        from pypdf import PdfReader
    except ImportError:
        sys.exit('Need `pdftotext` (brew install poppler) or `pip install pypdf` to read the PDF.')
    return [(pg.extract_text(extraction_mode='layout') or '') for pg in PdfReader(pdf).pages]


def printed_number(text):
    for line in reversed([l for l in text.splitlines() if l.strip()][-4:]):
        m = FOOTER.search(line.strip())
        if m:
            return int(m.group(1))
    return None


def strip_footer(text):
    return '\n'.join(l for l in text.splitlines() if not FOOTER.search(l.strip())).rstrip()


def sha256(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(1 << 20), b''):
            h.update(chunk)
    return h.hexdigest()


def load():
    if not os.path.exists(CACHE):
        sys.exit('No Phrasebank registered. Run: phrasebank.py setup /path/to/Academic-Phrasebank.pdf\n'
                 f'(or set {ENV_PDF}). Candidates found: ' + (', '.join(find_candidates()) or 'none'))
    with open(CACHE, encoding='utf-8') as f:
        return json.load(f)


# ---------- commands ----------

def cmd_setup(a):
    pdf = a.pdf or os.environ.get(ENV_PDF)
    if not pdf:
        cands = find_candidates()
        if len(cands) != 1:
            sys.exit('Pass the PDF path explicitly. Candidates: ' + (', '.join(cands) or 'none found'))
        pdf = cands[0]
    pdf = os.path.abspath(os.path.expanduser(pdf))
    if not os.path.isfile(pdf):
        sys.exit(f'Not a file: {pdf}')
    raw = extract_pages(pdf)
    pages, offset_votes = {}, []
    for i, t in enumerate(raw, start=1):
        n = printed_number(t)
        if n is not None:
            offset_votes.append(i - n)
    offset = max(set(offset_votes), key=offset_votes.count) if offset_votes else 0
    for i, t in enumerate(raw, start=1):
        n = printed_number(t)
        pages[str(n if n is not None else i - offset)] = strip_footer(t)
    alltext = '\n'.join(raw)
    matches_map = (len(raw) == MAPPED_EDITION['pdf_pages'] and MAPPED_EDITION['marker'] in alltext)
    data = {'source': pdf, 'sha256': sha256(pdf), 'pdf_pages': len(raw), 'offset': offset,
            'matches_page_map': matches_map, 'pages': pages}
    os.makedirs(CACHE_DIR, exist_ok=True)
    with open(CACHE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)
    print(f'Registered {pdf}\n  {len(raw)} PDF pages, printed page = PDF page - {offset}\n  cache: {CACHE}')
    print('  edition: matches the page map in 12-phrasebank.md' if matches_map else
          '  edition: DIFFERENT from the mapped 2015 PDF — page numbers in 12-phrasebank.md will be off;'
          ' locate sections with `search` and cite section names, not the mapped pages.')


def cmd_status(a):
    d = load()
    print(json.dumps({k: v for k, v in d.items() if k != 'pages'}, indent=1, ensure_ascii=False))
    if not os.path.exists(d['source']):
        print('warning: the source PDF has moved; the cache still works.')


def parse_pages(spec):
    out = []
    for part in spec.split(','):
        part = part.strip()
        if '-' in part:
            lo, hi = part.split('-', 1)
            out.extend(range(int(lo), int(hi) + 1))
        elif part:
            out.append(int(part))
    return out


def cmd_show(a):
    d = load()
    for n in parse_pages(a.pages):
        text = d['pages'].get(str(n))
        if text is None:
            print(f'=== tr. {n}: not in this copy ===')
            continue
        text = re.sub(r'\n{3,}', '\n\n', text)
        print(f'=== tr. {n} ===\n{text}\n')


def cmd_search(a):
    d = load()
    rx = re.compile(a.regex, re.I)
    hits = 0
    for n in sorted(d['pages'], key=int):
        lines = d['pages'][n].splitlines()
        for i, line in enumerate(lines):
            if rx.search(line):
                lo, hi = max(0, i - a.context), min(len(lines), i + a.context + 1)
                block = '\n      '.join(l.rstrip() for l in lines[lo:hi] if l.strip())
                print(f'tr. {n:>3}: {block}')
                hits += 1
                if hits >= a.limit:
                    print(f'… stopped at {a.limit} hits (use --limit)')
                    return
    if not hits:
        print('no match')


# ---------- audit: which sentences rest on a traceable frame ----------

def tokens(s):
    s = s.replace('’', "'").replace('‘', "'").lower()
    return re.findall(r"[a-z]+(?:'[a-z]+)?", s)


SLOT = re.compile(r"\b(?:X|Y|Z|Xs|Ys|Zs|Xi|Xii|XYZ|Smith|Jones|Brown|Patel|Zhao|Wang|Al-Masry|O’Brien)\b(?:’s|'s)?")


def build_index(d, nmax=8):
    """n-gram index (3..nmax words) plus sentence openers, both mapped to printed pages.

    Cells are split at wide layout gaps (table columns) and at placeholder slots (X, Smith…),
    so the literal wording on either side of a slot is indexed on its own.
    """
    idx, openers = {}, {}
    for n in PHRASE_PAGES:
        text = d['pages'].get(str(n), '')
        for line in text.splitlines():
            for cell in re.split(r'\s{3,}', line):
                head = cell.strip().split(',')[0]
                if ',' in cell and 1 <= len(tokens(head)) <= 4 and not SLOT.search(head):
                    openers.setdefault(tuple(tokens(head)), set()).add(n)   # "Traditionally," "In contrast,"
                for frag in SLOT.split(cell):
                    t = tokens(frag)
                    for k in range(3, min(nmax, len(t)) + 1):
                        for i in range(len(t) - k + 1):
                            g = tuple(t[i:i + k])
                            if not all(w in STOP for w in g):
                                idx.setdefault(g, set()).add(n)
    return idx, openers


def read_text(path):
    if path == '-':
        return sys.stdin.read()
    if path.lower().endswith('.docx'):
        ns = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
        root = ET.fromstring(zipfile.ZipFile(path).read('word/document.xml'))
        return '\n'.join(''.join(t.text or '' for t in p.iter(ns + 't')) for p in root.iter(ns + 'p'))
    with open(path, encoding='utf-8') as f:
        return f.read()


def sentences(text):
    out = []
    for para in text.splitlines():
        para = para.strip()
        # skip headings (no closing punctuation) and reference-list entries
        if len(para.split()) < 4 or para.startswith('[') or not re.search(r'[.!?:;]["”’)\]]*$', para):
            continue
        protected = re.sub(r'\b(e\.g|i\.e|et al|etc|vs|cf|Fig|No)\.', lambda m: m.group(0).replace('.', '§'), para)
        for s in re.split(r'(?<=[.!?])\s+(?=[A-Z“"‘(\[])', protected):
            s = s.replace('§', '.').strip()
            if len(s.split()) >= 4:
                out.append(s)
    return out


def cmd_audit(a):
    d = load()
    idx, openers = build_index(d)
    rows = []
    for k, s in enumerate(sentences(read_text(a.file)), start=1):
        t = tokens(s)
        covered, found, i = [False] * len(t), [], 0
        head = tuple(tokens(s.split(',')[0])) if ',' in s else ()
        if head in openers:
            found.append((' '.join(head) + ',', sorted(openers[head])))
            covered[:len(head)] = [True] * len(head)
            i = len(head)
        while i < len(t):
            best = None
            for n in range(min(8, len(t) - i), 2, -1):
                g = tuple(t[i:i + n])
                if g in idx:
                    best = (n, g)
                    break
            if best:
                n, g = best
                found.append((' '.join(g), sorted(idx[g])))
                for j in range(i, i + n):
                    covered[j] = True
                i += n
            else:
                i += 1
        cov = sum(covered) / len(t) if t else 0
        # frame = a 4+-word run or a sentence opener; fragment = only 3-word runs (often generic English)
        strength = ('frame' if any(len(g.split()) >= 4 or g.endswith(',') for g, _ in found)
                    else 'fragment' if found else 'none')
        rows.append((k, s, found, cov, strength))
    if a.json:
        print(json.dumps([{'n': k, 'sentence': s, 'strength': st, 'coverage': round(c, 2),
                           'frames': [{'ngram': g, 'pages': p} for g, p in f]}
                          for k, s, f, c, st in rows], ensure_ascii=False, indent=1))
        return
    print('| # | Sentence | Match | Phrasebank wording (tr.) | Cover |\n|---|---|---|---|---|')
    for k, s, f, c, st in rows:
        short = s if len(s) <= 110 else s[:107] + '…'
        frames = '; '.join(f'“{g}” ({",".join(map(str, p[:3]))}{"…" if len(p) > 3 else ""})' for g, p in f) or '—'
        print(f'| {k} | {short} | {st if st != "none" else "**none**"} | {frames} | {c:.0%} |')
    count = {x: sum(r[4] == x for r in rows) for x in ('frame', 'fragment', 'none')}
    mean = sum(r[3] for r in rows) / len(rows) if rows else 0
    print(f'\n{len(rows)} sentences — frame {count["frame"]} · fragment only {count["fragment"]} · '
          f'none {count["none"]} · mean coverage {mean:.0%}')
    print('Heuristic only: a match shows traceable wording, not a correct move. "fragment" is a 3-word run, '
          'often generic English — confirm it. "none" may still rest on a grammar/style note (tr. 93–104) '
          'or a one-word connector — check by hand and log the licence.')


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest='cmd', required=True)
    p = sub.add_parser('setup'); p.add_argument('pdf', nargs='?'); p.set_defaults(f=cmd_setup)
    p = sub.add_parser('status'); p.set_defaults(f=cmd_status)
    p = sub.add_parser('show'); p.add_argument('pages'); p.set_defaults(f=cmd_show)
    p = sub.add_parser('search'); p.add_argument('regex')
    p.add_argument('--context', type=int, default=0); p.add_argument('--limit', type=int, default=60)
    p.set_defaults(f=cmd_search)
    p = sub.add_parser('audit'); p.add_argument('file'); p.add_argument('--json', action='store_true')
    p.set_defaults(f=cmd_audit)
    a = ap.parse_args()
    a.f(a)


if __name__ == '__main__':
    main()
