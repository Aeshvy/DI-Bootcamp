# ASCII Mini-Game

castle = """

                                       ,.=,,==. ,,_
                      _ ,====, _    |I|`` ||  `|I `|
                     |`I|    || `==,|``   ^^   ``  |
                     | ``    ^^    ||_,===TT`==,,_ |
                     |,==Y``Y==,,__| \L=_-`'   +J/`
                      \|=_  ' -=#J/..-|=_-     =|
                       |=_   -;-='`. .|=_-     =|----T--,
                       |=/\  -|=_-. . |=_-/^\  =||-|-|::|____
                       |=||  -|=_-. . |=_-| |  =|-|-||::\____
                       |=LJ  -|=_-. . |=_-|_| =||-|-|:::::::
                       |=_   -|=_-_.  |=_-     =|-|-||:::::::
                       |=_   -|=//^\. |=_-     =||-|-|:::::::
                   ,   |/&_,_-|=||  | |=_-     =|-|-||:::::::
                ,--``8%,/    ',%||  | |=_-     =||-|-|%::::::
            ,---`_,888`  ,.'''''`-.,|,|/!,--,.&\|&\-,|&#:::::
           |;:;K`__,...;=\_____,=``           %%%&     %#,---
           |;::::::::::::|       `'.________+-------\   ``
          /8M%;:::;;:::::|                  |        `-------
"""

knight = """
      _,.
    ,` -.)
   ( _/-\\-._
  /,|`--._,-^|            ,
  \_| |`-._/||          ,'|
    |  `-, / |         /  /
    |     || |        /  /
     `r-._||/   __   /  /
 __,-<_     )`-/  `./  /
'  \   `---'   \   /  /
    |           |./  /
    /           //  /
\_/' \         |/  /
 |    |   _,^-'/  /
 |    , ``  (\/  /
  \,.->._    \X-=/^
  (  /   `-._//^`
   `Y-.____(__}
    |     {__)
          ()
"""


doors = """
      ______             ______             ______
   ,-' ;  ! `-.       ,-' ;  ! `-.       ,-' ;  ! `-.
  / :  !  :  . \     / :  !  :  . \     / :  !  :  . \\
 |_ ;   __:  ;  |   |_ ;   __:  ;  |   |_ ;   __:  ;  |
 )| .  :)(.  !  |   )| .  :)(.  !  |   )| .  :)(.  !  |
 |"    (##)  _  |   |"    (##)  _  |   |"    (##)  _  |
 |  :  ;`'  (_) (   |  :  ;`'  (_) (   |  :  ;`'  (_) (
 |  :  :  .     |   |  :  :  .     |   |  :  :  .     |
 )_ !  ,  ;  ;  |   )_ !  ,  ;  ;  |   )_ !  ,  ;  ;  |
 || .  .  :  :  |   || .  .  :  :  |   || .  .  :  :  |
 |" .  |  :  .  |   |" .  |  :  .  |   |" .  |  :  .  |
 |mt-2_;----.___|   |mt-2_;----.___|   |mt-2_;----.___|
        RED              YELLOW               BLUE
"""

canine = '''

                                          _.-.._         _._
                                     _,/^^,y./  ^^^^"""^^\= \\
                                     \y###XX;/  /     \    ^\^\\
                                       `\Y^   /   .-==||==-.)^^
                   ,.-=""""=-.__       /^ (  (   -/<0>++<0>(
                 .^      .: . . :^===(^ \ (  (  /```^^^^^^^)
                /      .: .,GGGGp,_ .(   \   /    /-(o'~'o))
              .^      : . gGG"""YGG}. \   )   / /  _/-====-\\
             /       (. .gGP  __ ~~ . .\  \  (    (  _.---._)
            /        (. (GGb,,)GGp. . . \_-^-.__(_ /______./
           (          \ . `"!GGP^ . . . . ^=-._--_--^^^^^~)
           (        /^^^\_. . . . . . . . . . . . . . . . )
           )       /     /._. . . . . . . . . . . . . ._.=)
           \      /      |  ^"=.. . . . . . . ._++""\"^    \\
            \    |       |       )^|^^~'---'~^^      \     )
            )   /        )      /   \                 \    \\
            |`  |        \     /\    \                (    /
            |   |         (   (  \ . .\               |   (
            )   |         )   )   ^^^^^^              |   |
           /. . \         |  '|                       )   (
           ^^^^^^         )    \                      /. . \\
                          / . . \                     ^^^^^^
                          ^^^^^^^
'''

