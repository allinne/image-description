# image-description
Gets image URL, returns its description

## Prerequisites
Python 3.9
BLIP base (Salesforce) 8-12 VRAM
```
pip install torch torchvision transformers pillow huggingface_hub
huggingface-cli download Salesforce/blip-image-captioning-base --local-dir ./models/blip-base
```

## Run
```
time python describe.py
```

## Example of output
```
2025-10-01 20:27:13.253385 Loaded
2025-10-01 20:27:13.253454 Processing 575373896.jpg
2025-10-01 20:27:13.984246 Description: a hotel room with a large bed, a green couch and a television
2025-10-01 20:27:13.984273 Processing 575374562.jpg
2025-10-01 20:27:14.358548 Description: a desk with a lamp and a book on it
2025-10-01 20:27:14.358571 Processing 583560095.jpg
2025-10-01 20:27:14.641396 Description: the dining area at the restaurant
2025-10-01 20:27:14.641418 Processing 585683353.jpg
2025-10-01 20:27:15.035989 Description: a bed or beds in a room at the white horse
2025-10-01 20:27:15.036011 Processing 594877746.jpg
2025-10-01 20:27:15.368883 Description: a bathroom with a sink, mirror and shower
2025-10-01 20:27:15.368910 Done
python describe.py  3.80s user 1.16s system 51% cpu 9.634 total
```
