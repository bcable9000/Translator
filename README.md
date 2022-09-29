# Translator
	A personal project with an new take on the 'traditional' methods of learning a language. The translations are a little more chaotic than programs like Duolingo, just like real life. It uses Mad Libs style sentence creation, along with a personal dictionary and Google Translate API (pygoogletranslation) to translate newly added verbs. This is especially useful for verbs that are irregular, such as 'ir', that would require hard-coded conjugations every time a new one is added. This also gives the user the option to go into the yml (see below) and fix any conjugations that were wrong. 

There are 4 main files:
- Tranlator[x].py: Is the main code for running the program, where x is the current version
- Conjugation.py: Connects to google translate to help conjugate verbs/sentences
- conjugations.yml: The database for storing saved conjugations. Can edit this via notepad if a verb has an incorrect conjugation
- Dictionary.txt: The text file that stores all words currently used, in the format [English],[Spanish 1]...[Spanish n],[type of word]. Spaish 1,...,Spanish n is used to map one English word to multiple Spanish ones.