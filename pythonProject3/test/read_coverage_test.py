import unittest

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

class TestReadFile(unittest.TestCase):
    def test_read_existing_file(self):
        text = read_file("existing_file.txt")
        self.assertIsNotNone(text)

    def test_read_non_existing_file(self):
        with self.assertRaises(FileNotFoundError):
            read_file("non_existing_file.txt")

if __name__ == "__main__":
    unittest.main()
