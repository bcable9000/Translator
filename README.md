# Translator
	A personal project with an new take on the 'traditional' methods of learning a language. A little more chaotic, just like real life. It uses Mad Libs style sentence creation, along with a personal dictionary and Google Translate API to translate newly added verbs. This is especially useful for verbs that are irregular, such as 'ir', that would require hard-coded conjugations every time a new one is added. This also gives the user the option to go into the yml (see below) and fix any conjugations that were wrong. 

There are 4 main files:
- Tranlator[x].py: Is the main code for running the program
- Conjugation.py: Connects to google translate to help conjugate verbs/sentences
- conjugations.yml: The database for storing saved conjugations. Can edit this via notepad if a verb has an incorrect conjugation
- Dictionary.txt: The text file that stores all words currently used, in the format [english],[spanish 1]...[spanish n],[type of word]. Spaish 1,...,Spanish n just means that a single english word can translate to n spanish words
