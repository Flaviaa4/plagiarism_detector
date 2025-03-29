#!/usr/bin/env python3

with open("essay-1.txt", "r") as file1:
    data_1 = file1.read().lower()

with open("essay-2.txt", "r") as file2:
    data_2 = file2.read().lower()

special_characters = "\n-,.;()[]"
char = ""
for i in data_1:
    if i not in special_characters:
        char += i

var = ""
for i in data_2:
    if i not in special_characters:
        var += i

essay_1 = char
essay_2 = var

clean_essay_1 = essay_1.split(" ")
clean_essay_2 = essay_2.split(" ")


class PlagiarismChecker:
    """
    Class for checking plagiarism.
    Args:
        clean_essay_1 -> set
        clean_essay_2 -> set
    Returns:
        common words, differences, and percentage
    """

    def __init__(self, clean_essay_1, clean_essay_2):
        """Initializes two sets."""
        self.clean_essay_1 = set(clean_essay_1)
        self.clean_essay_2 = set(clean_essay_2)

    def common_words(self):
        """Finding common words."""
        common_words = self.clean_essay_1 & self.clean_essay_2
        print(", ".join(common_words))

    def difference(self):
        """Finding differences."""
        differences = self.clean_essay_1 - self.clean_essay_2
        print(", ".join(differences))

    def search_words(self):
        """Searching for a word."""
        word_to_search = input("Enter a word: ").lower()
        counter_1 = sum(1 for word in self.clean_essay_1 if word == word_to_search)
        counter_2 = sum(1 for word in self.clean_essay_2 if word == word_to_search)

        print(
            f"Word: {word_to_search} is found in essay1 {counter_1} times "
            f"and {counter_2} times in essay2"
        )
        return counter_1 > 0 or counter_2 > 0

    def plagiarism_percentage(self):
        """Calculating plagiarism percentage."""
        nbr_common_words = len(self.clean_essay_1 & self.clean_essay_2)
        total_common_words = len(self.clean_essay_1 | self.clean_essay_2)
        percentage = (nbr_common_words * 100) / total_common_words

        if percentage >= 50:
            print(
                f"Student has plagiarized\n"
                f"Plagiarism percentage: {percentage:.2f}%"
            )
            return True
        else:
            print(
                f"Student did not plagiarize\n"
                f"Plagiarism percentage: {percentage:.2f}%"
            )
            return False


def main():
    """Function to run the application."""
    while True:
        print("-" * 80)
        print("Welcome to our Plagiarism Application services\n")
        print("Choose your option between 1-5")
        print("1. Search for common words")
        print("2. Search different words")
        print("3. Input a word to search in essay 1 and 2")
        print("4. Calculate Plagiarism")
        print("5. Exit the application")

        plagiarism = PlagiarismChecker(clean_essay_1, clean_essay_2)
        try:
            user_input = int(input("Enter your choice: "))
        except ValueError:
            print("❌ Error! Please enter a number between 1-5.")
            continue

        if user_input == 1:
            plagiarism.common_words()
        elif user_input == 2:
            plagiarism.difference()
        elif user_input == 3:
            print(plagiarism.search_words())
        elif user_input == 4:
            print(plagiarism.plagiarism_percentage())
        elif user_input == 5:
            print("✔️ Exiting Application...\nThanks for using our services!")
            break
        else:
            print("❌ Error! Choose a value between 1-5.")
            continue


if __name__ == "__main__":
    main()
