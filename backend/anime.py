import torch

# Load once when server starts
device = "cuda" if torch.cuda.is_available() else "cpu"

model = torch.hub.load(
    "bryandlee/animegan2-pytorch:main",
    "generator",
    pretrained="celeba_distill",
    trust_repo=True
)

face2paint = torch.hub.load(
    "bryandlee/animegan2-pytorch:main",
    "face2paint",
    size=512,
    trust_repo=True
)


def cartoonify(pil_image):

    try:

        output_image = face2paint(
            model,
            pil_image
        )

        return output_image

    except Exception as e:

        print("❌ Cartoonify failed:", e)

        return pil_image