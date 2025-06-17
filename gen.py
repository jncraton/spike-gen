from PIL import Image, ImageDraw
from random import randint, shuffle


def draw_card(name, hp, types, attacks, rainbow, fa):
    """Draw a single Spikeye card"""
    if rainbow:
        hp = hp * 2

    textcolor = "black"

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
            textcolor = "white"
        except FileNotFoundError:
            fa = False
        if rainbow and fa:
            rainbow_img = Image.open(f"media/types/rainbowfa.png").convert("RGBA")
            img.paste(rainbow_img, (0, 0, 225, 350), rainbow_img)

    if not fa:
        # Draw main art border
        draw.rectangle([(10, 30), (215, 150)], fill="tan", outline="black", width=1)

        # Draw main art
        spike_img = Image.open(f"media/spikeyes/{name.lower()}01.png").convert("RGBA")
        img.paste(spike_img, (10, 30, 215, 150))

        if rainbow:
            rainbow_img = Image.open(f"media/types/rainbow.png").convert("RGBA")
            img.paste(rainbow_img, (10, 30, 215, 150), rainbow_img)

    # Draw name
    draw.text((15, 15), name, textcolor)

    # Draw hp
    draw.text((175, 15), f"HP : {hp}", textcolor)

    # Add the type icon
    for (x, t) in enumerate(types):
        type_img = Image.open(f"media/types/{t.lower()}.png").convert("RGBA")
        img.paste(type_img, (154 - x * 12, 10, 170 - x * 12, 26), type_img)

    # Draw each attack
    for a, y in zip(attacks, list(range(165, 350, 40))):
        draw.text((15, y), f"{a['name']}", textcolor)
        draw.text((15, y + 15), f"{a['description']}", textcolor)
        draw.text((200, y), f"{a['damage']}", textcolor)

        energy_img = Image.open(f"media/types/energy.png").convert("RGBA")
        for x in range(a['energy']):
            img.paste(energy_img, (154 - x * 12, y, 166 - x * 12, y+12), energy_img)
    
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
        if attack['name'] == name:
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

    for card in csv.DictReader(open('cards.csv')):
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
        )

if __name__ == "__main__":
    main()