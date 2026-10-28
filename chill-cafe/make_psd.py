import json
from PIL import Image
from psd_tools import PSDImage
from psd_tools.api.layers import PixelLayer
order = json.load(open('layers/order.json'))
for n in ['709x236', '2836x944']:
    flat = Image.open(f'chill-cafe-{n}.png').convert('RGB')
    psd = PSDImage.new('RGB', flat.size, color=(255, 255, 255))
    bg = PixelLayer.frompil(Image.new('RGB', flat.size, (255, 255, 255)), psd, 'background-white')
    psd.append(bg)
    for name in order:
        psd.append(PixelLayer.frompil(Image.open(f'layers/chill-cafe-{n}__{name}.png').convert('RGBA'), psd, name))
    psd.save(f'chill-cafe-{n}.psd')
    r = PSDImage.open(f'chill-cafe-{n}.psd'); print(n, r.size, [l.name for l in r])
