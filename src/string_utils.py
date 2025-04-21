class StringUtils:
    def reverse(self, text):
        return text[::-1]
        
    def capitalize_words(self, text):
        return ' '.join(word.capitalize() for word in text.split())
        
    def count_vowels(self, text):
        return sum(1 for char in text.lower() if char in 'aeiou')
