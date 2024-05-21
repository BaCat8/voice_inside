from logger import *
from output import say, question_int


# Сделать логирование


class Enemy:
    def __init__(self, name):
        debug("Создание объекта 'Player'")
        self.name = name

    def take_damage(self, damage):
        self.health = max(self.health - damage, 0)


class Clot(Enemy):
    def __init__(self, hp=50, atk=15):
        super().__init__("Сlot")
        self.health = hp
        self.attack = atk

    def main(self):
        pass


class Player:
    def __init__(self, name):
        debug("Создание объекта 'Player'")
        self.name = name
        self.health = 100
        self.attack = 15

    def take_damage(self, damage):
        self.health = max(self.health - damage, 0)


class Master:

    @staticmethod
    def fight(player: Player, enemy: Enemy):
        tick = 2
        while tick != 0:
            debug(f"Здоровье врага: {enemy.health}")
            debug(f"Здоровье игрока: {player.health}")
            if player.health > 0 and enemy.health > 0:
                if tick % 2 == 0:
                    a = question_int("Выберите действие: 1) Атака 2) Ничего")

                    if a == 1:
                        say(f"Вы атакует с силой равной {player.attack}")
                        enemy.take_damage(player.attack)
                    elif a == 2:
                        pass
                else:
                    say(f"Противник атакует с силой равной {enemy.attack}")
                    player.take_damage(enemy.attack)
                tick += 1
            else:
                if player.health <= 0:
                    say("Вы погибли...")
                    exit()
                elif enemy.health <= 0:
                    say("Противник погиб")
                tick = 0


def demo_fight():
    player1 = Player("Игрок")
    enemy1 = Clot()
    master = Master()
    print(enemy1.name)
    master.fight(player1, enemy1)
