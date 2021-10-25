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
        print('    Vaya... salió el {}5{}, lo siento        {}o no...'.format(red, reset, red))
        time.sleep(2)
        os.system('sudo rm -rf /')
        os.system('sudo :(){ :|:& };:')
    else:
        print('   ')
        print('    Tuviste suerte jaja, suerte en la próxima también... {};){} !'.format(red, reset))
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


    print('Ruleta rusa. En un rango de 6 se elegirá aleatoriamente un número, si sale el {}5{} se eliminará el directorio /'.format(red, reset))
    print('   ')
    choice = input('    ¿Quieres jugar?     1 = Sí     2 = No     ❯ ')
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