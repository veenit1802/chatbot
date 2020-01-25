import random,copy
import time
import os
import speech_recognition as sr
from gtts import gTTS
# class table which contain the input sentence and their respective output
class table:

    # function reflextable which cnotain the data or the sentence and their output
    def reflextable(self,x):

        # reflections is a dictionary which stores the data
        reflections={
            "hi" : ["hello","hi there","hey","namaste","ciao"],
            "how are you": ["i am good","i am good how are you"],
            "what are your hobby": ["chatting with you","to lost in your memories","making effort to help you"],
            "i am fine":["good to know that"],
            "do you love me":["yes i love you so much","you are my only love","you are my charming hero"],
            "what is your name": ["my name is tobimaru","i am tobimaru"],
            "open documents": ["nautilus /home/veenit/Documents &","shell","sure","ok","as you wish","my pleasure","love to"],
            "open desktop": ["nautilus /home/veenit/Desktop &","shell","sure","ok","as you wish","my pleasure","love to"],
            "open downloads":["nautilus /home/veenit/Downloads &","shell","sure","ok","as you wish","my pleasure","love to"],
            "open pictures":["nautilus /home/veenit/Pictures &","shell","sure","ok","as you wish","my pleasure","love to"],
            "open music":["nautilus /home/veenit/Music &","shell","sure","ok","as you wish","my pleasure","love to"],
            "open video":["nautilus /home/veenit/Videos &","shell","sure","ok","as you wish","my pleasure","love to"],
            "open vscode":["code","shell","sure","ok","as you wish","my pleasure","love to"],
            "open vscode in documents":["code /home/veenit/Documents","shell","sure","ok","as you wish","my pleasure","love to"],
            "open vscode in desktop":["code /home/veenit/Desktop","shell","sure","ok","as you wish","my pleasure","love to"],
            "open google chrome":["google-chrome &","shell","sure","ok","as you wish","my pleasure","love to"],
            "open brave":["brave-browser &","shell","sure","ok","as you wish","my pleasure","love to"],
            "open simplenote":["simplenote &","shell","sure","ok","as you wish","my pleasure","love to"],
            "open firefox":["firefox &","shell","sure","ok","as you wish","my pleasure","love to"],
            "open rhythmbox":["rhythmbox &","shell","sure","ok","as you wish","my pleasure","love to"],
            "open nautilus":["nautilus &","shell","sure","ok","as you wish","my pleasure","love to"],
            "open mines":["gnome-mines &","shell","sure","ok","as you wish","my pleasure","love to"],
            "open system monitor":["gnome-system-monitor &","shell","sure","ok","as you wish","my pleasure","love to"]
            }
        str1='' # str1 variable to hold the sentence value
        if(x in reflections.keys() and len(reflections[x])>1 and reflections[x][1]=="shell"): # to comapre if input is in the dictionary and it is a shell comman
            os.system(reflections[x][0])  # to execute the shell command
            k=len(reflections[x]) # to find the length of the respective key value list
            k=random.randrange(2,k,1) # to generate the random index for the input sentence
            str1=''.join(reflections[x][k]) # to convert the list string to string
        elif(x in reflections.keys()):
            k=len(reflections[x]) # to find the length of the respective key value list
            k=random.randrange(0,k,1) # to generate the random index for the input sentence
            str1=''.join(reflections[x][k]) # to convert the list string to string
        else:
            str1="i didn't get it"
        return str1  # to return the string


# this the agent class which will perform the respective operatin
class Agent(table):
    # to take the input and perform the respective operation on the sentence and to generate the respective output
    def  sentencefinder(self):

        #to take the word input
        language='en'
        x=sr.Recognizer()
        with sr.Microphone() as source:
            audio=x.listen(source)
        k=x.recognize_google(audio)

#to convert all the letter to lower case
        k=k.lower()

        #to decide  the time for which we want to delay the ouput
        # t=0.5

        while(k!="exit"): # infinite loop until the user types exit or close
            if(k=="bye"):               # exit the program if the user the types yes after giving the output as bye
                print("bye")
                break                           # break the loop after giving the output 
             # time.sleep(t)               # time delay to make the user think that the computer is proessing like human being and then giving the output
            p=self.reflextable(k)       # check the respective sentence in the dictinoary
            speech=gTTS(text=p,lang=language,slow=False)
            speech.save("output.mp3")
            os.system("play output.mp3 &")
            with sr.Microphone() as source:
                audio=x.listen(source)
            
            try:
                k=x.recognize_google(audio)
                k=k.lower()
                print(k)
            except sr.UnknownValueError:
                speech=gTTS(text="i didn't get it",lang=language,slow=False)
                speech.save("output.mp3")
                os.system("play output.mp3 &")

                            


def main():                             # main function to call the agent class functoin sentencefinder
    sentence=Agent()                    # creating the object to the class Agent
    sentence.sentencefinder()           # calling to the function sentencefinder


if __name__ =="__main__":             # to let the python know that the main function exits
    main()



    


