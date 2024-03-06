
# I use Tabs
# You can use cheat 777

import os
from random import choice
from time import sleep
import urllib.request

if os.path.exists('hangman_lists.py'):
	import hangman_lists
else:
	url = 'https://raw.githubusercontent.com/InJoy09/hangman_game/main/hangman_lists.py'
	message = '\nDownload file: hangman_list.py\n' + url + '\n'
	try:
		urllib.request.urlretrieve(url, 'hangman_lists.py')
	except:
		print(message)
		exit('missing file: hangman_list.py')
	else:
		import hangman_lists


words: list
phrases: list


def set_language():
	global words
	global phrases
	
	st = '\nРусский язык(1)\nEnglish language(2)\n\nВведите цифру/Enter a number: _ '
	lang = input(st)
	
	if lang == '1':
		words = hangman_lists.words_rus
		phrases = hangman_lists.phrases_rus
	else:
		words = hangman_lists.words_eng
		phrases = hangman_lists.phrases_eng

	
def display_hangman(tries):
	gallows = ['\n', '-' * 11, '|        |', '|', '|\n|', '|', '|', '\n']
	
	hangman = [
		'|        0',
		'|        |\n|        |',
		'|       /|\n|        |',
		'|       /|\\\n|        |',
		'|       /',
		'|       / \\'
	]
	
	for i, j in enumerate([3, 4, 4, 4, 5, 5][:tries]):
		gallows[j] = hangman[i]
	
	[print(el) for el in gallows]
	

def to_play():
	target_word = choice(words).upper()
	tries = 0
	user_word = ['_'] * len(target_word)
	display_hangman(0)
	
	while '_' in user_word and tries < 6:
		print(phrases[0], *user_word)
		letter = input(phrases[1]).upper()
		
		if letter == '777': print(f'"{target_word}"')
		
		index = target_word.find(letter) if letter else -1
		
		if index == -1: tries += 1
		
		while index != -1:
			user_word[index] = letter
			index = target_word.find(letter, index + 1)
		
		display_hangman(tries)

	return True if tries < 6 else False


def main():
	set_language()
	
	clear = 'cls' if os.name == 'nt' else 'clear'
	lets_game = True
	
	while lets_game:
		result = to_play()
		
		if result:
			print(phrases[2])
		else:
			for i in range(7):
				os.system(clear)
				display_hangman(i)
				sleep(0.5)
		
				print(phrases[4])

		again = input(phrases[3])
		
		lets_game = True if again in 'yд' else False
		
	print(phrases[5])
	
	
main()
