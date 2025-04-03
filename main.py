import random
import sys
import os
import termios
import fcntl
from os import system as system
from time import sleep as sleep
from colors import *
from lists import *

def ignore_keyboard():
    fd = sys.stdin.fileno()
    oldterm = termios.tcgetattr(fd)
    newattr = termios.tcgetattr(fd)
    newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
    termios.tcsetattr(fd, termios.TCSANOW, newattr)
    oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
    fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)
    return oldterm, oldflags, fd

def restore_keyboard(oldterm, oldflags, fd):
    termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
    fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)

def rarityFunc():
    global dmgTypeSwitch, statCount, rarityProb, rarity, rarityColor, dmgBase, statBase
    dmgTypeSwitch = []

    rarityProb = random.random()
    for type, details in rarityDict.items():
        color, range1, range2, threshold, statBase = details

        if rarityProb <= threshold:
            rarity = type
            rarityColor = color
            dmgBase = random.randint(range1, range2)
            break

    if rarityProb > 0.9:
        dmgTypeSwitch = True
        statCount = random.randint(1, 4)
    elif rarityProb <= 0.9:
        statCount = random.randint(1, 2)

    if statCount == 0:
        end = ''
    else:
        end = '\n'

    print(f'Rarity: {rarityColor}{rarity}{DEFAULT}{end}')

def dmgTypeFunc():
    global damageType, damageColor, dmgBonus

    damageType = random.choice(list(dmgType.keys()))
    damageColor = dmgType[damageType][0]
    damageDesc = dmgType[damageType][1]
    dmgBonus = f'{damageColor}+{random.randint(10, 30)}{DEFAULT}'

    if dmgTypeSwitch == True:
        print(f"Damage: {dmgBase} {dmgBonus}")
        print(f"Damage Type: {damageColor}{damageType}*{DEFAULT}")
        print(f'{damageColor}{ITALIC}*{damageDesc}.{DEFAULT}\n')
    else:
        print(f"Damage: {dmgBase}\n")

def statPrint(n): 
    global statPastList

    n = min(n, len(stat))
    randomStats = random.sample(list(stat.keys()), n)
    statPastList = []

    for randomStat in randomStats:
        statColor = stat[randomStat][0]
        statNum = statBase + random.randint(1, 20)
        statPastList.append(f'+{statNum} {statColor}{ITALIC}{randomStat}{DEFAULT}')
        print(f'+{statNum} {statColor}{ITALIC}{randomStat}{DEFAULT}')

    return '\n'.join(statPastList)

def runePrint(dct, n):
    global color, desc, runePastList, runeStr
    runePastList = []
    runeStr = ''

    n = min(n, len(dct))
    randomRunes = random.sample(list(dct.keys()), n)

    for runes in randomRunes:
        color = dct[runes][0]
        desc = dct[runes][1]

        print(f'\n{ITALIC}Engraved with a {color}{ITALIC}Rune of {runes}*{DEFAULT}.')
        print(f'{color}{ITALIC}*{desc}.{DEFAULT}')
        runePastList.append(f'{color}{ITALIC}{runes}{DEFAULT}')
        runeStr = f"{FAINT}{ITALIC}Runes: {DEFAULT}{', '.join(runePastList)}"

    return runeStr

def prefixGeneration(material):

    materialPrefix = random.choice(material)
    adjectivePrefix = random.choice(descriptor)
    person = random.choice(people)
    personPrefix = f"{person[0].upper() + person[1:]}'s"

    prefixType = [
        materialPrefix,
        adjectivePrefix,
        personPrefix,
    ]

    prefixCombo = [
        random.choice(prefixType),
        f"{adjectivePrefix} {materialPrefix}",
        f"{personPrefix} {materialPrefix}",
        f"{personPrefix} {adjectivePrefix} {materialPrefix}"
    ]

    prefix = random.choice(prefixCombo)
    return prefix

def weaponGeneration():
    weaponGen = random.choice(weapon)
    weaponName = f"{prefixGeneration(weaponMaterial)} {weaponGen}"

    print(f'{BOLD}{weaponName}{DEFAULT}\n')
    rarityFunc()
    dmgTypeFunc()
    stats = statPrint(statCount)
    runes = runePrint(weaponRune, random.randint(0, 2))

    if dmgTypeSwitch == True:
        name = f"{weaponName} of {damageColor}{damageType} Damage{DEFAULT}"
        damage = f"{dmgBase} {damageColor}{dmgBonus}{DEFAULT}"
    else:
        name = f"{weaponName}"
        damage = dmgBase

    details = f"Damage: {damage}"

    if stats:
        details += f"\n{stats}"
    if runes:
        details += f"\n{runes}"

    pastGen.append({
        "name": f'{rarityColor}{rarity}{DEFAULT} {name}',
        "details": details.strip(),
        "custom_name": None
    })

