from colors import *

potion = {
    "Healing": [RED, "Restores health",'Instant'],
    "Mana": [BLUE, "Restores mana", 'Instant'],
    "Strength": [CYAN, "Increase your strength",5],
    "Goblin’s Brew": [DARK_GREEN,"Enhances physical agility and grants night vision but causes minor hallucinations", 10],
    "Invisibility": [FAINT, "Become invisible to the naked eye",7],
    "Beast's Essence": [PURPLE, "Temporarily transforms the drinker into a powerful, feral beast with enhanced senses and strength",3],
}

spell = {
    "Healing Touch": [RED, 'Heal wounds with a simple touch', 12],
    "Thoughtsight": [BLUE, 'Read the minds of others', 20],
    "Frost Blade": [ICE, 'Create a weapon of solid ice', 27],
    "Ethereal Grasp": [PURPLE, 'Grab objects with a magic hand',13],
    "Mage Bullet": [YELLOW, 'Fire a bullet of pure energy', 48],
    "Allspeak": [CYAN, 'Understand any language for a short time', 52],
    "Tainted Horror": [FAINT, 'Create a fear that spreads through minds like a virus',80],
    "Bloodhex": [RED, 'Any wound that bleeds will bleed forever',32],
    "Dragon's Breath": [RED, 'Unleash a powerful strand of flames',64],
}

descriptor = [
    'Enchanted',
    'Cursed',
    'Divine',
    'Gilded',
    'Old',
    'Broken',
    'Blessed',
    'Runic',
    'Ancient',
]

weapon = [
    'Cutlass',
    'Sword',
    'Shortsword', 
    'Longsword', 
    'Axe', 
    'Greataxe', 
    'Battleaxe',
    'Double-Bladed Axe', 
    'Warhammer', 
    'Mace', 
    'Morningstar', 
    'Flail', 
    'Spear', 
    'Halberd', 
    'Glaive', 
    'Dagger', 
    'Scimitar', 
    'Greatsword', 
    'Rapier', 
    'Stiletto', 
    'Broadsword', 
    'Pike'
]

weaponMaterial = [
    "Bone",
    "Iron",
    "Steel",
    "Bronze",
    "Silver",
    "Gold",
    "Dragonbone",
    "Obsidian",
    "Crystal",
    "Ebony",
    "Stone",
    "Glass",
]

# Rarity color, minimum damage, maximum damage, probability threshold, stat bonus

rarityDict = {
    "Common":[LIGHT_GREEN,1,20,0.4,5],
    "Uncommon":[BLUE,21,40,0.7,10],
    "Rare":[PURPLE,41,60,0.9,15],
    "Epic":[RED,61,80,0.99,20],
    "Legendary":[YELLOW,81,100,1.0,25],
}

stat = {
    "Attack speed": [YELLOW],
    "Maximum mana": [BLUE],
    "Maximum health": [RED],
    "Loot chance": [YELLOW],
    "Health regen": [RED],
    "Mana regen": [BLUE],
    "Critical hit chance": [CYAN],
    "Critical hit damage": [CYAN],
    "Magic resistance": [BLUE],
    "Stamina regen": [PURPLE],
    "Evasion": [YELLOW],
    "Armor penetration": [FAINT],
    "Lifesteal": [RED],
    "Movement speed": [YELLOW],
}

dmgType = {
    'Blood': [RED,'Increases critical hit chance and damage'],
    'Lightning': [YELLOW,'Initiates a chain attack through multiple enemies'],
    'Frost': [ICE,'Slows down enemy movement speed with each hit'],
    'Acid': [LIGHT_GREEN,'Deals additional corrosive damage on enemy armor'],
    'Holy': [YELLOW,'Deals additional divine damage that pierces all forms of defense'],
    'Poison': [DARK_GREEN,'Deals additional damage over time'],
    'Fire': [RED,'Sets enemies on fire for additional damage over time'],
    'Arcane': [BLUE,'Temporarily lowers all enemy stats on hit'],
}

