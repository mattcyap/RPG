#  File: RPG.py
#  Description: Simulate Combat between 2 Fantasy characters.
#  Student's Name: Matthew Yap
#  Student's UT EID: my5476
#  Course Name: CS 313E 
#  Unique Number: 51470
#
#  Date Created: 9/20/2017
#  Date Last Modified: 9/21/2017

#   class defines all the weapons possible for wielding
class Weapon:

    #   initializing the different weapons atk values
    def __init__(self, x):
        self.hand = x
        self.dmg = 1

        if x == "dagger":
            self.dmg = 4
        elif x == "axe":
            self.dmg = 6
        elif x == "staff":
            self.dmg = 6
        elif x == "sword":
            self.dmg = 10
        elif x == "none":
            self.dmg = 1

#   class defines all the armors possible for wearing
class Armor:

    #   initializing the different armors def values
    def __init__(self, x):
        self.body = x

        self.df = 10

        if x == "plate":
            self.df = 2
        elif x == "chain":
            self.df = 5
        elif x == "leather":
            self.df = 8
        elif x == "none":
            self.df = 10

#   class defines the characters and what actions they can perform
class RPGCharacter:

    #   lets a character equip a weapon
    def wield(self, new_Weapon):
        #   checks whether it is a weapon too heavy for certain classes
        if new_Weapon.hand == ("sword" or "axe"):
            #   checks whether the character is a class that cannot hold heavy weapons
            if self.start_sp > 0:
                print("Weapon not allowed for this character class.")
            else:
                self.hand = new_Weapon.hand

                if self.hand == "dagger":
                    self.dmg = 4
                elif self.hand == "axe":
                    self.dmg = 6
                elif self.hand == "staff":
                    self.dmg = 6
                elif self.hand == "sword":
                    self.dmg = 10
                elif self.hand == "none":
                    self.dmg = 1
        
                print(self.name, "is now wielding a(n)", self.hand)
        else:
            self.hand = new_Weapon.hand

            if self.hand == "dagger":
                self.dmg = 4
            elif self.hand == "axe":
                self.dmg = 6
            elif self.hand == "staff":
                self.dmg = 6
            elif self.hand == "sword":
                self.dmg = 10
            elif self.hand == "none":
                self.dmg = 1
        
            print(self.name, "is now wielding a(n)", self.hand)

    #   lets a character unequip a weapon 
    def unwield(self):

        self.hand = "none"
        self.dmg = 1

        print(self.name, "is no longer wielding anything.")

    #   lets a charcter put on a set of armor
    def putOnArmor(self, new_Armor):

        #   checks if the armor is heavy
        if self.start_sp > 0:
            print("Armor not allowed for this character class.")

        else:            

            self.body = new_Armor.body

            if self.body == "plate":
                self.df = 2
            elif self.body == "chain":
                self.df = 5
            elif self.body == "leather":
                self.df = 8
            elif self.body == "none":
                self.df = 10

            print(self.name, "is now wearing", self.body)

    #   lets characters take off armor
    def takeOffArmor(self):
        self.body = "none"
        self.df = 10
        print(self.name, "is no longer wearing anything.")

    #   lets a character attack another character
    def fight(self, enemy):
        print(self.name, "attacks", enemy.name, "with a(n)", self.hand)
        enemy.hp = enemy.hp - self.dmg
        print(self.name, "does", self.dmg, "damage to", enemy.name)
        print(enemy.name, "is now down to", enemy.hp, "health")
        enemy.checkForDefeat()
        
    #   lets a character cast a spell
    def castSpell(self, spell, enemy):
        self.spell = spell

        #   figures out which spell is being casted
        if self.spell == "Fireball":
            if self.sp >= 3:
                print(self.name, "casts Fireball at", enemy.name)
                self.sp = self.sp - 3
                enemy.hp = enemy.hp - 5
                print(self.name, "does 5 damage to", enemy.name)
                print(enemy.name, "is now down to", enemy.hp, "health")
                enemy.checkForDefeat()
            else:
                print("Insufficient spell points")
        elif self.spell == "Lightning Bolt":
            if self.sp >= 10:
                print(self.name, "casts LightningBolt at", enemy.name)
                self.sp = self.sp - 10
                enemy.hp = enemy.hp - 10
                print(self.name, "does 10 damage to", enemy.name)
                print(enemy.name, "is now down to", enemy.hp, "health")
                enemy.checkForDefeat()
            else:
                print("Insufficient spell points")
        elif self.spell == "Heal":
            if self.sp >= ((self.max_hp - self.hp) or 6):
                print(self.name, "casts Heal at", enemy.name)
                if (enemy.max_hp - enemy.hp) < 6:
                    self.sp = self.sp - (enemy.max_hp - enemy.hp)
                    enemy.hp = enemy.max_hp
                    print(self.name, "heals", enemy.name, "for", (enemy.max_hp - enemy.hp), "health points.")
                    print(enemy.name, "is now at", enemy.hp, "health")
                else:
                    enemy.hp = enemy.hp + 6
                    self.sp = self.sp - 6
                    print(self.name, "heals", enemy.name, "for 6 health points.")
                    print(enemy.name, "is now at", enemy.hp, "health")
        else:
            print("Unknown spell name. Spell failed.")

    #   checks to see if a character is defeated
    def checkForDefeat(enemy):
        if enemy.hp <= 0:
            print(enemy.name, "has been defeated!")
                
