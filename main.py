import sys

if len(sys.argv) < 2:
	print("Usage: python3 main.py <path_to_book>")
	sys.exit(1)
else:
	filepath = sys.argv[1]

def get_book_text(filepath):
	with open(filepath) as f:
		file_contents = f.read()
	return file_contents

book_text = get_book_text(filepath)

from stats import word_counter, character_counter, dic_to_list

total_words = word_counter(book_text)
character_tally = character_counter(book_text)
sorted_char_list = dic_to_list(character_tally)

print(f"{total_words} words found in the document")
print("============ BOOKBOT ============")
print(f"Analyzing book found at{filepath}...")
print("----------- Word Count ----------")
print(f"Found {total_words} total words")
print("--------- Character Count -------")

for char_dic in sorted_char_list:
	char = char_dic["character"]
	count = char_dic["count"]
	if char.isalpha():
		print(f"{char}: {count}")

print("============= END ===============")
