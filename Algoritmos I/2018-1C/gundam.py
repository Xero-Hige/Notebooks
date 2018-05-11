class GunplaPart():

    WAIST = "Waist"
    R_ARM = "Right Arm"
    L_ARM = "Left Arm"
    CHEST = "Chest"
    HEAD = "Head"
    BACKPACK = "Backpack"

    def __init__(self,name,part_type,size=0,weight=50,armor=0):
        self.name = name
        self.part_type = part_type
        self.size = size
        self.weight = weight
        self.armor = armor

    def get_part_name(self):
        return self.name

    def get_weight(self):
        return self.weight

    def get_part_type(self):
        return self.part_type

    def get_size(self):
        return self.size

    def get_armor(self):
        return self.armor

    def get_hitpoints(self):
        return 3*self.size*self.weight + 1.5 * self.armor

    def __repr__(self):
        return (f"Gunpla Part: {self.name} <({self.part_type})>"
                f"\n\t Size: {self.size}"
                f"\n\t Armor: {self.armor}"
                f"\n\t Hitpoints: {self.get_hitpoints()}"
                f"\n\t Weight: {self.weight}")

    def __str__ (self):
        return f"Gunpla Part: {self.name} <({self.part_type})>"

import random import randint,random,choice

class Gun():

    def __init__(self,name,rounds=0,damage_per_shot=0):

        self.name = name
        self.rounds = rounds
        self.damage_per_shot = damage_per_shot

    def atack(self,gundam):
        damage = 0

        for _ in range(randint(0,self.rounds+1)):
            damage += self.damage_per_shot * (1 if random() > 0.15 else 1.5)

        gundam.receive_damage(damage)


class BeamSaber(object):

    def __init__(self,name,damage=0):

        self.name = name
        self.damage = damage

    def atack(self,gundam):
        damage = 0

        for _ in range(randint(1,4)):
            damage += self.damage * choice([1,1.5])

        gundam.receive_damage(damage)
