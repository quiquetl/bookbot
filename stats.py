def word_counter(book_text):
	word_list = book_text.split()
	total_words = len(word_list)
	return total_words

def character_counter(book_text):
	character_count = {}
	lower_case_book = book_text.lower()
	for character in lower_case_book:
		if character in character_count:
			character_count[character] += 1
		else:
			character_count[character] = 1
	return character_count

def dic_to_list(character_count):
	char_list = []
	for char, count in character_count.items():
		char_data = {"character": char, "count": count}
		char_list.append(char_data)

	def sort_on(char_list):
		return char_list["count"]

	char_list.sort(reverse=True, key=sort_on)

	return char_list

		