def armorGeneration():
    armorGen = random.choice(armor)
    armorName = f'{prefixGeneration(armorMaterial)} {armorGen}'
    print(f'{BOLD}{armorName}{DEFAULT}\n')
    rarityFunc()
    armorRuneProb = random.random()

    stats = statPrint(statCount)
    runes = runePrint(armorRune, random.randint(0, 2))

    details = ""
    if stats:
        details += f"\n{stats}"
    if runes:
        details += f"\n{runes}"

    pastGen.append({
        "name": f"{rarityColor}{rarity}{DEFAULT} {armorName}",
        "details": details.strip(),
        "custom_name": None
    })

def spellGeneration():
    spellGen = random.choice(list(spell.keys()))

    color = spell[spellGen][0]
    desc = spell[spellGen][1]
    cost = spell[spellGen][2]

    name = f'Scroll of {spellGen}{DEFAULT}'
    mana = f'Mana Cost: {BLUE}{cost}{DEFAULT}'

    print(f'{BOLD}{name}\n')
    print(f'{mana}\n')
    print(f'{color}{ITALIC}{desc}.{DEFAULT}')
    pastGen.append({
        "name": color + name + DEFAULT,
        "details": mana,
        "custom_name": None
    })

def potionStrength():
    global strengthBonus, strengthType
    strength = {
        'Strong': [10, 15],
        'Mild': [5, 10],
        'Weak': [1, 5],
    }
    strengthType = random.choice(list(strength.keys()))
    strengthBonus = random.randint(strength[strengthType][0], strength[strengthType][1])

def potionGeneration():
    potionStrength()

    potionGen = random.choice(list(potion.keys()))

    color = potion[potionGen][0]
    desc = potion[potionGen][1]
    time = potion[potionGen][2]

    nameType = [
        f'Potion of {potionGen}',
        f'{potionGen} Potion',
    ]

    def contains_space(input_string):
        return ' ' in input_string

    if contains_space(potionGen):
        name = potionGen
    else:
        name = random.choice(nameType)

    if time == "Instant":
        duration = f"Duration: {time}"
    else:
        time = time + strengthBonus
        duration = f'Duration: {time} minutes'

    print(f'{BOLD}{strengthType} {name}{DEFAULT}\n')
    print(f'{duration}\n')
    print(f'{color}{ITALIC}{desc}.{DEFAULT}')
    pastGen.append({
        "name": f"{color}{strengthType} {name}{DEFAULT}",
        "details": duration,
        "custom_name": None
    })


def correct_text(text: str) -> str: 
    words = text.split() 
    for i in range(len(words) - 1):
        if words[i].lower() == 'a' and words[i + 1][0].lower() in 'aeiou': 
            words[i] = 'an' 
    return ' '.join(words)

def loreGeneration():
    loreContainer = random.choice(container)
    loreAdjective = random.choice(adjective)
    loreBuilding = random.choice(building)
    lorePlace = random.choice(place)
    loreTrait = random.choice(trait)
    lorePeople = random.choice(people)
    lorePerson = loreTrait + " " + lorePeople
    
    loreLocationType = random.choice(["person", "container"])
    if loreLocationType == "person":
        loreVerb = random.choice(verb[:4]) + " from a"
        loreGen = f"{loreVerb} {lorePerson} in a {loreAdjective} {lorePlace}"
    else:
        loreVerb = random.choice(verb[4:]) + " in a"
        loreGen = f"{loreVerb} {loreContainer} in a {loreAdjective} {loreBuilding}"
    
    print(f"\n{ITALIC}{correct_text(loreGen)}.{DEFAULT}")

# -------------------------------

def sysMessage(color,text,time=None):
    if time is not None:
        wait = time
    else:
        wait = 1
    print(f'\n{color}{text}{DEFAULT}')
    sleep(wait)
    system('clear')

def renameItem(item=None):
    custom_name = input("\nEnter a custom name for this item: ")
    if item is not None:
        original_name = pastGen[item]["name"]
    else:
        original_name = pastGen[-1]["name"]

    if "Scroll of" or "Potion" in original_name:
        renamed_display = f"{custom_name}\n{original_name}"
    else:
        renamed_display = custom_name

    if item is not None:
        pastGen[item]["custom_name"] = renamed_display
    else:
        pastGen[-1]["custom_name"] = renamed_display

    sleep(0.1)
    sysMessage(LIGHT_GREEN, 'Item named successfully.')

