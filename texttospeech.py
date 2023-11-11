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


#89 111 117 39 118 101 32 100 111 110 101 32 115 111 109 101 116 104 105 110 103 46 32 68 105 100 110 39 116 32 121 111 117 63