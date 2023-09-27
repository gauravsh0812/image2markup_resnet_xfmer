import os

import numpy as np
from albumentations.pytorch.transforms import ToTensorV2
from image_to_latex.lit_models import LitResNetTransformer
from PIL import Image
import argparse


script_path = os.path.dirname(os.path.realpath(__file__))

# Load model
lit_model = LitResNetTransformer.load_from_checkpoint("artifacts/model.ckpt")
lit_model.freeze()

# Load transform
transform = ToTensorV2()

def test_img(img_path: str) -> str:
    
    # Load image
    img_path = os.path.join(script_path, img_path)

    # Transform image
    image = Image.open(img_path).convert("L")
    image_tensor = transform(image=np.array(image))["image"] 
    
    # Predict
    pred = lit_model.model.predict(image_tensor.unsqueeze(0).float())[0]
    decoded = lit_model.tokenizer.decode(pred.tolist())  
    decoded_str = " ".join(decoded)
    return decoded_str

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Test image to latex')
    parser.add_argument('--img_path', type=str, help='Path to image')
    args = parser.parse_args()
    img_path = args.img_path
    print(test_img(img_path))