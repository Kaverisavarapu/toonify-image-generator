from PIL import Image

from backend.anime import cartoonify


def generate_cartoon(
    original_path,
    output_path
):

    image = Image.open(
        original_path
    )

    cartoon_image = cartoonify(
        image
    )

    cartoon_image.save(
        output_path
    )

    return output_path