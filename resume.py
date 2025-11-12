def read_resume_file():
    """
    Opens and reads the file named 'resume.txt' line by line,
    preserving all original spacing and characters.
    """
    file_path = 'resume.txt'
    print(f"--- Reading content from: {file_path} ---")
    
    try:
        # 'r' is for read mode. The 'with' statement handles file closing.
        with open(file_path, 'r') as file:
            for line in file:
                # print(line, end='') preserves the file's original line breaks.
                print(line, end='')

    except FileNotFoundError:
        print(f"\nError: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"\nAn error occurred: {e}")

# Call the function to execute the reading process
read_resume_file()