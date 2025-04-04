class Book:
    def __init__(self, filepath: str):
        self.filepath = filepath

    def get_text(self):
        with open(self.filepath) as text:
            document = text.read()
        return document

    def get_filepath(self):
        return self.filepath

    def sort_characters(self):
        characters = self.count_characters()
        sorted_items = sorted(characters.items(), key=lambda item: item[1], reverse=True)
        sorted_characters = [{"character": k, "count": v} for k, v in sorted_items]
        return sorted_characters

    def count_characters(self):
        characters = {}
        text = self.get_text()

        for char in text:
            char_lower = char.lower()
            if char_lower in characters:
                characters[char_lower] += 1
            else:
                characters[char_lower] = 1

        return characters

    def count_words(self):
        text = self.get_text()
        number_words = len(text.split())
        return number_words
