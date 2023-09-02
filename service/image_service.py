import torch
from lavis.models import load_model_and_preprocess
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model, vis_processors, _ = load_model_and_preprocess(name="blip_caption",
                                                     model_type="large_coco",
                                                     is_eval=True, device=device)

# setup device to use
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


def process_image(raw_image):
    image = vis_processors["eval"](raw_image).unsqueeze(0).to(device)
    result = model.generate({"image": image})
    return result
