import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pandas as pd
import matplotlib.pyplot as plt
"""
_________________________________________________________________________________________________________________________________
Adding Some codes to read the Data set using the voice commands. So please Don't try it at home to show every one the magic.
as you also having titenium in your blood and may serious issue for your family member.

"""
# Read the data set from online is best idea

def dataindir():
    lists = os.listdir()
    matching = [s for s in lists if ".csv" in s]
    try:
        print(f"Boss the available data sets are \n {matching}")
        speak(f"Boss the available data sets are{matching}")
        speak("Boss Choose one of the data set to read by saying its positional number")
        chance=2
        while chance==2:
            try:
                choose = int(takeCommand())
                global df
                df = pd.read_csv(matching[choose-1])
                df.columns = map(str, df.columns)
                df.columns = df.columns.str.lower()
                global columnnames
                columnnames = df.columns
                chance=3
            except:
                speak("unable to read the data")
                chance=2
    except:
        speak("sorry boss cant find more data set")

#__________________________________________________________________________________________________________________________________
# Search for the voice engines in the computer
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices)

print(voices[1].id)  # its the voice of ZIRA
print(voices[0].id)
# Set engine the voice as your requirment

engine.setProperty('voice', voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    # Engine the Speak the audio string
# Function to wish me
def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Aman")
    elif hour >= 12 and hour <= 18:
        speak("Good Afternoon Aman")
    else:
        speak("Good Evening Aman")
    speak("I am your personal Assistent")
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognising")
        query = r.recognize_google(audio, language='en-in')
        print("User Said: ", query)
    except Exception as e:
        speak(e)
        speak("Sorry BOSS, I can't understand. Say That Again...")
        return 'None'
    return query

if __name__ == "__main__":
    wish()
    a = 1
    b = 1
    # Infinite while loop
    while a == 1:
        query = takeCommand().lower()
        b=1
        #logics to execute many tasks as desired
        if 'wikipedia' in query:
            speak("searching wikipedia...")
            query = query.replace("Wikipedia", " ")
            if 'aman' in query:
                speak("Sorry Boss Your name in not registered in Wikipedia ")
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("Accorging to wikipedia ")
                print(results)
                speak(results)
            except:
                speak('Sorry Sir, I cant find any result from wikipedia')
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
        elif 'open google' in query:
            webbrowser.open('google.com')
        elif 'play music' in query:
            music_dir = "E:\\ENTAIRTENTMENT\\VDO\\hbd\\Songs"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
            a = 2
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H")
            if int(strTime) > 12:
                strTime = str(int(strTime) - 12)
            print(strTime)
            time = datetime.datetime.now().strftime("%M:%S")
            print(f"Sir, The time is {strTime}:{time}")
            speak(f"Sir, The time is {strTime}:{time}")
        elif 'exit' in query:
            speak("Boss, Good bye, Feel free to call me, when ever you want")
            a = 2
        elif 'are you doing' in query:
            speak(" I am Listening to you ! ")
            speak(" I can open google... Open youtube... open app you want... say you date and time... try me .. i will be an good assistant")
        elif 'good joke' in query:
            speak("Sorry I dont tell good joke like cortana.becaust you have not tought me about it")
            """
            I am going to write an data query for the exploration of data using the virtual assistant 
            Lets have a look on the query . Its going to be so much fun.
            ________________________________xxxxxx Data Exploration xxxxxxx______________________________________________________________________________________
            """
        elif 'look on data' in query:
            dataindir()
            speak(f"Boss this Data contains {df.shape[0]} rows and {df.shape[1]} columns")
            speak(" You can have a look on head, tail of the data set. also you can visualize ,plot graph using the data set")
            speak("What Do you want to see boss")
            while b == 1:
                graph=1
                dataquery = takeCommand().lower()
                if 'head' in dataquery:
                    speak("Boss, Here is the first 5 rows of the data")
                    print(df.head())

                elif 'tail' in dataquery:
                    speak("Boss, Here is the last 5 rows of the data")
                    print(df.tail())
                elif 'information' in dataquery:
                    speak("Hello Boss, Here is the information of the data set")
                    print(df.info())
                elif 'column names' in dataquery:
                    speak("Boss the column names are")
                    print(columnnames)
                    """
                    Graph plotting Module For plotting interactive graph using the voice command
                    ________________________XXXXXXXX----GRAPH-----XXXXXXXXX________________________________________
                    """
                elif 'plot graph' in dataquery:
                    speak("Graph of which category boss : ")
                    graph = 1
                    while graph ==1:
                        graphquery = takeCommand().lower()
                        if 'change colours' in graphquery:
                            speak("Which color you want")
                            colour = takeCommand().lower()
                            coll = str(colour)
                            speak(f"ok boss we set the color of all plot to {coll}")
                        elif 'histogram' in graphquery:
                            print(columnnames)
                            speak("Which column boss")
                            columnquery = takeCommand().lower()
                            if columnquery in columnnames:
                                speak("Ok boss let me plot")
                                try:
                                    df[columnquery].plot(kind = 'hist',color=coll)
                                    plt.show()
                                except:
                                    df[columnquery].plot(kind='hist')
                                    plt.show()
                            else:
                                speak(
                                    "Ok Boss I am unable to find, so kindly write the position of the column name")
                                print("Write the column name here : ")
                                numberofcol = int(input()) + 1
                                df.iloc[:, numberofcol].hist()
                                plt.show()
                        elif 'scatter plot' in graphquery:
                            print(columnnames)
                            speak("Boss, Which will be on x axis")
                            xaxis = takeCommand().lower()
                            if xaxis in columnnames:
                                pass
                            else:
                                speak(
                                    "Ok Boss I am unable to find, so kindly write the position of the column name")
                                print("Write the column number here : ")
                                numbex = int(input())
                                xaxis = columnnames[numbex-1]
                            speak("Boss, Which will be on y axis")
                            yaxis = takeCommand().lower()
                            if yaxis in columnnames:
                                pass
                            else:
                                speak(
                                    "Ok Boss I am unable to find, so kindly write the position of the column name")
                                print("Write the column number here : ")
                                numbey = int(input())
                                yaxis = columnnames[numbey - 1]
                            try:
                                plt.scatter(x=xaxis,y=yaxis,data=df,color=coll)
                                plt.show()
                            except:
                                try:
                                    plt.scatter(x=xaxis, y=yaxis, data=df)
                                    plt.show()
                                except:
                                    speak("Sorry boss unable to plot")
                            # speak("Sorry boss, this is not available, its under development")
                        elif 'box plot' in graphquery:
                            speak("Which column boss")
                            print(columnnames)
                            columnquery = takeCommand().lower()
                            if columnquery in columnnames:
                                speak("Ok boss let me plot")
                                try:
                                    df[columnquery].plot(kind='box',color=coll)
                                    plt.show()
                                except:
                                    df[columnquery].plot(kind='box')
                                    plt.show()
                            else:
                                speak(
                                    "Ok Boss I am unable to find, so kindly write the position of the column name")
                                print("Write the column name here : ")
                                numberofcol = int(input()) + 1
                                df.iloc[:, numberofcol].box()
                                plt.show()
                        elif 'exit plot' in graphquery:
                            graph = 2
                            speak("Boss we will Exit the plotting menu, say what to do with data")
                            """
                            Graph plotting Module For plotting interactive graph using the voice command
                            ________________________XXXXXXXX----GRAPH ENDS HERE-----XXXXXXXXX________________________________________
                            """
                elif 'exit data' in dataquery:
                    speak("ok boss say What to do next")
                    b=2
        else:
            speak(f"I think you say..!{query}")







