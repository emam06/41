import qrcode, re, pathlib
from qrcode.constants import ERROR_CORRECT_Q

URL = "https://m-techapp.com/m/chill/"   # cafe menu link
q = qrcode.QRCode(error_correction=ERROR_CORRECT_Q, border=0, box_size=1)
q.add_data(URL); q.make(fit=True)
m = q.get_matrix(); n = len(m)

def in_eye(r, c):
    return (r < 7 and c < 7) or (r < 7 and c >= n-7) or (r >= n-7 and c < 7)

dots = []
for r in range(n):
    for c in range(n):
        if m[r][c] and not in_eye(r, c):
            dots.append(f'<rect x="{c-.02}" y="{r-.02}" width="1.04" height="1.04" rx=".22"/>')
def eye(x, y):
    return (f'<rect x="{x+.5}" y="{y+.5}" width="6" height="6" rx="1" fill="none" stroke="url(#qg)" stroke-width="1"/>'
            f'<rect x="{x+2}" y="{y+2}" width="3" height="3" rx=".5" fill="url(#qg)"/>')
qr_svg = (f'<svg viewBox="0 0 {n} {n}" xmlns="http://www.w3.org/2000/svg" width="100%" height="100%">'
          '<defs><linearGradient id="qg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#2a1a10"/><stop offset="1" stop-color="#4a2c19"/></linearGradient></defs>'
          f'<g fill="url(#qg)">{"".join(dots)}</g>{eye(0,0)}{eye(n-7,0)}{eye(0,n-7)}</svg>')

def icon(name):
    s = pathlib.Path(f'assets/{name}.svg').read_text()
    s = re.sub(r'<title>.*?</title>', '', s)
    return s.replace('<svg ', '<svg fill="currentColor" ', 1)

wifi = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round">'
        '<path d="M2.5 9a14 14 0 0 1 19 0"/><path d="M5.8 12.6a9.3 9.3 0 0 1 12.4 0"/><path d="M9 16.2a4.6 4.6 0 0 1 6 0"/>'
        '<circle cx="12" cy="19.6" r="1.3" fill="currentColor" stroke="none"/></svg>')
cup = ('<svg viewBox="0 0 120 120" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round">'
       '<path d="M22 52h66v22a26 26 0 0 1-26 26H48a26 26 0 0 1-26-26z"/><path d="M88 58h8a12 12 0 0 1 0 24h-9"/>'
       '<path d="M14 108h82"/><path d="M42 40c-5-6 5-10 0-18M58 40c-5-6 5-10 0-18M74 40c-5-6 5-10 0-18"/></svg>')

icons = ['x','tiktok','instagram','whatsapp','facebook','pubg','youtube']
icon_html = ''.join(f'<span class="ic">{icon(i)}</span>' for i in icons)

