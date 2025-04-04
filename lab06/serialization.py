## yerr yerr

class Item:
    def __init__(self, name, summary='', rarity='common'):
        self.name = name
        self.summary = summary
        self.rarity = rarity
        self._ownership = ''

    def pick_up(self, character: str):
        self._ownership = character
        return f"{self.name} is in the name of {character}."
    
    def throw_away(self):
        self._ownership = ''
        return f"{self.name} is trashed!"
    
    def use(self):
        if not self._ownership:
            return "No Output"
        return f"{self.name} is used."
    
    def __str__(self):
        return f"{self.name} {self.rarity} - {self.summary}"
    
class Weapon(Item):
    def __init__(self, name, damage, weapon_type, summary='', rarity='common'):
        super().__init__(name, summary, rarity)
        self.damage = damage
        self.weapon_type = weapon_type
        self.attack_modifier = 1.15 if rarity == 'legendary' else 1.0
        self.equipped = False

    def equip(self):
        if not self._ownership:
            return "NO OUTPUT"
        self.equipped = True
        return f"{self.name} is equipped by {self._ownership}."
   
    def use(self):
        if not self.equipped:
            return "NO OUTPUT"
        return f"{self.name} is used, dealing {round(self.damage * self.attack_modifier)} damage."

class Shield(Item):
    def __init__(self, name, defense, broken=False, description='', rarity='common'):
        super().__init__(name, summary='', rarity='')
        self.defense = defense
        self.broken = broken
        self.defense_modifier = 1.10 if rarity == 'legendary' else 1.0
        self.equipped = False

    def equip(self):
        if not self._ownership:
            return "NO OUTPUT"
        self.equipped = True
        return f"{self.name} is equipped by {self._ownership}."
   
    def use(self):
        if not self.equipped:
            return "NO OUTPUT"
        modifier = 0.5 if self.broken else 1.0
        return f"{self.name} is used, blocking {round(self.defense * self.defense_modifier * modifier)} damage."

class Potion(Item):
    def __init__(self, name, potion_type, value, effective_time=0, summary
                 ='', rarity='common'):
        super().__init__(name, summary, rarity)
        self.potion_type = potion_type
        self.value = value
        self.effective_time = effective_time
        self.used = False
   
    def use(self):
        if not self._ownership or self.used:
            return "NO OUTPUT"
        self.used = True
        return f"{self._ownership} used {self.name}, and {self.potion_type} increased by {self.value} for {self.effective_time}s."
   
    @classmethod
    def from_ability(cls, name, owner, potion_type):
        potion = cls(name, potion_type, value=50, effective_time=30, rarity='common')
        potion.pick_up(owner)
        return potion

# Example Usage
if __name__ == "__main__":
    sword = Weapon(name='Chipotle', damage=100, weapon_type='sword', rarity='legendary')
    print(sword.pick_up('Normak'))
    print(sword.equip())
    print(sword.use())
   
    shield = Shield(name='CapMerica', defense=50, broken=False, rarity='epic')
    print(shield.pick_up('Yerr'))
    print(shield.equip())
    print(shield.use())
   
    potion = Potion.from_ability(name='Power Boost', owner='Kam', potion_type='attack')
    print(potion)
    print(potion.use())
    print(potion.use())

class Item:
    def __init__(self, name, description='', rarity='common'):
        self.name = name
        self.description = description
        self.rarity = rarity
        self._ownership = ''

    def pick_up(self, character: str):
        self._ownership = character
        return f"{self.name} is now owned by {character}."
   
    def throw_away(self):
        self._ownership = ''
        return f"{self.name} is thrown away."
   
    def use(self):
        if not self._ownership:
            return "NO OUTPUT"
        return f"{self.name} is used."

    def __str__(self):
        return f"{self.name} ({self.rarity}) - {self.description}"

class Weapon(Item):
    def __init__(self, name, damage, weapon_type, summary='', rarity='common'):
        super().__init__(name, summary, rarity)
        self.damage = damage
        self.weapon_type = weapon_type
        self.attack_modifier = 1.15 if rarity == 'legendary' else 1.0
        self.equipped = False

    def equip(self):
        if not self._ownership:
            return "NO OUTPUT"
        self.equipped = True
        return f"{self.name} is equipped by {self._ownership}."
   
    def use(self):
        if not self.equipped:
            return "NO OUTPUT"
        return f"{self.name} is used, dealing {round(self.damage * self.attack_modifier)} damage."

class Shield(Item):
    def __init__(self, name, defense, broken=False, summary='', rarity='common'):
        super().__init__(name, summary, rarity)
        self.defense = defense
        self.broken = broken
        self.defense_modifier = 1.30 if rarity == 'legendary' else 1.0
        self.equipped = False

    def equip(self):
        if not self._ownership:
            return "NO OUTPUT"
        self.equipped = True
        return f"{self.name} is equipped by {self._ownership}."
   
    def use(self):
        if not self.equipped:
            return "NO OUTPUT"
        modifier = 0.5 if self.broken else 1.0
        return f"{self.name} is used, blocking {round(self.defense * self.defense_modifier * modifier)} damage."

