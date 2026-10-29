"""Builds four black & white Safari Wi-Fi card designs (709x236) as HTML.
Every card element is a direct child of #c carrying data-l="<layer name>" so
render.js can export each one as its own PSD layer."""
import pathlib, re, qrcode
from qrcode.constants import ERROR_CORRECT_Q

URL = "https://m-techapp.com/m/safari/"   # menu link (same pattern as the Chill card)
PHONE = "01222881514"
COPY = "جميع الحقوق محفوظة لشبكة أم - تك 2021 - إمام محمود"

# ---------------------------------------------------------------- shared bits
_q = qrcode.QRCode(error_correction=ERROR_CORRECT_Q, border=0, box_size=1)
_q.add_data(URL); _q.make(fit=True)
M = _q.get_matrix(); N = len(M)

def qr_svg(style="sharp", fg="#000"):
    def eye_zone(r, c):
        return (r < 7 and c < 7) or (r < 7 and c >= N - 7) or (r >= N - 7 and c < 7)
    rx = {"sharp": 0, "soft": .18, "round": .42}[style]
    pad = 0 if style == "sharp" else .04
    cells = "".join(
        f'<rect x="{c-.015+pad}" y="{r-.015+pad}" width="{1.03-2*pad}" height="{1.03-2*pad}" rx="{rx}"/>'
        for r in range(N) for c in range(N) if M[r][c] and not eye_zone(r, c))
    er = {"sharp": 0, "soft": 1.0, "round": 2.2}[style]
    def eye(x, y):
        return (f'<path fill-rule="evenodd" d="M{x+er} {y}h{7-2*er}a{er} {er} 0 0 1 {er} {er}v{7-2*er}a{er} {er} 0 0 1 -{er} {er}h-{7-2*er}a{er} {er} 0 0 1 -{er} -{er}v-{7-2*er}a{er} {er} 0 0 1 {er} -{er}z'
                f'M{x+1} {y+1}v5h5v-5z"/>'
                f'<rect x="{x+2}" y="{y+2}" width="3" height="3" rx="{er/2.4}"/>')
    return (f'<svg viewBox="0 0 {N} {N}" xmlns="http://www.w3.org/2000/svg" width="100%" height="100%" fill="{fg}" shape-rendering="crispEdges">'
            f'{cells}{eye(0,0)}{eye(N-7,0)}{eye(0,N-7)}</svg>')

def icon(name):
    s = pathlib.Path(f'assets/{name}.svg').read_text()
    s = re.sub(r'<title>.*?</title>', '', s)
    return s.replace('<svg ', '<svg fill="currentColor" ', 1)

ICONS = ['x', 'tiktok', 'instagram', 'whatsapp', 'facebook', 'pubg', 'youtube']
def icons(cls="ic"):
    return "".join(f'<span class="{cls}">{icon(i)}</span>' for i in ICONS)

WIFI = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round">'
        '<path d="M2.5 9a14 14 0 0 1 19 0"/><path d="M5.8 12.6a9.3 9.3 0 0 1 12.4 0"/><path d="M9 16.2a4.6 4.6 0 0 1 6 0"/>'
        '<circle cx="12" cy="19.6" r="1.5" fill="currentColor" stroke="none"/></svg>')

FONTS = """
@font-face{font-family:Archivo;src:url(assets/Archivo.ttf);font-weight:100 900}
@font-face{font-family:Bodoni;src:url(assets/Bodoni.ttf);font-weight:400 900}
@font-face{font-family:Josefin;src:url(assets/Josefin.ttf);font-weight:100 700}
@font-face{font-family:DMSerif;src:url(assets/DMSerif.ttf)}
@font-face{font-family:Plex;src:url(assets/PlexAr-Medium.ttf);font-weight:500}
@font-face{font-family:Plex;src:url(assets/PlexAr-Bold.ttf);font-weight:700}
@font-face{font-family:Reem;src:url(assets/ReemKufi.ttf);font-weight:400 700}
@font-face{font-family:Amiri;src:url(assets/Amiri-Bold.ttf);font-weight:700}
@font-face{font-family:Taj;src:url(assets/Tajawal-Bold.ttf);font-weight:700}
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:709px;height:236px;overflow:hidden;background:#fff}
#c{position:relative;width:709px;height:236px;overflow:hidden;background:#fff;color:#000}
#c>*{position:absolute}
svg{display:block}
"""