death = '''

               ...
             ;::::;
           ;::::; :;
         ;:::::'   :;
        ;:::::;     ;.
       ,:::::'       ;           OOO\\
       ::::::;       ;          OOOOO\\
       ;:::::;       ;         OOOOOOOO
      ,;::::::;     ;'         / OOOOOOO
    ;:::::::::`. ,,,;.        /  / DOOOOOO
  .';:::::::::::::::::;,     /  /     DOOOO
 ,::::::;::::::;;;;::::;,   /  /        DOOO
;`::::::`'::::::;;;::::: ,#/  /          DOOO
:`:::::::`;::::::;;::: ;::#  /            DOOO
::`:::::::`;:::::::: ;::::# /              DOO
`:`:::::::`;:::::: ;::::::#/               DOO
 :::`:::::::`;; ;:::::::::##                OO
 ::::`:::::::`;::::::::;:::#                OO
 `:::::`::::::::::::;'`:;::#                O
  `:::::`::::::::;' /  / `:#
   ::::::`:::::;'  /  /   `#

'''

treasure = '''

*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************

'''




print(castle)
print('''
Welcome to Treasure Island.
Your mission is to find the treasure.
''')





first_path = (input("You find a castle in the woods. Where do you want to go?\nType 'enter' or 'leave' ")).lower()

if first_path == 'enter':
    print(knight)

    second_path = (input("You meet a Knight inside the castle. What do you do?\nType 'talk' or 'fight' ")).lower()

    if second_path == 'talk':
        print(doors)

        third_path = (input("Your charisma has proven worthwhile. The Knight let you pass. Which door do you pick?\nRED, YELLOW or BLUE? ")).lower()

        if third_path == 'red':
            print(treasure)
            print("You entered the red door and found the treasure!")
        elif third_path == 'yellow':
            print(death)
            print("You entered the yellow door and fell to your death.\nGame Over.")
        elif third_path() == 'blue':
            print(canine)
            print("You entered the blue door. A giant canine has shred you into pieces.\nGame Over.")
    else: print("The Knight has won the battle. You lost the fight.\nGame Over.")

else: print("You left the abandoned castle and died in the woods of starvation.\nGame Over.")



# Ride Height Calculator

height = (int(input("Welcome aboard!\nHow tall are you? ")))
price = 0

if height >= 120:
    age = (int(input("You're tall enough to enter.\nHow old are you? ")))
    if age <= 12:
        price = 5
        print("Child tickets are $5")
    elif 12 <= age <=18:
        price = 10
        print("Youth tickets are $10")
    elif 44 <= age <= 55:
        price = 0
        print("Seens like you're having a midlife crisis. The price is free!")
    else:
        price = 15
        print("Adult tickets are $15")

    photo = input("Would you like a photo? (Type 'y' for Yes or 'n' for No): ")
    if photo.lower() == 'y':
        price += 3
        print(f"Your total price is ${price}.")
    else:
        print(f"Your total price is ${price}.")

else:
    print("You are not tall enough!")


# Pizza Place

print("Welcome to Little Rome Pizza Deliveries!")

size = input("What size pizza would you like? S, M or L: ")
pepperoni = input("Do you want extra pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

price = 0

if size.lower() == "s":
    print("Small pizza is $15")
    price += 15
elif size.lower() == 'm':
    print("Medium pizza is $20")
    price += 20
elif size.lower() == 'l':
    print("Large pizza is $25")
    price += 25
else:
    print("Input error!")

if pepperoni.lower() == 'y':
    if size == 's':
        price += 2
    else:
        price += 3

if extra_cheese.lower() == 'y':
    price += 1

    
print(f'your total is ${price}. Enjoy your meal!')
