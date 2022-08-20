
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

class igrashka_prostaya(Zavod):
    def borovizacia(self):
        print("Створенна іграшка з іменем {}, кольором {} та типом {}".format(self.name,self.color,self.type))


class neo_borov(Zavod):
    def borovizacia(self):
        print("Створенна іграшка з іменем {}, кольором {} та типом {} ".format(self.name,self.color,self.type))

class svin(Zavod):
    def borovizacia(self):
        print("Створенна іграшка з іменем {}, кольором {} та типом {} ".format(self.name,self.color,self.type))

    

igrashkai =[
svin("Джеракс","Зелений","Проста іграшка"),
neo_borov("Нотеіл","Чорний","Нео боров"),
svin ("Топсон","Блакитний","Модифікована іграшка")
]

for igrashka1 in igrashkai:
    igrashka1.SiroyPodpivaas()
    igrashka1.ZshutuyPodpivaas()
    igrashka1.PofarbovanuyPodpivaas()
    igrashka1.borovizacia()