def page(css, body):
    return f'<!doctype html><html lang="ar"><head><meta charset="utf-8"><style>{FONTS}{css}</style></head><body><div id="c">{body}</div></body></html>'

# ================================================================ 01  SWISS
def d1():
    css = """
.rule{left:236px;right:24px;top:14px;height:6px;background:#000}
.divider{left:226px;top:14px;width:2px;height:208px;background:#000}
.qr{left:20px;top:10px;width:172px;height:172px;padding:6px;background:#fff}
.scan{left:24px;top:186px;font:800 13px/1 Archivo;letter-spacing:3px;display:flex;align-items:center;gap:8px}
.scan svg{width:22px;height:10px}
.sup{left:24px;bottom:9px;display:flex;align-items:center;gap:6px;direction:ltr}
.sup b{font:800 12px/1 Archivo;letter-spacing:.2px}
.sup i{width:1.5px;height:12px;background:#000}
.sup span{font:700 9px/1 Plex;direction:rtl}
.title{left:244px;top:20px;font:900 64px/1 Archivo;letter-spacing:-3px}
.title sup{font:700 11px/1 Archivo;letter-spacing:1px;vertical-align:top;position:relative;top:10px;margin-left:6px}
.ar{right:96px;top:32px;font:700 32px/1 Plex;direction:rtl}
.wifi{right:24px;top:28px;width:54px;height:54px;background:#000;color:#fff;display:flex;align-items:center;justify-content:center}
.wifi svg{width:32px;height:32px}
.tag{left:246px;top:94px;font:700 9px/1 Archivo;letter-spacing:3.2px}
.lab{right:24px;top:90px;font:700 14px/1 Plex;direction:rtl}
.field{left:246px;right:24px;top:112px;height:46px;border:3px solid #000}
.field:before,.field:after{content:"";position:absolute;top:-3px;width:14px;height:14px;background:#000}
.field:before{left:-3px}.field:after{right:-3px}
.soc{left:246px;right:24px;top:166px;display:flex;justify-content:space-between}
.ic{width:30px;height:30px;background:#000;color:#fff;display:flex;align-items:center;justify-content:center}
.ic svg{width:15px;height:15px}
.hr{left:246px;right:24px;top:203px;height:1.5px;background:#000}
.mt{left:246px;top:207px;display:flex;align-items:center;gap:7px}
.mt img{width:22px;height:22px}
.mt span{font:800 9px/1 Archivo;letter-spacing:2.4px}
.copy{right:24px;top:212px;font:500 9.5px/1 Plex;text-align:right;direction:rtl;white-space:nowrap}
"""
    body = f'''
<div class="rule" data-l="top-rule"></div><div class="divider" data-l="divider"></div>
<div class="qr" data-l="qr">{qr_svg("sharp")}</div>
<div class="scan" data-l="scan-me">SCAN FOR MENU <svg viewBox="0 0 22 10"><path d="M0 5h19M15 1l5 4-5 4" fill="none" stroke="#000" stroke-width="2"/></svg></div>
<div class="sup" data-l="support"><b>{PHONE}</b><i></i><span>للدعم الفني وطلب الخدمة</span></div>
<div class="title" data-l="title">Safari<sup>®</sup></div>
<div class="ar" data-l="title-arabic">سفاري</div>
<div class="wifi" data-l="wifi-badge">{WIFI}</div>
<div class="tag" data-l="tagline">FREE WI-FI / GUEST NETWORK</div>
<div class="lab" data-l="login-label">رقم تسجيل الدخول</div>
<div class="field" data-l="login-field"></div>
<div class="soc" data-l="social-icons">{icons()}</div>
<div class="hr" data-l="footer-rule"></div>
<div class="mt" data-l="mtech-logo"><img src="assets/mtech-mono.png"><span>POWERED BY M-TECH</span></div>
<div class="copy" data-l="copyright">{COPY}</div>'''
    return page(css, body)

