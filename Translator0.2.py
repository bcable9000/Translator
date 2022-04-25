import time
import random
from Conjugation import conjugate
from googletrans import Translator
translator = Translator(service_urls=['translate.google.com'])

###imports###

#Initializing variables#

##Creating an array of all the words
file = open("./Dictionary.txt", "r")
temp = file.readline().split()
english = {}
i = 0
while temp[0]:
    english[i] = temp
    print(temp)
    temp = file.readline().replace('\n', '').split(',')
    i += 1
file.close()

i = 0

##Creating parts of sentences 
nouns = {}
verbs = {}
for i in english:
    if "noun" in english[i]:
        nouns[len(nouns)] = english[i]
    elif "verb" in english[i]:
        verbs[len(verbs)] = english[i]       
subjects = {
    0 : ("I", "yo"),
    1 : ("you", "tú"),
    2 : ("he", "él"),
    3 : ("she", "ella"),
    4 : ("you (formal)", "usted"),
    5 : ("we (m)", "nosotros"),
    6 : ("we (f)", "nosotras"),
    7 : ("they (formal)", "ustedes"),
    8 : ("they (m)", "ellos"),
    9 : ("they (f)", "ellas"),
}
tenses = ("present")

words = len(english)
translation = ""

print(f"""Welcome to Translator 0.1
This is still in Beta so please be patient, as some functions may not work or will work incorrectly
The number of available words: {words}""")

def langmodeselect():
    return input("\nWhat mode do you want?\n1. English to Spanish\n2. Spanish to English\n3. Both\n")

def flashcards():
    #initialize variables
    temp = ''
    answer = ''
    langmode = langmodeselect()
    repeats = 0
    #Start loop
    while answer not in ("stop", "exit", "quit"):    
        if repeats > 0:
            input()
        else:
            repeats = 1
        rng = random.randrange(0,words)
        ##Lang 1 is English->Spanish, Lang 2 is vice versa##
        if langmode == '1':
            lang = 1
        elif langmode == '2':
            lang = 2
        else:
            lang = random.randrange(0,2)
        if lang == 1:
            answer = input(f"{english[rng][0]}\n")
            answer = answer.lower()
            if answer in english[rng] or answer[4:] in english[rng]:
                print('Congratulations! You got it right\n')
            elif answer not in ("stop", "exit", "quit"):
                x = english[rng][1]
##                print(f'You guessed: {answer}')
                print(f'Correct word: {x}\n')
        elif lang == 2:   
            answer = input(f"{english[rng][1]}\n")
            answer = answer.lower()
            if answer in english[rng] or answer[4:] in english[rng]:
                print('Congratulations! You got it right\n')
            elif answer not in ("stop", "exit", "quit"):
                x = english[rng][1]
##                print(f'You guessed: {answer}')
                print(f'Correct word: {x}\n')
                
def createsentence():
    ##Initializes variables##
    langmode = langmodeselect()
    answer = ''
    repeats = 0
    while answer not in ("stop", "exit", "quit"):    
        if langmode == '1':
            lang = 1
        elif langmode == '2':
            lang = 2
        else:
            lang = random.randrange(1,3)
        if repeats > 0:
            input()
        else:
            repeats = 1
        noun = nouns[random.randrange(0,len(nouns))]
        verb = verbs[random.randrange(0,len(verbs))]
        subject = subjects[random.randrange(0,len(subjects))]
        print(f'''
            Verb is: {verb}
            noun is: {noun}
            subject is: {subject}
            language: {lang}
            ''')
        sentences = { ##The pre-made sentences that are used, similar to Mad-Libs##
            0 : (f'{subject[0]} {conjugate ("to want", "present", subject[0])} {verb[0]} with the {noun[0]}',
                 f'{subject[1]} {conjugate ("querer", "present", subject[1])} {verb[1]} con {noun[1]}'),
            1 : (f'the {noun[0]} {conjugate(verb[0], "present", "it")} the tree',
                 f'{noun[1]} {conjugate(verb[1], "present", "it")} el árbol'),
            2 : (f'{subject[0]} {conjugate(verb[0], "present", subject[0])} the {noun[0]}',
                 f'{subject[1]} {conjugate(verb[1], "present", subject[1])} {noun[1]}')
        }
        rng = random.randrange(0, len(sentences))
        print(f'Number was: {rng}')
        ##Lang 1 is English->Spanish, Lang 2 is vice versa##
        if lang == 1:
            answer = input(f'\nSentence:\n{sentences[rng][0].capitalize()}.\n')
            answer = answer.lower()
            if answer == f'{sentences[rng][1]}':
                print('Congratualations!')
            elif answer in ("stop", "exit", "quit"):
                main()
            else:
                print(f'Correct sentence:\n{sentences[rng][1].capitalize()}.')
        elif lang == 2:
            answer = input(f'\nSentence:\n{sentences[rng][1].capitalize()}.\n')
            answer = answer.lower()
            if answer == f'{sentences[rng][0]}':
                print('Congratualations!')
            elif answer in ("stop", "exit", "quit"):
                main()
            else:
                print(f'Correct sentence: \n{sentences[rng][0].capitalize()}.')

def changelog():
    print()
    file1 = open("./changelog.txt", "r")
    print(file1.read())
    file1.close()

def main ():
    repeats = 0
    while True:
        if repeats > 0:
            time.sleep(1)
        else:
            repeats = 1
        mode = input("\nWhat would you like to do?\n1. Start Flashcards \n2. Work with sentences\n3. See all words\n4. See all English words\n5. View Changelog\n")
        if mode == "1" or mode.lower() == "start":
            flashcards()
        elif mode == "2":
            createsentence()
        elif mode == "3":
            print('\nCurrent words are:')
            for k,v in english.items():
                print(f'{k}. {v}')
            print('Enter any input to continue')
            while input() == '3':
                None
        elif mode == "4":
            print("\nEnglish words are:")
            for k, v in english.items():
                print(f"{k}. {v[0].capitalize()}")
            print('Enter any input to continue')
            while input() == '4':
                None
        elif mode == '5':
            changelog()
            print('\nEnter any input to continue')
            while input() == '5':
                None
        #Solely for testing out googletrans; not an actual mode
        elif mode == '6':
            translation = translator.translate('He to walk to the store', src='en', dest='es')
            print(translation.text)
        else:
            break
    mode = input('Are you sure you want to quit? Y/N\n')
    if mode.lower() == 'n' or mode.lower() == 'no':
        main()
    else:
        print('Thanks for playing!')

main()
