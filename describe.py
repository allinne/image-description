

import datetime
# Install:
# pip install torch torchvision transformers pillow huggingface_hub
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import torch

# Download:
# huggingface-cli download Salesforce/blip-image-captioning-base --local-dir ./models/blip-base
model_path = './models/blip-base'

def L(s):
     print(str(datetime.datetime.utcnow()) + ' ' + s)

# Load processor and model into VRAM
L('Starting')
processor = BlipProcessor.from_pretrained(model_path)
model = BlipForConditionalGeneration.from_pretrained(model_path, torch_dtype=torch.float16, device_map='auto')
L('Loaded')

pics = ('575373896.jpg', '575374562.jpg', '583560095.jpg', '585683353.jpg', '594877746.jpg')
for p in pics:
    L(f'Processing {p}')
    img = Image.open('test/' + p).convert('RGB')
    inputs = processor(images=img, return_tensors='pt').to(model.device)

    with torch.no_grad():
        ids = model.generate(**inputs, max_new_tokens=30)
        caption = processor.decode(ids[0], skip_special_tokens=True)
    L(f'Description: {caption}')

L('Done')
