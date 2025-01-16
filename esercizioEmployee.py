class Employee:
    def __init__(self, name, h_pay):
        self.name = name
        self.h_pay = h_pay

    # metodo di istanza
    def calc_wage(self):
        print(f"RAL di {self.name}")
        ral = self.h_pay * 8 * 20 * 12
        return ral
    def calc_tredicesima(self):
        ral= self.h_pay * 8 * 20 * 12
        tredicesima= ral  / 12 * 0.8
        return tredicesima


    def say_hello(self):
        print(f"Ciao, sono {self.name} e prendo {self.h_pay}€ all'ora")


# Le classi Manager e Clerk sono versioni 'specializzate' della classe Employee, ma hanno le stesse caratteristiche di base e possono accedere a metodi e attributi di Employee attraverso la funzione super()

class Manager(Employee):
    yearly_bonus = 20  # variabile di classe


    def __init__(self, name, h_pay, division):
        super().__init__(name, h_pay)  # SCARICABARILE
        self.division = division
    def calc_wage(self):
      #ral base
        ral= super().calc_wage()
        tredicesima = super().calc_tredicesima()
        self.yearly_bonus = (ral * self.yearly_bonus) / 100
        totale= ral + self.yearly_bonus + tredicesima
        return totale



class Clerk(Employee):
    def __init__(self, name, h_pay, boss):
        super().__init__(name, h_pay)  # scaricabarile
        self.boss = boss

    def calc_wage(self):
            # ral base
            ral = super().calc_wage()
            tredicesima = super().calc_tredicesima()
            totale = ral  + tredicesima
            return totale


class Intern(Clerk):
    forfait = 500

    def __init__(self, name, boss):
        super().__init__(name, 0, boss)

    # override del metodo calc_wage()
    def calc_wage(self):
        ral = self.forfait * 12
        return ral


obj1 = Manager("Elon Musk", 50, "Mondo")
obj2 = Clerk("Pippo", 35, obj1)
obj3 = Intern("Povero Gabbiano", obj1)
obj1.say_hello()
obj2.say_hello()
obj3.say_hello()
print(obj1.calc_wage())
print(obj2.calc_wage())
print(obj3.calc_wage())
