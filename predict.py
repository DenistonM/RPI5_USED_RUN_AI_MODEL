import os
import numpy as np
from PIL import Image
from ai_edge_litert.interpreter import Interpreter

FOLDER = "test_images"
EXTS = (".png", ".jpg", ".jpeg", ".bmp", ".webp")

labels = open("labels.txt").read().splitlines()

interp = Interpreter(model_path="model.tflite")
interp.allocate_tensors()
inp = interp.get_input_details()[0]
out = interp.get_output_details()[0]

files = sorted(f for f in os.listdir(FOLDER) if f.lower().endswith(EXTS))

if not files:
    print(f"No images found in '{FOLDER}'. Upload photos there first.")

for name in files:
    img = Image.open(os.path.join(FOLDER, name)).convert("RGB").resize((224, 224))
    x = np.expand_dims(np.array(img, dtype=np.float32), 0)

    interp.set_tensor(inp["index"], x)
    interp.invoke()
    probs = interp.get_tensor(out["index"])[0]

    i = int(np.argmax(probs))
    print(f"{name:30s} -> {labels[i]} ({probs[i]*100:.1f}%)   "
          f"CG: {probs[0]*100:.1f}%  DM: {probs[1]*100:.1f}%")
