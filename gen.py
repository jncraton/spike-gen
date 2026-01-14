from PIL import Image, ImageDraw, ImageFont
from random import randint, shuffle
from datetime import datetime

# use a truetype font
title_font = ImageFont.truetype("noto-sans-webfont.extracondensedbold.ttf", 14)
font = ImageFont.truetype("noto-sans-webfont.regular.ttf", 10)


def draw_card(name, hp, types, attacks, rainbow, fa, textcolor="black", description=""):
    """Draw a single Spikeye card"""
    if rainbow:
        hp = hp * 1

    # Create empty image
    img = Image.new("RGB", (225, 350))

    # Initialize draw object
    draw = ImageDraw.Draw(img)

    # Create border and background
    draw.rectangle([(0, 0), (225, 350)], fill="white", outline="tan", width=5)

    # Draw Art
    if fa:
        # Draw fullart
        try:
            filename = f"media/spikeyes/{name.lower()}01_fa.png"
            spike_img = Image.open(filename).convert("RGBA")
            img.paste(spike_img, (0, 0, 225, 350))
        except FileNotFoundError:
            fa = False
        if rainbow and fa:
            rainbow_img = Image.open(f"media/types/rainbowfa.png").convert("RGBA")
            img.paste(rainbow_img, (0, 0, 225, 350), rainbow_img)

    if not fa:
        # Draw main art border
        draw.rectangle([(10, 30), (215, 150)], fill="tan", outline="black", width=1)

        # Draw main art
        spike_img = Image.open(f"media/spikeyes/{name.lower().replace(' ', '-')}01.png").convert("RGBA")
        img.paste(spike_img, (10, 30, 215, 150))

        if rainbow:
            rainbow_img = Image.open(f"media/types/rainbow.png").convert("RGBA")
            img.paste(rainbow_img, (10, 30, 215, 150), rainbow_img)

    # Draw name
    if rainbow:
        draw.text((60, 8), name, textcolor, font=title_font)
        rainbow_img = Image.open(f"media/spikeyes/rainbow.png").convert("RGBA")
        img.paste(rainbow_img, (15, 15, 55, 24), rainbow_img)
    else:
        draw.text((15, 8), name, textcolor, font=title_font)
    # Draw hp
    if hp > 0:
        draw.text((160, 8), f"HP : {hp}", textcolor, font=title_font)

    if len(description) > 0:
        # Draw description
        draw.text((15, 161), description, textcolor, font=font)
    else:
        # Add the type icon
        for (x, t) in enumerate(types):
            type_img = Image.open(f"media/types/{t.lower()}.png").convert("RGBA")
            img.paste(type_img, (139 - x * 12, 10, 155 - x * 12, 26), type_img)

        # Draw each attack
        for a, y in zip(attacks, list(range(165, 350, 40))):
            draw.text((15, y - 4), f"{a['name']}", textcolor, font=title_font)
            draw.text((15, y + 15), f"{a['description']}", textcolor, font=font)
            draw.text((200, y - 4), f"{a['damage']}", textcolor, font=title_font)

            energy_img = Image.open(f"media/types/energy.png").convert("RGBA")
            for x in range(a["energy"]):
                img.paste(
                    energy_img, (154 - x * 12, y, 166 - x * 12, y + 12), energy_img
                )

    draw.text((160, 332), datetime.today().strftime("%Y-%m-%d"), textcolor, font=font)

    # Save the image
    attack_ids = "-".join([str(a["id"]) for a in attacks])

    tags = []
    if rainbow:
        tags.append("Rainbow")
    if fa:
        tags.append("fa")

    if len(tags) == 0:
        tags_str = ""
    else:
        tags_str = "-" + "-".join(tags)

    img.save(f"cards/{'-'.join(types)}-{name}{tags_str}-{hp}-{attack_ids}.png")
    # img.show()


def get_attack(name):
    from attacks import attacks

    for attack in attacks:
        if attack["name"] == name:
            return attack
    else:
        print(f"No attack for {name}")
        exit(1)


def main():
    from spikeyes import spikeyes
    import csv

    # Remove any old cards
    import os

    for filename in os.listdir("cards"):
        if filename.endswith(".png"):
            os.remove(os.path.join("cards", filename))

    for card in csv.DictReader(open("cards.csv")):
        types = [card["type1"], card["type2"], card["type3"]]
        types = [t for t in types if t]

        attacks = [card["attack1"], card["attack2"], card["attack3"]]
        attacks = [get_attack(a) for a in attacks if a]

        draw_card(
            name=card["name"],
            hp=int(card["hp"]),
            types=types,
            attacks=attacks,
            rainbow=card["rainbow"] == "y",
            fa=card["fullart"] == "y",
            textcolor=card["textcolor"] or "black",
            description=card["description"],
        )


if __name__ == "__main__":
    main()
