from PIL import Image, ImageDraw
from random import randint, shuffle


def draw_card(name, hp, type, attacks):
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

    # Add the type icon
    type_img = Image.open(f"media/types/{type.lower()}.png").convert("RGBA")
    img.paste(type_img, (154, 10, 170, 26), type_img)

    # Draw main art border
    draw.rectangle([(10, 30), (215, 150)], fill="tan", outline="black", width=1)

    # Draw main art
    spike_img = Image.open(f"media/spikeyes/{name.lower()}01.png")
    img.paste(spike_img, (10, 30, 215, 150))

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
    img.save(f"cards/{name}.png")
    img.show()


spikeyes = [
    {
        "name": "Britebulb",
        "hp": 140,
        "type": "Lightning",
    },
    {
        "name": "Grassnlaid",
        "hp": 140,
        "type": "Leaf",
    },
    {
        "name": "Smokeos",
        "hp": 140,
        "type": "Flame",
    },
]

attacks = [
    {
        "types": ["Flame"],
        "name": "Firespin",
        "energy": ["Flame"] * 3,
        "description": "",
        "damage": 30,
    },
    {
        "types": ["Flame"],
        "name": "Flame punch",
        "energy": ["Flame"] * 3,
        "description": "",
        "damage": 40,
    },
    {
        "types": ["Flame"],
        "name": "Wildfire",
        "energy": ["Flame"] * 5,
        "description": "This attack does 20 damage to this card.",
        "damage": 140,
    },
    {
        "types": ["Flame"],
        "name": "Steam wall",
        "energy": ["Flame"] * 2 + ["Wave"] * 2,
        "description": "Halve the next damage done to this card.",
        "damage": "",
    },
    {
        "types": ["Flame"],
        "name": "lava pour",
        "energy": ["Flame"] * 4,
        "description": "your opponent is burned",
        "damage": 50,
    },
    {
        "types": ["Flame", "Lightning"],
        "name": "Hot bolt",
        "energy": ["Flame"] * 2 + ["Lightning"] * 3,
        "description": "",
        "damage": 140,
    },
    {
        "types": ["Flame"],
        "name": "Charcoal",
        "energy": ["Flame"] * 3 + ["stone"],
        "description": "",
        "damage": 120,
    },
    {
        "types": ["Flame"],
        "name": "Grassfire",
        "energy": ["Flame"] * 1 + ["Leaf"] * 4,
        "description": "+ 100 if your opponent is leaf type",
        "damage": 100,
    },
    {
        "types": ["Flame"],
        "name": "Thunder slam",
        "energy": ["Flame"] * 3,
        "description": "",
        "damage": 30,
    },
]


def main():
    for spikeye in spikeyes[-1:]:
        hp = spikeye["hp"] + randint(-4, 4) * 10

        allowed_attacks = [a for a in attacks if spikeye["type"] in a["types"]]
        shuffle(allowed_attacks)

        draw_card(spikeye["name"], hp, spikeye["type"], allowed_attacks[:4])


if __name__ == "__main__":
    main()
