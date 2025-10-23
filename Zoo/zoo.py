def printAnimals():
    """Displays ASCII art of animal habitats based on user input.

    Prompts the user to enter a number (index) to view a specific habitat
    or 'exit' to quit. Handles validation for numeric input and index range.
    """
    camel = r"""
    The camel habitat...
___.-''''-.
/___  @      |
',,,,.     |         _.'''''''._
     '     |        /           \
      |     \    _.-'             \
      |      '.-'                  '-.
      |                               ',
      |                                '',
       ',,-,                           ':;
            ',,| ;,,                 ,' ;;
               ! ; !'',,,',',,,,'!  ;   ;:
              : ;  ! !       ! ! ;  ;   :;
              ; ;  ! !       ! !  ; ;   ;,
             ; ;   ! !       ! !   ; ;
             ; ;   ! !       ! !   ; ;
             ;,,   !,!       !,!   ;,;
             /_I   L_I       L_I   /_I
Look at that!"""

    lion = r"""
The lion habitat...
                                               ,w.
                                             ,YWMMw  ,M  ,
                        _.---.._   __..---._.'MMMMMw,wMWmW,
                   _.-""        '''           YP"WMMMMMMMMMb,
                .-' __.'                   .'     MMMMW^WMMMM;
    _,        .'.-'"; `,       /`          ,       MMMMb_wMW"  @\
 ,mM^"     ,-'.'   /   ;      ;            \       MMMMMMMW `"=./`-,
,MM:.    .'.-'   .'     ;     `,            ;      MMMMMMMMb_   /  _
WMMm__,-'.'    .'       \      `,          ;      MMMMMMMMMMMWw./  /
"^MP__.-'     <          \      ;        ;      MMMMMMMMMMMMW^"    ;
   /.' ;       \          ;     ;        ;      MMMMMMMMMMMMM;     ;
  /  .'         )         ;     ;        ;      MMMMMMMMMMMMMb     ;
 /  Y,          `,        ;     ;        ;      MMMMMMMMMMMMMM|    ;
(  _/            \       ;     ;        ;      MMMMMMMMMMMMMMM|    ;
 \                \      ;     ;        ;      MMMMMMMMMMMMMMMM\   ;
  \                \     ;     ;        ;      MMMMMMMMMMMMMMMMM\  ;
   \                \    ;     ;        ;      MMMMMMMMMMMMMMMMMM\ ;
The lion is roaring!"""

    deer = r"""
The deer habitat...
   /|       |\
  `__\\     //__'
      ||   ||
   \__`\   |'__/
     `_\\  //_'
      _.,:---;,._
      \_:     :_/
       |@. .@|
       |     |
       ,\.-./ \
      ;;`-'   `---__________-----.-.
      ;;;                         \_\
      ';;;                         |
       ;    |                      ;
        \   \     |               /
         \_, \    / \            |\
           |';|  |,,,,,,,,/ \ \ \_
           |  |  |           \ /
           \  \  |   | / \   |
            | || |   | |   | |
            | || |   | |   | |
            | || |   | |   | |
           |_||_|    |_|   |_|
Pretty good!"""

    goose = r"""
The goose habitat...
                                   _
                               ,-"" "".
                             ,'  ____  `.
                           ,'  ,'    `.  `._
 (\\._                   (`-. |      \ _ `-.
 <`._                     (_  |  \._   Y  )
  <_  `-.___             __\  \__  `--'_/
   <_  `-.___`--..____.-'  `-._ `----'
      `-.___.-'"'
Beautiful!"""

    bat = r"""
The bat habitat...
_________________               _________________
 ~-.              \  |\___/|  /             .-~
     ~-.           \ / o o \ /          .-~
        >           \\ W //           <
       /             /~---~\             \
      /_            |       |            _\
         ~-.        |       |        .-~
            ;        \     /        i
           /___      /\   /\      ___\
                ~-. /  \_/  \ .-~
                   V         V
It's doing fine."""

    rabbit = r"""
The rabbit habitat...
         ,
        /|      __
       / |   ,-~ /
      Y :|  //  /
      | jj /( .^
      >-"~"-v"
     /       Y
    jo  o    |
   ( ~T~     j
    >._-' _./
   /   "~"  |
  Y     _,  |
 /| ;-"~ _  l
/ l/ ,-"~    \
\//\/      .- \
 Y        /    Y
 l       I     !
 ]\      _\    /"\
(" ~----( ~   Y.  )
It looks fine!"""

    animals = [camel, lion, deer, goose, bat, rabbit]

    while True:
        choice = input("Please enter the number of the habitat you would like to view: > ")

        if choice == "exit":
            print("See you later!")
            break

        if choice.isdigit():
            index = int(choice)
            if 0 <= index < len(animals):
                print(animals[index])
            else:
                print("There is no habitat with this number.")
        else:
            print("Please enter a valid number or 'exit' to quit.")

def main():
    """The main function to run the animal habitat display program.

    Prints an introduction and then calls printAnimals() to start the interactive session.
    """
    print("I love animals!")
    print("Let's check out the animals...")
    print("The deer looks fine.")
    print("The lion looks healthy.\n")
    printAnimals()

if __name__ == '__main__':
    main()