# ================================================================ 02  NOIR
def d2():
    css = """
#c{background:#000;color:#fff}
.frame{left:6px;top:6px;right:6px;bottom:6px;border:1px solid #fff;border-radius:16px}
.qr{left:22px;top:16px;width:176px;height:176px;padding:12px;background:#fff;border-radius:14px}
.scan{left:22px;width:176px;top:198px;text-align:center;font:600 10px/1 Archivo;letter-spacing:5px;padding-left:5px}
.sup{left:22px;width:176px;top:214px;display:flex;justify-content:center;gap:7px;align-items:center;direction:ltr}
.sup b{font:700 11px/1 Archivo;letter-spacing:.8px}
.sup span{font:500 8.5px/1 Plex;direction:rtl}
.divider{left:214px;top:22px;bottom:22px;width:0;border-left:1.5px dotted #fff}
.title{left:236px;top:6px;font:800 66px/1 Bodoni;letter-spacing:-1px;font-variation-settings:"opsz" 11}
.title i{font-weight:500}
.tag{left:238px;top:74px;display:flex;align-items:center;gap:9px;font:600 8.5px/1 Archivo;letter-spacing:3.6px}
.tag:before{content:"";width:34px;height:1px;background:#fff}
.wifi{right:30px;top:20px;width:52px;height:52px;border:1.5px solid #fff;border-radius:50%;display:flex;align-items:center;justify-content:center}
.wifi:before{content:"";position:absolute;inset:3px;border:1px solid #fff;border-radius:50%}
.wifi svg{width:28px;height:28px}
.lab{right:30px;top:96px;display:flex;align-items:center;gap:8px;direction:rtl;font:700 14px/1 Plex}
.lab:before{content:"";width:6px;height:6px;background:#fff;transform:rotate(45deg)}
.labe{left:238px;top:99px;font:600 8.5px/1 Archivo;letter-spacing:3.6px}
.field{left:236px;right:30px;top:116px;height:44px;background:#fff;border-radius:22px}
.soc{left:236px;right:30px;top:164px;display:flex;justify-content:space-between}
.ic{width:28px;height:28px;border:1.5px solid #fff;border-radius:50%;display:flex;align-items:center;justify-content:center}
.ic svg{width:13px;height:13px}
.hr{left:236px;right:30px;top:202px;border-top:1.5px dotted #fff}
.mt{left:236px;top:206px;display:flex;align-items:center;gap:7px}
.mt img{width:20px;height:20px}
.mt span{font:600 8px/1 Archivo;letter-spacing:2.6px}
.copy{right:30px;top:211px;font:500 9px/1 Plex;text-align:right;direction:rtl;white-space:nowrap}
"""
    body = f'''
<div class="frame" data-l="frame"></div>
<div class="qr" data-l="qr">{qr_svg("round")}</div>
<div class="scan" data-l="scan-me">SCAN · MENU</div>
<div class="sup" data-l="support"><b>{PHONE}</b><span>للدعم الفني وطلب الخدمة</span></div>
<div class="divider" data-l="divider"></div>
<div class="title" data-l="title">Safari</div>
<div class="tag" data-l="tagline">FREE WI-FI · GUEST ACCESS</div>
<div class="wifi" data-l="wifi-badge">{WIFI}</div>
<div class="labe" data-l="login-label-en">LOGIN NUMBER</div>
<div class="lab" data-l="login-label">رقم تسجيل الدخول</div>
<div class="field" data-l="login-field"></div>
<div class="soc" data-l="social-icons">{icons()}</div>
<div class="hr" data-l="footer-rule"></div>
<div class="mt" data-l="mtech-logo"><img src="assets/mtech-mono-outline.png"><span>POWERED BY M-TECH</span></div>
<div class="copy" data-l="copyright">{COPY}</div>'''
    return page(css, body)

# ================================================================ 03  TRIBAL / GEOMETRIC
def zig(w, flip=False):
    # solid triangle row + thin line, repeated (pure vector, 1-bit friendly)
    t = ''.join(f'<path d="M{i*14} 10l7 -10l7 10z"/>' for i in range(int(w/14)+1))
    line = f'<rect x="0" y="12" width="{w}" height="1.6"/>'
    g = f'<g fill="#000">{t}{line}</g>'
    tr = f'transform="translate(0 14) scale(1 -1)"' if flip else ''
    return f'<svg width="{w}" height="14" viewBox="0 0 {w} 14"><g {tr}>{g}</g></svg>'

