import random
class Menu:
    
    def MOTD() -> str:
        motds = [
        "I hope you have a good day and good things happen to you.",
        "Remember, every moment is an opportunity to shine.",
        "May today be filled with sunshine and smiles for you.",
        "Sending positive vibes your way for a wonderful day ahead!",
        "Every challenge you face is an opportunity to grow.",
        "Today is a blank canvas, paint it beautifully.",
        "May your day overflow with joy and success.",
        "Wishing you strength and serenity for today.",
        "Embrace the present moment and find joy in it.",
        "You're capable of amazing things. Never forget that.",
        "Today, be the reason someone else smiles.",
        "Believe in the power of positivity today.",
        "Sending you energy and light for the day ahead.",
        "Remember, kindness and patience go a long way.",
        "Take a deep breath, cherish the moment, and move forward with confidence."
        ]
        return(random.choice(motds))
    
    #this is unnccessary, just for looks
    
    def welcomeMessage() -> None:
        print('**********************************************************************************\n')
        print('                    Welcome to Trevor\'s WGUPS implementation!')
        print('          Please refer to this menu in order to interact with this program.')
        print('              ' + Menu.MOTD())
        print('\n**********************************************************************************\n\n')
        
    #created a function for this for extensibility later for portfolio project
    
    def optionMenu() -> None:
        print('Enter (Q) to quit.')
        print('Enter M to display this menu')
        print('Enter (S) + [time] to view the status of packages at a given time.')
        print('An example of a status lookup request is as follows:')
        print('S 9:30')
        
        
        