weaponRune = {
    'Dread': [PURPLE,"Inflicts terrible fear upon enemies"],
    'Paralysis': [FAINT,"Inflicts sudden paralysis upon enemies"],
    'Lifesteal': [RED,"Heals the user for damage dealt to enemies"],
    'Rage': [RED,"Multiplies damage dealt to enemies with each hit"],
    'Shattering': [FAINT,"Increases chance to break enemy armor"],
    'Berserk': [PURPLE,"Increases attack speed by 2x after a critical hit"],
    'Blinding Light': [YELLOW,"Emits a flash of light on hit, blinding the enemy"],
    'Knowledge': [BLUE,"Increases mana for damage dealt to enemies"],
    'Bloodlust': [RED,"Increases damage dealt for damage received"],
}

armor = [
    'Cap',
    'Helmet',
    'Great Helm',

    'Shirt',
    'Tunic',
    'Chestplate',
    'Cuirass',
    'Brigandine',

    'Vambrace',
    'Gauntlets',
    'Gloves',

    'Trousers',
    'Leggings',
    'Greaves',

    'Boots',
    'Stompers',
    'Walkers',
]

armorMaterial = [
    'Leather',
    'Hide',
    'Scale Mail',
    'Bone',
    'Ring Mail',
    'Chainmail',
    'Iron',
    'Steel',
    'Dragon Scale',
]

armorRune = {
    'Protection': [RED,'Reduces all damage taken'],
    'Aegis': [BLUE,'Generates a magic shield when health drops too low'],
    'Resistance': [FAINT,'Significantly reduces knockback from hits'],
    'Permanence': [YELLOW,'Greatly increases armor durability'],
    'Warding': [PURPLE,'Increases chances to negate magic effects'],
    'Absorption': [BLUE,'Absorbs a portion of magic damage taken and converts to mana'],
    'Repelling': [FAINT,'Knocks back attackers when taking hits'],
}

# ---------------------------

people = [
    'king',
    'noble',
    'duke',
    'knight',

    'merchant',
    'hermit',
    'adventurer',
    
    'cultist',
    'priest',
    
    'captain',
    'soldier',

    'barbarian',
    'warrior',
    'rogue',
    'ranger',
    'monk',
    'paladin',
    'wizard',
    'warlock',
    'sorcerer',
    'bard',
    'druid',

    'thief',
    'mercenary',
    'bandit',
    'assassin',
    'pirate',
    
    'witch',
    'mage',
    'summoner',
    'necromancer',

    'elf',
    'dwarf',
    'goblin',
    'orc',
]


act = ['Stolen', 'Picked up', 'Looted', 'Acquired']

container = ['collection', 'stockpile', 'cache', 'chest', 'hoard', 'stash', 'corpse', 'secret safe', 'secret chest', 'hidden safe', 'hidden chest', 'hidden stash', 'secret stash', 'barrel','bag']

building = ['manor', 'inn', 'house', 'tavern', 'bandit hideout', 'store', 'tower', 'crypt', 'keep', 'dungeon', 'castle', 'mansion', 'hut', 'camp', 'outpost', 'fortress', 'prison']

trait = ['old', 'kind', 'ruthless', 'mad', 'disgraced', 'haughty', 'wanted', 'former', 'exalted', 'revered', 'hated', 'despised', 'infamous', 'famous', 'notorious', 'evil','corrupt','graceful','wise']

buildingAdjective = ['abandoned', 'dirty', 'filthy', 'rundown', 'old', 'empty', 'remote', 'faraway', 'overgrown', 'deserted']

place = ['village on a hill', 'seaside village', 'grand city', 'small town', 'small village', 'small city', 'coastal city', 'forest', 'mountain', 'desert', 'swamp', 'cave', 'ruin', 'ruins']

city = ['Imperius', 'Vellichor', 'Providence', 'Gregarious', 'Saccharine']

lore = ['kill', 'slay', 'take down', 'murder', 'assassinate']