class File:
    def __init__(self, name, size, file_type):
        self.name = name
        self.size = size
        self.type = file_type


class FileManager:
    def __init__(self):
        self.files = []

    def add_file(self):
        name = input("Enter file name: ")
        size = input("Enter file size: ")
        file_type = input("Enter file type: ")

        if not name or not size or not file_type:
            print("Error: Missing fields")
            return

        # Duplicate check
        for f in self.files:
            if f.name == name and f.size == size:
                print("Duplicate file found!")
                return

        new_file = File(name, size, file_type)
        self.files.append(new_file)
        print("File added successfully!")

    def view_files(self):
        if not self.files:
            print("No files stored.")
            return

        print("\nStored Files:")
        for i, f in enumerate(self.files, 1):
            print(f"{i}. Name: {f.name}, Size: {f.size}, Type: {f.type}")

    def run(self):
        while True:
            print("\n1. Add File")
            print("2. View Files")
            print("3. Exit")

            choice = input("Enter choice: ")

            if choice == '1':
                self.add_file()
            elif choice == '2':
                self.view_files()
            elif choice == '3':
                break
            else:
                print("Invalid choice")


# Run the program
if __name__ == "__main__":
    manager = FileManager()
    manager.run()