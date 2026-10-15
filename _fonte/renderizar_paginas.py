import os, subprocess, sys
from PIL import Image
D = os.path.dirname(os.path.abspath(__file__))
PUB = os.path.join(os.path.dirname(D), "public", "assets", "paginas-iniciais")
os.makedirs(os.path.join(PUB, "web"), exist_ok=True)
t = open(os.path.join(D, "paginas.tpl.html"), encoding="utf8").read()
t = t.replace("{{ILU_CSS}}", open(os.path.join(D, "ilu.css"), encoding="utf8").read()).replace("{{SPRITE}}", open(os.path.join(D, "sprite.html"), encoding="utf8").read())
html = os.path.join(D, "paginas.html"); open(html, "w", encoding="utf8").write(t)
chrome = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
for n in range(1, 5):
    png = os.path.join(PUB, f"{n:02d}.png")
    url = "file:///" + html.replace("\\", "/") + f"?page={n}"
    subprocess.run([chrome, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1",
                    "--window-size=1672,941", "--virtual-time-budget=9000", f"--screenshot={png}", url], check=True, capture_output=True, timeout=90)
    im = Image.open(png).convert("RGB")
    print(n, im.size)
    im.save(os.path.join(PUB, "web", f"{n:02d}.webp"), quality=86, method=6)
