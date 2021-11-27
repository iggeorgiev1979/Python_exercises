# import sys
# sys.path.append(".")
from unittest import TestCase, main
from project.hero import Hero


class TestHero(TestCase):
    def setUp(self):
        self.hero = Hero(username="Ivan", level=10, health=50, damage=30)
        self.enemy_hero = Hero(username="Petko", level=10, health=40, damage=20)
    
    def test_constructor(self):
        self.assertEqual("Ivan", self.hero.username)
        self.assertEqual(10, self.hero.level)
        self.assertEqual(50, self.hero.health)
        self.assertEqual(30, self.hero.damage)
    
    def test_str_method(self):
        correct_str = f"Hero Ivan: 10 lvl\nHealth: 50\nDamage: 30\n"
        self.assertEqual(correct_str, self.hero.__str__())
    
    def test_battle_method_when_the_names_are_equal(self):
        self.enemy_hero.username = "Ivan"
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.enemy_hero)
        self.assertEqual("You cannot fight yourself", str(ex.exception))
    
    def test_battle_method_when_the_hero_health_is_zero_or_less(self):
        self.hero.health = 0
        with self.assertRaises(ValueError) as er:
            self.hero.battle(self.enemy_hero)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(er.exception))
    
    def test_battle_method_when_the_enemy_health_is_zero_or_less(self):
        self.enemy_hero.health = 0
        with self.assertRaises(ValueError) as er:
            self.hero.battle(self.enemy_hero)
        self.assertEqual("You cannot fight Petko. He needs to rest", str(er.exception))
    
    def test_draw(self):
        self.hero.damage = 50
        self.enemy_hero.damage = 60
        self.assertEqual("Draw", self.hero.battle(self.enemy_hero))
    
    def test_win(self):
        self.hero.damage = 60
        self.enemy_hero.damage = 1
        self.assertEqual("You win", self.hero.battle(self.enemy_hero))

        self.assertEqual(45, self.hero.health)
        self.assertEqual(11, self.hero.level)
        self.assertEqual(65, self.hero.damage)
    
    def test_lose(self):
        self.hero.damage = 1
        self.assertEqual("You lose", self.hero.battle(self.enemy_hero))

        self.assertEqual(35, self.enemy_hero.health)
        self.assertEqual(11, self.enemy_hero.level)
        self.assertEqual(25, self.enemy_hero.damage)

if __name__ == "__main__":
    main()
