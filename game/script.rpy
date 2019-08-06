# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Elon")

define f = Character("Henrik")

define r = Character("Robin")

define t = Character("Ted")

define o = Character("Obama")

define g = Character("Grimes")

define c = Character("Cheeki")


#define pov = Character("[povname]")


# The game starts here.

# python:
    #povname = renpy.input("What is your name?")
    #povname = povname.strip()

    #if not povname:
        #povname = "Pika Chu"

#pov "My name is [povname]!"

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    #scene bg americana at truecenter:
        #zoom 1.5
    #show elon wtf at truecenter

    #e "What do you mean you've been working for Fisker this whole time?!"

    scene bg black at truecenter
    with fade

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    show elon pray at truecenter:
        zoom 0.6
    with dissolve

    # These display lines of dialogue.

    e "{cps=20}Hello.{/cps=20}"

    e "{cps=20}You may know me as the insanely successful {i}billionare{/i} Elon Musk, {/cps=20}"

    e "{cps=20}founder, CEO, and lead designer of {i}SpaceX{/i}; {/cps=20}"

    e "{cps=20}or as the co-founder, CEO, and product architect of {i}Tesla Motors{/i}. {/cps=20}"

    e "{cps=20}But starting today, I'm just your boss.{/cps=20}"

    image elon smile = "elon smile.png"
    show elon smile at truecenter:
        zoom 1.2

    e "{cps=20}There is much more to who I am than just my money.{/cps=20}"

    e "{cps=20}For better or worse, {/cps=20}"
    e "{cps=20}I think you'll realize that I am much different than the public view.{/cps=20}"

    show elon what at truecenter:
        zoom 0.3

    e "{cps=30}But that's enough about me for now.{/cps=30}"

    $ player_name = renpy.input("What is your name?")

    $ player_name = player_name.strip()

    if player_name == "Henrik Fisker" or player_name == "henrik fisker":
        $ player_name="not henrik"
        show elon what
        e "{cps=20}You're not Fisker!{/cps=20}"
        e "{cps=20}Don't sully your image with our rival's name!{/cps=20}"

    if player_name == "not henrik" or player_name == "Not Henrik" or player_name == "not Henrik":
        $ player_name="funny one"
        show elon smile
        e "{cps=20}You're a funny one!{/cps=20}"
        e "{cps=20} I think you'll fit in just fine at Tesla!{/cps=20}"

    if player_name == "":
        $ player_name="Space X"

    if player_name == "Elon Musk" or player_name == "elon musk":
        $ player_name="not elon"
        e "{cps=20}I'm flattered, but I assure you{/cps=20}"
        show elon smile
        e "{cps=20}you're not Elon, I am.{/cps=20}"

    if player_name=="not Elon" or player_name=="not elon" or player_name=="Not Elon":
        $ player_name="Doppel Ganger"
        show elon smile
        e"{cps=20}You're a funny one!{/cps=20}"
        e"{cps=20}I think you'll fit in just fine at Tesla!{/cps=20}"


    show elon stand:
        zoom 1.1


    e "{cps=20}Wonderful to meet you, %(player_name)s!{/cps=20}"

    e "{cps=20}I hope you enjoy working with me at Tesla.{/cps=20}"

    e "{cps=40}Well, see you {i}tomorrow{/i}!{/cps=40}"

    hide elon stand

    scene bg suss with fade

    show henrik peeved at truecenter with dissolve:
        zoom 2.2

    f "{cps=20}I'm glad he's finally gone.{/cps=20}"

    f "{cps=30}'Who am {i}I{/i}?' You ask?{/cps=30}"

    f "{cps=20}That is irrelevant.{/cps=20}"

    f "{cps=30}But I'll tell you what is not irrelevant:{/cps=30}"

    f "{cps=10}{i}Tesla Automotive's highly confidential car blueprints{/i}{/cps=10}"

    f "{cps=20}It's rather simple.{/cps=20}"

    f "{cps=10}You {s}steal{/s} ahem, {i}retrieve{/i} the plans for me and I'll see to it that you never have to work a single day again.{/cps=10}"

    menu:
        "Sounds good to me!  I'm all for extra pocket money.":
            f "{cps=10}Splendid.{/cps=10}"
            f "{cps=30}Please take my card.  I will be in contact with you.{/cps=30}"
            f "{cps=20}Oh, and if anyone feels inclined to ask to whom you were speaking...{/cps=20}"
            f "{cps=30}You know what to do. {/cps=30}"
            f "{cps=30}I look forward to working with you, %(player_name)s{/cps=30}"


        "I am offended that you would even think for a second that I would betray Elon.":
            f "{cps=30} I see...{/cps=30}"
            f "{cps=30} You are certainly welcome to reconsider.{/cps=30}"
            f "{cps=30} Here is my card. {/cps=30}"
            f "{cps=30} Call me should you change your mind. {/cps=30}"
            f "{cps=20} If anyone asks, I was never here. {/cps=20}"
            f "{cps=10} Good day. {/cps=10}"



    label after_menu:
        hide henrik peeved
        "{cps=20} You read the card the mysterious man gave to you.{/cps=20}"
        "{cps=10} HENRIK FISKER {/cps=10}"
        "{cps=10} CEO OF FISKER AUTOMOTIVE CO {/cps=10}"
        "{cps=10} CELL: 818-XXX-XXXX {/cps=10}"
        "{cps=20} There was something ominous about the man and his lofty title.{/cps=20}"
        "{cps=20} You brushed off your misgivings about Henrik, and steeled yourself to face what unknowns tommorrow would bring.{/cps=20}"
    #povname = renpy.input(prompt, default='your name', allow=None, exclude='{}', length=None, with_none=None,  pixel_width=None)

    scene bg elonroom at truecenter
    show elon frown at right with fade:
        zoom 1.2

    e "{cps=30} I have a bad feeling about tommorrow... {/cps=30}"

    e "{cps=30}What about you, Cheeki?{/cps=30}"

    show cheeki normal at top with fade:
        zoom 1.5

    c "{cps=25}CHIRP!{/cps=25}"

    e "{cps=30}You're right, tommorrow is gonna be just fine.{/cps=30}"

    e "{cps=30}The sinking feeling in my gut must just be the Taco Bell from earlier. {/cps=30}"

    e "{cps=30}Let's go to bed, friend.{/cps=30}"










    # This ends the game.

    return
