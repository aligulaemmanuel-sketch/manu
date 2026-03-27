class AnagramChecker:
    def __init__(self, file_path="words.txt"):
        # Load the file and store words in a set for O(1) lookup speed
        with open(file_path, 'r', encoding='utf-8') as f:
            self.word_list = {word.strip().lower() for word in f.readlines() if word.strip()}

    def is_valid_word(self, word):
        return word.lower() in self.word_list

    def get_anagrams(self, word):
        word = word.lower()
        target_sorted = sorted(word)
        anagrams = []

        for w in self.word_list:
            if w != word and sorted(w) == target_sorted:
                anagrams.append(w)
        return sorted(anagrams)

    @staticmethod
    def is_anagram(word1, word2):
        return sorted(word1.lower()) == sorted(word2.lower())
