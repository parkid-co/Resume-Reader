def read_resume_file():
    file_path = 'Resume-Reader/Resume.txt'
    print(f"--- Reading content from: {file_path} ---")
    try:
        with open(file_path, 'r') as file:
            for line in file:
                print(line, end='')
    except FileNotFoundError:
        print(f"\nError: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"\nAn error occurred: {e}")
read_resume_file()
