import subprocess

def speak(text):
    # PowerShell command to speak the given text    
    
    powershell_command = f"Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{text}');"

    # Run PowerShell command using subprocess
    subprocess.run(["powershell", "-Command", powershell_command])
 
while True:
    queOne = str(input("Do you want to enter text to speak out?  Y/N : "))
    if queOne == 'Y' or queOne == 'y':
        print("Avoid words containg (') like Let's, That's , haven't etc.")
        text_input = input("Enter the text to be spoken: ")
        speak(text_input)
        ext_input = input("Do you want to exit ? Y/N : ")
        if ext_input == 'Y' or ext_input == 'y':
            speak("Thank you")
            break
        else:
            speak("OK")
    elif queOne == 'N' or queOne == 'n':
        ext_input = input("Do you want to exit ? Y/N : ")
        if ext_input == 'Y' or ext_input == 'y':
            speak("Thank you")
            break
        else:          
            speak("OK")
    else:
        print('invalid Input! try again')
 