html = f'''<!doctype html><html lang="ar"><head><meta charset="utf-8"><style>
@font-face{{font-family:Play;src:url(assets/Playfair.ttf);font-weight:400 900}}
@font-face{{font-family:Taj;src:url(assets/Tajawal-Bold.ttf);font-weight:700}}
@font-face{{font-family:Taj;src:url(assets/Tajawal-Medium.ttf);font-weight:500}}
@font-face{{font-family:Cai;src:url(assets/Cairo.ttf);font-weight:200 1000}}
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:709px;height:236px;overflow:hidden;background:#fff}}
#c{{position:relative;width:709px;height:236px;overflow:hidden;background:#fff;color:#4a2c19;font-family:Taj,sans-serif}}
#c>*{{position:absolute}}
.frame{{left:262px;top:8px;right:8px;bottom:8px;border:1.5px solid #d3a85c;border-radius:14px}}
.frame:after{{content:"";position:absolute;inset:3px;border:1px solid rgba(201,154,75,.3);border-radius:11px}}
.cupbg{{right:92px;top:62px;width:130px;height:130px;color:rgba(201,154,75,.13)}}
.qr{{left:22px;top:10px;width:176px;height:176px;background:#fff;border-radius:12px;padding:10px;
 box-shadow:0 0 0 2px #d3a85c,0 4px 12px rgba(80,50,20,.22)}}
.scan{{left:0;width:220px;top:190px;text-align:center;font:700 15px/1 Cai,sans-serif;letter-spacing:6px;color:#3b2415;padding-left:6px}}
.scan i{{display:inline-block;width:5px;height:5px;background:#c99a4b;transform:rotate(45deg);margin:0 2px 2px}}
.sup{{left:0;width:240px;bottom:7px;display:flex;justify-content:center;align-items:center;gap:7px;direction:ltr;
 font:700 10.5px/1 Taj,sans-serif;color:#4a2c19}}
.sup b{{font:800 13.5px/1 Cai,sans-serif;letter-spacing:.4px;background:#2a1a10;color:#f3d9a0;padding:3px 7px;border-radius:9px}}
.sup span{{direction:rtl}}
.title{{left:284px;top:7px;width:320px}}
.title h1{{font:800 46px/1 Play,serif;letter-spacing:.5px;background:linear-gradient(180deg,#e8c070 0%,#c08c36 50%,#8a5d1c 100%);
 -webkit-background-clip:text;color:transparent;filter:drop-shadow(0 1.5px 1.5px rgba(90,55,15,.3))}}
.title h1 span{{font-style:italic;font-weight:600}}
.tag{{display:flex;align-items:center;gap:8px;margin-top:5px;font:600 9px/1 Cai,sans-serif;letter-spacing:3.4px;color:#8e6428}}
.tag:before,.tag:after{{content:"";height:1px;width:22px;background:linear-gradient(90deg,transparent,#c99a4b)}}
.tag:after{{transform:scaleX(-1)}}
.wifi{{right:26px;top:14px;width:48px;height:48px;border-radius:50%;display:flex;align-items:center;justify-content:center;
 color:#2a1a10;background:linear-gradient(145deg,#f8e2b0,#c99a4b 60%,#9a6d2c);box-shadow:0 3px 8px rgba(80,50,20,.35),inset 0 1px 1px rgba(255,255,255,.6)}}
.wifi svg{{width:28px;height:28px}}
.wifi:before{{content:"";position:absolute;inset:-4px;border-radius:50%;border:1px solid rgba(201,154,75,.6)}}
.lab{{right:24px;top:84px;display:flex;align-items:center;gap:8px;direction:rtl;font:700 14px/1 Taj,sans-serif;color:#4a2c19}}
.lab:before{{content:"";width:6px;height:6px;background:#c99a4b;transform:rotate(45deg)}}
.field{{left:280px;right:24px;top:104px;height:46px;border-radius:23px;
 background:linear-gradient(180deg,#fffdf8,#f6ecd7);border:2px solid #d3a85c;box-shadow:inset 0 2px 4px rgba(90,60,25,.15),0 2px 6px rgba(80,50,20,.18)}}
.soc{{left:280px;right:24px;top:160px;display:flex;justify-content:space-between;align-items:center}}
.ic{{width:28px;height:28px;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#4a2c19;
 background:#fbf5e8;border:1.5px solid #c99a4b;box-shadow:0 2px 4px rgba(80,50,20,.2)}}
.ic svg{{width:14px;height:14px}}
.mt{{left:280px;bottom:12px;display:flex;align-items:center;gap:7px}}
.mt img{{width:30px;height:30px;border-radius:8px;box-shadow:0 2px 5px rgba(0,0,0,.35)}}
.mt small{{display:block;font:500 7px/1 Cai,sans-serif;letter-spacing:1.6px;color:#8e6428;text-transform:uppercase}}
.mt b{{display:block;font:800 11px/1.2 Cai,sans-serif;letter-spacing:2px;color:#2a1a10}}
.copy{{right:24px;bottom:12px;direction:rtl;font:500 9.5px/1.3 Taj,sans-serif;color:#6b4a2a;text-align:right}}
</style></head><body><div id="c">
<div class="frame" data-l="frame"></div><div class="cupbg" data-l="cup">{cup}</div>
<div class="qr" data-l="qr">{qr_svg}</div>
<div class="scan" data-l="scan-me">SCAN<i></i>ME</div>
<div class="sup" data-l="support"><b>01222881514</b><span>للدعم الفني وطلب الخدمة</span></div>
<div class="title" data-l="title"><h1>Chill <span>Cafe</span></h1><div class="tag">FREE WI-FI · RELAX &amp; ENJOY</div></div>
<div class="wifi" data-l="wifi-badge">{wifi}</div>
<div class="lab" data-l="login-label">رقم تسجيل الدخول</div><div class="field" data-l="login-field"></div>
<div class="soc" data-l="social-icons">{icon_html}</div>
<div class="mt" data-l="mtech-logo"><img src="assets/mtech-logo.png"><div><small>Powered by</small><b>M-TECH</b></div></div>
<div class="copy" data-l="copyright">جميع الحقوق محفوظة لشبكة أم - تك 2021<br>إمام محمود</div>
</div></body></html>'''
pathlib.Path('design.html').write_text(html)