def d3():
    css = """
.qr{left:20px;top:14px;width:176px;height:176px;padding:10px;background:#fff;border:3.5px solid #000}
.qr:before,.qr:after{content:"";position:absolute;width:12px;height:12px;background:#000;top:-3.5px}
.qr:before{left:-3.5px}.qr:after{right:-3.5px}
.scan{left:20px;width:176px;top:190px;height:22px;background:#000;color:#fff;text-align:center;font:600 12px/22px Josefin;letter-spacing:6px;padding-left:6px}
.sup{left:20px;width:176px;top:216px;display:flex;justify-content:center;gap:7px;align-items:center;direction:ltr}
.sup b{font:700 11px/1 Josefin;letter-spacing:.8px}
.sup span{font:700 9px/1 Plex;direction:rtl}
.band1{left:214px;right:24px;top:10px}
.band2{left:214px;right:24px;bottom:10px}
.title{left:226px;top:28px;font:600 50px/1 Josefin;letter-spacing:9px}
.ar{right:30px;top:24px;font:700 46px/1.15 Reem;direction:rtl}
.sep{left:520px;top:50px;width:14px;height:14px;background:#000;transform:rotate(45deg)}
.pill{left:230px;top:84px;height:22px;padding:0 12px 0 8px;background:#000;color:#fff;border-radius:11px;display:flex;align-items:center;gap:7px;font:700 9px/1 Josefin;letter-spacing:3px}
.pill svg{width:14px;height:14px}
.lab{right:26px;top:90px;display:flex;align-items:center;gap:8px;direction:rtl;font:700 14px/1 Plex}
.lab:before{content:"";width:7px;height:7px;background:#000;transform:rotate(45deg)}
.field{left:230px;right:26px;top:114px;height:38px;border:2px solid #000;box-shadow:inset 0 0 0 4px #fff,inset 0 0 0 5.5px #000}
.soc{left:230px;right:26px;top:158px;display:flex;justify-content:space-between}
.ic{width:28px;height:28px;border:2px solid #000;border-radius:50%;display:flex;align-items:center;justify-content:center}
.ic svg{width:13px;height:13px}
.mt{left:230px;top:192px;display:flex;align-items:center;gap:7px}
.mt img{width:20px;height:20px}
.mt span{font:700 8px/1 Josefin;letter-spacing:2.6px}
.copy{right:26px;top:198px;font:500 9px/1 Plex;text-align:right;direction:rtl;white-space:nowrap}
"""
    body = f'''
<div class="qr" data-l="qr">{qr_svg("sharp")}</div>
<div class="scan" data-l="scan-me">SCAN ME</div>
<div class="sup" data-l="support"><b>{PHONE}</b><span>للدعم الفني وطلب الخدمة</span></div>
<div class="band1" data-l="pattern-top">{zig(470)}</div>
<div class="band2" data-l="pattern-bottom">{zig(470, True)}</div>
<div class="title" data-l="title">SAFARI</div>
<div class="sep" data-l="diamond"></div>
<div class="ar" data-l="title-arabic">سفاري</div>
<div class="pill" data-l="wifi-tag">{WIFI}FREE WI-FI</div>
<div class="lab" data-l="login-label">رقم تسجيل الدخول</div>
<div class="field" data-l="login-field"></div>
<div class="soc" data-l="social-icons">{icons()}</div>
<div class="mt" data-l="mtech-logo"><img src="assets/mtech-mono.png"><span>POWERED BY M-TECH</span></div>
<div class="copy" data-l="copyright">{COPY}</div>'''
    return page(css, body)

# ================================================================ 04  EXPEDITION LABEL
EMBLEM = ('<svg viewBox="0 0 100 100"><defs><clipPath id="cc"><circle cx="50" cy="50" r="44"/></clipPath></defs>'
          '<circle cx="50" cy="50" r="48" fill="#fff" stroke="#000" stroke-width="4"/>'
          '<g clip-path="url(#cc)" fill="#000">'
          '<circle cx="74" cy="30" r="9"/>'
          '<path d="M0 80 Q28 68 52 77 T100 72 V100 H0z"/>'
          '<path d="M37 80 C37 68 33 60 36 50" fill="none" stroke="#000" stroke-width="3.2" stroke-linecap="round"/>'
          '<path d="M36 62 C42 58 48 55 53 50" fill="none" stroke="#000" stroke-width="2.2" stroke-linecap="round"/>'
          '<ellipse cx="36" cy="45" rx="22" ry="5.5"/><ellipse cx="22" cy="49" rx="12" ry="3.6"/><ellipse cx="52" cy="47" rx="13" ry="3.8"/>'
          '<path d="M14 28l3 -3l3 3M26 20l2.4 -2.4l2.4 2.4" fill="none" stroke="#000" stroke-width="1.6"/>'
          '</g></svg>')
