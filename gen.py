from PIL import Image, ImageDraw


def draw_card(name, hp):
    """Draw a single Spikeye card"""

    # Create empty image
    img = Image.new("RGB", (225, 350))

    # Initialize draw object
    draw = ImageDraw.Draw(img)

    # Create border and background
    draw.rectangle([(0, 0), (225, 350)], fill="white", outline="tan", width=5)

    # Draw name
    draw.text((15, 15), name, "black")

    # Draw hp
    draw.text((175, 15), f"HP : {hp}", "black")

    draw.rectangle([(10, 30), (215, 150)], fill="white", outline="black", width=1)

    # Add the type icon
    type_img = Image.open("media/types/lightning.png")
    img.paste(type_img, (154, 10, 170, 26), type_img)

    # Save the image
    img.save(f"{name}.png")


spikeyes = [
{
    "name": "Brightbulb",
    "hp": "140",
},
]

for spikeye in spikeyes:
    draw_card(spikeye['name'], spikeye['hp'])