from PIL import Image

from backend.anime import cartoonify

from backend.effects import (
    apply_realistic_oil_painting,
    apply_realistic_pencil_sketch,
    apply_vintage_effect,
    apply_watercolor_canvas,
    apply_pop_art
)


def generate_effect(
    input_path,
    output_path,
    effect
):

    image = Image.open(
        input_path
    ).convert("RGB")

    if effect == "Anime":

        result = cartoonify(image)

    elif effect == "Oil Painting":

        result = Image.fromarray(
            apply_realistic_oil_painting(image)
        )

    elif effect == "Pencil Sketch":

        result = Image.fromarray(
            apply_realistic_pencil_sketch(image)
        )

    elif effect == "Vintage":

        result = Image.fromarray(
            apply_vintage_effect(image)
        )

    elif effect == "Watercolor":

        result = Image.fromarray(
            apply_watercolor_canvas(image)
        )

    elif effect == "Pop Art":

        result = apply_pop_art(image)

    else:

        result = image

    result.save(
        output_path
    )

    return output_path