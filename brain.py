from modules.language import Language
from modules.action_executor import ActionExecutor
from list import dictionary
from modules.database import Database

class Einstein:
    def __init__(self):
        self.language = Language(dictionary)  # Initialize Language instance
        self.action_executor = ActionExecutor(Database())  # Initialize ActionExecutor instance

def main():
    einstein = Einstein()
    print("Loading Einstein...")
    print('Calibrating database and Preferences...')
    print("Active...")
    
    input_sentence = input("Please type a command: ")
    action, target = einstein.language.interpret_input(input_sentence)

    if (action, target) in einstein.language.pos_dictionary:
        interpretation = einstein.action_executor.execute_action(action, target)
    else:
        interpretation = "I don't understand the input."

    print("Interpretation:", interpretation)

if __name__ == '__main__':
    main()
