class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = list(file_names)

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                check = file.read().lower()
                for mark in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    check = check.replace(mark, ' ')
            all_words[file_name] = check.split()
        return all_words

    def find(self, word):
        dict_find = {}
        for value, key in self.get_all_words().items():
            if word.lower() in key:
                dict_find[value] = key.index(word.lower()) + 1
        return dict_find

    def count(self, word):
        dict_count = {}
        for value, key in self.get_all_words().items():
            words_count = key.count(word.lower())
            dict_count[value] = words_count
        return dict_count


if __name__ == '__main__':
    finder2 = WordsFinder('test_file.txt')
    print(finder2.get_all_words())  # Все слова
    print(finder2.find('TEXT'))  # 3 слово по счёту
    print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