class Potion(Item):
    def __init__(self, name, potion_type, value, effective_time=0, summary='', rarity='common'):
        super().__init__(name, summary, rarity)
        self.potion_type = potion_type
        self.value = value
        self.effective_time = effective_time
        self.used = False
   
    def use(self):
        if not self._ownership or self.used:
            return "NO OUTPUT"
        self.used = True
        return f"{self._ownership} used {self.name}, and {self.potion_type} increased by {self.value} for {self.effective_time}s."
   
    @classmethod
    def from_ability(cls, name, owner, potion_type):
        potion = cls(name, potion_type, value=50, effective_time=30, rarity='common')
        potion.pick_up(owner)
        return potion
    
class Item:
    def __init__(self, name, legendary=False):
        self.name = name
        self.legendary = legendary
    
    def __str__(self):
        if self.legendary:
            return f"*** LEGENDARY ITEM: {self.name} ***"
        return f"Item: {self.name}"

class Weapon(Item):
    def __init__(self, name, damage, legendary=False):
        super().__init__(name, legendary)
        self.damage = damage
    
    def attack_move(self):
        return "Basic attack!"
    
    def __str__(self):
        return f"Weapon: {self.name}, Damage: {self.damage}" + (" (LEGENDARY)" if self.legendary else "")

class OneHandedWeapon(Weapon):
    def attack_move(self):
        return "Quick Slash!"

class TwoHandedWeapon(Weapon):
    def attack_move(self):
        return "Powerful Swing!"

class Pike(Weapon):
    def attack_move(self):
        return "Thrusts forward!"

class RangeWeapon(Weapon):
    def attack_move(self):
        return "Projectiles Incoming HEEEE!"

class Inventory:
    def __init__(self, owner=None):
        self.owner = owner
        self.items = []

    def add_item(self, item):
        self.items.append(item)
    
    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
    
    def view(self):
        for item in self.items:
            print(item)


## Examples 

mastery_sword = OneHandedWeapon("Mastery Sword", 310, legendary=True)
osama = TwoHandedWeapon("Osama", 550, legendary=True)
normak = Pike("Normak", 295, legendary=True)
jfk = RangeWeapon("JFK", 510, legendary=True)

## inventory
kam_backpack = Inventory(owner="kam")

## view inventory
kam_backpack.view()

## add items
kam_backpack.add_item(jfk)


import json

class Item:
    def to_json(self):
        raise NotImplementedError("Subclasses should add this method.")

class Weapon(Item):
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def to_json(self):
        return {
            'type': 'weapon',
            'name': self.name,
            'damage': self.damage
        }

class Potion(Item):
    def __init__(self, name, healing):
        self.name = name
        self.healing = healing

    def to_json(self):
        return {
            'type': 'potion',
            'name': self.name,
            'healing': self.healing
        }

class Shield(Item):
    def __init__(self, name, defense):
        self.name = name
        self.defense = defense

    def to_json(self):
        return {
            'type': 'shield',
            'name': self.name,
            'defense': self.defense
        }

class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

def to_json(self):
        """
        converts the inventory object into a JSON dictionary.
        
        Returns:
            dict: A JSON representation of the Inventinventoryory and its items.
        """
        return {
            'inventory': [item.to_json() for item in self.items]
        }

def inventory_json_encoder(obj):
    if isinstance(obj, Inventory):
        return obj.to_json()
    elif isinstance(obj, Item):
        return obj.to_json()
    raise TypeError(f"Object of type {obj.__class__.__name__} is not JSON serializable.")

inventory = Inventory()
inventory.add_item(Weapon("Sword", 50))
inventory.add_item(Potion("Health Potion", 30))
inventory.add_item(Shield("Iron Shield", 25))

# serialize inventory
with open('inventory.json', 'w') as f:
    json.dump(inventory, f, default=inventory_json_encoder, indent=4)

class Weapon(Item):
    @classmethod
    def from_json(cls, data):
        return cls(name=data['name'], damage=data['damage'])

class Potion(Item):
    @classmethod
    def from_json(cls, data):
        return cls(name=data['name'], healing=data['healing'])

class Shield(Item):
    @classmethod
    def from_json(cls, data):
        return cls(name=data['name'], defense=data['defense'])

class Inventory:
    @classmethod
    def from_json(cls, data):
        inventory = cls()
        for item_data in data['inventory']:
            if item_data['type'] == 'weapon':
                inventory.add_item(Weapon.from_json(item_data))
            elif item_data['type'] == 'potion':
                inventory.add_item(Potion.from_json(item_data))
            elif item_data['type'] == 'shield':
                inventory.add_item(Shield.from_json(item_data))
        return inventory

# Deserialization example
with open('inventory.json', 'r') as f:
    data = json.load(f)
    restored_inventory = Inventory.from_json(data)

# Check the restored inventory
for item in restored_inventory.items:
    print(f"Item: {item.name}, Type: {item.__class__.__name__}")

## yee


