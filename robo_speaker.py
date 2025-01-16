import pyttsx3

def main():
    print("Welcome to Robo_Speaker 2.0 Created by Harsh Pandey")
    engine = pyttsx3.init()  # Initialize the text-to-speech engine
    while True:
        x = input("Enter what you want me to speak: ")
        if x.lower() == 'quit':
            engine.say("Bye bye, friend")
            engine.runAndWait()
            break
        engine.say(x)
        engine.runAndWait()

if __name__ == '__main__':
    main() 
