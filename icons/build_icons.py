"""Yapı tipi ikon setini üretir (48x48 grid, 2.5px çizgi, currentColor).

Kullanım: python icons/build_icons.py
Çıktı: icons/svg/*.svg ve icons/preview.html
"""
from pathlib import Path

S = 'fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"'
F = 'fill="currentColor"'

def st(d): return f'<path d="{d}" {S}/>'
def fl(d, evenodd=False):
    r = ' fill-rule="evenodd"' if evenodd else ''
    return f'<path d="{d}" {F}{r}/>'

def afl(d, evenodd=False):
    return fl(d, evenodd).replace('fill="currentColor"', 'fill="__ACC__"')
def ast(d):
    return st(d).replace('stroke="currentColor"', 'stroke="__ACC__"')

# Palet (referans görselden): koyu kahve mürekkep + tek vurgu rengi
INK = "#5C2E1F"
TERRA = "#D4795F"
TEAL = "#3E9688"

GROUND = st("M4 42H44")

ACCENT = {
  "cami": TERRA, "han": TERRA, "hamam": TEAL, "turbe": TEAL, "medrese": TEAL,
  "cesme": TEAL, "konak": TERRA, "mektep": TEAL, "tekke": TERRA, "kilise": TEAL,
  "kervansaray": TERRA, "imaret": TERRA, "diger": TEAL,
}

ICONS = {
  "cami": ("Cami", [
    GROUND,
    st("M8 42V27H32V42"),
    afl("M8.5 27A11.5 11.5 0 0 1 31.5 27Z"),
    st("M20 15.5V10"),
    fl("M17 42V36Q17 32 20 30.5Q23 32 23 36V42Z"),
    st("M37 42V19M42 42V19M35.5 25H43.5"),
    fl("M36 19L39.5 7L43 19Z"),
  ]),
  "han": ("Han", [
    GROUND,
    st("M4 13H44M7 13V42M41 13V42"),
    afl("M11 25V20A2 2 0 0 1 15 20V25Z M17.5 25V20A2 2 0 0 1 21.5 20V25Z M26.5 25V20A2 2 0 0 1 30.5 20V25Z M33 25V20A2 2 0 0 1 37 20V25Z"),
    st("M7 29H41"),
    fl("M19 42V35A5 5 0 0 1 29 35V42Z"),
    fl("M11 38V34H15V38Z M33 38V34H37V38Z"),
  ]),
  "hamam": ("Hamam", [
    GROUND,
    st("M8 42V28H40V42"),
    afl("M11 28A13 13 0 0 1 37 28Z"
       "M17.5 24.5a1.6 1.6 0 1 0 3.2 0a1.6 1.6 0 1 0 -3.2 0Z"
       "M22.4 20.5a1.6 1.6 0 1 0 3.2 0a1.6 1.6 0 1 0 -3.2 0Z"
       "M27.3 24.5a1.6 1.6 0 1 0 3.2 0a1.6 1.6 0 1 0 -3.2 0Z", evenodd=True),
    fl("M21 42V36A3 3 0 0 1 27 36V42Z"),
    st("M18 11q-2 -2 0 -4M24 11q-2 -2 0 -4q2 -2 0 -4M30 11q-2 -2 0 -4"),
  ]),
  "turbe": ("Türbe", [
    GROUND,
    afl("M10 24L24 5L38 24Z"),
    st("M12 42V24H36V42M17 24V42M31 24V42"),
    fl("M21.5 35V30Q21.5 27.5 24 26.5Q26.5 27.5 26.5 30V35Z"),
  ]),
  "medrese": ("Medrese", [
    GROUND,
    st("M5 42V23H16M32 23H43V42"),
    st("M16 42V12H32V42"),
    afl("M19 42V27Q19 20 24 16.5Q29 20 29 27V42Z"),
    fl("M6.5 23A4.5 4.5 0 0 1 15.5 23Z M32.5 23A4.5 4.5 0 0 1 41.5 23Z"),
    fl("M9 34V30A2 2 0 0 1 13 30V34Z M35 34V30A2 2 0 0 1 39 30V34Z"),
  ]),
  "cesme": ("Çeşme", [
    st("M7 8H41M10 8V36M38 8V36"),
    st("M16 30V21Q16 15 24 12Q32 15 32 21V30"),
    ast("M24 21V24"),
    afl("M24 25.5Q26.5 29 26.5 30.5A2.5 2.5 0 0 1 21.5 30.5Q21.5 29 24 25.5Z"),
    fl("M7 36H41V42H7Z"),
  ]),
  "konak": ("Konak", [
    GROUND,
    afl("M3 16L12 8H36L45 16Z"),
    st("M6 16V28H42V16"),
    fl("M10 25V19H13V25Z M17 25V19H20V25Z M28 25V19H31V25Z M35 25V19H38V25Z"),
    st("M10 42V28M38 42V28M10 33L6 28M38 33L42 28"),
    fl("M21 42V35A3 3 0 0 1 27 35V42Z"),
  ]),
  "mektep": ("Mektep", [
    afl("M4 36Q14 32 24 36Q34 32 44 36V42Q34 38 24 42Q14 38 4 42Z"),
    st("M13 32V21H35V32"),
    fl("M13 21A11 11 0 0 1 35 21Z"),
    st("M24 10V5"),
    fl("M21.5 32V27.5A2.5 2.5 0 0 1 26.5 27.5V32Z"),
  ]),
  "tekke": ("Tekke ve Zaviye", [
    afl("M17 30L19 9Q24 2 29 9L31 30Z"),
    st("M10 35Q10 30 17 30H31Q38 30 38 35Q38 40 31 40H17Q10 40 10 35Z"),
    st("M14 35H34"),
    st("M8 44H40"),
  ]),
  "kilise": ("Kilise", [
    GROUND,
    st("M6 42V28L17 18L28 28V42"),
    st("M17 28m-2.5 0a2.5 2.5 0 1 0 5 0a2.5 2.5 0 1 0 -5 0"),
    fl("M14 42V37A3 3 0 0 1 20 37V42Z"),
    st("M30 42V17H40V42"),
    afl("M29 17L35 9L41 17Z"),
    st("M35 9V2M32.5 4.5H37.5"),
    fl("M33.5 27V23.5A1.5 1.5 0 0 1 36.5 23.5V27Z"),
  ]),
  "kervansaray": ("Kervansaray", [
    GROUND,
    st("M4 42V19H10V42M38 42V19H44V42"),
    st("M10 25H16M32 25H38"),
    st("M16 42V12H32V42"),
    afl("M19 42V28Q19 21 24 18Q29 21 29 28V42Z"),
    st("M13 31V36M35 31V36"),
  ]),
  "imaret": ("İmaret", [
    st("M7 24H41"),
    afl("M10 26H38V28Q38 40 24 40Q10 40 10 28Z"),
    st("M15 40L13 44M33 40L35 44M8 44H40"),
    st("M18 19q-2 -2.5 0 -5q2 -2.5 0 -5M24 19q-2 -2.5 0 -5q2 -2.5 0 -5q2 -2.5 0 -3M30 19q-2 -2.5 0 -5q2 -2.5 0 -5"),
  ]),
  "diger": ("Diğer", [
    st("M7 7H22V22H7Z M26 26H41V41H26Z"),
    afl("M26 7H41V22H26Z"),
    fl("M7 26H22V41H7Z"),
  ]),
}

