from pygoogletranslation import Translator
import json
import yaml
import pprint
translator = Translator()

def checkfile(verb,tense,subject):
    #Opens the file and creates dict
    with open('conjugations.yml', 'r') as yaml_file:
        iverbs = yaml.safe_load(yaml_file)
    
    if verb in iverbs:
        if tense in iverbs[verb]:
            if subject in iverbs[verb][tense]:
                return iverbs[verb][tense][subject]
    return False

def writefile(verb,tense,subject,conjugation):
    ##Open file, create dict with iverbs
    with open('conjugations.yml', 'r') as yaml_file:
        iverbs = yaml.safe_load(yaml_file)
    
    #Allows user to verify/change verb conjugations before they are added
    check = input(f'What is the correct conjugation of \'{subject} {conjugation} ({verb},{tense})\'?\n(leave blank if correct)\n')
    if  check != '':
        conjugation = check

    ##Write conjugation to iverbs
    if verb in iverbs:
        if tense in iverbs[verb]:
            if subject in iverbs[verb][tense]:
                return iverbs[verb][tense][subject]
            else:   ##adds subject/conjugation pair
                iverbs[verb][tense][subject] = conjugation
        else:       ##adds tense with subject/conjugation pair
            iverbs[verb][tense] = {subject:conjugation}
    else:           ##adds the verb,tense, and subject/conjugation pair
        iverbs[verb] = {tense:{subject:conjugation}}

    ##write iverbs to file
    with open('conjugations.yml', 'w') as yaml_file:
     yaml.dump(iverbs, stream=yaml_file, default_flow_style=False)
        
    return 0

def conjugate(verb, tense, subject): ##subjects are: I, you, it (third person singular), they (third person plural), and we
    ##need to change subject to ensure it matches
    if subject in ("yo"):
        subject = "I"
    elif subject in ("tú"):
        subject = "you"
    elif subject in ("he", "she", "ella", "él", "usted", "you (formal)"):
        subject = "it"
    elif subject in ("they (f)", "they (m)", "they (formal)", "ellos", "ellas", "ustedes"):
        subject = "they"
    elif subject in ("we (f)", "we (m)", "nosotros", "nosotras"):
        subject = "we"
    ##check to see if answer is already cached
    check = checkfile(verb, tense, subject)
    if check:
        return check
    
    ##Determines if English or Spanish by ending of verb
    ending = verb[(len(verb) - 2):]
    if ending in ("er", "ir", "ar"): #0 is english, 1 is spanish
        language = 1 
    else:
        language = 0
        
    ##Initializing other variables
    conjugation = ''
    translation = ''
    i = 0
    
    ##If it's spanish, turns it into English
    if language == 1:
        translation = translator.translate(verb,src='es',dest='en')
        translation = translation.text
    ##If it's English, conjugate as normal
    if tense == "present":
        if subject == "it":
            conjugation += verb + "s"
        else:
            conjugation = verb
    conjugation = conjugation[3:]
    if language == 1:
        translation = translator.translate(subject + ' '+ verb,src='es',dest='en')
        translation = translation.text
        
    writefile(verb,tense,subject,conjugation)
    return conjugation

def test2(verb):
    translation2 = translator.translate(verb, src='es', dest='en')
    print(translation2.text)

def hardcodeDirectory():
    ##Only use if you want to replace the current directory with a hard-coded one
    iverbs = { #iverbs = irregular verbs
        #4
        'ir': {
            'present' : {
                'I' : 'voy a', "you" : "vas a", "it" : "va a", "they" : "van a", "we" : "vamos a"}},
        'to go' : {
           'present' : {
                'I' : 'go to', 'you' : 'go to', 'it' : 'goes to', 'they' : 'go to', 'we' : 'go to'}},
        #6
        'querer' : {
            'present' : {
                'I' : 'quiero', 'you' : 'quieres', 'it' : 'quiere', 'they' : 'quieren', 'we' : 'queremos'}},
    }

    ##Writes Directory to file
    with open('conjugations.yml', 'w') as yaml_file:
     yaml.dump(iverbs, stream=yaml_file, default_flow_style=False)

    ##Read Dictionary from file
    with open('conjugations.yml', 'r') as yaml_file:
        iverbs = yaml.safe_load(yaml_file)
      
    ##print("Data type after reconstruction : ", type(js))
    print(iverbs)

def test():
    conjugation = 'selecctiones'
    check = input(f'What is the correct conjugation of \'{conjugation}\'?\n(leave blank if correct)\n')
    if  check != '':
        conjugation = check
    print(conjugation)


