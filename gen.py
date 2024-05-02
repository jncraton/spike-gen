from PIL import Image, ImageDraw

def draw_card(name, hp):
    img = Image.new("RGB", (225, 350))
    draw = ImageDraw.Draw(img)
    draw.rectangle([(0, 0), (225, 350)], fill="grey", outline="white", width=10)

    draw.text((15, 15), name, "white")
    draw.text((175, 15), f"HP : {hp}", "white")
    img.save(f"{name}.png")

draw_card("Brightbulb", "80")