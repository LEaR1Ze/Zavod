
class Zavod:
    def __init__(self, name, color, type):
        self.name = name
        self.color = color
        self.type = type

    def SiroyPodpivaas(self):
        print("Закупаєм сировину")

    def ZshutuyPodpivaas(self):
        print("Шиєм")
    
    def PofarbovanuyPodpivaas(self):
        print("Фарбуєм")

class igrashka(Zavod):
    def borov(self):
        return ("Створенна іграшка з іменем {}, кольором {} та типом {}").format(self.name,self.color,self.type)

igrashka1 = igrashka("Подпівас","Зелений","Тварина")
igrashka1.SiroyPodpivaas()
igrashka1.ZshutuyPodpivaas()
igrashka1.PofarbovanuyPodpivaas()

print(igrashka1.borov())



