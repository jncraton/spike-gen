from PIL import Image, ImageDraw
from random import randint, shuffle


def draw_card(name, hp, type, attacks, rainbow):
    """Draw a single Spikeye card"""
    if rainbow:
        hp = hp * 2
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

    # Add the type icon
    type_img = Image.open(f"media/types/{type.lower()}.png").convert("RGBA")
    img.paste(type_img, (154, 10, 170, 26), type_img)

    # Draw main art border
    draw.rectangle([(10, 30), (215, 150)], fill="tan", outline="black", width=1)

    # Draw main art
    spike_img = Image.open(f"media/spikeyes/{name.lower()}01.png").convert("RGBA")
    img.paste(spike_img, (10, 30, 215, 150))

    if rainbow:
        rainbow_img = Image.open(f"media/types/rainbow.png").convert("RGBA")
        img.paste(rainbow_img, (10, 30, 215, 150), rainbow_img)

    # Draw each attack
    for a, y in zip(attacks, list(range(165, 350, 40))):
        draw.text((15, y), f"{a['name']}", "black")
        draw.text((15, y + 15), f"{a['description']}", "black")
        draw.text((200, y), f"{a['damage']}", "black")

        for i, energy in enumerate(a["energy"]):
            x = 100 + i * 18
            energy_img = Image.open(f"media/types/{energy.lower()}.png").convert("RGBA")
            img.paste(energy_img, (x, y, x + 16, y + 16), energy_img)

    # Save the image
    attack_ids = "-".join([str(a["id"]) for a in attacks])
    img.save(f"cards/{type}-{name}-{hp}-{attack_ids}.png")
    img.show()


def main():
    from attacks import attacks
    from spikeyes import spikeyes

    for spikeye in spikeyes[-1:]:
        hp = spikeye["hp"] + randint(-4, 4) * 10

        if randint(1, 36) == 1:
            rainbow = True
        else:
            rainbow = False

        allowed_attacks = [a for a in attacks if spikeye["type"] in a["types"]]
        shuffle(allowed_attacks)

        draw_card(spikeye["name"], hp, spikeye["type"], allowed_attacks[:4], rainbow)


if __name__ == "__main__":
    main()