def svg(body, size=48, title=None):
    t = f"<title>{title}</title>" if title else ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" '
            f'viewBox="0 0 48 48" role="img">{t}' + "".join(body) + "</svg>")

def mono(markup):
    return markup.replace("__ACC__", "currentColor")

def colored(markup, key, ink=INK):
    return markup.replace("__ACC__", ACCENT[key]).replace("currentColor", ink)

def main():
    root = Path(__file__).parent
    out_m = root / "svg"; out_m.mkdir(exist_ok=True)
    out_c = root / "svg-color"; out_c.mkdir(exist_ok=True)
    cards = []
    for key, (label, body) in ICONS.items():
        raw = svg(body, title=label)
        (out_m / f"{key}.svg").write_text(mono(raw) + "\n", encoding="utf-8")
        (out_c / f"{key}.svg").write_text(colored(raw, key) + "\n", encoding="utf-8")
        big = colored(svg(body, size=56), key)
        badge = colored(svg(body, size=32), key, ink="#FFF8EE")
        small = colored(svg(body, size=24), key)
        cards.append(f'''<figure class="card">
  <div class="tile">{big}</div>
  <div class="badge">{badge}</div>
  <div class="row"><span class="sm">{small}</span><figcaption>{label}</figcaption></div>
  <code>{key}.svg</code>
</figure>''')
    (root / "preview.html").write_text(PREVIEW.replace("{{CARDS}}", "\n".join(cards)), encoding="utf-8")

PREVIEW = """<!doctype html><html lang="tr"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Yapı İkonları</title>
<style>
:root{--ink:#5C2E1F;--paper:#EEEAE3;--card:#FBF8F2;--muted:#8A7F72;--text:#5A5146}
body{margin:0;background:var(--paper);color:var(--text);font:15px/1.4 system-ui,-apple-system,"Segoe UI",sans-serif;padding:40px 16px}
h1{font-weight:600;font-size:22px;margin:0 auto 4px;max-width:1040px;letter-spacing:.02em}
p.lead{margin:0 auto 28px;max-width:1040px;color:var(--muted)}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:16px;max-width:1040px;margin:0 auto}
.card{margin:0;background:var(--card);border-radius:14px;padding:20px 14px 14px;display:flex;flex-direction:column;align-items:center;gap:12px}
.tile{color:var(--ink);height:64px;display:flex;align-items:center}
.badge{width:52px;height:52px;border-radius:50%;background:var(--ink);color:#fff;display:flex;align-items:center;justify-content:center}
.row{display:flex;align-items:center;gap:8px;color:var(--text)}
figcaption{font-weight:600;font-size:14px}
code{font-size:11px;color:var(--muted)}
</style></head><body>
<h1>Yapı Tipi İkonları</h1>
<p class="lead">48×48 grid · 2.5px çizgi · dolu/boş dengesi · koyu kahve + ikon başına tek vurgu rengi (terracotta / teal). Üstte 56px, ortada rozet (32px), altta 24px liste boyutu.</p>
<div class="grid">
{{CARDS}}
</div></body></html>
"""

if __name__ == "__main__":
    main()
