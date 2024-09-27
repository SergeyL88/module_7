from re import split


class WordsFinder():

    def __init__(self, *file_names):
        self.file_names = [*file_names]

    def get_all_words(self):
        all_words = dict()
        symbols_list = [',', '.', '=', '!', '?', ';', ':', ' - ', '\n']
        for files in self.file_names:
            with open(files, 'r') as temp_file:
                temp_string = temp_file.read().lower()
                for symbol in symbols_list:
                    temp_string = temp_string.replace(symbol, ' ')
            all_words[files] = temp_string.split()
        return all_words

    def find(self, word):
        result = dict()
        for file_name, word_in_file in self.get_all_words().items():
            if word.lower() in word_in_file:
                result[file_name] = word_in_file.index(word.lower()) + 1
        return result

    def count(self, word):
        result = dict()
        counter = 0
        for file_name, word_in_file in self.get_all_words().items():
            for words in word_in_file:
                if word.lower() == words:
                    counter += 1
            result[file_name] = counter
            counter = 0
        return result


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
