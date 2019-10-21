from os.path import exists

def intro():
    print("\nThis program asks to enter some sentences, until you just press [enter].\nWhen you are done with the input, the program with print all the lines.\nAfter that, it will ask you if you would like to save it to a file.\n")

def input_text():
    text_list = []
    while(True):
        question = input("Enter a sentence: ")
        if(len(question) is 0):
            return text_list
        else:
            text_list.append(question)

def print_list_to_screen(text_list):
    for i in text_list:
        print(i)

def question_choice(question, possible_answer_tuple):
    while(True):
        ask_question = input(question)
        for k in possible_answer_tuple:
            if(ask_question == k):
                return ask_question

def save_to_file(file_name, text_list):
    if (not exists(file_name)):
        f = open(file_name, "x")
        f.close()
    else:
        choice = question_choice("This file already exists, want to overwrite it? (y/n) ", ("y", "n"))
        if(choice is "n"):
            exit()
    f = open(file_name, "w")
    data = ""
    for t in text_list:
        data += f"{t}\n"
    f.write(data)
    f.close()

def save_question(text_list):
    choice = question_choice("Would you like to save the list to a file (y/n) ", ("y", "n"))
    file_name = input("Enter the name of the file, example, list.txt: ")
    if(choice is "n"):
        exit()
    save_to_file(file_name, text_list)

def wordprocessor_app():
    intro()
    text_list = input_text()
    print_list_to_screen(text_list)
    save_question(text_list)
    question = question_choice("Would you like to make another list? (y/n): ", ("y", "n"))
    if(question is "y"):
        return wordprocessor_app()
    else:
        exit()

def main():
    wordprocessor_app()

if __name__ == "__main__":
    main()
