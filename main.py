"""
Zombiola Simulation

@ author Noah Klaus
@ version 1.0
"""

class Scientist(object):
    def __init__(self, _ID, _health, _fieldOfStudy):
        self.ID = _ID
        self.health = _health
        self.x = 0
        self.y = 0
        self.fieldOfStudy = _fieldOfStudy
        self.hunger = 0

    def Consume(self):
        print("A Scientist Cannot Consume...")

    def Walk(self):
        print("A Scientist Cannot Walk...")

    def Attack(self):
        print("A Scientist Cannot Attack...")


class Susceptible(Scientist):
    # MUST IMPLEMENT ATTRIBUTES OF
    # 1.) BuildingMaterials

    def Consume(self):
        print("Susceptible: " + str(self.ID) + " consumes " + "<?what was consumed?>")

    def Walk(self):
        print("Susceptible: " + str(self.ID) + " walks " + "<?how far?>")

    def Attack(self):
        print("Susceptible: " + str(self.ID) + " attacked " + "<?what was attacked?>")

    def Starve(self):
        print("Susceptible: " + str(self.ID) + " starved to death.")

    def BuildShelter(self):
        print("Susceptible: " + str(self.ID) + " builds shelter.")

    def GatherMaterials(self):
        print("Susceptible: " + str(self.ID) + " gathers materials.")

    def GatherFood(self):
        print("Susceptible: " + str(self.ID) + " gathers food.")

    def PerformExperiment(self):
        print("Susceptible: " + str(self.ID) + " performs experiment.")

    def HelpBuildBoat(self):
        print("Susceptible: " + str(self.ID) + " helps build the boat.")

    def SubmissiveAndBreedable(self):
        print(f"{self.ID} is Submissive and Breedable")



class Infected(Susceptible):
    # MUST IMPLEMENT ATTRIBUTES OF
    # 1.) Time Infected
    # 2.) Hunger

    def Consume(self):
        print("Infected: " + str(self.ID) + " consumes " + "<?who/what was consumed?>")

    def Walk(self):
        print("Infected: " + str(self.ID) + " walks " + "<?moves how much?>")

    def Attack(self):
        print("Infected: " + str(self.ID) + " attacks " + "<?who was attacked?>")

    def TimeInfected(self):
        print("Infected: " + str(self.ID) + " has been infected for " + "<?how long?>")


class Mutated(Infected):
    # MUST IMPLEMENT ATTRIBUTES OF
    # 1.) Mutation

    def Consume(self):
        print("Mutated: " + str(self.ID) + " consumes " + "<?who/what was consumed?>")

    def Walk(self):
        print("Mutated: " + str(self.ID) + " walks " + "<?moves how much?>")

    def Attack(self):
        print("Mutated: " + str(self.ID) + " attacks " + "<?who was attacked?>")

class Recovered(Infected):
    # MUST IMPLEMENT ATTRIBUTES OF
    # 1.) BuildingMaterials
    # 2.) Immune
    # 3.) BuildingMaterials

    def Consume(self):
        print("Recovered: " + str(self.ID) + " consumes " + "<?what was consumed?>")

    def Walk(self):
        print("Recovered: " + str(self.ID) + " walks " + "<?how far?>")

    def Attack(self):
        print("Recovered: " + str(self.ID) + " attacked " + "<?what was attacked?>")

    def Starve(self):
        print("Recovered: " + str(self.ID) + " starved to death.")

    def BuildShelter(self):
        print("Recovered: " + str(self.ID) + " builds shelter.")

    def GatherMaterials(self):
        print("Recovered: " + str(self.ID) + " gathers materials.")

    def GatherFood(self):
        print("Recovered: " + str(self.ID) + " gathers food.")

    def PerformExperiment(self):
        print("Recovered: " + str(self.ID) + " performs experiment.")

    def HelpBuildBoat(self):
        print("Recovered: " + str(self.ID) + " helps build the boat.")


class Dead(object):
    # ATTRIBUTES TO ADD
    # 1.) Date of Death

    def Consume(self):
        print("Dead people cannot consume")

    def Walk(self):
        print("Dead cannot walk")

    def Attack(self):
        print("Dead cannot attack")
