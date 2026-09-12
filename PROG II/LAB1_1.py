class Diary:
    def __init__(self):
        self.entries = []

    def add_entry(self, text):
        self.entries.append(text)

    def remove_entry(self, index):
        if 0 <= index < len(self.entries):
            del self.entries[index]
        else:
            raise IndexError("Entry index out of range.")

    def get_entries(self):
        return self.entries

    def save(self, filename):
        with open(filename, "w") as file:
            for entry in self.entries:
                file.write(entry + "\n")

    def load(self, filename):
        with open(filename, "r") as file:
            self.entries = [line.strip() for line in file]

    def print_statistics(self):
        total_entries = len(self.entries)
        avg_length = (
            sum(len(entry) for entry in self.entries) / total_entries
            if total_entries > 0
            else 0
        )
        print(f"Total entries: {total_entries}")
        print(f"Average entry length: {avg_length:.2f}")

    def __str__(self):
        if not self.entries:
            return ""
        return "\n".join(self.entries)