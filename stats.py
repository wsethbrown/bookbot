def count_words(text):
  words = text.split()
  num_words = len(words)
  print(f"Found {num_words} total words")

def count_letters(text):
  letters = {}
  for char in text:
    lowercase_char = char.lower()
    if lowercase_char in letters:
      letters[lowercase_char] += 1
    else:
      letters[lowercase_char] = 1
  return letters

def sort_letters(letters):
  def sort_on(item):
    return item["num"]

  letters_list = []
  for char in letters:
    letters_list.append({"char": char, "num": letters[char]})

  letters_list.sort(reverse=True, key=sort_on)
  return letters_list