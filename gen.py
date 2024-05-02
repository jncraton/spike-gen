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

    draw.rectangle([(160, 10), (170, 20)], fill="yellow", outline="black", width=1)
    # Save the image
    img.save(f"{name}.png")


draw_card("Brightbulb", "120")
draw_card("Benji", "1000")
