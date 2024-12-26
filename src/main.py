import sys
import os
from englexer import EngLexer
from engparser import EngParser
from engevaluator import EngEvaluator

def main():
    # Check if a file path was provided as an argument
    if len(sys.argv) < 2:
        print("Error: Please provide a file path")
        sys.exit(1)

    # Get the file path from command line arguments
    file_path = sys.argv[1]
    if file_path[-4:] != ".eng":
        print("Wrong file format")
        sys.exit(1)
    filename = file_path.split(".")[0]
    

    # Check if the file exists
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' does not exist")
        sys.exit(1)
    
    try:
        # Open and read the file
        tokens = EngLexer(file_path).lex()
        parsednodes = EngParser().parsetokens(tokens)
        EngEvaluator(parsednodes)



    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()