STAR = '<svg viewBox="0 0 10 10" width="8" height="8"><path d="M5 0l1.3 3.6 3.7.2-2.9 2.3 1 3.6L5 7.5 1.9 9.7l1-3.6L0 3.8l3.7-.2z" fill="#000"/></svg>'

def d4():
    css = """
.b1{left:6px;top:6px;right:6px;bottom:6px;border:3px solid #000;border-radius:16px}
.b2{left:12px;top:12px;right:12px;bottom:12px;border:1px solid #000;border-radius:11px}
.qr{left:26px;top:20px;width:158px;height:158px;padding:8px;background:#fff;border:3px solid #000;border-radius:12px}
.ribbon{left:26px;width:158px;top:174px;height:20px;background:#000;color:#fff;border-radius:10px;text-align:center;font:400 11px/20px DMSerif;letter-spacing:2.6px}
.sup{left:14px;width:184px;top:200px;display:flex;justify-content:center;align-items:center;gap:6px;direction:ltr}
.sup b{font:400 13px/1 DMSerif;letter-spacing:.6px}
.sup span{font:700 8.5px/1 Plex;direction:rtl}
.divider{left:200px;top:24px;bottom:24px;width:0;border-left:1.5px dashed #000}
.emblem{right:28px;top:20px;width:64px;height:64px}
.title{left:218px;top:16px;font:400 62px/1 DMSerif;letter-spacing:-.5px}
.ar{left:432px;top:30px;font:700 30px/1 Amiri;direction:rtl}
.tag{left:220px;top:80px;display:flex;align-items:center;gap:8px;font:700 8.5px/1 Archivo;letter-spacing:3.2px}
.lab{right:28px;top:98px;display:flex;align-items:center;gap:7px;direction:rtl;font:700 14px/1 Amiri}
.labe{left:220px;top:101px;font:700 8.5px/1 Archivo;letter-spacing:3.2px}
.field{left:218px;right:28px;top:118px;height:42px;border:2.5px dashed #000;border-radius:9px}
.soc{left:218px;right:28px;top:168px;height:30px;background:#000;border-radius:15px;color:#fff;display:flex;justify-content:space-between;align-items:center;padding:0 12px}
.ic svg{width:14px;height:14px}
.mt{left:220px;top:202px;display:flex;align-items:center;gap:6px}
.mt img{width:18px;height:18px}
.mt span{font:700 7.5px/1 Archivo;letter-spacing:2.4px}
.copy{right:30px;top:206px;font:500 9px/1 Plex;text-align:right;direction:rtl;white-space:nowrap}
"""
    body = f'''
<div class="b1" data-l="border-outer"></div><div class="b2" data-l="border-inner"></div>
<div class="qr" data-l="qr">{qr_svg("soft")}</div>
<div class="ribbon" data-l="scan-me">SCAN FOR MENU</div>
<div class="sup" data-l="support"><b>{PHONE}</b><span>للدعم الفني وطلب الخدمة</span></div>
<div class="divider" data-l="divider"></div>
<div class="emblem" data-l="emblem">{EMBLEM}</div>
<div class="title" data-l="title">Safari</div>
<div class="tag" data-l="tagline">{STAR}FREE WI-FI EXPEDITION{STAR}</div>
<div class="labe" data-l="login-label-en">ACCESS NO.</div>
<div class="lab" data-l="login-label">رقم تسجيل الدخول</div>
<div class="field" data-l="login-field"></div>
<div class="soc" data-l="social-icons">{icons()}</div>
<div class="mt" data-l="mtech-logo"><img src="assets/mtech-mono.png"><span>POWERED BY M-TECH</span></div>
<div class="copy" data-l="copyright">{COPY}</div>'''
    return page(css, body)

for i, fn in enumerate([d1, d2, d3, d4], 1):
    pathlib.Path(f'design{i}.html').write_text(fn())
print("built")
