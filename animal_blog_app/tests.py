from django.test import TestCase
from .models import Animal

# Create your tests here.


class AnimalModelTest(TestCase):

    @staticmethod
    def print_info(messages):
        count = Animal.objects.count()
        print(f'{messages}: all_animals = {count}')

    def setUp(self):
        print('-' * 50)
        self.print_info('Start setUp')
        self.animal = Animal.objects.create(breed='Бульдог', nickname='Слуньтявый', age=6, email='slun@test.ru')
        Animal.objects.create(breed='Сибирский', nickname='Мурзик', age=3)
        Animal.objects.create(breed='Гризли', nickname='Миша', age=7)
        Animal.objects.create(breed='Шимпонзе', nickname='Аркаша', age=10, email='arka@test.ru')
        self.print_info('Finish setUp')

    def test_animal_creations(self):
        """Проверка создания объектов Animal"""
        self.print_info('Start test_animal_creations')
        self.assertEqual(self.animal.breed, 'Бульдог')
        self.assertEqual(self.animal.nickname, 'Слуньтявый')
        self.assertEqual(self.animal.age, 6)
        self.assertEqual(self.animal.email, 'slun@test.ru')
        self.print_info('Finish test_animal_creations')

    def test_animal_get_all_records(self):
        """Проверка получения всех записей из БД"""
        self.print_info('Start test_animal_get_all_records')
        animal = Animal.objects.all()
        count_animal = len([i for i in animal])
        self.assertEqual(len(animal), count_animal)
        self.print_info('Finish test_animal_get_all_records')

    def test_animal_get_record(self):
        """Проверка получения одной записи"""
        self.print_info('Start test_animal_get_record')
        arka = Animal.objects.get(nickname='Аркаша')
        self.assertEqual(arka.age, 10)
        self.print_info('Finish test_animal_get_record')

    def test_animal_str(self):
        """Проверка метода __str__"""
        self.print_info('Start test_animal_str')
        expected_str = 'Бульдог Слуньтявый 6'
        self.assertEqual(str(self.animal), expected_str)
        self.print_info('Finish test_animal_str')

    def test_animal_get_ful_name(self):
        """Проверка метода get_ful_name"""
        self.print_info('Start test_animal_get_ful_name')
        expected_str = 'Бульдог Слуньтявый'
        self.assertEqual(self.animal.get_full_name(), expected_str)
        self.print_info('Finish test_animal_get_ful_name')

    def test_animal_adult(self):
        """Проверка метода is_adult"""
        self.print_info('Start test_animal_adult')
        expected_age = [i.age for i in Animal.objects.all() if i.age >= 5]
        self.assertTrue(self.animal.is_adult(), expected_age)
        self.print_info('Finish test_animal_adult')

    def test_animal_price_default_value(self):
        """Проверка значения по умолчанию для price"""
        self.print_info('Start test_animal_price_default_value')
        animal = Animal.objects.create(breed='Шпиц', age=4)
        self.assertEqual(animal.price, 1000)
        self.assertNotEqual(animal.price, 1001)
        self.print_info('Finish test_animal_price_default_value')

    def test_animal_max_length(self):
        """Проверка значения поля breed на аргумент max_length"""
        self.print_info('Start test_animal_max_length')
        sum_letter_animal = Animal.objects.create(breed='Алабааааааааааааааааааааааааааааааааааааааааааааaй')
        self.assertEqual(len(sum_letter_animal.breed), 50)
        self.print_info('Finish test_animal_max_length')

    def test_animal_delete(self):
        """Проверка на удаление записи из БД"""
        self.print_info('Start test_animal_delete')
        Animal.objects.get(nickname='Аркаша').delete()
        arka = [i.nickname for i in Animal.objects.all()]
        self.assertNotIn('Аркаша', arka)
        self.print_info('Finish test_animal_delete')

    def test_animal_db(self):
        """Проверка изменений данных"""
        self.print_info('Start test_animal_db')
        animal = Animal.objects.all()
        animal.filter(nickname='Аркаша').update(age=5)
        self.assertEqual(Animal.objects.get(nickname='Аркаша').age, 5)
        self.print_info('Finish test_animal_db')
