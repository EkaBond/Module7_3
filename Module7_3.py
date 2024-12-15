import string

class WordsFinder:

    def __init__(self, *name):
        self.file_name = name

    def get_all_words(self):
        all_words = {}
        l = ''
        for i in self.file_name:
            with open(i, encoding='utf-8') as file:
                for line in file:
                    line = line.lower()
                    new_line = line.translate(str.maketrans("", "", string.punctuation))
                    l = l + new_line
                    l1 = l.split()
                all_words = {self.file_name: l1}
            return all_words

    def find(self, world):
        dict1 = {}
        for key in self.get_all_words().values():
            a = (key.index(world.lower())) +1
            dict1 = {self.file_name : a}
            return dict1


    def count(self, world):
        dict2 = {}
        n = 0
        for key in self.get_all_words().values():
            if world.lower() in key:
                n = key.count(world.lower())
                dict2 = {self.file_name : n}
            return dict2


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))