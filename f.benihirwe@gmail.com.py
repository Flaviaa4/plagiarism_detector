#!/usr/bin/env python3


with open("essay-1.txt", "r") as file1:
    data_1 = file1.read().lower()
    
with open("essay-2.txt", "r") as file2:
    data_2 = file2.read().lower()

special_characters = "\n-,.;()[]"
char = ""
for i in data_1:
    if i in special_characters:
        char += ""
    else:
        char += i

var = ""
for i in data_2:
    if i in special_characters:
        var += ""
    else:
        var += i

essay_1 = char
essay_2 = var
    
clean_essay_1 = essay_1.split(" ")
clean_essay_2 = essay_2.split(" ")

class PlagiarismChecker:
    '''
        Class for checking plagirsm
        Args:
            clean_essay_1 -> set
            clean_essay_2 -> set
        return common words, differences, and percentage
    '''
    def __init__(self, clean_essay_1, clean_essay_2):
        '''
            Initializes two sets
        '''
        self.clean_essay_1 = set(clean_essay_1)
        self.clean_essay_2 = set(clean_essay_2)

    
    def common_words(self):
        '''Finding commons words'''
        common_words = self.clean_essay_1 & self.clean_essay_2
        for words in common_words:
            print(words, end=", ")
    
    def difference(self):
        '''Finding differences'''
        differences = self.clean_essay_1 - self.clean_essay_2
        print(", ".join(differences))
    
    def search_words(self):
        '''Searching the words'''
        word_to_search = input("Enter a word: \n").lower()
        counter_1 = 0
        counter_2 = 0

        for word in self.clean_essay_1:
            if word == word_to_search:
                counter_1 += 1

        for word in self.clean_essay_2:
            if word == word_to_search:
                counter_2 += 1

        print(f"Word: {word_to_search} is found in essay1 {counter_1} times "
              f"and {counter_2} times in essay2") 

        return True if counter_1 > 0 or counter_2 > 0 else False

    def plagiarism_percentage(self):
        nbr_common_words = len(self.clean_essay_1 & self.clean_essay_2)
        total_common_words = len(self.clean_essay_1 | self.clean_essay_2)
        percentage = (nbr_common_words * 100) / total_common_words
        if percentage >= 50:
            print(f"Student has plagiarised\n"
            f"Plagiarism percentage: {percentage:.2f}")
            return True
        else:
            print(f"Student did not plagiarise\n"
            f"Plagiarism percentage: {percentage:.2f}")
            return False

def main():
    '''
        Function to run the application
    '''
    while True:
        print("---------------------------------------------------------------------------------------\n")
        print("Welcome to our Plagiarism Application services\n")
        
        print("________________________________________________________________________________________\n")

        print("Choose your option between 1-5")
        print("1.Search for common words\n")
        print("2. Search different words\n")
        print("3.Input a word to search in essay 1 and 2\n")
        print("4.Calculate Plagiarism\n")
        print("5.Exit the application\n")
        
        plagiarism = PlagiarismChecker(clean_essay_1, clean_essay_2)
        user_input = int(input("Enter your choice: \n"))

        if user_input == 1:
            plagiarism.common_words()
        elif user_input == 2:
            plagiarism.difference()
        elif user_input == 3:
            print(plagiarism.search_words())
        elif user_input == 4:
            print(plagiarism.plagiarism_percentage())
        elif user_input == 5:
            print("✔️ Exiting Application...\nThanks for using our services")
            break
        else:
            print("❌ Error! Choose a value between 1-5")
            continue

if __name__ == "__main__":
    main()
