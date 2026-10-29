"""Assemble layered PSDs (one layer per card element) from layers/ + flat PNGs from out/."""
import json
from PIL import Image
from psd_tools import PSDImage
from psd_tools.api.layers import PixelLayer
for d in range(1, 5):
    order = json.load(open(f'layers/d{d}-order.json'))
    for tag in ['709x236', '2836x944']:
        size = Image.open(f'out/safari-{d}-{tag}.png').size
        psd = PSDImage.new('RGB', size, color=(255, 255, 255))
        psd.append(PixelLayer.frompil(Image.new('RGB', size, (255, 255, 255)), psd, 'background-white'))
        for name in order:
            psd.append(PixelLayer.frompil(Image.open(f'layers/d{d}-{tag}__{name}.png').convert('RGBA'), psd, name))
        psd.save(f'out/safari-{d}-{tag}.psd')
    print(d, PSDImage.open(f'out/safari-{d}-2836x944.psd').size, len(order) + 1, 'layers')
