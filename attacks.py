attacks = [
    {
        "types": ["Flame"],
        "name": "Firespin",
        "description": "",
        "damage": 30,
    },
    {
        "types": ["Flame"],
        "name": "Flame punch",
        "description": "",
        "damage": 40,
    },
    {
        "types": ["Flame"],
        "name": "Wildfire",
        "description": "This attack does 20 damage to this card.",
        "damage": 60,
    },
    {
        "types": ["Flame"],
        "name": "Steam wall",
        "description": "Halve the next damage done to this card.",
        "damage": "",
    },
    {
        "types": ["Flame"],
        "name": "lava pour",
        "description": "your opponent is burned",
        "damage": 50,
    },
    {
        "types": ["Flame", "Lightning"],
        "name": "Hot bolt",
        "description": "",
        "damage": 140,
    },
    {
        "types": ["Flame"],
        "name": "Charcoal",
        "description": "",
        "damage": 120,
    },
    {
        "types": ["Flame"],
        "name": "Grassfire",
        "description": "+ 100 if your opponent is leaf type",
        "damage": 100,
    },
    {
        "types": ["Lightning"],
        "name": "Thunder slam",
        "description": "",
        "damage": 50,
    },
    {
        "types": ["Lightning"],
        "name": "Lightning rod",
        "description": "Lightning moves do x2 their normal damage",
        "damage": 50,
    },
    {
        "types": ["Wave", "Lightning"],
        "name": "Storm",
        "description": "20 damage each turn to all cards",
        "damage": 20,
    },
    {
        "types": ["Leaf", "Wave"],
        "name": "Seaweed",
        "description": "",
        "damage": 120,
    },
    {
        "types": ["Wave"],
        "name": "Wave",
        "description": "",
        "damage": 90,
    },
    {
        "types": ["Spell"],
        "name": "Energy Sheild",
        "description": "Halve the next damage done to this card",
        "damage": "",
    },
    {
        "types": ["Leaf"],
        "name": "Growth",
        "description": "Draw a card.",
        "damage": "",
    },
    {
        "types": ["Leaf"],
        "name": "Grass Spin",
        "description": "",
        "damage": 76,
    },
    {
        "types": ["Leaf"],
        "name": "Leaf Smack",
        "description": "",
        "damage": 110,
    },]

for i, attack in enumerate(attacks):
    attack["id"] = i
