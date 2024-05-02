from PIL import Image, ImageDraw

def draw_card(name, hp):
    """ Draw a single Spikeye card """

    # Create empty image
    img = Image.new("RGB", (225, 350))

    # Initialize draw object
    draw = ImageDraw.Draw(img)

    # Create border and background
    draw.rectangle([(0, 0), (225, 350)], fill="grey", outline="white", width=10)

    # Draw name
    draw.text((15, 15), name, "white")

    # Draw hp
    draw.text((175, 15), f"HP : {hp}", "white")

    # Save the image
    img.save(f"{name}.png")

draw_card("Brightbulb", "80")