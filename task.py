import re

class TextProcessor:
    def process_text(self, text):
        # Разделяем текст на слова и обрабатываем каждое слово
        def remove_repeated_letters(word):
            seen = set()
            result = []
            for char in word:
                if char.lower() not in seen:  # Учитываем регистр
                    seen.add(char.lower())
                    result.append(char)
            return ''.join(result)

        # Используем регулярное выражение для разделения текста на слова с учётом пунктуации
        tokens = re.findall(r'\w+|[^\w\s]', text, re.UNICODE)
        processed_tokens = [remove_repeated_letters(token) if token.isalpha() else token for token in tokens]
        
        # Собираем обработанные токены обратно в текст
        return ''.join(
            token if not re.match(r'\w', token) else f" {token}" for token in processed_tokens
        ).strip()