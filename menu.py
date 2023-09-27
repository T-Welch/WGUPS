import random

#this is for printing the menu in the user interface, I had a bunch of messages of the day loaded and 
#would call a random one for inspiration and to give it a unique kind of feel but it was corny
#and unnecessary for the program to function so i removed it. i will add it back in if/when I add 
#this program to my portfolio though 
class Menu:    
    def welcomeMessage() -> None:
        print('**********************************************************************************\n')
        print('                    Welcome to Trevor\'s WGUPS implementation!')
        print('          Please refer to this menu in order to interact with this program.')
        # print('              ' + Menu.MOTD())
        print('\n**********************************************************************************\n\n')
        
    #created a function for this for extensibility later for portfolio project
    
    def optionMenu() -> None:
        print('Enter (Q) to quit.')
        print('Enter M to display this menu')
        print('Enter (S) + [time] to view the status of packages at a given time.')
        print('Enter (p) + [packageID] to view the status of a single package.')
        print('An example of a status lookup request is as follows:')
        print('\"S 09:30:10\" or \"p 21\"')
        print()
        
        
        