def handleDeletion(user_input):

    try:
        parts = user_input.split()[1].replace(' ', '')
        indices = set()

        def add_range(start, end):
            if start > end or start < 1 or end > len(pastGen):
                raise ValueError(f"Invalid range, {end} too high.")
            indices.update(range(start - 1, end))

        for part in parts.split(','):
            if '-' in part:
                start, end = map(int, part.split('-'))
                add_range(start, end)
            else:
                item_index = int(part) - 1
                if item_index < 0 or item_index >= len(pastGen):
                    raise ValueError(f"Invalid item number: {part}")
                indices.add(item_index)

        confirmDeletion = input(RED + "\nAre you sure you want to delete this? Type 'Yes' or 'No': " + DEFAULT)

        if confirmDeletion.lower() == 'yes':
            for index in sorted(indices, reverse=True):
                pastGen.pop(index)
            sysMessage(LIGHT_GREEN, 'Deleted successfully.')
        elif confirmDeletion.lower() == 'no':
            sysMessage(LIGHT_GREEN, 'Canceled.')
            pastList()
        else:
            sysMessage(RED, 'Invalid input. Please enter "Yes" or "No".')
            pastList()

    except (IndexError, ValueError) as e:
        error_message = str(e) if "Invalid" in str(e) else 'Invalid input. Use "Delete <number(s)>".'
        sysMessage(RED, error_message)

def handleRenaming(user_input):
    try:
        index = int(user_input.split()[1]) - 1
        if 0 <= index < len(pastGen):
            renameItem(index)
        else:
            num = user_input.split()[1]
            sysMessage(RED, f'Invalid item number: {num}')
    except (IndexError, ValueError):
        sysMessage(RED, 'Invalid input. Use "rename <number>".')

def pastListDisplay():
    print(f"{BOLD}{UNDERLINE}Generated Loot{DEFAULT}:\n")
    for i, loot in enumerate(pastGen, start=1):
        name_display = loot["custom_name"] if loot["custom_name"] else loot["name"]
        print(f'[{i}] - {name_display}\n{loot["details"]}\n')

def pastList():
    system('clear')
    sleep(0.1)
    pastListDisplay()

    while True:
        user_input = input('[ENTER] to keep generating loot.\n\'Clear\' to clear generated loot\n\'Delete <number(s) or range>\' to delete item(s)\n\'Rename <number>\' to rename an item\n\n: ')
        if user_input.lower() == 'clear':
            clearConfirmation = input(RED + "\nAre you sure you want to clear generated loot? Type 'Yes' or 'No': " + DEFAULT)
            if clearConfirmation.lower() == 'yes':
                pastGen.clear()
                system('clear')
                enterPrompt()
                break
            elif clearConfirmation.lower() == 'no':
                pastListDisplay()
        elif user_input.lower().startswith('delete'):
            handleDeletion(user_input)
            pastListDisplay()
        elif user_input.lower().startswith('rename'):
            handleRenaming(user_input)
            pastListDisplay()
        elif user_input == '':
            generate()
            break
        else:
            sysMessage(RED, 'Invalid input.')
            pastListDisplay()

def generate():
    system('clear')
    sleep(0.1)
    random.choice(genTypes)()
    loreGeneration()

displayEnter = '\nPress [ENTER] to generate loot.'

def enterPrompt():
    global first_item_generated
    first_item_generated = False
    while not first_item_generated:
        user_input = input(f'{displayEnter}\n\n: ')
        if user_input == "":
            oldterm, oldflags, fd = ignore_keyboard()
            generate()
            restore_keyboard(oldterm, oldflags, fd)
            first_item_generated = True
        else:
            sysMessage(RED, 'Invalid input.')

def main_prompt():
    return input(f'{displayEnter}\n(P) to see generated loot\n(N) to name this item\n\n: ').lower()

# --------------------------------------------

pastGen = []
genTypes = [
    weaponGeneration,
    armorGeneration,
    spellGeneration,
    potionGeneration,
]
system('clear')
enterPrompt()
while True:
    user_input = main_prompt() if first_item_generated else enterPrompt()

    if user_input == '':
        oldterm, oldflags, fd = ignore_keyboard()
        generate()
        restore_keyboard(oldterm, oldflags, fd)
        first_item_generated = True
    elif user_input == 'p' and first_item_generated:
        pastList()
    elif user_input == 'n' and first_item_generated:
        renameItem()
        pastList()
    else:
        sysMessage(RED, 'Invalid input.')
        enterPrompt()