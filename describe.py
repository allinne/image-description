
# Install:
# pip install torch torchvision transformers pillow huggingface_hub
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import torch

# Download:
# huggingface-cli download Salesforce/blip-image-captioning-base --local-dir ./models/blip-base
model_id = "./models/blip-base"

# Load processor and model into VRAM
processor = BlipProcessor.from_pretrained(model_id)
model = BlipForConditionalGeneration.from_pretrained(model_id, torch_dtype=torch.float16, device_map="auto")

image_path = "test/575373896.jpg"
image = Image.open(image_path).convert("RGB")
inputs = processor(images=image, return_tensors="pt").to(model.device)

with torch.no_grad():
    output_ids = model.generate(**inputs, max_new_tokens=30)
    caption = processor.decode(output_ids[0], skip_special_tokens=True)

print("Generated caption:", caption)
