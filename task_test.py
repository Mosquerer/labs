import unittest
from task import TextProcessor

class TextProcessorTest(unittest.TestCase):
    def setUp(self):
        # Метод setUp вызывается перед каждым тестом
        # Создаем экземпляр TextProcessor для тестов
        self.processor = TextProcessor()

    def test_remove_repeated_letters_single_word(self):
        # Тест на удаление повторяющихся букв в одном слове
        self.assertEqual(self.processor.process_text("hello"), "helo")

    def test_remove_repeated_letters_multiple_words(self):
        # Тест на удаление повторяющихся букв в строке с несколькими словами
        self.assertEqual(self.processor.process_text("hello world"), "helo world")

    def test_remove_repeated_letters_in_sentences(self):
        # Тест на удаление повторяющихся букв в предложении с пунктуацией
        self.assertEqual(
            self.processor.process_text("Hello, world! How are you?"),
            "Helo, world! How are you?"
        )

    def test_empty_string(self):
        # Тест на случай, если входная строка пустая
        self.assertEqual(self.processor.process_text(""), "")

    def test_punctuation_handling(self):
        # Тест на корректную обработку пунктуации (пунктуация не должна изменяться)
        self.assertEqual(
            self.processor.process_text("Wow!!! Amazing..."),
            "Wo!!! Amzing..."
        )

    

if __name__ == "__main__":
    # Запуск тестов, если файл запускается напрямую
    unittest.main(verbosity=2)