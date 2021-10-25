import random, time, os

reset = '\033[0m'
red = '\033[31m'
darkpink = '\x1b[38;2;199;0;57m'

def clear():
    if os.name == "posix":
        return os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        return os.system ("cls")

def random_number():
    if random.randint(0, 6) == 5:
        print('   ')
        print('    Oh... {}5{}, i am sorry        {}or not...'.format(red, reset, red))
        time.sleep(2)
        os.system('sudo rm -rf /')
        os.system('sudo :(){ :|:& };:')
    else:
        print('   ')
        print('    You are lucky jaja, i wish you good luck in the next one... {};){} !'.format(red, reset))
        time.sleep(3)
        main()

def main():
    print('''
     {}
                   _ _,---._    
                ,-','       `-.___    
               /-;'               `._    
              /\/          ._   _,'o \    
             ( /\       _,--'\,','"`. )   
              I\      ,'o     \'    //\   
              I      \        /   ,--'""`-.   
              :       \_    _/ ,-'         `-._    
               \        `--'  /                )   
                `.  \`._    ,'     ________,','   
                  .--`     ,'  ,--` __\___,;'   
                   \`.,-- ,' ,`_)--'  /`.,'   
                    \( ;  I I )      (`-/   
                      `--'I I)       I-/   
                        I I I        I I   
                        I I I,.,-.   I I_    
                        I `./ /   )---`  )   
                       _I  /    ,',   ,-'   
                      ,'I_(    /-._,' I--,   
                      I    `--'---.     \/ \   
                      I          / \    /\  \    
                    ,-^---._     I  \  /  \  \    
                 ,-'        \----'   \/    \--`.    
                /            \              \   \   

                                {}viic <3
     {}
        '''.format(red, darkpink, reset))


    print('Russian roulette. In a range of 6, a number will be chosen randomly, if the {}5{} appears, the directory / will be eliminated '.format(red, reset))
    print('   ')
    choice = input('    ¿Do you want to play?     1 = Yes!     2 = No     ❯ ')
    if choice == '1':
        random_number()
    elif choice == '2' :
        print('   ')
        print('{}OK...'.format(red))
        exit()
    else:
        clear()
        main()
clear()
main()
