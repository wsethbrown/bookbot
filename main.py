import sys
from stats import count_words, count_letters, sort_letters

def main():
  if len(sys.argv) > 1:
    book_path = sys.argv[1]
  else:
    print(f"Usage: python3 main.py <path_to_book>")
    sys.exit(1)

  text = get_books_text(book_path)

  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {book_path}...")
  print("----------- Word Count ----------")
  count_words(text)
  print("--------- Character Count -------")

  char_dict = count_letters(text)
  sorted_letters = sort_letters(char_dict)

  for item in sorted_letters:
    if item["char"].isalpha():
      print(f"{item['char']}: {item['num']}")

  print("============= END ===============")

def get_books_text(file_path):
  with open(file_path) as f:
    return f.read()

main()