#   subclass that allows for the fighter class
class Fighter(RPGCharacter):

    #   initializes the stats for a fighter
    def __init__(self, name):
        self.name = name
        self.hp = 40
        self.max_hp = 40
        self.sp = 0
        self.start_sp = 0
        self.hand = "none"
        self.dmg = 1
        self.body = "none"
        self.df = 10

    def __str__(self):
        return str("\n"+self.name+"\n"+"  Current Health: "+str(self.hp)+"\n"+"  Current Spell Points: "+ str(self.sp)+"\n"+"  Wielding: "+str(self.hand)+"\n"+"  Wearing: "+str(self.body)+"\n"+"  Armor class: "+str(self.df)+"\n")
        
#   subclass that allows for the wizard
class Wizard(RPGCharacter):

    #   initializes the stats for a wizard
    def __init__(self, name):
        self.name = name
        self.hp = 16
        self.max_hp = 16
        self.sp = 20
        self.start_sp = 20
        self.hand = "none"
        self.dmg = 1
        self.body = "none"
        self.df = 10

    def __str__(self):
        return str("\n"+self.name+"\n"+"  Current Health: "+str(self.hp)+"\n"+"  Current Spell Points: "+ str(self.sp)+"\n"+"  Wielding: "+str(self.hand)+"\n"+"  Wearing: "+str(self.body)+"\n"+"  Armor class: "+str(self.df)+"\n")
        

def main():

    plateMail = Armor("plate")
    chainMail = Armor("chain")
    sword = Weapon("sword")
    staff = Weapon("staff")
    axe = Weapon("axe")

    gandalf = Wizard("Gandalf the Grey")
    gandalf.wield(staff)
    
    aragorn = Fighter("Aragorn")
    aragorn.putOnArmor(plateMail)
    aragorn.wield(axe)
    
    print(gandalf)
    print(aragorn)

    gandalf.castSpell("Fireball",aragorn)
    aragorn.fight(gandalf)

    print(gandalf)
    print(aragorn)
    
    gandalf.castSpell("Lightning Bolt",aragorn)
    aragorn.wield(sword)

    print(gandalf)
    print(aragorn)

    gandalf.castSpell("Heal",gandalf)
    aragorn.fight(gandalf)

    gandalf.fight(aragorn)
    aragorn.fight(gandalf)

    print(gandalf)
    print(aragorn)


main()
