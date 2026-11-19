"""# ============================================================

# OAKHAVEN: WINGS OF TOMORROW

# ACT I — A FOX WITHOUT A HOME

# SCENE 1 — A VERY LONG ROAD

# ============================================================

# ------------------------------------------------------------

# CHARACTERS

# ------------------------------------------------------------

define rowan = Character(

    "Rowan",

    color="#e89a55",

    image="rowan"

)

define thought = Character(

    "Rowan",

    color="#e89a55",

    image="rowan",

    what_italic=True

)

define driver = Character(

    "Bus Driver",

    color="#aab8c8"

)

define elliot = Character("Elliot", color="#a7c98a")

# ------------------------------------------------------------

# PLAYER DATA

# ------------------------------------------------------------

default wallet = 35

default medical_debt = 85000

default brother_reply = ""

default first_destination = ""

default interview_complete = False

default breakfast_purchased = False

default current_location = "City Bus"

default elliot_met = False

default elliot_friendship = 0

default cafe_visited = False

default breakfast_choice = ""

default breakfast_cost = 0

default breakfast_eaten = False

default cafe_quest_unlocked = False

default housing_info_found = False

# ------------------------------------------------------------

# BACKGROUNDS

# Backgrounds are loaded from game/images/backgrounds/.

# ------------------------------------------------------------

image bg bus = "images/backgrounds/bg_bus.png"

image bg town = "images/backgrounds/bg_town.png"

image bg terminal = "images/backgrounds/bg_terminal.png"

image bg market = "images/backgrounds/bg_market.png"

image bg cafe = "images/backgrounds/bg_cafe.png"

image bg park = "images/backgrounds/bg_park.png"

image bg company = "images/backgrounds/bg_company.png"

# Black transition background

image bg black = Solid("#000000")

# ------------------------------------------------------------

# ROWAN'S CHARACTER SPRITES

#

# All eight expressions use the same position and size.

# xalign 0.27 = right side of the screen.

# yalign 1.0 = bottom of the screen.

# zoom 1.25 = sprite size.

# ------------------------------------------------------------

image rowan neutral:

    "images/characters/rowan_neutral.png"

    xalign 0.27

    yalign 1.0

    zoom 1.25

image rowan happy:

    "images/characters/rowan_happy.png"

    xalign 0.27

    yalign 1.0

    zoom 1.25

image rowan nervous:

    "images/characters/rowan_nervous.png"

    xalign 0.27

    yalign 1.0

    zoom 1.25

image rowan embarrassed:

    "images/characters/rowan_embarrassed.png"

    xalign 0.27

    yalign 1.0

    zoom 1.25

image rowan sad:

    "images/characters/rowan_sad.png"

    xalign 0.27

    yalign 1.0

    zoom 1.25

image rowan angry:

    "images/characters/rowan_angry.png"

    xalign 0.27

    yalign 1.0

    zoom 1.25

image rowan surprised:

    "images/characters/rowan_surprised.png"

    xalign 0.27

    yalign 1.0

    zoom 1.25

image rowan tired:

    "images/characters/rowan_tired.png"

    xalign 0.27

    yalign 1.0

    zoom 1.25

# ============================================================

# LOCATION INTRODUCTION SCREEN

# ============================================================

screen location_title(location, time):

    zorder 50

    frame:

        xalign 0.5

        yalign 0.13

        padding (35, 20)

        background "#182330dd"

        vbox:

            spacing 8

            xalign 0.5

            text location:

                size 32

                color "#ffffff"

                xalign 0.5

            text time:

                size 18

                color "#c8d5df"

                xalign 0.5

# ============================================================

# PHONE NOTIFICATION SCREEN

# ============================================================

screen phone_notification(sender, timestamp, message):

    zorder 100

    modal True

    frame:

        xalign 0.97

        yalign 0.04

        xsize 480

        padding (24, 20)

        background "#202a36ee"

        vbox:

            spacing 12

            hbox:

                spacing 8

                text sender:

                    size 23

                    color "#ffffff"

                    bold True

                null width 1

                text timestamp:

                    size 15

                    color "#aab8c8"

            text message:

                size 19

                color "#ffffff"

                line_spacing 5

            null height 8

            textbutton "Continue":

                action Return()

                text_size 17

                text_color "#ffffff"

                text_hover_color "#83dfb0"

# ============================================================

# LOCATION INTRODUCTION HELPER

# Displays the location once, then removes it.

# ============================================================

label show_location_intro(location, time):

    show screen location_title(location, time)

    pause 2.5

    hide screen location_title

    return

# ============================================================

# GAME START

# ============================================================

label start:

    call act1_scene1

    call act1_scene2

    return

# ============================================================

# ACT I — SCENE 1

# A VERY LONG ROAD

# ============================================================

label act1_scene1:

    scene bg black

    with fade

    centered "{size=48}{color=#ffffff}OAKHAVEN{/color}{/size}"

    centered "{size=24}{color=#c8d5df}Wings of Tomorrow{/color}{/size}"

    pause 2.0

    centered "{size=22}ACT I{/size}"

    centered "{size=32}A Fox Without a Home{/size}"

    pause 2.0

    # --------------------------------------------------------

    # CITY BUS — 7:18 AM

    # --------------------------------------------------------

    scene bg bus

    with fade

    call show_location_intro(

        "Somewhere on the highway",

        "Monday — 7:18 AM"

    )

    show rowan neutral

    "The bus rumbled along the highway, its engine vibrating through the floor."

    "Outside the window, the scenery slowly began to change."

    "Tall buildings gave way to green hills, quiet neighborhoods, and distant forests."

    "Rowan sat alone beside the window, his backpack resting against his knees."

    "A young red fox with tired eyes, fluffy ears, and a tail that refused to sit still."

    "He had been traveling for hours."

    "And he was still a little bit terrified."

    rowan nervous "Okay..."

    rowan nervous "First day. New town. New job."

    thought nervous "Just don't mess this up."

    "He adjusted the strap of his backpack."

    thought nervous "Please, please, please let this work."

    pause 0.8

    # --------------------------------------------------------

    # MEDICAL BILL — 7:19 AM

    # --------------------------------------------------------

    call screen phone_notification(

        "MEDICAL BILLING",

        "7:19 AM",

        "Payment reminder: Your outstanding medical balance is $85,000. Please review your account."

    )

    show rowan sad

    "Rowan stared at the notification."

    "His ears slowly lowered."

    rowan sad "...Right."

    thought sad "Eighty-five thousand dollars."

    thought nervous "No pressure."

    "He locked his phone and placed it face-down on his lap."

    "For a moment, he just watched the passing scenery."

    pause 0.8

    # --------------------------------------------------------

    # BROTHER'S MESSAGE — 7:20 AM

    # --------------------------------------------------------

    call screen phone_notification(

        "Little Brother 💙",

        "7:20 AM",

        "Hey Rowan!! Are you there yet? Don't forget to eat breakfast, okay? You always skip it when you're nervous. Good luck with the job interview!! I know you can do it. Love you!! 💙"

    )

    show rowan happy

    "Rowan's expression softened."

    "A tiny smile appeared on his muzzle."

    thought happy "He's always looking out for me..."

    "He opened the message and started typing."

    menu:

        "What should Rowan reply?"

        "I'll be okay. Don't worry about me!":

            $ brother_reply = "I'll be okay. Don't worry about me!"

            rowan happy "I'll be okay. Don't worry about me!"

            "He added a little heart before sending it."

        "I miss you already. I'll call you tonight.":

            $ brother_reply = "I miss you already. I'll call you tonight."

            rowan sad "I miss you already. I'll call you tonight."

            "He hesitated before pressing send."

            "He really did miss him."

        "I'm nervous, but I'll do my best. Love you!":

            $ brother_reply = "I'm nervous, but I'll do my best. Love you!"

            rowan nervous "I'm nervous, but I'll do my best. Love you!"

            "It felt a little embarrassing to admit."

            "But it was true."

    "Message sent."

    thought happy "I have to make this work."

    pause 1.0

    driver "OakHaven coming up! We'll be arriving in a few minutes!"

    show rowan surprised

    "Rowan's ears perked up."

    # --------------------------------------------------------

    # APPROACHING OAKHAVEN — 7:24 AM

    # --------------------------------------------------------

    scene bg town

    with dissolve

    call show_location_intro(

        "Approaching OakHaven",

        "Monday — 7:24 AM"

    )

    show rowan surprised

    "There it was."

    "OakHaven."

    "A quiet town surrounded by rolling green hills and thick pine forests."

    "Its streets were lined with little shops, apartment buildings, and trees covered in morning dew."

    "A large sign stood near the entrance to town."

    centered "{size=30}{color=#ffffff}OAKHAVEN{/color}{/size}"

    centered "{size=17}{color=#dce8df}A COMMUNITY BUILT FOR TOMORROW{/color}{/size}"

    "Rowan watched the town pass by."

    rowan happy "It's... actually really pretty."

    "A little farther down the road, he spotted a large modern building."

    "The sign on its front read:"

    centered "{size=25}{color=#ffffff}OAKHAVEN REMOTE LOGISTICS{/color}{/size}"

    "The company he had applied to."

    "The company that might finally give him a chance."

    thought nervous "That's where I'm going."

    # --------------------------------------------------------

    # BUS TERMINAL — 7:42 AM

    # --------------------------------------------------------

    scene bg terminal

    with dissolve

    call show_location_intro(

        "OakHaven Central Bus Terminal",

        "Monday — 7:42 AM"

    )

    show rowan nervous

    "The bus pulled into the terminal."

    driver "OakHaven Central! Last stop!"

    "Rowan stood, grabbed his backpack, and carefully made his way toward the doors."

    rowan happy "Thank you!"

    driver "Have a good one, kid."

    "Rowan stepped down onto the pavement."

    "The bus pulled away behind him."

    "And just like that..."

    "He was here."

    pause 0.8

    "A cool morning breeze brushed through his fur."

    "Rowan looked around the terminal."

    "People hurried past with coffee cups and bags."

    "Somewhere nearby, a bicycle bell rang."

    "A car horn sounded in the distance."

    "Everything was unfamiliar."

    thought nervous "Okay. I can do this."

    "He opened his phone and checked his notes."

    centered "{size=30}{color=#ffffff}ROWAN'S TO-DO LIST{/color}{/size}"

    centered "{color=#83df9b}✓ Arrive in OakHaven{/color}"

    centered "{color=#ffffff}□ Find somewhere affordable to stay{/color}"

    centered "{color=#ffffff}□ Attend job interview — 10:00 AM{/color}"

    centered "{color=#ffffff}□ Get hired{/color}"

    centered "{color=#ffffff}□ Start paying off medical debt{/color}"

    pause 1.5

    "He looked at the last item for a little too long."

    thought sad "One step at a time."

    # --------------------------------------------------------

    # MARKET STREET — 7:48 AM

    # --------------------------------------------------------

    scene bg market

    with dissolve

    call show_location_intro(

        "Market Street",

        "Monday — 7:48 AM"

    )

    show rowan neutral

    "A short walk brought Rowan to the entrance of Market Street."

    "The street was beginning to wake up."

    "Shopkeepers were opening their doors."

    "A delivery van rolled past."

    "The smell of fresh bread drifted through the air."

    "Rowan spotted several places nearby."

    "A small café with warm lights glowing through its windows."

    "A convenience store on the opposite corner."

    "A path leading toward a green park."

    "And, farther down the road..."

    "The OakHaven Remote Logistics campus."

    "He checked his phone again."

    # --------------------------------------------------------

    # INTERVIEW REMINDER

    # --------------------------------------------------------

    call screen phone_notification(

        "INTERVIEW REMINDER",

        "7:48 AM",

        "Reminder: Your interview is scheduled for Monday at 10:00 AM. Location: Main Reception, OakHaven Logistics Campus. Please arrive 15 minutes early."

    )

    show rowan nervous

    "Rowan swallowed."

    rowan nervous "Ten o'clock..."

    thought nervous "I've got time."

    thought nervous "I've got plenty of time."

    pause 0.5

    "He looked down at his wallet."

    "Thirty-five dollars."

    "That was everything he had available right now."

    thought nervous "Maybe I should find something to eat."

    thought sad "Or maybe I should save the money."

    "His stomach gave a quiet growl."

    rowan embarrassed "...Traitor."

    "He let out a nervous little laugh."

    "For the first time that morning, he felt himself relax just a little."

    "He took a deep breath."

    show rowan neutral

    rowan "Okay."

    rowan "Let's make today count."

    # --------------------------------------------------------

    # FIRST DESTINATION CHOICE

    # --------------------------------------------------------

    menu:

        "Where should Rowan go first?"

        "Visit Whiskers Café":

            $ first_destination = "Whiskers Café"

            jump act1_scene1_cafe

        "Visit OakHaven Remote Logistics":

            $ first_destination = "OakHaven Remote Logistics"

            jump act1_scene1_company

        "Take a walk through Pinewood Park":

            $ first_destination = "Pinewood Park"

            jump act1_scene1_park

        "Explore Market Street":

            $ first_destination = "Market Street"

            jump act1_scene1_explore

# ============================================================

# BRANCH 1 — WHISKERS CAFÉ

# ============================================================

label act1_scene1_cafe:

    scene bg cafe

    with fade

    call show_location_intro(

        "Whiskers Café",

        "Monday — 8:05 AM"

    )

    show rowan nervous

    "A little bell jingled as Rowan approached the café."

    "Warm light spilled through the front windows."

    "The smell of coffee and freshly baked bread drifted outside."

    centered "{size=34}{color=#ffffff}WHISKERS CAFÉ{/color}{/size}"

    "Rowan looked through the window."

    "There were a few customers inside."

    "It seemed quiet."

    thought nervous "I could probably afford something small..."

    "He adjusted his backpack."

    show rowan happy

    rowan "Alright. Breakfast."

    "He reached for the door handle."

    "The little bell jingled again as he stepped inside."

    "Warm air surrounded him."

    "For the first time since arriving in OakHaven, Rowan felt like he could sit down."

    "Just for a little while."

    jump act1_scene1_end

# ============================================================

# BRANCH 2 — OAKHAVEN REMOTE LOGISTICS

# ============================================================

label act1_scene1_company:

    scene bg company

    with fade

    call show_location_intro(

        "OakHaven Remote Logistics",

        "Monday — 8:05 AM"

    )

    show rowan surprised

    "Rowan followed the road toward the logistics campus."

    "The building was larger up close."

    "Modern glass windows reflected the morning sunlight."

    "Small delivery drones could be seen flying between different sections of the campus."

    centered "{size=29}{color=#ffffff}OAKHAVEN REMOTE LOGISTICS{/color}{/size}"

    "Rowan stopped outside the main entrance."

    rowan surprised "Whoa..."

    "A drone zipped overhead."

    "Its small motors made a quiet buzzing sound."

    thought happy "So this is where I'll be working..."

    "He checked the time."

    "Still far too early for his interview."

    "He decided to take a closer look around the outside of the building."

    jump act1_scene1_end

# ============================================================

# BRANCH 3 — PINEWOOD PARK

# ============================================================

label act1_scene1_park:

    scene bg park

    with fade

    call show_location_intro(

        "Pinewood Park",

        "Monday — 8:05 AM"

    )

    show rowan happy

    "Rowan followed a nearby path toward the park."

    "Tall pine trees surrounded the walking trail."

    "The morning sunlight filtered through their branches."

    "A few birds chirped from somewhere overhead."

    "There were benches along the path and a small pond farther ahead."

    "Rowan found an empty bench and sat down."

    "His tail curled around his side."

    thought happy "Maybe I needed this."

    "For a moment, he didn't think about the interview."

    "Or the debt."

    "Or how much everything depended on today."

    "He simply listened to the birds."

    jump act1_scene1_end

# ============================================================

# BRANCH 4 — MARKET STREET

# ============================================================

label act1_scene1_explore:

    scene bg market

    with fade

    call show_location_intro(

        "Market Street",

        "Monday — 8:05 AM"

    )

    show rowan neutral

    "Rowan decided to explore the street before committing to anywhere."

    "There were little shops on both sides of the road."

    "A convenience store."

    "A clothing shop."

    "A small grocery store."

    "A few apartments sat above the businesses."

    "He wondered how much rent cost around here."

    thought nervous "I really need somewhere to stay."

    "He looked at the shop windows as he walked."

    thought happy "Maybe OakHaven wouldn't be such a bad place to start over."

    jump act1_scene1_end

# ============================================================

# SCENE 1 END

# ============================================================

label act1_scene1_end:

    scene bg black

    with fade

    centered "{size=36}{color=#ffffff}SCENE 1 COMPLETE{/color}{/size}"

    centered "{size=23}A Very Long Road{/size}"

    pause 1.5

    "Rowan's first morning in OakHaven had begun."

    "There was still a job interview ahead."

    "A place to find."

    "And a very long road toward paying off his family's debt."

    "But he wasn't alone in the world."

    "Not completely."

    "And perhaps OakHaven had more waiting for him than he expected."

    pause 1.5

    return

# ============================================================

# ACT I — SCENE 2: FIRST IMPRESSIONS

# ============================================================

label act1_scene2:

    $ current_location = "Whiskers Café"

    scene bg cafe

    with fade

    call show_location_intro("Whiskers Café", "Monday — 8:12 AM")

    $ cafe_visited = True

    show rowan nervous:

        xalign 0.27

        yalign 1.0

        zoom 1.25

    "The little bell above the café door jingled."

    "Warm air surrounded Rowan as he stepped inside."

    "The café smelled of freshly brewed coffee, warm bread, and something sweet."

    "A few customers sat at the tables."

    "Behind the counter stood a brown deer wearing a green cardigan and a pair of glasses."

    "He was arranging a few pastries when he noticed Rowan."

    show rowan surprised

    "The deer looked up and smiled."

    elliot "Oh! Good morning!"

    elliot "Welcome to Whiskers Café!"

    show rowan nervous

    rowan "G-Good morning..."

    elliot "First time here?"

    rowan "Y-Yeah. I just arrived in OakHaven."

    "The deer leaned against the counter."

    elliot "Really? Welcome to town, then!"

    elliot "I'm Elliot, by the way. I own the place."

    "He offered a friendly wave."

    $ elliot_met = True

    $ elliot_friendship += 1

    rowan "I'm Rowan. Nice to meet you."

    elliot "Nice to meet you too, Rowan!"

    "Elliot glanced at Rowan's backpack."

    elliot "So, what brings you to OakHaven?"

    menu:

        "What should Rowan tell Elliot?"

        "I'm here for a job interview.":

            $ elliot_friendship += 1

            rowan nervous "I'm here for a job interview."

            elliot "Oh! That's exciting!"

            elliot "Where at?"

            rowan "OakHaven Remote Logistics."

            elliot "Ah, the drone delivery company!"

            elliot "They're always looking for people."

            elliot "Good luck! I hope it goes well."

            thought happy "He seems nice..."

        "I just moved here. I'm trying to start over.":

            $ elliot_friendship += 2

            rowan sad "I just moved here. I'm trying to start over."

            elliot "Well, you've come to a pretty good place for that."

            elliot "OakHaven can be a little quiet sometimes, but the people are generally friendly."

            elliot "I'm sure you'll find your place."

            show rowan embarrassed

            rowan "Th-Thanks..."

            elliot "Of course!"

        "It's a little complicated...":

            rowan nervous "It's... a little complicated."

            elliot "Ah. Fair enough."

            elliot "You don't have to explain anything."

            elliot "Sometimes a fresh cup of coffee is all someone needs."

            show rowan happy

            rowan "Heh... yeah."

    "Elliot glanced toward the display case."

    elliot "Have you eaten breakfast yet?"

    "Rowan's stomach gave a small growl."

    show rowan embarrassed

    rowan "...Maybe."

    elliot "That sounds like a no."

    "Elliot chuckled."

    elliot "Well, we've got a few things available."

    elliot "Nothing too fancy, but everything's fresh."

    # --------------------------------------------------------

    # BREAKFAST MENU

    # --------------------------------------------------------

    $ breakfast_choice = ""

    $ breakfast_cost = 0

    menu:

        "What should Rowan order? (Wallet: $[wallet])"

        "Butter toast — $3":

            $ breakfast_choice = "Butter toast"

            $ breakfast_cost = 3

        "Fresh sandwich — $7":

            $ breakfast_choice = "Fresh sandwich"

            $ breakfast_cost = 7

        "Coffee — $4":

            $ breakfast_choice = "Coffee"

            $ breakfast_cost = 4

        "Apple pastry — $3":

            $ breakfast_choice = "Apple pastry"

            $ breakfast_cost = 3

        "Tea — $3":

            $ breakfast_choice = "Tea"

            $ breakfast_cost = 3

        "Nothing. Save the money.":

            $ breakfast_choice = "Nothing"

            $ breakfast_cost = 0

    if breakfast_cost > 0:

        if wallet >= breakfast_cost:

            $ wallet -= breakfast_cost

            $ breakfast_purchased = True

            $ breakfast_eaten = True

            rowan nervous "Could I... um... have the [breakfast_choice.lower()], please?"

            elliot "Absolutely!"

            "Elliot prepared Rowan's order."

            "A few moments later, he placed it on the counter."

            elliot "There you go!"

            rowan happy "Thank you!"

            "Rowan paid and carefully picked up his food."

            elliot "Enjoy!"

            "Rowan took a bite."

            "It was simple, but surprisingly good."

            thought happy "Oh... that's actually really nice."

        else:

            rowan embarrassed "Actually... I don't think I have enough."

            elliot "Oh! Don't worry about it."

            "Elliot put the food away."

            elliot "Maybe another time."

    else:

        rowan nervous "I think I'll save my money."

        elliot "That's alright!"

        elliot "Just don't forget to eat something later, okay?"

        rowan embarrassed "I'll try..."

    # --------------------------------------------------------

    # SITTING BY THE WINDOW

    # --------------------------------------------------------

    "Rowan found a small table beside the window."

    "He placed his backpack beside the chair and sat down."

    show rowan neutral

    "Outside, Market Street was slowly getting busier."

    "People walked past the café windows."

    "A delivery van stopped near the curb."

    "For a moment, Rowan almost forgot how nervous he had been."

    thought happy "Maybe this place isn't so bad."

    "He pulled out his phone."

    "His brother's earlier message was still open."

    "Rowan smiled faintly."

    thought happy "I should call him later."

    # --------------------------------------------------------

    # COMMUNITY NOTICEBOARD

    # --------------------------------------------------------

    "After finishing his breakfast, Rowan noticed a large noticeboard near the café entrance."

    "It was covered with colorful flyers and handwritten notes."

    "One flyer caught his attention."

    centered "{size=30}{color=#ffffff}OAKHAVEN COMMUNITY BOARD{/color}{/size}"

    centered "{size=23}{color=#a7c98a}COMMUNITY GATHERING{/color}{/size}"

    centered "{size=18}Pinewood Park — Saturday Morning{/size}"

    centered "{size=18}Everyone is welcome!{/size}"

    "Another notice advertised affordable rooms for rent."

    centered "{size=23}{color=#83b7df}ROOMS AVAILABLE{/color}{/size}"

    centered "{size=18}OakHaven Community Housing Office{/size}"

    centered "{size=18}Affordable accommodation for new residents{/size}"

    "Rowan leaned closer to read the details."

    $ housing_info_found = True

    $ cafe_quest_unlocked = True

    thought happy "Affordable rooms... I should remember that."

    menu:

        "What should Rowan do?"

        "Ask Elliot about affordable housing.":

            $ elliot_friendship += 2

            show rowan nervous

            rowan "Um... Elliot?"

            elliot "Yeah?"

            rowan "Do you know anything about the rooms on that notice?"

            elliot "Oh! The Community Housing Office."

            elliot "They help people who are new to OakHaven find affordable places to stay."

            elliot "You should definitely stop by sometime."

            rowan happy "Really? That would be helpful."

            elliot "Of course!"

            elliot "There's also a little apartment building near Market Street."

            elliot "Sometimes they have rooms available."

            thought happy "That's something, at least."

            "Rowan took a picture of the flyer."

        "Read more of the flyers.":

            "Rowan spent a few minutes looking through the other notices."

            "There were advertisements for community events, volunteer opportunities, and local services."

            "He found another small flyer advertising a weekend market."

            thought happy "There's quite a lot going on around here."

            "He took a picture of the housing notice."

        "Return to the table.":

            "Rowan decided he had enough information for now."

            "He returned to his table and picked up his backpack."

    # --------------------------------------------------------

    # ELLIOT CHECKS IN

    # --------------------------------------------------------

    "A little while later, Elliot walked over to Rowan's table."

    elliot "Everything alright over here?"

    show rowan happy

    rowan "Y-Yeah. Everything's really nice."

    elliot "Glad to hear it!"

    "Elliot pulled out the chair opposite Rowan."

    elliot "Mind if I sit for a minute?"

    rowan "Oh! N-No, go ahead."

    "Elliot sat down."

    elliot "So, do you have somewhere to stay yet?"

    show rowan nervous

    rowan "Not... exactly."

    elliot "Ah."

    elliot "Well, don't panic."

    elliot "There are a few affordable places around town."

    elliot "The housing office is probably your best starting point."

    rowan "I'll look into it."

    elliot "Good!"

    "Elliot smiled."

    elliot "OakHaven's a pretty welcoming place."

    elliot "It might take a little while, but you'll find your people."

    show rowan embarrassed

    rowan "I-I hope so."

    # --------------------------------------------------------

    # GETTING TO KNOW ROWAN

    # --------------------------------------------------------

    elliot "So, Rowan..."

    elliot "How are you feeling about everything?"

    menu:

        "What should Rowan say?"

        "I'm nervous about my interview.":

            $ elliot_friendship += 2

            show rowan nervous

            rowan "Honestly? I'm really nervous about the interview."

            rowan "I really need this job."

            elliot "That's understandable."

            elliot "First interviews are always a little scary."

            elliot "Just take a breath and be yourself."

            elliot "You've got this."

            show rowan happy

            rowan "Thanks..."

            thought happy "That actually helps."

        "I'm not very good at meeting new people.":

            $ elliot_friendship += 2

            show rowan embarrassed

            rowan "I'm... not really good at meeting new people."

            elliot "Really?"

            "Elliot smiled."

            elliot "Well, you're doing pretty well right now!"

            show rowan embarrassed

            rowan "A-Ah..."

            "Rowan's ears lowered."

            elliot "Sorry! Didn't mean to embarrass you."

            "Elliot chuckled softly."

        "I'd rather not talk about it.":

            show rowan nervous

            rowan "I'd... rather not talk about it."

            elliot "No problem."

            elliot "Everyone deserves a little privacy."

            rowan "Thanks."

            elliot "Anytime."

    # --------------------------------------------------------

    # INTERVIEW REMINDER — 8:47 AM

    # --------------------------------------------------------

    call screen phone_notification(

        "INTERVIEW REMINDER",

        "8:47 AM",

        "Reminder: Your interview at OakHaven Remote Logistics is approaching. Please arrive at Main Reception by 9:45 AM."

    )

    show rowan surprised

    "Rowan looked at his phone."

    rowan "Oh!"

    thought nervous "Right! The interview!"

    "He quickly checked the time."

    "He still had time, but he didn't want to be late."

    show rowan nervous

    rowan "I should probably get going."

    elliot "Got an interview?"

    rowan "Y-Yeah. At OakHaven Remote Logistics."

    elliot "Oh, right!"

    elliot "Well, I won't keep you."

    "Elliot stood up."

    elliot "Good luck, Rowan."

    elliot "And hey..."

    elliot "You're welcome here anytime."

    show rowan happy

    rowan "Really?"

    elliot "Of course!"

    elliot "First cup of tea is on the house next time."

    show rowan embarrassed

    rowan "Y-You don't have to do that..."

    elliot "I know."

    elliot "I want to."

    "Rowan's cheeks turned a little pink."

    rowan "Th-Thank you, Elliot."

    elliot "Anytime!"

    $ elliot_friendship += 1

    # --------------------------------------------------------

    # NEW ACQUAINTANCE

    # --------------------------------------------------------

    "Rowan adjusted his backpack."

    "He felt a little less like a stranger than he had when he first walked through the door."

    thought happy "Maybe I can make friends here."

    centered "{size=30}{color=#a7c98a}NEW ACQUAINTANCE{/color}{/size}"

    centered "{size=26}Elliot{/size}"

    centered "{size=18}Owner of Whiskers Café{/size}"

    pause 1.5

    centered "{size=30}{color=#83b7df}NEW SIDE QUEST{/color}{/size}"

    centered "{size=25}A Familiar Face at the Café{/size}"

    centered "{size=18}Visit Elliot again sometime.{/size}"

    pause 2.0

    # --------------------------------------------------------

    # LEAVING THE CAFÉ — 8:50 AM

    # --------------------------------------------------------

    scene bg market

    with dissolve

    call show_location_intro("Market Street", "Monday — 8:50 AM")

    show rowan happy:

        xalign 0.27

        yalign 1.0

        zoom 1.25

    "Rowan stepped outside."

    "The little bell jingled behind him."

    "He looked back through the window."

    "Elliot waved from behind the counter."

    rowan happy "Bye!"

    elliot "See you later!"

    "Rowan waved back."

    "Then he turned toward the road leading to OakHaven Remote Logistics."

    "His interview was getting closer."

    "He still needed somewhere to live."

    "He still had a very long way to go."

    "But at least he had met someone."

    thought happy "One step at a time."

    # --------------------------------------------------------

    # UPDATED CHECKLIST

    # --------------------------------------------------------

    centered "{size=30}{color=#ffffff}ROWAN'S TO-DO LIST{/color}{/size}"

    centered "{color=#83df9b}✓ Arrive in OakHaven{/color}"

    centered "{color=#83df9b}✓ Visit Whiskers Café{/color}"

    centered "{color=#83df9b}✓ Meet Elliot{/color}"

    centered "{color=#ffffff}□ Find somewhere affordable to stay{/color}"

    centered "{color=#ffffff}□ Attend job interview — 10:00 AM{/color}"

    centered "{color=#ffffff}□ Get hired{/color}"

    centered "{color=#ffffff}□ Start paying off medical debt{/color}"

    pause 2.0

    # --------------------------------------------------------

    # SCENE 2 COMPLETE

    jump act1_scene2_end

label act1_scene2_end:

    scene bg black

    with fade

    centered "{size=36}{color=#ffffff}SCENE 2 COMPLETE{/color}{/size}"

    centered "{size=23}First Impressions{/size}"

    pause 1.5

    "A warm cup of tea."

    "A friendly conversation."

    "And a new face in a town full of strangers."

    "Perhaps OakHaven was already beginning to feel a little more like home."

    pause 2.0

    return

"""
# ============================================================


"""


# OAKHAVEN: WINGS OF TOMORROW



# ACT I — A FOX WITHOUT A HOME



# SCENE 1 — A VERY LONG ROAD



# ============================================================



# ------------------------------------------------------------



# CHARACTERS



# ------------------------------------------------------------



define rowan = Character(



    "Rowan",



    color="#e89a55",



    image="rowan"



)



define thought = Character(



    "Rowan",



    color="#e89a55",



    image="rowan",



    what_italic=True



)



define driver = Character(



    "Bus Driver",



    color="#aab8c8"



)



define elliot = Character("Elliot", color="#a7c98a")



# ------------------------------------------------------------



# PLAYER DATA



# ------------------------------------------------------------



default wallet = 35



default medical_debt = 85000



default brother_reply = ""



default first_destination = ""



default interview_complete = False



default breakfast_purchased = False



default current_location = "City Bus"



default elliot_met = False



default elliot_friendship = 0



default cafe_visited = False



default breakfast_choice = ""



default breakfast_cost = 0



default breakfast_eaten = False



default cafe_quest_unlocked = False



default housing_info_found = False



# ------------------------------------------------------------



# BACKGROUNDS



# Backgrounds are loaded from game/images/backgrounds/.



# ------------------------------------------------------------



image bg bus = "images/backgrounds/bg_bus.png"



image bg town = "images/backgrounds/bg_town.png"



image bg terminal = "images/backgrounds/bg_terminal.png"



image bg market = "images/backgrounds/bg_market.png"



image bg cafe = "images/backgrounds/bg_cafe.png"



image bg park = "images/backgrounds/bg_park.png"



image bg company = "images/backgrounds/bg_company.png"



# Black transition background



image bg black = Solid("#000000")



# ------------------------------------------------------------



# ROWAN'S CHARACTER SPRITES



#



# All eight expressions use the same position and size.



# xalign 0.27 = right side of the screen.



# yalign 1.0 = bottom of the screen.



# zoom 1.25 = sprite size.



# ------------------------------------------------------------



image rowan neutral:



    "images/characters/rowan_neutral.png"



    xalign 0.27



    yalign 1.0



    zoom 1.25



image rowan happy:



    "images/characters/rowan_happy.png"



    xalign 0.27



    yalign 1.0



    zoom 1.25



image rowan nervous:



    "images/characters/rowan_nervous.png"



    xalign 0.27



    yalign 1.0



    zoom 1.25



image rowan embarrassed:



    "images/characters/rowan_embarrassed.png"



    xalign 0.27



    yalign 1.0



    zoom 1.25



image rowan sad:



    "images/characters/rowan_sad.png"



    xalign 0.27



    yalign 1.0



    zoom 1.25



image rowan angry:



    "images/characters/rowan_angry.png"



    xalign 0.27



    yalign 1.0



    zoom 1.25



image rowan surprised:



    "images/characters/rowan_surprised.png"



    xalign 0.27



    yalign 1.0



    zoom 1.25



image rowan tired:



    "images/characters/rowan_tired.png"



    xalign 0.27



    yalign 1.0



    zoom 1.25


# ------------------------------------------------------------
# ELLIOT'S CHARACTER SPRITES
# ------------------------------------------------------------
# Elliot stands on the right side, opposite Rowan.

image elliot neutral:

    "images/characters/elliot_neutral.png"

    xalign 0.73

    yalign 1.0

    zoom 1.10

image elliot happy:

    "images/characters/elliot_happy.png"

    xalign 0.73

    yalign 1.0

    zoom 1.10

image elliot smug:

    "images/characters/elliot_smug.png"

    xalign 0.73

    yalign 1.0

    zoom 1.10

image elliot surprised:

    "images/characters/elliot_surprised.png"

    xalign 0.73

    yalign 1.0

    zoom 1.10

image elliot embarrassed:

    "images/characters/elliot_embarrassed.png"

    xalign 0.73

    yalign 1.0

    zoom 1.10

image elliot sad:

    "images/characters/elliot_sad.png"

    xalign 0.73

    yalign 1.0

    zoom 1.10

image elliot angry:

    "images/characters/elliot_angry.png"

    xalign 0.73

    yalign 1.0

    zoom 1.10

image elliot tired:

    "images/characters/elliot_tired.png"

    xalign 0.73

    yalign 1.0

    zoom 1.10



# ============================================================



# LOCATION INTRODUCTION SCREEN



# ============================================================



screen location_title(location, time):



    zorder 50



    frame:



        xalign 0.5



        yalign 0.13



        padding (35, 20)



        background "#182330dd"



        vbox:



            spacing 8



            xalign 0.5



            text location:



                size 32



                color "#ffffff"



                xalign 0.5



            text time:



                size 18



                color "#c8d5df"



                xalign 0.5



# ============================================================



# PHONE NOTIFICATION SCREEN



# ============================================================



screen phone_notification(sender, timestamp, message):



    zorder 100



    modal True



    frame:



        xalign 0.97



        yalign 0.04



        xsize 480



        padding (24, 20)



        background "#202a36ee"



        vbox:



            spacing 12



            hbox:



                spacing 8



                text sender:



                    size 23



                    color "#ffffff"



                    bold True



                null width 1



                text timestamp:



                    size 15



                    color "#aab8c8"



            text message:



                size 19



                color "#ffffff"



                line_spacing 5



            null height 8



            textbutton "Continue":



                action Return()



                text_size 17



                text_color "#ffffff"



                text_hover_color "#83dfb0"



# ============================================================



# LOCATION INTRODUCTION HELPER



# Displays the location once, then removes it.



# ============================================================



label show_location_intro(location, time):



    show screen location_title(location, time)



    pause 2.5



    hide screen location_title



    return



# ============================================================



# GAME START



# ============================================================



label start:



    call act1_scene1



    call act1_scene2



    return



# ============================================================



# ACT I — SCENE 1



# A VERY LONG ROAD



# ============================================================



label act1_scene1:



    scene bg black



    with fade



    centered "{size=48}{color=#ffffff}OAKHAVEN{/color}{/size}"



    centered "{size=24}{color=#c8d5df}Wings of Tomorrow{/color}{/size}"



    pause 2.0



    centered "{size=22}ACT I{/size}"



    centered "{size=32}A Fox Without a Home{/size}"



    pause 2.0



    # --------------------------------------------------------



    # CITY BUS — 7:18 AM



    # --------------------------------------------------------



    scene bg bus



    with fade



    call show_location_intro(



        "Somewhere on the highway",



        "Monday — 7:18 AM"



    )



    show rowan neutral



    "The bus rumbled along the highway, its engine vibrating through the floor."



    "Outside the window, the scenery slowly began to change."



    "Tall buildings gave way to green hills, quiet neighborhoods, and distant forests."



    "Rowan sat alone beside the window, his backpack resting against his knees."



    "A young red fox with tired eyes, fluffy ears, and a tail that refused to sit still."



    "He had been traveling for hours."



    "And he was still a little bit terrified."



    rowan nervous "Okay..."



    rowan nervous "First day. New town. New job."



    thought nervous "Just don't mess this up."



    "He adjusted the strap of his backpack."



    thought nervous "Please, please, please let this work."



    pause 0.8



    # --------------------------------------------------------



    # MEDICAL BILL — 7:19 AM



    # --------------------------------------------------------



    call screen phone_notification(



        "MEDICAL BILLING",



        "7:19 AM",



        "Payment reminder: Your outstanding medical balance is $85,000. Please review your account."



    )



    show rowan sad



    "Rowan stared at the notification."



    "His ears slowly lowered."



    rowan sad "...Right."



    thought sad "Eighty-five thousand dollars."



    thought nervous "No pressure."



    "He locked his phone and placed it face-down on his lap."



    "For a moment, he just watched the passing scenery."



    pause 0.8



    # --------------------------------------------------------



    # BROTHER'S MESSAGE — 7:20 AM



    # --------------------------------------------------------



    call screen phone_notification(



        "Little Brother 💙",



        "7:20 AM",



        "Hey Rowan!! Are you there yet? Don't forget to eat breakfast, okay? You always skip it when you're nervous. Good luck with the job interview!! I know you can do it. Love you!! 💙"



    )



    show rowan happy



    "Rowan's expression softened."



    "A tiny smile appeared on his muzzle."



    thought happy "He's always looking out for me..."



    "He opened the message and started typing."



    menu:



        "What should Rowan reply?"



        "I'll be okay. Don't worry about me!":



            $ brother_reply = "I'll be okay. Don't worry about me!"



            rowan happy "I'll be okay. Don't worry about me!"



            "He added a little heart before sending it."



        "I miss you already. I'll call you tonight.":



            $ brother_reply = "I miss you already. I'll call you tonight."



            rowan sad "I miss you already. I'll call you tonight."



            "He hesitated before pressing send."



            "He really did miss him."



        "I'm nervous, but I'll do my best. Love you!":



            $ brother_reply = "I'm nervous, but I'll do my best. Love you!"



            rowan nervous "I'm nervous, but I'll do my best. Love you!"



            "It felt a little embarrassing to admit."



            "But it was true."



    "Message sent."



    thought happy "I have to make this work."



    pause 1.0



    driver "OakHaven coming up! We'll be arriving in a few minutes!"



    show rowan surprised



    "Rowan's ears perked up."



    # --------------------------------------------------------



    # APPROACHING OAKHAVEN — 7:24 AM



    # --------------------------------------------------------



    scene bg town



    with dissolve



    call show_location_intro(



        "Approaching OakHaven",



        "Monday — 7:24 AM"



    )



    show rowan surprised



    "There it was."



    "OakHaven."



    "A quiet town surrounded by rolling green hills and thick pine forests."



    "Its streets were lined with little shops, apartment buildings, and trees covered in morning dew."



    "A large sign stood near the entrance to town."



    centered "{size=30}{color=#ffffff}OAKHAVEN{/color}{/size}"



    centered "{size=17}{color=#dce8df}A COMMUNITY BUILT FOR TOMORROW{/color}{/size}"



    "Rowan watched the town pass by."



    rowan happy "It's... actually really pretty."



    "A little farther down the road, he spotted a large modern building."



    "The sign on its front read:"



    centered "{size=25}{color=#ffffff}OAKHAVEN REMOTE LOGISTICS{/color}{/size}"



    "The company he had applied to."



    "The company that might finally give him a chance."



    thought nervous "That's where I'm going."



    # --------------------------------------------------------



    # BUS TERMINAL — 7:42 AM



    # --------------------------------------------------------



    scene bg terminal



    with dissolve



    call show_location_intro(



        "OakHaven Central Bus Terminal",



        "Monday — 7:42 AM"



    )



    show rowan nervous



    "The bus pulled into the terminal."



    driver "OakHaven Central! Last stop!"



    "Rowan stood, grabbed his backpack, and carefully made his way toward the doors."



    rowan happy "Thank you!"



    driver "Have a good one, kid."



    "Rowan stepped down onto the pavement."



    "The bus pulled away behind him."



    "And just like that..."



    "He was here."



    pause 0.8



    "A cool morning breeze brushed through his fur."



    "Rowan looked around the terminal."



    "People hurried past with coffee cups and bags."



    "Somewhere nearby, a bicycle bell rang."



    "A car horn sounded in the distance."



    "Everything was unfamiliar."



    thought nervous "Okay. I can do this."



    "He opened his phone and checked his notes."



    centered "{size=30}{color=#ffffff}ROWAN'S TO-DO LIST{/color}{/size}"



    centered "{color=#83df9b}✓ Arrive in OakHaven{/color}"



    centered "{color=#ffffff}□ Find somewhere affordable to stay{/color}"



    centered "{color=#ffffff}□ Attend job interview — 10:00 AM{/color}"



    centered "{color=#ffffff}□ Get hired{/color}"



    centered "{color=#ffffff}□ Start paying off medical debt{/color}"



    pause 1.5



    "He looked at the last item for a little too long."



    thought sad "One step at a time."



    # --------------------------------------------------------



    # MARKET STREET — 7:48 AM



    # --------------------------------------------------------



    scene bg market



    with dissolve



    call show_location_intro(



        "Market Street",



        "Monday — 7:48 AM"



    )



    show rowan neutral



    "A short walk brought Rowan to the entrance of Market Street."



    "The street was beginning to wake up."



    "Shopkeepers were opening their doors."



    "A delivery van rolled past."



    "The smell of fresh bread drifted through the air."



    "Rowan spotted several places nearby."



    "A small café with warm lights glowing through its windows."



    "A convenience store on the opposite corner."



    "A path leading toward a green park."



    "And, farther down the road..."



    "The OakHaven Remote Logistics campus."



    "He checked his phone again."



    # --------------------------------------------------------



    # INTERVIEW REMINDER



    # --------------------------------------------------------



    call screen phone_notification(



        "INTERVIEW REMINDER",



        "7:48 AM",



        "Reminder: Your interview is scheduled for Monday at 10:00 AM. Location: Main Reception, OakHaven Logistics Campus. Please arrive 15 minutes early."



    )



    show rowan nervous



    "Rowan swallowed."



    rowan nervous "Ten o'clock..."



    thought nervous "I've got time."



    thought nervous "I've got plenty of time."



    pause 0.5



    "He looked down at his wallet."



    "Thirty-five dollars."



    "That was everything he had available right now."



    thought nervous "Maybe I should find something to eat."



    thought sad "Or maybe I should save the money."



    "His stomach gave a quiet growl."



    rowan embarrassed "...Traitor."



    "He let out a nervous little laugh."



    "For the first time that morning, he felt himself relax just a little."



    "He took a deep breath."



    show rowan neutral



    rowan "Okay."



    rowan "Let's make today count."



    # --------------------------------------------------------



    # FIRST DESTINATION CHOICE



    # --------------------------------------------------------



    menu:



        "Where should Rowan go first?"



        "Visit Whiskers Café":



            $ first_destination = "Whiskers Café"



            jump act1_scene1_cafe



        "Visit OakHaven Remote Logistics":



            $ first_destination = "OakHaven Remote Logistics"



            jump act1_scene1_company



        "Take a walk through Pinewood Park":



            $ first_destination = "Pinewood Park"



            jump act1_scene1_park



        "Explore Market Street":



            $ first_destination = "Market Street"



            jump act1_scene1_explore



# ============================================================



# BRANCH 1 — WHISKERS CAFÉ



# ============================================================



label act1_scene1_cafe:



    scene bg cafe



    with fade



    call show_location_intro(



        "Whiskers Café",



        "Monday — 8:05 AM"



    )



    show rowan nervous



    "A little bell jingled as Rowan approached the café."



    "Warm light spilled through the front windows."



    "The smell of coffee and freshly baked bread drifted outside."



    centered "{size=34}{color=#ffffff}WHISKERS CAFÉ{/color}{/size}"



    "Rowan looked through the window."



    "There were a few customers inside."



    "It seemed quiet."



    thought nervous "I could probably afford something small..."



    "He adjusted his backpack."



    show rowan happy



    rowan "Alright. Breakfast."



    "He reached for the door handle."



    "The little bell jingled again as he stepped inside."



    "Warm air surrounded him."



    "For the first time since arriving in OakHaven, Rowan felt like he could sit down."



    "Just for a little while."



    jump act1_scene1_end



# ============================================================



# BRANCH 2 — OAKHAVEN REMOTE LOGISTICS



# ============================================================



label act1_scene1_company:



    scene bg company



    with fade



    call show_location_intro(



        "OakHaven Remote Logistics",



        "Monday — 8:05 AM"



    )



    show rowan surprised



    "Rowan followed the road toward the logistics campus."



    "The building was larger up close."



    "Modern glass windows reflected the morning sunlight."



    "Small delivery drones could be seen flying between different sections of the campus."



    centered "{size=29}{color=#ffffff}OAKHAVEN REMOTE LOGISTICS{/color}{/size}"



    "Rowan stopped outside the main entrance."



    rowan surprised "Whoa..."



    "A drone zipped overhead."



    "Its small motors made a quiet buzzing sound."



    thought happy "So this is where I'll be working..."



    "He checked the time."



    "Still far too early for his interview."



    "He decided to take a closer look around the outside of the building."



    jump act1_scene1_end



# ============================================================



# BRANCH 3 — PINEWOOD PARK



# ============================================================



label act1_scene1_park:



    scene bg park



    with fade



    call show_location_intro(



        "Pinewood Park",



        "Monday — 8:05 AM"



    )



    show rowan happy



    "Rowan followed a nearby path toward the park."



    "Tall pine trees surrounded the walking trail."



    "The morning sunlight filtered through their branches."



    "A few birds chirped from somewhere overhead."



    "There were benches along the path and a small pond farther ahead."



    "Rowan found an empty bench and sat down."



    "His tail curled around his side."



    thought happy "Maybe I needed this."



    "For a moment, he didn't think about the interview."



    "Or the debt."



    "Or how much everything depended on today."



    "He simply listened to the birds."



    jump act1_scene1_end



# ============================================================



# BRANCH 4 — MARKET STREET



# ============================================================



label act1_scene1_explore:



    scene bg market



    with fade



    call show_location_intro(



        "Market Street",



        "Monday — 8:05 AM"



    )



    show rowan neutral



    "Rowan decided to explore the street before committing to anywhere."



    "There were little shops on both sides of the road."



    "A convenience store."



    "A clothing shop."



    "A small grocery store."



    "A few apartments sat above the businesses."



    "He wondered how much rent cost around here."



    thought nervous "I really need somewhere to stay."



    "He looked at the shop windows as he walked."



    thought happy "Maybe OakHaven wouldn't be such a bad place to start over."



    jump act1_scene1_end



# ============================================================



# SCENE 1 END



# ============================================================



label act1_scene1_end:



    scene bg black



    with fade



    centered "{size=36}{color=#ffffff}SCENE 1 COMPLETE{/color}{/size}"



    centered "{size=23}A Very Long Road{/size}"



    pause 1.5



    "Rowan's first morning in OakHaven had begun."



    "There was still a job interview ahead."



    "A place to find."



    "And a very long road toward paying off his family's debt."



    "But he wasn't alone in the world."



    "Not completely."



    "And perhaps OakHaven had more waiting for him than he expected."



    pause 1.5



    return



# ============================================================



# ACT I — SCENE 2: FIRST IMPRESSIONS



# ============================================================



label act1_scene2:



    $ current_location = "Whiskers Café"



    scene bg cafe



    with fade



    call show_location_intro("Whiskers Café", "Monday — 8:12 AM")



    $ cafe_visited = True



    show rowan nervous:



        xalign 0.27



        yalign 1.0



        zoom 1.25


    # Elliot is already behind the counter when Rowan enters.

    show elliot neutral



    "The little bell above the café door jingled."



    "Warm air surrounded Rowan as he stepped inside."



    "The café smelled of freshly brewed coffee, warm bread, and something sweet."



    "A few customers sat at the tables."



    "Behind the counter stood a brown deer wearing a green cardigan and a pair of glasses."



    "He was arranging a few pastries when he noticed Rowan."



    show rowan surprised



    show elliot happy

    "The deer looked up and smiled."



    elliot "Oh! Good morning!"



    show elliot neutral

    elliot "Welcome to Whiskers Café!"



    show rowan nervous



    rowan "G-Good morning..."



    elliot "First time here?"



    rowan "Y-Yeah. I just arrived in OakHaven."



    "The deer leaned against the counter."



    show elliot happy

    elliot "Really? Welcome to town, then!"



    elliot "I'm Elliot, by the way. I own the place."



    "He offered a friendly wave."



    $ elliot_met = True



    $ elliot_friendship += 1



    rowan "I'm Rowan. Nice to meet you."



    elliot "Nice to meet you too, Rowan!"



    "Elliot glanced at Rowan's backpack."



    show elliot neutral

    elliot "So, what brings you to OakHaven?"



    menu:



        "What should Rowan tell Elliot?"



        "I'm here for a job interview.":



            $ elliot_friendship += 1



            rowan nervous "I'm here for a job interview."



            show elliot happy

            elliot "Oh! That's exciting!"



            elliot "Where at?"



            rowan "OakHaven Remote Logistics."



            elliot "Ah, the drone delivery company!"



            elliot "They're always looking for people."



            elliot "Good luck! I hope it goes well."



            thought happy "He seems nice..."



        "I just moved here. I'm trying to start over.":



            $ elliot_friendship += 2



            rowan sad "I just moved here. I'm trying to start over."



            elliot "Well, you've come to a pretty good place for that."



            elliot "OakHaven can be a little quiet sometimes, but the people are generally friendly."



            elliot "I'm sure you'll find your place."



            show rowan embarrassed



            rowan "Th-Thanks..."



            elliot "Of course!"



        "It's a little complicated...":



            rowan nervous "It's... a little complicated."



            show elliot neutral

            elliot "Ah. Fair enough."



            elliot "You don't have to explain anything."



            elliot "Sometimes a fresh cup of coffee is all someone needs."



            show rowan happy



            rowan "Heh... yeah."



    "Elliot glanced toward the display case."



    elliot "Have you eaten breakfast yet?"



    "Rowan's stomach gave a small growl."



    show rowan embarrassed



    rowan "...Maybe."



    elliot "That sounds like a no."



    "Elliot chuckled."



    elliot "Well, we've got a few things available."



    elliot "Nothing too fancy, but everything's fresh."



    # --------------------------------------------------------



    # BREAKFAST MENU



    # --------------------------------------------------------



    $ breakfast_choice = ""



    $ breakfast_cost = 0



    menu:



        "What should Rowan order? (Wallet: $[wallet])"



        "Butter toast — $3":



            $ breakfast_choice = "Butter toast"



            $ breakfast_cost = 3



        "Fresh sandwich — $7":



            $ breakfast_choice = "Fresh sandwich"



            $ breakfast_cost = 7



        "Coffee — $4":



            $ breakfast_choice = "Coffee"



            $ breakfast_cost = 4



        "Apple pastry — $3":



            $ breakfast_choice = "Apple pastry"



            $ breakfast_cost = 3



        "Tea — $3":



            $ breakfast_choice = "Tea"



            $ breakfast_cost = 3



        "Nothing. Save the money.":



            $ breakfast_choice = "Nothing"



            $ breakfast_cost = 0



    if breakfast_cost > 0:



        if wallet >= breakfast_cost:



            $ wallet -= breakfast_cost



            $ breakfast_purchased = True



            $ breakfast_eaten = True



            rowan nervous "Could I... um... have the [breakfast_choice.lower()], please?"



            show elliot happy

            elliot "Absolutely!"



            "Elliot prepared Rowan's order."



            "A few moments later, he placed it on the counter."



            elliot "There you go!"



            rowan happy "Thank you!"



            "Rowan paid and carefully picked up his food."



            elliot "Enjoy!"



            "Rowan took a bite."



            "It was simple, but surprisingly good."



            thought happy "Oh... that's actually really nice."



        else:



            rowan embarrassed "Actually... I don't think I have enough."



            elliot "Oh! Don't worry about it."



            "Elliot put the food away."



            elliot "Maybe another time."



    else:



        rowan nervous "I think I'll save my money."



        elliot "That's alright!"



        elliot "Just don't forget to eat something later, okay?"



        rowan embarrassed "I'll try..."



    # --------------------------------------------------------



    # SITTING BY THE WINDOW



    # --------------------------------------------------------



    "Rowan found a small table beside the window."



    "He placed his backpack beside the chair and sat down."



    show rowan neutral



    "Outside, Market Street was slowly getting busier."



    "People walked past the café windows."



    "A delivery van stopped near the curb."



    "For a moment, Rowan almost forgot how nervous he had been."



    thought happy "Maybe this place isn't so bad."



    "He pulled out his phone."



    "His brother's earlier message was still open."



    "Rowan smiled faintly."



    thought happy "I should call him later."



    # --------------------------------------------------------



    # COMMUNITY NOTICEBOARD



    # --------------------------------------------------------



    "After finishing his breakfast, Rowan noticed a large noticeboard near the café entrance."



    "It was covered with colorful flyers and handwritten notes."



    "One flyer caught his attention."



    centered "{size=30}{color=#ffffff}OAKHAVEN COMMUNITY BOARD{/color}{/size}"



    centered "{size=23}{color=#a7c98a}COMMUNITY GATHERING{/color}{/size}"



    centered "{size=18}Pinewood Park — Saturday Morning{/size}"



    centered "{size=18}Everyone is welcome!{/size}"



    "Another notice advertised affordable rooms for rent."



    centered "{size=23}{color=#83b7df}ROOMS AVAILABLE{/color}{/size}"



    centered "{size=18}OakHaven Community Housing Office{/size}"



    centered "{size=18}Affordable accommodation for new residents{/size}"



    "Rowan leaned closer to read the details."



    $ housing_info_found = True



    $ cafe_quest_unlocked = True



    thought happy "Affordable rooms... I should remember that."



    menu:



        "What should Rowan do?"



        "Ask Elliot about affordable housing.":



            $ elliot_friendship += 2



            show rowan nervous



            rowan "Um... Elliot?"



            elliot "Yeah?"



            rowan "Do you know anything about the rooms on that notice?"



            elliot "Oh! The Community Housing Office."



            elliot "They help people who are new to OakHaven find affordable places to stay."



            elliot "You should definitely stop by sometime."



            rowan happy "Really? That would be helpful."



            elliot "Of course!"



            elliot "There's also a little apartment building near Market Street."



            elliot "Sometimes they have rooms available."



            thought happy "That's something, at least."



            "Rowan took a picture of the flyer."



        "Read more of the flyers.":



            "Rowan spent a few minutes looking through the other notices."



            "There were advertisements for community events, volunteer opportunities, and local services."



            "He found another small flyer advertising a weekend market."



            thought happy "There's quite a lot going on around here."



            "He took a picture of the housing notice."



        "Return to the table.":



            "Rowan decided he had enough information for now."



            "He returned to his table and picked up his backpack."



    # --------------------------------------------------------



    # ELLIOT CHECKS IN



    # --------------------------------------------------------



    "A little while later, Elliot walked over to Rowan's table."



    elliot "Everything alright over here?"



    show rowan happy



    rowan "Y-Yeah. Everything's really nice."



    elliot "Glad to hear it!"



    "Elliot pulled out the chair opposite Rowan."



    elliot "Mind if I sit for a minute?"



    rowan "Oh! N-No, go ahead."



    "Elliot sat down."



    elliot "So, do you have somewhere to stay yet?"



    show rowan nervous



    rowan "Not... exactly."



    elliot "Ah."



    elliot "Well, don't panic."



    elliot "There are a few affordable places around town."



    elliot "The housing office is probably your best starting point."



    rowan "I'll look into it."



    elliot "Good!"



    "Elliot smiled."



    elliot "OakHaven's a pretty welcoming place."



    elliot "It might take a little while, but you'll find your people."



    show rowan embarrassed



    rowan "I-I hope so."



    # --------------------------------------------------------



    # GETTING TO KNOW ROWAN



    # --------------------------------------------------------



    elliot "So, Rowan..."



    elliot "How are you feeling about everything?"



    menu:



        "What should Rowan say?"



        "I'm nervous about my interview.":



            $ elliot_friendship += 2



            show rowan nervous



            rowan "Honestly? I'm really nervous about the interview."



            rowan "I really need this job."



            elliot "That's understandable."



            elliot "First interviews are always a little scary."



            elliot "Just take a breath and be yourself."



            elliot "You've got this."



            show rowan happy



            rowan "Thanks..."



            thought happy "That actually helps."



        "I'm not very good at meeting new people.":



            $ elliot_friendship += 2



            show rowan embarrassed



            rowan "I'm... not really good at meeting new people."



            elliot "Really?"



            "Elliot smiled."



            elliot "Well, you're doing pretty well right now!"



            show rowan embarrassed



            rowan "A-Ah..."



            "Rowan's ears lowered."



            show elliot embarrassed

            elliot "Sorry! Didn't mean to embarrass you."



            "Elliot chuckled softly."



        "I'd rather not talk about it.":



            show rowan nervous



            rowan "I'd... rather not talk about it."



            show elliot happy

            elliot "No problem."



            elliot "Everyone deserves a little privacy."



            rowan "Thanks."



            elliot "Anytime."



    # --------------------------------------------------------



    # INTERVIEW REMINDER — 8:47 AM



    # --------------------------------------------------------



    call screen phone_notification(



        "INTERVIEW REMINDER",



        "8:47 AM",



        "Reminder: Your interview at OakHaven Remote Logistics is approaching. Please arrive at Main Reception by 9:45 AM."



    )



    show rowan surprised



    "Rowan looked at his phone."



    rowan "Oh!"



    thought nervous "Right! The interview!"



    "He quickly checked the time."



    "He still had time, but he didn't want to be late."



    show rowan nervous



    rowan "I should probably get going."



    elliot "Got an interview?"



    rowan "Y-Yeah. At OakHaven Remote Logistics."



    elliot "Oh, right!"



    elliot "Well, I won't keep you."



    "Elliot stood up."



    elliot "Good luck, Rowan."



    elliot "And hey..."



    elliot "You're welcome here anytime."



    show rowan happy



    rowan "Really?"



    elliot "Of course!"



    elliot "First cup of tea is on the house next time."



    show rowan embarrassed



    rowan "Y-You don't have to do that..."



    elliot "I know."



    elliot "I want to."



    "Rowan's cheeks turned a little pink."



    rowan "Th-Thank you, Elliot."



    elliot "Anytime!"



    $ elliot_friendship += 1



    # --------------------------------------------------------



    # NEW ACQUAINTANCE



    # --------------------------------------------------------



    "Rowan adjusted his backpack."



    "He felt a little less like a stranger than he had when he first walked through the door."



    thought happy "Maybe I can make friends here."



    centered "{size=30}{color=#a7c98a}NEW ACQUAINTANCE{/color}{/size}"



    centered "{size=26}Elliot{/size}"



    centered "{size=18}Owner of Whiskers Café{/size}"



    pause 1.5



    centered "{size=30}{color=#83b7df}NEW SIDE QUEST{/color}{/size}"



    centered "{size=25}A Familiar Face at the Café{/size}"



    centered "{size=18}Visit Elliot again sometime.{/size}"



    pause 2.0



    # --------------------------------------------------------



    # LEAVING THE CAFÉ — 8:50 AM



    # --------------------------------------------------------



    scene bg market



    with dissolve



    call show_location_intro("Market Street", "Monday — 8:50 AM")



    show rowan happy:



        xalign 0.27



        yalign 1.0



        zoom 1.25



    "Rowan stepped outside."



    "The little bell jingled behind him."



    "He looked back through the window."



    "Elliot waved from behind the counter."



    rowan happy "Bye!"



    elliot "See you later!"



    "Rowan waved back."



    "Then he turned toward the road leading to OakHaven Remote Logistics."



    "His interview was getting closer."



    "He still needed somewhere to live."



    "He still had a very long way to go."



    "But at least he had met someone."



    thought happy "One step at a time."



    # --------------------------------------------------------



    # UPDATED CHECKLIST



    # --------------------------------------------------------



    centered "{size=30}{color=#ffffff}ROWAN'S TO-DO LIST{/color}{/size}"



    centered "{color=#83df9b}✓ Arrive in OakHaven{/color}"



    centered "{color=#83df9b}✓ Visit Whiskers Café{/color}"



    centered "{color=#83df9b}✓ Meet Elliot{/color}"



    centered "{color=#ffffff}□ Find somewhere affordable to stay{/color}"



    centered "{color=#ffffff}□ Attend job interview — 10:00 AM{/color}"



    centered "{color=#ffffff}□ Get hired{/color}"



    centered "{color=#ffffff}□ Start paying off medical debt{/color}"



    pause 2.0



    # --------------------------------------------------------



    # SCENE 2 COMPLETE



    jump act1_scene2_end



label act1_scene2_end:



    scene bg black



    with fade



    centered "{size=36}{color=#ffffff}SCENE 2 COMPLETE{/color}{/size}"



    centered "{size=23}First Impressions{/size}"



    pause 1.5



    "A warm cup of tea."



    "A friendly conversation."



    "And a new face in a town full of strangers."



    "Perhaps OakHaven was already beginning to feel a little more like home."



    pause 2.0



    return


"""

"""
# ============================================================



# OAKHAVEN: WINGS OF TOMORROW



# ACT I — A FOX WITHOUT A HOME



# SCENE 1 — A VERY LONG ROAD



# ============================================================



# ------------------------------------------------------------



# CHARACTERS



# ------------------------------------------------------------



define rowan = Character(



    "Rowan",



    color="#e89a55",



    image="rowan"



)



define thought = Character(



    "Rowan",



    color="#e89a55",



    image="rowan",



    what_italic=True



)



define driver = Character(



    "Bus Driver",



    color="#aab8c8"



)



define elliot = Character("Elliot", color="#a7c98a")

define nyx = Character("Nyx", color="#a99be8")



# ------------------------------------------------------------



# PLAYER DATA



# ------------------------------------------------------------



default wallet = 35



default medical_debt = 85000



default brother_reply = ""



default first_destination = ""



default interview_complete = False



default breakfast_purchased = False



default current_location = "City Bus"



default elliot_met = False



default elliot_friendship = 0



default cafe_visited = False



default breakfast_choice = ""



default breakfast_cost = 0



default breakfast_eaten = False



default cafe_quest_unlocked = False



default housing_info_found = False
default elliot_trust = 0
default elliot_like = 0
default elliot_love = 0

default nyx_met = False
default nyx_trust = 0
default nyx_like = 0
default nyx_love = 0



# ------------------------------------------------------------



# BACKGROUNDS



# Backgrounds are loaded from game/images/backgrounds/.



# ------------------------------------------------------------



image bg bus = "images/backgrounds/bg_bus.png"



image bg town = "images/backgrounds/bg_town.png"



image bg terminal = "images/backgrounds/bg_terminal.png"



image bg market = "images/backgrounds/bg_market.png"



image bg cafe = "images/backgrounds/bg_cafe.png"



image bg park = "images/backgrounds/bg_park.png"



image bg company = "images/backgrounds/bg_company.png"



# Black transition background



image bg black = Solid("#000000")



# ------------------------------------------------------------



# ROWAN'S CHARACTER SPRITES



#



# All eight expressions use the same position and size.



# xalign 0.27 = right side of the screen.
# In this layout, 0.27 places Rowan on the left side of the screen.



# yalign 1.0 = bottom of the screen.



# zoom 1.25 = sprite size.



# ------------------------------------------------------------



image rowan neutral:



    "images/characters/rowan_neutral.png"



    xalign 0.27



    yalign 1.0



    zoom 1.25
    yoffset -150



image rowan happy:



    "images/characters/rowan_happy.png"



    xalign 0.27



    yalign 1.0



    zoom 1.25
    yoffset -150



image rowan nervous:



    "images/characters/rowan_nervous.png"



    xalign 0.27



    yalign 1.0



    zoom 1.25
    yoffset -150



image rowan embarrassed:



    "images/characters/rowan_embarrassed.png"



    xalign 0.27



    yalign 1.0



    zoom 1.25
    yoffset -150



image rowan sad:



    "images/characters/rowan_sad.png"



    xalign 0.27



    yalign 1.0



    zoom 1.25
    yoffset -150



image rowan angry:



    "images/characters/rowan_angry.png"



    xalign 0.27



    yalign 1.0



    zoom 1.25
    yoffset -150



image rowan surprised:



    "images/characters/rowan_surprised.png"



    xalign 0.27



    yalign 1.0



    zoom 1.25
    yoffset -150



image rowan tired:



    "images/characters/rowan_tired.png"



    xalign 0.27



    yalign 1.0



    zoom 1.25
    yoffset -150


# ------------------------------------------------------------
# ELLIOT'S CHARACTER SPRITES
# ------------------------------------------------------------
# Elliot stands on the right side, opposite Rowan.

image elliot neutral:

    "images/characters/elliot_neutral.png"

    xalign 0.73

    yalign 1.0

    zoom 1.10
    yoffset -150

image elliot happy:

    "images/characters/elliot_happy.png"

    xalign 0.73

    yalign 1.0

    zoom 1.10
    yoffset -150

image elliot smug:

    "images/characters/elliot_smug.png"

    xalign 0.73

    yalign 1.0

    zoom 1.10
    yoffset -150

image elliot surprised:

    "images/characters/elliot_surprised.png"

    xalign 0.73

    yalign 1.0

    zoom 1.10
    yoffset -150

image elliot embarrassed:

    "images/characters/elliot_embarrassed.png"

    xalign 0.73

    yalign 1.0

    zoom 1.10
    yoffset -150

image elliot sad:

    "images/characters/elliot_sad.png"

    xalign 0.73

    yalign 1.0

    zoom 1.10
    yoffset -150

image elliot angry:

    "images/characters/elliot_angry.png"

    xalign 0.73

    yalign 1.0

    zoom 1.10
    yoffset -150

image elliot tired:

    "images/characters/elliot_tired.png"

    xalign 0.73

    yalign 1.0

    zoom 1.10
    yoffset -150



# ============================================================




# ------------------------------------------------------------
# NYX'S CHARACTER SPRITES
# Nyx is a black cat. Their sprites are placed above the dialogue box.
# ------------------------------------------------------------
image nyx neutral:
    "images/characters/nyx_neutral.png"
    xalign 0.73
    yalign 1.0
    zoom 1.10
    yoffset -150

image nyx happy:
    "images/characters/nyx_happy.png"
    xalign 0.73
    yalign 1.0
    zoom 1.10
    yoffset -150

image nyx smug:
    "images/characters/nyx_smug.png"
    xalign 0.73
    yalign 1.0
    zoom 1.10
    yoffset -150

image nyx annoyed:
    "images/characters/nyx_annoyed.png"
    xalign 0.73
    yalign 1.0
    zoom 1.10
    yoffset -150

image nyx surprised:
    "images/characters/nyx_surprised.png"
    xalign 0.73
    yalign 1.0
    zoom 1.10
    yoffset -150

image nyx embarrassed:
    "images/characters/nyx_embarrassed.png"
    xalign 0.73
    yalign 1.0
    zoom 1.10
    yoffset -150

image nyx sad:
    "images/characters/nyx_sad.png"
    xalign 0.73
    yalign 1.0
    zoom 1.10
    yoffset -150
# LOCATION INTRODUCTION SCREEN



# ============================================================



screen location_title(location, time):



    zorder 50



    frame:



        xalign 0.5



        yalign 0.13



        padding (35, 20)



        background "#182330dd"



        vbox:



            spacing 8



            xalign 0.5



            text location:



                size 32



                color "#ffffff"



                xalign 0.5



            text time:



                size 18



                color "#c8d5df"



                xalign 0.5



# ============================================================




# ============================================================
# RELATIONSHIP STATUS
# Press R during gameplay to view Trust, Like, and Love.
# ============================================================
screen relationship_hotkey():
    key "r" action ToggleScreen("relationship_status")
    key "R" action ToggleScreen("relationship_status")

screen relationship_status():
    modal True
    zorder 200
    key "K_ESCAPE" action Hide("relationship_status")
    frame:
        xalign 0.5
        yalign 0.5
        xsize 900
        ymaximum 760
        padding (35, 28)
        background "#172332ee"
        vbox:
            spacing 14
            text "RELATIONSHIPS" size 36 color "#ffffff" xalign 0.5
            text "Your choices shape how the people of OakHaven feel about Rowan." size 18 color "#cbd6e2" xalign 0.5
            null height 8
            text "Elliot" size 28 color "#a7c98a"
            hbox:
                spacing 14
                text "Trust" xsize 90
                bar value VariableValue("elliot_trust", 100) xmaximum 560
                text "[elliot_trust]/100" xsize 90
            hbox:
                spacing 14
                text "Like" xsize 90
                bar value VariableValue("elliot_like", 100) xmaximum 560
                text "[elliot_like]/100" xsize 90
            hbox:
                spacing 14
                text "Love" xsize 90
                bar value VariableValue("elliot_love", 100) xmaximum 560
                text "[elliot_love]/100" xsize 90
            null height 10
            if nyx_met:
                text "Nyx" size 28 color "#a99be8"
                hbox:
                    spacing 14
                    text "Trust" xsize 90
                    bar value VariableValue("nyx_trust", 100) xmaximum 560
                    text "[nyx_trust]/100" xsize 90
                hbox:
                    spacing 14
                    text "Like" xsize 90
                    bar value VariableValue("nyx_like", 100) xmaximum 560
                    text "[nyx_like]/100" xsize 90
                hbox:
                    spacing 14
                    text "Love" xsize 90
                    bar value VariableValue("nyx_love", 100) xmaximum 560
                    text "[nyx_love]/100" xsize 90
            else:
                text "Nyx — not met yet" size 23 color "#a99be8"
            null height 12
            text "Press R or Esc to close" size 16 color "#cbd6e2" xalign 0.5
            textbutton "Close" action Hide("relationship_status") xalign 0.5
# PHONE NOTIFICATION SCREEN



# ============================================================



screen phone_notification(sender, timestamp, message):



    zorder 100



    modal True



    frame:



        xalign 0.97



        yalign 0.04



        xsize 480



        padding (24, 20)



        background "#202a36ee"



        vbox:



            spacing 12



            hbox:



                spacing 8



                text sender:



                    size 23



                    color "#ffffff"



                    bold True



                null width 1



                text timestamp:



                    size 15



                    color "#aab8c8"



            text message:



                size 19



                color "#ffffff"



                line_spacing 5



            null height 8



            textbutton "Continue":



                action Return()



                text_size 17



                text_color "#ffffff"



                text_hover_color "#83dfb0"



# ============================================================



# LOCATION INTRODUCTION HELPER



# Displays the location once, then removes it.



# ============================================================



label show_location_intro(location, time):



    show screen location_title(location, time)



    pause 2.5



    hide screen location_title



    return



# ============================================================



# GAME START



# ============================================================



label start:
    show screen relationship_hotkey



    call act1_scene1



    call act1_scene2



    return



# ============================================================



# ACT I — SCENE 1



# A VERY LONG ROAD



# ============================================================



label act1_scene1:



    scene bg black



    with fade



    centered "{size=48}{color=#ffffff}OAKHAVEN{/color}{/size}"



    centered "{size=24}{color=#c8d5df}Wings of Tomorrow{/color}{/size}"



    pause 2.0



    centered "{size=22}ACT I{/size}"



    centered "{size=32}A Fox Without a Home{/size}"



    pause 2.0



    # --------------------------------------------------------



    # CITY BUS — 7:18 AM



    # --------------------------------------------------------



    scene bg bus



    with fade



    call show_location_intro(



        "Somewhere on the highway",



        "Monday — 7:18 AM"



    )



    show rowan neutral



    "The bus rumbled along the highway, its engine vibrating through the floor."



    "Outside the window, the scenery slowly began to change."



    "Tall buildings gave way to green hills, quiet neighborhoods, and distant forests."



    "Rowan sat alone beside the window, his backpack resting against his knees."



    "A young red fox with tired eyes, fluffy ears, and a tail that refused to sit still."



    "He had been traveling for hours."



    "And he was still a little bit terrified."



    rowan nervous "Okay..."



    rowan nervous "First day. New town. New job."



    thought nervous "Just don't mess this up."



    "He adjusted the strap of his backpack."



    thought nervous "Please, please, please let this work."



    pause 0.8



    # --------------------------------------------------------



    # MEDICAL BILL — 7:19 AM



    # --------------------------------------------------------



    call screen phone_notification(



        "MEDICAL BILLING",



        "7:19 AM",



        "Payment reminder: Your outstanding medical balance is $85,000. Please review your account."



    )



    show rowan sad



    "Rowan stared at the notification."



    "His ears slowly lowered."



    rowan sad "...Right."



    thought sad "Eighty-five thousand dollars."



    thought nervous "No pressure."



    "He locked his phone and placed it face-down on his lap."



    "For a moment, he just watched the passing scenery."



    pause 0.8



    # --------------------------------------------------------



    # BROTHER'S MESSAGE — 7:20 AM



    # --------------------------------------------------------



    call screen phone_notification(



        "Little Brother 💙",



        "7:20 AM",



        "Hey Rowan!! Are you there yet? Don't forget to eat breakfast, okay? You always skip it when you're nervous. Good luck with the job interview!! I know you can do it. Love you!! 💙"



    )



    show rowan happy



    "Rowan's expression softened."



    "A tiny smile appeared on his muzzle."



    thought happy "He's always looking out for me..."



    "He opened the message and started typing."



    menu:



        "What should Rowan reply?"



        "I'll be okay. Don't worry about me!":



            $ brother_reply = "I'll be okay. Don't worry about me!"



            rowan happy "I'll be okay. Don't worry about me!"



            "He added a little heart before sending it."



        "I miss you already. I'll call you tonight.":



            $ brother_reply = "I miss you already. I'll call you tonight."



            rowan sad "I miss you already. I'll call you tonight."



            "He hesitated before pressing send."



            "He really did miss him."



        "I'm nervous, but I'll do my best. Love you!":



            $ brother_reply = "I'm nervous, but I'll do my best. Love you!"



            rowan nervous "I'm nervous, but I'll do my best. Love you!"



            "It felt a little embarrassing to admit."



            "But it was true."



    "Message sent."



    thought happy "I have to make this work."



    pause 1.0



    driver "OakHaven coming up! We'll be arriving in a few minutes!"



    show rowan surprised



    "Rowan's ears perked up."



    # --------------------------------------------------------



    # APPROACHING OAKHAVEN — 7:24 AM



    # --------------------------------------------------------



    scene bg town



    with dissolve



    call show_location_intro(



        "Approaching OakHaven",



        "Monday — 7:24 AM"



    )



    show rowan surprised



    "There it was."



    "OakHaven."



    "A quiet town surrounded by rolling green hills and thick pine forests."



    "Its streets were lined with little shops, apartment buildings, and trees covered in morning dew."



    "A large sign stood near the entrance to town."



    centered "{size=30}{color=#ffffff}OAKHAVEN{/color}{/size}"



    centered "{size=17}{color=#dce8df}A COMMUNITY BUILT FOR TOMORROW{/color}{/size}"



    "Rowan watched the town pass by."



    rowan happy "It's... actually really pretty."



    "A little farther down the road, he spotted a large modern building."



    "The sign on its front read:"



    centered "{size=25}{color=#ffffff}OAKHAVEN REMOTE LOGISTICS{/color}{/size}"



    "The company he had applied to."



    "The company that might finally give him a chance."



    thought nervous "That's where I'm going."



    # --------------------------------------------------------



    # BUS TERMINAL — 7:42 AM



    # --------------------------------------------------------



    scene bg terminal



    with dissolve



    call show_location_intro(



        "OakHaven Central Bus Terminal",



        "Monday — 7:42 AM"



    )



    show rowan nervous



    "The bus pulled into the terminal."



    driver "OakHaven Central! Last stop!"



    "Rowan stood, grabbed his backpack, and carefully made his way toward the doors."



    rowan happy "Thank you!"



    driver "Have a good one, kid."



    "Rowan stepped down onto the pavement."



    "The bus pulled away behind him."



    "And just like that..."



    "He was here."



    pause 0.8



    "A cool morning breeze brushed through his fur."



    "Rowan looked around the terminal."



    "People hurried past with coffee cups and bags."



    "Somewhere nearby, a bicycle bell rang."



    "A car horn sounded in the distance."



    "Everything was unfamiliar."



    thought nervous "Okay. I can do this."



    "He opened his phone and checked his notes."



    centered "{size=30}{color=#ffffff}ROWAN'S TO-DO LIST{/color}{/size}"



    centered "{color=#83df9b}✓ Arrive in OakHaven{/color}"



    centered "{color=#ffffff}□ Find somewhere affordable to stay{/color}"



    centered "{color=#ffffff}□ Attend job interview — 10:00 AM{/color}"



    centered "{color=#ffffff}□ Get hired{/color}"



    centered "{color=#ffffff}□ Start paying off medical debt{/color}"



    pause 1.5



    "He looked at the last item for a little too long."



    thought sad "One step at a time."



    # --------------------------------------------------------



    # MARKET STREET — 7:48 AM



    # --------------------------------------------------------



    scene bg market



    with dissolve



    call show_location_intro(



        "Market Street",



        "Monday — 7:48 AM"



    )



    show rowan neutral



    "A short walk brought Rowan to the entrance of Market Street."



    "The street was beginning to wake up."



    "Shopkeepers were opening their doors."



    "A delivery van rolled past."



    "The smell of fresh bread drifted through the air."



    "Rowan spotted several places nearby."



    "A small café with warm lights glowing through its windows."



    "A convenience store on the opposite corner."



    "A path leading toward a green park."



    "And, farther down the road..."



    "The OakHaven Remote Logistics campus."



    "He checked his phone again."



    # --------------------------------------------------------



    # INTERVIEW REMINDER



    # --------------------------------------------------------



    call screen phone_notification(



        "INTERVIEW REMINDER",



        "7:48 AM",



        "Reminder: Your interview is scheduled for Monday at 10:00 AM. Location: Main Reception, OakHaven Logistics Campus. Please arrive 15 minutes early."



    )



    show rowan nervous



    "Rowan swallowed."



    rowan nervous "Ten o'clock..."



    thought nervous "I've got time."



    thought nervous "I've got plenty of time."



    pause 0.5



    "He looked down at his wallet."



    "Thirty-five dollars."



    "That was everything he had available right now."



    thought nervous "Maybe I should find something to eat."



    thought sad "Or maybe I should save the money."



    "His stomach gave a quiet growl."



    rowan embarrassed "...Traitor."



    "He let out a nervous little laugh."



    "For the first time that morning, he felt himself relax just a little."



    "He took a deep breath."



    show rowan neutral



    rowan "Okay."



    rowan "Let's make today count."



    # --------------------------------------------------------



    # FIRST DESTINATION CHOICE



    # --------------------------------------------------------



    menu:



        "Where should Rowan go first?"



        "Visit Whiskers Café":



            $ first_destination = "Whiskers Café"



            jump act1_scene1_cafe



        "Visit OakHaven Remote Logistics":



            $ first_destination = "OakHaven Remote Logistics"



            jump act1_scene1_company



        "Take a walk through Pinewood Park":



            $ first_destination = "Pinewood Park"



            jump act1_scene1_park



        "Explore Market Street":



            $ first_destination = "Market Street"



            jump act1_scene1_explore



# ============================================================



# BRANCH 1 — WHISKERS CAFÉ



# ============================================================



label act1_scene1_cafe:



    scene bg cafe



    with fade



    call show_location_intro(



        "Whiskers Café",



        "Monday — 8:05 AM"



    )



    show rowan nervous



    "A little bell jingled as Rowan approached the café."



    "Warm light spilled through the front windows."



    "The smell of coffee and freshly baked bread drifted outside."



    centered "{size=34}{color=#ffffff}WHISKERS CAFÉ{/color}{/size}"



    "Rowan looked through the window."



    "There were a few customers inside."



    "It seemed quiet."



    thought nervous "I could probably afford something small..."



    "He adjusted his backpack."



    show rowan happy



    rowan "Alright. Breakfast."



    "He reached for the door handle."



    "The little bell jingled again as he stepped inside."



    "Warm air surrounded him."



    "For the first time since arriving in OakHaven, Rowan felt like he could sit down."



    "Just for a little while."



    jump act1_scene1_end



# ============================================================



# BRANCH 2 — OAKHAVEN REMOTE LOGISTICS



# ============================================================



label act1_scene1_company:



    scene bg company



    with fade



    call show_location_intro(



        "OakHaven Remote Logistics",



        "Monday — 8:05 AM"



    )



    show rowan surprised



    "Rowan followed the road toward the logistics campus."



    "The building was larger up close."



    "Modern glass windows reflected the morning sunlight."



    "Small delivery drones could be seen flying between different sections of the campus."



    centered "{size=29}{color=#ffffff}OAKHAVEN REMOTE LOGISTICS{/color}{/size}"



    "Rowan stopped outside the main entrance."



    rowan surprised "Whoa..."



    "A drone zipped overhead."



    "Its small motors made a quiet buzzing sound."



    thought happy "So this is where I'll be working..."



    "He checked the time."



    "Still far too early for his interview."



    "He decided to take a closer look around the outside of the building."



    jump act1_scene1_end



# ============================================================



# BRANCH 3 — PINEWOOD PARK



# ============================================================



label act1_scene1_park:



    scene bg park



    with fade



    call show_location_intro(



        "Pinewood Park",



        "Monday — 8:05 AM"



    )



    show rowan happy



    "Rowan followed a nearby path toward the park."



    "Tall pine trees surrounded the walking trail."



    "The morning sunlight filtered through their branches."



    "A few birds chirped from somewhere overhead."



    "There were benches along the path and a small pond farther ahead."



    "Rowan found an empty bench and sat down."



    "His tail curled around his side."



    thought happy "Maybe I needed this."



    "For a moment, he didn't think about the interview."



    "Or the debt."



    "Or how much everything depended on today."



    "He simply listened to the birds."



    jump act1_scene1_end



# ============================================================



# BRANCH 4 — MARKET STREET



# ============================================================



label act1_scene1_explore:



    scene bg market



    with fade



    call show_location_intro(



        "Market Street",



        "Monday — 8:05 AM"



    )



    show rowan neutral



    "Rowan decided to explore the street before committing to anywhere."



    "There were little shops on both sides of the road."



    "A convenience store."



    "A clothing shop."



    "A small grocery store."



    "A few apartments sat above the businesses."



    "He wondered how much rent cost around here."



    thought nervous "I really need somewhere to stay."



    "He looked at the shop windows as he walked."



    thought happy "Maybe OakHaven wouldn't be such a bad place to start over."



    jump act1_scene1_end



# ============================================================



# SCENE 1 END



# ============================================================



label act1_scene1_end:



    scene bg black



    with fade



    centered "{size=36}{color=#ffffff}SCENE 1 COMPLETE{/color}{/size}"



    centered "{size=23}A Very Long Road{/size}"



    pause 1.5



    "Rowan's first morning in OakHaven had begun."



    "There was still a job interview ahead."



    "A place to find."



    "And a very long road toward paying off his family's debt."



    "But he wasn't alone in the world."



    "Not completely."



    "And perhaps OakHaven had more waiting for him than he expected."



    pause 1.5



    return



# ============================================================



# ACT I — SCENE 2: FIRST IMPRESSIONS



# ============================================================



label act1_scene2:



    $ current_location = "Whiskers Café"



    scene bg cafe



    with fade



    call show_location_intro("Whiskers Café", "Monday — 8:12 AM")



    $ cafe_visited = True



    show rowan nervous:



        xalign 0.27



        yalign 1.0



        zoom 1.25
        yoffset -150


    # Elliot is already behind the counter when Rowan enters.

    show elliot neutral



    "The little bell above the café door jingled."



    "Warm air surrounded Rowan as he stepped inside."



    "The café smelled of freshly brewed coffee, warm bread, and something sweet."



    "A few customers sat at the tables."



    "Behind the counter stood a brown deer wearing a green cardigan and a pair of glasses."



    "He was arranging a few pastries when he noticed Rowan."



    show rowan surprised



    show elliot happy

    "The deer looked up and smiled."



    show elliot neutral
    show elliot happy
    elliot "Oh! Good morning!"



    show elliot neutral

    show elliot happy
    elliot "Welcome to Whiskers Café!"



    show rowan nervous



    show elliot happy
    rowan "G-Good morning..."



    show elliot neutral
    elliot "First time here?"



    show elliot happy
    rowan "Y-Yeah. I just arrived in OakHaven."



    "The deer leaned against the counter."



    show elliot happy

    elliot "Really? Welcome to town, then!"



    show elliot neutral
    elliot "I'm Elliot, by the way. I own the place."



    "He offered a friendly wave."



    $ elliot_met = True



    $ elliot_friendship += 1
    $ elliot_trust += 1
    $ elliot_like += 2



    show elliot happy
    rowan "I'm Rowan. Nice to meet you."



    show elliot neutral
    elliot "Nice to meet you too, Rowan!"



    "Elliot glanced at Rowan's backpack."



    show elliot neutral

    elliot "So, what brings you to OakHaven?"



    menu:



        "What should Rowan tell Elliot?"



        "I'm here for a job interview.":



            $ elliot_friendship += 1
            $ elliot_trust += 1
            $ elliot_like += 1



            show elliot happy
            rowan nervous "I'm here for a job interview."



            show elliot happy

            elliot "Oh! That's exciting!"



            show elliot neutral
            elliot "Where at?"



            rowan "OakHaven Remote Logistics."



            show elliot neutral
            elliot "Ah, the drone delivery company!"



            show elliot neutral
            elliot "They're always looking for people."



            show elliot happy
            elliot "Good luck! I hope it goes well."



            thought happy "He seems nice..."



        "I just moved here. I'm trying to start over.":



            $ elliot_friendship += 2
            $ elliot_trust += 2
            $ elliot_like += 1



            show elliot neutral
            rowan sad "I just moved here. I'm trying to start over."



            show elliot neutral
            elliot "Well, you've come to a pretty good place for that."



            show elliot neutral
            elliot "OakHaven can be a little quiet sometimes, but the people are generally friendly."



            show elliot happy
            elliot "I'm sure you'll find your place."



            show rowan embarrassed



            rowan "Th-Thanks..."



            show elliot happy
            elliot "Of course!"



        "It's a little complicated...":



            $ elliot_trust += 1
            show elliot neutral
            rowan nervous "It's... a little complicated."



            show elliot neutral

            elliot "Ah. Fair enough."



            show elliot neutral
            elliot "You don't have to explain anything."



            show elliot happy
            elliot "Sometimes a fresh cup of coffee is all someone needs."



            show rowan happy



            rowan "Heh... yeah."



    "Elliot glanced toward the display case."



    show elliot neutral
    elliot "Have you eaten breakfast yet?"



    "Rowan's stomach gave a small growl."



    show rowan embarrassed



    show elliot smug
    rowan "...Maybe."



    show elliot smug
    elliot "That sounds like a no."



    "Elliot chuckled."



    show elliot neutral
    elliot "Well, we've got a few things available."



    show elliot neutral
    elliot "Nothing too fancy, but everything's fresh."



    # --------------------------------------------------------



    # BREAKFAST MENU



    # --------------------------------------------------------



    $ breakfast_choice = ""



    $ breakfast_cost = 0



    menu:



        "What should Rowan order? (Wallet: $[wallet])"



        "Butter toast — $3":



            $ breakfast_choice = "Butter toast"



            $ breakfast_cost = 3



        "Fresh sandwich — $7":



            $ breakfast_choice = "Fresh sandwich"



            $ breakfast_cost = 7



        "Coffee — $4":



            $ breakfast_choice = "Coffee"



            $ breakfast_cost = 4



        "Apple pastry — $3":



            $ breakfast_choice = "Apple pastry"



            $ breakfast_cost = 3



        "Tea — $3":



            $ breakfast_choice = "Tea"



            $ breakfast_cost = 3



        "Nothing. Save the money.":



            $ breakfast_choice = "Nothing"



            $ breakfast_cost = 0



    if breakfast_cost > 0:



        if wallet >= breakfast_cost:



            $ wallet -= breakfast_cost



            $ breakfast_purchased = True



            $ breakfast_eaten = True



            show elliot happy
            rowan nervous "Could I... um... have the [breakfast_choice.lower()], please?"



            show elliot happy

            elliot "Absolutely!"



            "Elliot prepared Rowan's order."



            "A few moments later, he placed it on the counter."



            show elliot happy
            elliot "There you go!"



            rowan happy "Thank you!"



            "Rowan paid and carefully picked up his food."



            show elliot happy
            elliot "Enjoy!"



            "Rowan took a bite."



            "It was simple, but surprisingly good."



            thought happy "Oh... that's actually really nice."



        else:



            rowan embarrassed "Actually... I don't think I have enough."



            show elliot neutral
            elliot "Oh! Don't worry about it."



            "Elliot put the food away."



            show elliot neutral
            elliot "Maybe another time."



    else:



        rowan nervous "I think I'll save my money."



        show elliot neutral
        elliot "That's alright!"



        show elliot neutral
        elliot "Just don't forget to eat something later, okay?"



        rowan embarrassed "I'll try..."



    # --------------------------------------------------------



    # SITTING BY THE WINDOW



    # --------------------------------------------------------



    "Rowan found a small table beside the window."



    "He placed his backpack beside the chair and sat down."



    show rowan neutral



    "Outside, Market Street was slowly getting busier."



    "People walked past the café windows."



    "A delivery van stopped near the curb."



    "For a moment, Rowan almost forgot how nervous he had been."



    thought happy "Maybe this place isn't so bad."



    "He pulled out his phone."



    "His brother's earlier message was still open."



    "Rowan smiled faintly."



    thought happy "I should call him later."



    # --------------------------------------------------------



    # COMMUNITY NOTICEBOARD



    # --------------------------------------------------------



    "After finishing his breakfast, Rowan noticed a large noticeboard near the café entrance."



    "It was covered with colorful flyers and handwritten notes."



    "One flyer caught his attention."



    centered "{size=30}{color=#ffffff}OAKHAVEN COMMUNITY BOARD{/color}{/size}"



    centered "{size=23}{color=#a7c98a}COMMUNITY GATHERING{/color}{/size}"



    centered "{size=18}Pinewood Park — Saturday Morning{/size}"



    centered "{size=18}Everyone is welcome!{/size}"



    "Another notice advertised affordable rooms for rent."



    centered "{size=23}{color=#83b7df}ROOMS AVAILABLE{/color}{/size}"



    centered "{size=18}OakHaven Community Housing Office{/size}"



    centered "{size=18}Affordable accommodation for new residents{/size}"



    "Rowan leaned closer to read the details."



    $ housing_info_found = True



    $ cafe_quest_unlocked = True



    thought happy "Affordable rooms... I should remember that."



    menu:



        "What should Rowan do?"



        "Ask Elliot about affordable housing.":



            $ elliot_friendship += 2
            $ elliot_trust += 2
            $ elliot_like += 1



            show rowan nervous



            show elliot neutral
            rowan "Um... Elliot?"



            show elliot neutral
            elliot "Yeah?"



            show elliot neutral
            rowan "Do you know anything about the rooms on that notice?"



            show elliot neutral
            elliot "Oh! The Community Housing Office."



            show elliot neutral
            elliot "They help people who are new to OakHaven find affordable places to stay."



            show elliot happy
            elliot "You should definitely stop by sometime."



            rowan happy "Really? That would be helpful."



            show elliot happy
            elliot "Of course!"



            show elliot neutral
            elliot "There's also a little apartment building near Market Street."



            show elliot neutral
            elliot "Sometimes they have rooms available."



            thought happy "That's something, at least."



            "Rowan took a picture of the flyer."



        "Read more of the flyers.":



            "Rowan spent a few minutes looking through the other notices."



            "There were advertisements for community events, volunteer opportunities, and local services."



            "He found another small flyer advertising a weekend market."



            thought happy "There's quite a lot going on around here."



            "He took a picture of the housing notice."



        "Return to the table.":



            "Rowan decided he had enough information for now."



            "He returned to his table and picked up his backpack."



    # --------------------------------------------------------



    # ELLIOT CHECKS IN



    # --------------------------------------------------------



    "A little while later, Elliot walked over to Rowan's table."



    show elliot neutral
    elliot "Everything alright over here?"



    show rowan happy



    rowan "Y-Yeah. Everything's really nice."



    show elliot happy
    elliot "Glad to hear it!"



    "Elliot pulled out the chair opposite Rowan."



    show elliot neutral
    elliot "Mind if I sit for a minute?"



    rowan "Oh! N-No, go ahead."



    "Elliot sat down."



    show elliot neutral
    elliot "So, do you have somewhere to stay yet?"



    show rowan nervous



    show elliot neutral
    rowan "Not... exactly."



    show elliot neutral
    elliot "Ah."



    show elliot neutral
    elliot "Well, don't panic."



    show elliot neutral
    elliot "There are a few affordable places around town."



    show elliot neutral
    elliot "The housing office is probably your best starting point."



    show elliot happy
    rowan "I'll look into it."



    show elliot neutral
    elliot "Good!"



    "Elliot smiled."



    show elliot neutral
    elliot "OakHaven's a pretty welcoming place."



    show elliot happy
    elliot "It might take a little while, but you'll find your people."



    show rowan embarrassed



    rowan "I-I hope so."



    # --------------------------------------------------------



    # GETTING TO KNOW ROWAN



    # --------------------------------------------------------



    show elliot neutral
    elliot "So, Rowan..."



    show elliot neutral
    elliot "How are you feeling about everything?"



    menu:



        "What should Rowan say?"



        "I'm nervous about my interview.":



            $ elliot_friendship += 2
            $ elliot_trust += 1
            $ elliot_like += 2



            show rowan nervous



            show elliot neutral
            rowan "Honestly? I'm really nervous about the interview."



            rowan "I really need this job."



            show elliot neutral
            elliot "That's understandable."



            show elliot neutral
            elliot "First interviews are always a little scary."



            show elliot neutral
            elliot "Just take a breath and be yourself."



            show elliot happy
            elliot "You've got this."



            show rowan happy



            rowan "Thanks..."



            thought happy "That actually helps."



        "I'm not very good at meeting new people.":



            $ elliot_friendship += 2
            $ elliot_trust += 1
            $ elliot_like += 2



            show rowan embarrassed



            show elliot smug
            rowan "I'm... not really good at meeting new people."



            show elliot happy
            elliot "Really?"



            "Elliot smiled."



            show elliot smug
            elliot "Well, you're doing pretty well right now!"



            show rowan embarrassed



            rowan "A-Ah..."



            "Rowan's ears lowered."



            show elliot embarrassed

            elliot "Sorry! Didn't mean to embarrass you."



            "Elliot chuckled softly."



        "I'd rather not talk about it.":



            show rowan nervous



            $ elliot_trust += 2
            show elliot neutral
            rowan "I'd... rather not talk about it."



            show elliot happy

            show elliot neutral
            elliot "No problem."



            show elliot neutral
            elliot "Everyone deserves a little privacy."



            rowan "Thanks."



            show elliot happy
            elliot "Anytime."



    # --------------------------------------------------------



    # INTERVIEW REMINDER — 8:47 AM



    # --------------------------------------------------------



    call screen phone_notification(



        "INTERVIEW REMINDER",



        "8:47 AM",



        "Reminder: Your interview at OakHaven Remote Logistics is approaching. Please arrive at Main Reception by 9:45 AM."



    )



    show rowan surprised



    "Rowan looked at his phone."



    rowan "Oh!"



    thought nervous "Right! The interview!"



    "He quickly checked the time."



    "He still had time, but he didn't want to be late."



    show rowan nervous



    rowan "I should probably get going."



    show elliot neutral
    elliot "Got an interview?"



    show elliot happy
    rowan "Y-Yeah. At OakHaven Remote Logistics."



    show elliot neutral
    elliot "Oh, right!"



    show elliot neutral
    elliot "Well, I won't keep you."



    "Elliot stood up."



    show elliot happy
    elliot "Good luck, Rowan."



    show elliot neutral
    elliot "And hey..."



    show elliot happy
    elliot "You're welcome here anytime."



    show rowan happy



    show elliot happy
    rowan "Really?"



    show elliot happy
    elliot "Of course!"



    show elliot happy
    elliot "First cup of tea is on the house next time."



    show rowan embarrassed



    rowan "Y-You don't have to do that..."



    show elliot neutral
    elliot "I know."



    show elliot happy
    elliot "I want to."



    "Rowan's cheeks turned a little pink."



    rowan "Th-Thank you, Elliot."



    show elliot happy
    elliot "Anytime!"



    $ elliot_friendship += 1
    $ elliot_trust += 1
    $ elliot_like += 1



    # --------------------------------------------------------



    # NEW ACQUAINTANCE



    # --------------------------------------------------------



    "Rowan adjusted his backpack."



    "He felt a little less like a stranger than he had when he first walked through the door."



    thought happy "Maybe I can make friends here."



    centered "{size=30}{color=#a7c98a}NEW ACQUAINTANCE{/color}{/size}"



    centered "{size=26}Elliot{/size}"



    centered "{size=18}Owner of Whiskers Café{/size}"



    pause 1.5



    centered "{size=30}{color=#83b7df}NEW SIDE QUEST{/color}{/size}"



    centered "{size=25}A Familiar Face at the Café{/size}"



    centered "{size=18}Visit Elliot again sometime.{/size}"



    pause 2.0



    # --------------------------------------------------------



    # LEAVING THE CAFÉ — 8:50 AM



    # --------------------------------------------------------



    scene bg market



    with dissolve



    call show_location_intro("Market Street", "Monday — 8:50 AM")



    show rowan happy:



        xalign 0.27



        yalign 1.0



        zoom 1.25
        yoffset -150



    "Rowan stepped outside."



    "The little bell jingled behind him."



    "He looked back through the window."



    "Elliot waved from behind the counter."



    rowan happy "Bye!"



    show elliot happy
    elliot "See you later!"



    "Rowan waved back."

    hide elliot
    show nyx neutral
    "Rowan had only taken a few steps when a black cat nearby glanced over."
    nyx "You're new around here, aren't you?"
    show rowan surprised
    rowan "H-Huh?"
    show nyx smug
    nyx "Backpack, nervous ears, and that very lost look. Kind of gives it away."
    show rowan embarrassed
    rowan "I... guess I'm not very subtle."
    show nyx happy
    nyx "Don't worry. OakHaven can be confusing on your first day. I'm Nyx."
    $ nyx_met = True
    $ nyx_trust += 1
    $ nyx_like += 1
    menu:
        "How should Rowan respond to Nyx?"
        "Apologize for being distracted.":
            show rowan embarrassed
            rowan "Sorry. I've got a lot on my mind today."
            show nyx happy
            nyx "Fair enough. First days can be a lot."
            $ nyx_trust += 2
            $ nyx_like += 1
        "Joke back about the lost look.":
            show rowan happy
            rowan "Well, at least I look consistently lost."
            show nyx smug
            nyx "That's one way to own it."
            $ nyx_like += 2
        "Introduce himself properly.":
            show rowan nervous
            rowan "I'm Rowan. Nice to meet you."
            show nyx neutral
            nyx "Nyx. And welcome to OakHaven, Rowan."
            $ nyx_trust += 1
            $ nyx_like += 1
    show nyx happy
    nyx "If you're looking for places around town, the community board inside the café is actually useful."
    rowan happy "Thanks. I'll remember that."
    "Nyx gave Rowan a small wave before heading down Market Street."
    hide nyx
    centered "{size=30}{color=#a99be8}NEW ACQUAINTANCE{/color}{/size}"
    centered "{size=26}Nyx{/size}"
    centered "{size=18}A local black cat{/size}"
    pause 1.5




    "Then he turned toward the road leading to OakHaven Remote Logistics."



    "His interview was getting closer."



    "He still needed somewhere to live."



    "He still had a very long way to go."



    "But at least he had met someone."



    thought happy "One step at a time."



    # --------------------------------------------------------



    # UPDATED CHECKLIST



    # --------------------------------------------------------



    centered "{size=30}{color=#ffffff}ROWAN'S TO-DO LIST{/color}{/size}"



    centered "{color=#83df9b}✓ Arrive in OakHaven{/color}"



    centered "{color=#83df9b}✓ Visit Whiskers Café{/color}"



    centered "{color=#83df9b}✓ Meet Elliot{/color}"
    centered "{color=#83df9b}✓ Meet Nyx{/color}"



    centered "{color=#ffffff}□ Find somewhere affordable to stay{/color}"



    centered "{color=#ffffff}□ Attend job interview — 10:00 AM{/color}"



    centered "{color=#ffffff}□ Get hired{/color}"



    centered "{color=#ffffff}□ Start paying off medical debt{/color}"



    pause 2.0



    # --------------------------------------------------------



    # SCENE 2 COMPLETE



    jump act1_scene2_end



label act1_scene2_end:



    scene bg black



    with fade



    centered "{size=36}{color=#ffffff}SCENE 2 COMPLETE{/color}{/size}"



    centered "{size=23}First Impressions{/size}"



    pause 1.5



    "A warm cup of tea."



    "A friendly conversation."



    "And a new face in a town full of strangers."



    "Perhaps OakHaven was already beginning to feel a little more like home."



    pause 2.0



    return


"""

# ============================================================



# OAKHAVEN: WINGS OF TOMORROW



# ACT I — A FOX WITHOUT A HOME



# SCENE 1 — A VERY LONG ROAD



# ============================================================



# ------------------------------------------------------------



# CHARACTERS



# ------------------------------------------------------------



define rowan = Character(



    "Rowan",



    color="#e89a55",



    image="rowan"



)



define thought = Character(



    "Rowan",



    color="#e89a55",



    image="rowan",



    what_italic=True



)



define driver = Character(



    "Bus Driver",



    color="#aab8c8"



)



define elliot = Character("Elliot", color="#a7c98a")

define nyx = Character("Nyx", color="#a99be8")
define milo = Character("Milo", color="#e6b86f")



# ------------------------------------------------------------



# PLAYER DATA



# ------------------------------------------------------------



default wallet = 35



default medical_debt = 85000



default brother_reply = ""



default first_destination = ""



default interview_complete = False



default breakfast_purchased = False



default current_location = "City Bus"



default elliot_met = False



default elliot_friendship = 0



default cafe_visited = False



default breakfast_choice = ""



default breakfast_cost = 0



default breakfast_eaten = False



default cafe_quest_unlocked = False



default housing_info_found = False
default elliot_trust = 0
default elliot_like = 0
default elliot_love = 0

default nyx_met = False
default nyx_trust = 0
default nyx_like = 0
default nyx_love = 0

# Milo — the upbeat community medic
default milo_met = False
default milo_trust = 0
default milo_like = 0
default milo_love = 0


# ------------------------------------------------------------
# EXPANDED ROMANCE SYSTEM
# ------------------------------------------------------------

# Important memories for each character.
default elliot_memories = []
default nyx_memories = []
default milo_memories = []

# One-time gift events.
default elliot_gift_received = False
default nyx_gift_received = False
default milo_gift_received = False

# One-time date events.
default elliot_date_completed = False
default nyx_date_completed = False
default milo_date_completed = False

# Confession and romance-route status.
default elliot_confessed = False
default nyx_confessed = False
default milo_confessed = False

default elliot_romance_active = False
default nyx_romance_active = False
default milo_romance_active = False

# Prevent one-time relationship events from repeating.
default elliot_spark_seen = False
default nyx_spark_seen = False
default milo_spark_seen = False

default elliot_crush_seen = False
default nyx_crush_seen = False
default milo_crush_seen = False

# Used by the romance activity menu.
default romance_target = ""




# ------------------------------------------------------------




# ------------------------------------------------------------
# RELATIONSHIP HELPERS
# ------------------------------------------------------------

init python:

    def change_relationship(character, trust=0, like=0, love=0):
        """
        Safely changes relationship values.
        Values always stay between 0 and 100.
        """

        for stat, amount in [
            ("trust", trust),
            ("like", like),
            ("love", love)
        ]:

            variable = character + "_" + stat
            current = getattr(store, variable)

            setattr(
                store,
                variable,
                max(0, min(100, current + amount))
            )


    def relationship_stage(character):

        trust = getattr(store, character + "_trust")
        like = getattr(store, character + "_like")
        love = getattr(store, character + "_love")

        if love >= 80 and trust >= 60 and like >= 60:
            return "Soulmates"

        elif love >= 60 and trust >= 40 and like >= 40:
            return "Deeply in Love"

        elif love >= 40 and trust >= 25 and like >= 25:
            return "Crushing"

        elif love >= 25:
            return "Growing Feelings"

        elif love >= 10:
            return "A Little Spark"

        elif like >= 40 and trust >= 40:
            return "Close Friends"

        elif like >= 20:
            return "Friends"

        elif like > 0:
            return "Acquaintances"

        return "Strangers"


    def can_go_on_date(character):

        trust = getattr(store, character + "_trust")
        love = getattr(store, character + "_love")
        completed = getattr(store, character + "_date_completed")

        return (
            trust >= 20
            and love >= 25
            and not completed
        )


    def can_confess(character):

        trust = getattr(store, character + "_trust")
        like = getattr(store, character + "_like")
        love = getattr(store, character + "_love")
        confessed = getattr(store, character + "_confessed")

        return (
            trust >= 40
            and like >= 40
            and love >= 60
            and not confessed
        )


# BACKGROUNDS



# Backgrounds are loaded from game/images/backgrounds/.



# ------------------------------------------------------------



image bg bus = "images/backgrounds/bg_bus.png"



image bg town = "images/backgrounds/bg_town.png"



image bg terminal = "images/backgrounds/bg_terminal.png"



image bg market = "images/backgrounds/bg_market.png"



image bg cafe = "images/backgrounds/bg_cafe.png"



image bg park = "images/backgrounds/bg_park.png"



image bg company = "images/backgrounds/bg_company.png"



# Black transition background



image bg black = Solid("#000000")



# ------------------------------------------------------------



# ROWAN'S CHARACTER SPRITES



#



# All eight expressions use the same position and size.



# xalign 0.27 = right side of the screen.
# In this layout, 0.27 places Rowan on the left side of the screen.



# yalign 1.0 = bottom of the screen.



# zoom 1.25 = sprite size.



# ------------------------------------------------------------



image rowan neutral:



    "images/characters/rowan_neutral.png"



    xalign 0.27



    yalign 1.0



    zoom 1.25
    yoffset -150



image rowan happy:



    "images/characters/rowan_happy.png"



    xalign 0.27



    yalign 1.0



    zoom 1.25
    yoffset -150



image rowan nervous:



    "images/characters/rowan_nervous.png"



    xalign 0.27



    yalign 1.0



    zoom 1.25
    yoffset -150



image rowan embarrassed:



    "images/characters/rowan_embarrassed.png"



    xalign 0.27



    yalign 1.0



    zoom 1.25
    yoffset -150



image rowan sad:



    "images/characters/rowan_sad.png"



    xalign 0.27



    yalign 1.0



    zoom 1.25
    yoffset -150



image rowan angry:



    "images/characters/rowan_angry.png"



    xalign 0.27



    yalign 1.0



    zoom 1.25
    yoffset -150



image rowan surprised:



    "images/characters/rowan_surprised.png"



    xalign 0.27



    yalign 1.0



    zoom 1.25
    yoffset -150



image rowan tired:



    "images/characters/rowan_tired.png"



    xalign 0.27



    yalign 1.0



    zoom 1.25
    yoffset -150


# ------------------------------------------------------------
# ELLIOT'S CHARACTER SPRITES
# ------------------------------------------------------------
# Elliot stands on the right side, opposite Rowan.

image elliot neutral:

    "images/characters/elliot_neutral.png"

    xalign 0.73

    yalign 1.0

    zoom 1.10
    yoffset -150

image elliot happy:

    "images/characters/elliot_happy.png"

    xalign 0.73

    yalign 1.0

    zoom 1.10
    yoffset -150

image elliot smug:

    "images/characters/elliot_smug.png"

    xalign 0.73

    yalign 1.0

    zoom 1.10
    yoffset -150

image elliot surprised:

    "images/characters/elliot_surprised.png"

    xalign 0.73

    yalign 1.0

    zoom 1.10
    yoffset -150

image elliot embarrassed:

    "images/characters/elliot_embarrassed.png"

    xalign 0.73

    yalign 1.0

    zoom 1.10
    yoffset -150

image elliot sad:

    "images/characters/elliot_sad.png"

    xalign 0.73

    yalign 1.0

    zoom 1.10
    yoffset -150

image elliot angry:

    "images/characters/elliot_angry.png"

    xalign 0.73

    yalign 1.0

    zoom 1.10
    yoffset -150

image elliot tired:

    "images/characters/elliot_tired.png"

    xalign 0.73

    yalign 1.0

    zoom 1.10
    yoffset -150



# ============================================================




# ------------------------------------------------------------
# NYX'S CHARACTER SPRITES
# Nyx is a black cat. Their sprites are placed above the dialogue box.
# ------------------------------------------------------------
image nyx neutral:
    "images/characters/nyx_neutral.png"
    xalign 0.73
    yalign 1.0
    zoom 1.10
    yoffset -150

image nyx happy:
    "images/characters/nyx_happy.png"
    xalign 0.73
    yalign 1.0
    zoom 1.10
    yoffset -150

image nyx smug:
    "images/characters/nyx_smug.png"
    xalign 0.73
    yalign 1.0
    zoom 1.10
    yoffset -150

image nyx annoyed:
    "images/characters/nyx_annoyed.png"
    xalign 0.73
    yalign 1.0
    zoom 1.10
    yoffset -150

image nyx surprised:
    "images/characters/nyx_surprised.png"
    xalign 0.73
    yalign 1.0
    zoom 1.10
    yoffset -150

image nyx embarrassed:
    "images/characters/nyx_embarrassed.png"
    xalign 0.73
    yalign 1.0
    zoom 1.10
    yoffset -150

image nyx sad:
    "images/characters/nyx_sad.png"
    xalign 0.73
    yalign 1.0
    zoom 1.10
    yoffset -150
# ------------------------------------------------------------
# MILO'S CHARACTER SPRITES
# Milo is a golden retriever medic, placed on the right opposite Rowan.
# Put milo_neutral.png, milo_happy.png, etc. in images/characters/.
# ------------------------------------------------------------
image milo neutral:
    "images/characters/milo_neutral.png"
    xalign 0.73
    yalign 1.0
    zoom 1.10
    yoffset -150

image milo happy:
    "images/characters/milo_happy.png"
    xalign 0.73
    yalign 1.0
    zoom 1.10
    yoffset -150

image milo smug:
    "images/characters/milo_smug.png"
    xalign 0.73
    yalign 1.0
    zoom 1.10
    yoffset -150

image milo surprised:
    "images/characters/milo_surprised.png"
    xalign 0.73
    yalign 1.0
    zoom 1.10
    yoffset -150

image milo embarrassed:
    "images/characters/milo_embarrassed.png"
    xalign 0.73
    yalign 1.0
    zoom 1.10
    yoffset -150

image milo sad:
    "images/characters/milo_sad.png"
    xalign 0.73
    yalign 1.0
    zoom 1.10
    yoffset -150

image milo angry:
    "images/characters/milo_angry.png"
    xalign 0.73
    yalign 1.0
    zoom 1.10
    yoffset -150

image milo tired:
    "images/characters/milo_tired.png"
    xalign 0.73
    yalign 1.0
    zoom 1.10
    yoffset -150


# LOCATION INTRODUCTION SCREEN



# ============================================================



screen location_title(location, time):



    zorder 50



    frame:



        xalign 0.5



        yalign 0.13



        padding (35, 20)



        background "#182330dd"



        vbox:



            spacing 8



            xalign 0.5



            text location:



                size 32



                color "#ffffff"



                xalign 0.5



            text time:



                size 18



                color "#c8d5df"



                xalign 0.5



# ============================================================




# ============================================================
# RELATIONSHIP STATUS
# Press R during gameplay to view Trust, Like, and Love.
# ============================================================
screen relationship_hotkey():
    key "r" action ToggleScreen("relationship_status")
    key "R" action ToggleScreen("relationship_status")


screen relationship_status():

    modal True
    zorder 200

    key "K_ESCAPE" action Hide("relationship_status")

    frame:
        xalign 0.5
        yalign 0.5
        xsize 1000
        ymaximum 800
        padding (35, 28)
        background "#172332f5"

        viewport:
            scrollbars "vertical"
            mousewheel True
            draggable True

            vbox:
                spacing 16

                text "RELATIONSHIPS":
                    size 36
                    color "#ffffff"
                    xalign 0.5

                text "The people of OakHaven are getting to know Rowan.":
                    size 18
                    color "#cbd6e2"
                    xalign 0.5

                text "Trust measures how much someone relies on Rowan.":
                    size 15
                    color "#aab8c8"
                    xalign 0.5

                text "Like measures friendship and affection.":
                    size 15
                    color "#aab8c8"
                    xalign 0.5

                text "Love measures romantic feelings.":
                    size 15
                    color "#f2a6c6"
                    xalign 0.5

                null height 10

                # ELLIOT

                text "Elliot":
                    size 28
                    color "#a7c98a"

                text "[relationship_stage('elliot')]":
                    size 19
                    color "#ffffff"

                hbox:
                    spacing 14
                    text "Trust" xsize 80
                    bar value VariableValue("elliot_trust", 100) xmaximum 550
                    text "[elliot_trust]/100"

                hbox:
                    spacing 14
                    text "Like" xsize 80
                    bar value VariableValue("elliot_like", 100) xmaximum 550
                    text "[elliot_like]/100"

                hbox:
                    spacing 14
                    text "Love" xsize 80
                    bar value VariableValue("elliot_love", 100) xmaximum 550
                    text "[elliot_love]/100"

                if elliot_romance_active:
                    text "Romance route: Active" color "#f2a6c6"
                elif can_confess("elliot"):
                    text "A confession opportunity is available!" color "#f2a6c6"
                elif can_go_on_date("elliot"):
                    text "A date opportunity is available!" color "#f2a6c6"

                null height 10

                # NYX

                text "Nyx":
                    size 28
                    color "#a99be8"

                if nyx_met:

                    text "[relationship_stage('nyx')]":
                        size 19
                        color "#ffffff"

                    hbox:
                        spacing 14
                        text "Trust" xsize 80
                        bar value VariableValue("nyx_trust", 100) xmaximum 550
                        text "[nyx_trust]/100"

                    hbox:
                        spacing 14
                        text "Like" xsize 80
                        bar value VariableValue("nyx_like", 100) xmaximum 550
                        text "[nyx_like]/100"

                    hbox:
                        spacing 14
                        text "Love" xsize 80
                        bar value VariableValue("nyx_love", 100) xmaximum 550
                        text "[nyx_love]/100"

                    if nyx_romance_active:
                        text "Romance route: Active" color "#f2a6c6"
                    elif can_confess("nyx"):
                        text "A confession opportunity is available!" color "#f2a6c6"
                    elif can_go_on_date("nyx"):
                        text "A date opportunity is available!" color "#f2a6c6"

                else:
                    text "Not met yet." color "#aab8c8"

                null height 10

                # MILO

                text "Milo":
                    size 28
                    color "#e6b86f"

                if milo_met:

                    text "[relationship_stage('milo')]":
                        size 19
                        color "#ffffff"

                    hbox:
                        spacing 14
                        text "Trust" xsize 80
                        bar value VariableValue("milo_trust", 100) xmaximum 550
                        text "[milo_trust]/100"

                    hbox:
                        spacing 14
                        text "Like" xsize 80
                        bar value VariableValue("milo_like", 100) xmaximum 550
                        text "[milo_like]/100"

                    hbox:
                        spacing 14
                        text "Love" xsize 80
                        bar value VariableValue("milo_love", 100) xmaximum 550
                        text "[milo_love]/100"

                    if milo_romance_active:
                        text "Romance route: Active" color "#f2a6c6"
                    elif can_confess("milo"):
                        text "A confession opportunity is available!" color "#f2a6c6"
                    elif can_go_on_date("milo"):
                        text "A date opportunity is available!" color "#f2a6c6"

                else:
                    text "Not met yet." color "#aab8c8"

                null height 20

                textbutton "Romance Activities":
                    xalign 0.5
                    action [
                        Hide("relationship_status"),
                        Call("romance_hub")
                    ]

                textbutton "Close":
                    xalign 0.5
                    action Hide("relationship_status")



# PHONE NOTIFICATION SCREEN



# ============================================================



screen phone_notification(sender, timestamp, message):



    zorder 100



    modal True



    frame:



        xalign 0.97



        yalign 0.04



        xsize 480



        padding (24, 20)



        background "#202a36ee"



        vbox:



            spacing 12



            hbox:



                spacing 8



                text sender:



                    size 23



                    color "#ffffff"



                    bold True



                null width 1



                text timestamp:



                    size 15



                    color "#aab8c8"



            text message:



                size 19



                color "#ffffff"



                line_spacing 5



            null height 8



            textbutton "Continue":



                action Return()



                text_size 17



                text_color "#ffffff"



                text_hover_color "#83dfb0"



# ============================================================



# LOCATION INTRODUCTION HELPER



# Displays the location once, then removes it.



# ============================================================



label show_location_intro(location, time):



    show screen location_title(location, time)



    pause 2.5



    hide screen location_title



    return



# ============================================================



# GAME START



# ============================================================



label start:
    show screen relationship_hotkey



    call act1_scene1



    call act1_scene2



    return



# ============================================================



# ACT I — SCENE 1



# A VERY LONG ROAD



# ============================================================



label act1_scene1:



    scene bg black



    with fade



    centered "{size=48}{color=#ffffff}OAKHAVEN{/color}{/size}"



    centered "{size=24}{color=#c8d5df}Wings of Tomorrow{/color}{/size}"



    pause 2.0



    centered "{size=22}ACT I{/size}"



    centered "{size=32}A Fox Without a Home{/size}"



    pause 2.0



    # --------------------------------------------------------



    # CITY BUS — 7:18 AM



    # --------------------------------------------------------



    scene bg bus



    with fade



    call show_location_intro(



        "Somewhere on the highway",



        "Monday — 7:18 AM"



    )



    show rowan neutral



    "The bus rumbled along the highway, its engine vibrating through the floor."



    "Outside the window, the scenery slowly began to change."



    "Tall buildings gave way to green hills, quiet neighborhoods, and distant forests."



    "Rowan sat alone beside the window, his backpack resting against his knees."



    "A young red fox with tired eyes, fluffy ears, and a tail that refused to sit still."



    "He had been traveling for hours."



    "And he was still a little bit terrified."



    rowan nervous "Okay..."



    rowan nervous "First day. New town. New job."



    thought nervous "Just don't mess this up."



    "He adjusted the strap of his backpack."



    thought nervous "Please, please, please let this work."



    pause 0.8



    # --------------------------------------------------------



    # MEDICAL BILL — 7:19 AM



    # --------------------------------------------------------



    call screen phone_notification(



        "MEDICAL BILLING",



        "7:19 AM",



        "Payment reminder: Your outstanding medical balance is $85,000. Please review your account."



    )



    show rowan sad



    "Rowan stared at the notification."



    "His ears slowly lowered."



    rowan sad "...Right."



    thought sad "Eighty-five thousand dollars."



    thought nervous "No pressure."



    "He locked his phone and placed it face-down on his lap."



    "For a moment, he just watched the passing scenery."



    pause 0.8



    # --------------------------------------------------------



    # BROTHER'S MESSAGE — 7:20 AM



    # --------------------------------------------------------



    call screen phone_notification(



        "Little Brother 💙",



        "7:20 AM",



        "Hey Rowan!! Are you there yet? Don't forget to eat breakfast, okay? You always skip it when you're nervous. Good luck with the job interview!! I know you can do it. Love you!! 💙"



    )



    show rowan happy



    "Rowan's expression softened."



    "A tiny smile appeared on his muzzle."



    thought happy "He's always looking out for me..."



    "He opened the message and started typing."



    menu:



        "What should Rowan reply?"



        "I'll be okay. Don't worry about me!":



            $ brother_reply = "I'll be okay. Don't worry about me!"



            rowan happy "I'll be okay. Don't worry about me!"



            "He added a little heart before sending it."



        "I miss you already. I'll call you tonight.":



            $ brother_reply = "I miss you already. I'll call you tonight."



            rowan sad "I miss you already. I'll call you tonight."



            "He hesitated before pressing send."



            "He really did miss him."



        "I'm nervous, but I'll do my best. Love you!":



            $ brother_reply = "I'm nervous, but I'll do my best. Love you!"



            rowan nervous "I'm nervous, but I'll do my best. Love you!"



            "It felt a little embarrassing to admit."



            "But it was true."



    "Message sent."



    thought happy "I have to make this work."



    pause 1.0



    driver "OakHaven coming up! We'll be arriving in a few minutes!"



    show rowan surprised



    "Rowan's ears perked up."



    # --------------------------------------------------------



    # APPROACHING OAKHAVEN — 7:24 AM



    # --------------------------------------------------------



    scene bg town



    with dissolve



    call show_location_intro(



        "Approaching OakHaven",



        "Monday — 7:24 AM"



    )



    show rowan surprised



    "There it was."



    "OakHaven."



    "A quiet town surrounded by rolling green hills and thick pine forests."



    "Its streets were lined with little shops, apartment buildings, and trees covered in morning dew."



    "A large sign stood near the entrance to town."



    centered "{size=30}{color=#ffffff}OAKHAVEN{/color}{/size}"



    centered "{size=17}{color=#dce8df}A COMMUNITY BUILT FOR TOMORROW{/color}{/size}"



    "Rowan watched the town pass by."



    rowan happy "It's... actually really pretty."



    "A little farther down the road, he spotted a large modern building."



    "The sign on its front read:"



    centered "{size=25}{color=#ffffff}OAKHAVEN REMOTE LOGISTICS{/color}{/size}"



    "The company he had applied to."



    "The company that might finally give him a chance."



    thought nervous "That's where I'm going."



    # --------------------------------------------------------



    # BUS TERMINAL — 7:42 AM



    # --------------------------------------------------------



    scene bg terminal



    with dissolve



    call show_location_intro(



        "OakHaven Central Bus Terminal",



        "Monday — 7:42 AM"



    )



    show rowan nervous



    "The bus pulled into the terminal."



    driver "OakHaven Central! Last stop!"



    "Rowan stood, grabbed his backpack, and carefully made his way toward the doors."



    rowan happy "Thank you!"



    driver "Have a good one, kid."



    "Rowan stepped down onto the pavement."



    "The bus pulled away behind him."



    "And just like that..."



    "He was here."



    pause 0.8



    "A cool morning breeze brushed through his fur."



    "Rowan looked around the terminal."



    "People hurried past with coffee cups and bags."



    "Somewhere nearby, a bicycle bell rang."



    "A car horn sounded in the distance."



    "Everything was unfamiliar."



    thought nervous "Okay. I can do this."



    "He opened his phone and checked his notes."



    centered "{size=30}{color=#ffffff}ROWAN'S TO-DO LIST{/color}{/size}"



    centered "{color=#83df9b}✓ Arrive in OakHaven{/color}"



    centered "{color=#ffffff}□ Find somewhere affordable to stay{/color}"



    centered "{color=#ffffff}□ Attend job interview — 10:00 AM{/color}"



    centered "{color=#ffffff}□ Get hired{/color}"



    centered "{color=#ffffff}□ Start paying off medical debt{/color}"



    pause 1.5



    "He looked at the last item for a little too long."



    thought sad "One step at a time."



    # --------------------------------------------------------



    # MARKET STREET — 7:48 AM



    # --------------------------------------------------------



    scene bg market



    with dissolve



    call show_location_intro(



        "Market Street",



        "Monday — 7:48 AM"



    )



    show rowan neutral



    "A short walk brought Rowan to the entrance of Market Street."



    "The street was beginning to wake up."



    "Shopkeepers were opening their doors."



    "A delivery van rolled past."



    "The smell of fresh bread drifted through the air."



    "Rowan spotted several places nearby."



    "A small café with warm lights glowing through its windows."



    "A convenience store on the opposite corner."



    "A path leading toward a green park."



    "And, farther down the road..."



    "The OakHaven Remote Logistics campus."



    "He checked his phone again."



    # --------------------------------------------------------



    # INTERVIEW REMINDER



    # --------------------------------------------------------



    call screen phone_notification(



        "INTERVIEW REMINDER",



        "7:48 AM",



        "Reminder: Your interview is scheduled for Monday at 10:00 AM. Location: Main Reception, OakHaven Logistics Campus. Please arrive 15 minutes early."



    )



    show rowan nervous



    "Rowan swallowed."



    rowan nervous "Ten o'clock..."



    thought nervous "I've got time."



    thought nervous "I've got plenty of time."



    pause 0.5



    "He looked down at his wallet."



    "Thirty-five dollars."



    "That was everything he had available right now."



    thought nervous "Maybe I should find something to eat."



    thought sad "Or maybe I should save the money."



    "His stomach gave a quiet growl."



    rowan embarrassed "...Traitor."



    "He let out a nervous little laugh."



    "For the first time that morning, he felt himself relax just a little."



    "He took a deep breath."



    show rowan neutral



    rowan "Okay."



    rowan "Let's make today count."



    # --------------------------------------------------------



    # FIRST DESTINATION CHOICE



    # --------------------------------------------------------



    menu:



        "Where should Rowan go first?"



        "Visit Whiskers Café":



            $ first_destination = "Whiskers Café"



            jump act1_scene1_cafe



        "Visit OakHaven Remote Logistics":



            $ first_destination = "OakHaven Remote Logistics"



            jump act1_scene1_company



        "Take a walk through Pinewood Park":



            $ first_destination = "Pinewood Park"



            jump act1_scene1_park



        "Explore Market Street":



            $ first_destination = "Market Street"



            jump act1_scene1_explore



# ============================================================



# BRANCH 1 — WHISKERS CAFÉ



# ============================================================



label act1_scene1_cafe:



    scene bg cafe



    with fade



    call show_location_intro(



        "Whiskers Café",



        "Monday — 8:05 AM"



    )



    show rowan nervous



    "A little bell jingled as Rowan approached the café."



    "Warm light spilled through the front windows."



    "The smell of coffee and freshly baked bread drifted outside."



    centered "{size=34}{color=#ffffff}WHISKERS CAFÉ{/color}{/size}"



    "Rowan looked through the window."



    "There were a few customers inside."



    "It seemed quiet."



    thought nervous "I could probably afford something small..."



    "He adjusted his backpack."



    show rowan happy



    rowan "Alright. Breakfast."



    "He reached for the door handle."



    "The little bell jingled again as he stepped inside."



    "Warm air surrounded him."



    "For the first time since arriving in OakHaven, Rowan felt like he could sit down."



    "Just for a little while."



    jump act1_scene1_end



# ============================================================



# BRANCH 2 — OAKHAVEN REMOTE LOGISTICS



# ============================================================



label act1_scene1_company:



    scene bg company



    with fade



    call show_location_intro(



        "OakHaven Remote Logistics",



        "Monday — 8:05 AM"



    )



    show rowan surprised



    "Rowan followed the road toward the logistics campus."



    "The building was larger up close."



    "Modern glass windows reflected the morning sunlight."



    "Small delivery drones could be seen flying between different sections of the campus."



    centered "{size=29}{color=#ffffff}OAKHAVEN REMOTE LOGISTICS{/color}{/size}"



    "Rowan stopped outside the main entrance."



    rowan surprised "Whoa..."



    "A drone zipped overhead."



    "Its small motors made a quiet buzzing sound."



    thought happy "So this is where I'll be working..."



    "He checked the time."



    "Still far too early for his interview."



    "He decided to take a closer look around the outside of the building."



    jump act1_scene1_end



# ============================================================



# BRANCH 3 — PINEWOOD PARK



# ============================================================



label act1_scene1_park:



    scene bg park



    with fade



    call show_location_intro(



        "Pinewood Park",



        "Monday — 8:05 AM"



    )



    show rowan happy



    "Rowan followed a nearby path toward the park."



    "Tall pine trees surrounded the walking trail."



    "The morning sunlight filtered through their branches."



    "A few birds chirped from somewhere overhead."



    "There were benches along the path and a small pond farther ahead."



    "Rowan found an empty bench and sat down."



    "His tail curled around his side."



    thought happy "Maybe I needed this."



    "For a moment, he didn't think about the interview."



    "Or the debt."



    "Or how much everything depended on today."



    "He simply listened to the birds."



    jump act1_scene1_end



# ============================================================



# BRANCH 4 — MARKET STREET



# ============================================================



label act1_scene1_explore:



    scene bg market



    with fade



    call show_location_intro(



        "Market Street",



        "Monday — 8:05 AM"



    )



    show rowan neutral



    "Rowan decided to explore the street before committing to anywhere."



    "There were little shops on both sides of the road."



    "A convenience store."



    "A clothing shop."



    "A small grocery store."



    "A few apartments sat above the businesses."



    "He wondered how much rent cost around here."



    thought nervous "I really need somewhere to stay."



    "He looked at the shop windows as he walked."



    thought happy "Maybe OakHaven wouldn't be such a bad place to start over."



    jump act1_scene1_end



# ============================================================



# SCENE 1 END



# ============================================================



label act1_scene1_end:



    scene bg black



    with fade



    centered "{size=36}{color=#ffffff}SCENE 1 COMPLETE{/color}{/size}"



    centered "{size=23}A Very Long Road{/size}"



    pause 1.5



    "Rowan's first morning in OakHaven had begun."



    "There was still a job interview ahead."



    "A place to find."



    "And a very long road toward paying off his family's debt."



    "But he wasn't alone in the world."



    "Not completely."



    "And perhaps OakHaven had more waiting for him than he expected."



    pause 1.5



    return



# ============================================================



# ACT I — SCENE 2: FIRST IMPRESSIONS



# ============================================================



label act1_scene2:



    $ current_location = "Whiskers Café"



    scene bg cafe



    with fade



    call show_location_intro("Whiskers Café", "Monday — 8:12 AM")



    $ cafe_visited = True



    show rowan nervous:



        xalign 0.27



        yalign 1.0



        zoom 1.25
        yoffset -150


    # Elliot is already behind the counter when Rowan enters.

    show elliot neutral



    "The little bell above the café door jingled."



    "Warm air surrounded Rowan as he stepped inside."



    "The café smelled of freshly brewed coffee, warm bread, and something sweet."



    "A few customers sat at the tables."



    "Behind the counter stood a brown deer wearing a green cardigan and a pair of glasses."



    "He was arranging a few pastries when he noticed Rowan."



    show rowan surprised



    show elliot happy

    "The deer looked up and smiled."



    show elliot neutral
    show elliot happy
    elliot "Oh! Good morning!"



    show elliot neutral

    show elliot happy
    elliot "Welcome to Whiskers Café!"



    show rowan nervous



    show elliot happy
    rowan "G-Good morning..."



    show elliot neutral
    elliot "First time here?"



    show elliot happy
    rowan "Y-Yeah. I just arrived in OakHaven."



    "The deer leaned against the counter."



    show elliot happy

    elliot "Really? Welcome to town, then!"



    show elliot neutral
    elliot "I'm Elliot, by the way. I own the place."



    "He offered a friendly wave."



    $ elliot_met = True



    $ elliot_friendship += 1
    $ elliot_trust += 1
    $ elliot_like += 2



    show elliot happy
    rowan "I'm Rowan. Nice to meet you."



    show elliot neutral
    elliot "Nice to meet you too, Rowan!"



    "Elliot glanced at Rowan's backpack."



    show elliot neutral

    elliot "So, what brings you to OakHaven?"



    menu:



        "What should Rowan tell Elliot?"



        "I'm here for a job interview.":



            $ elliot_friendship += 1
            $ elliot_trust += 1
            $ elliot_like += 1



            show elliot happy
            rowan nervous "I'm here for a job interview."



            show elliot happy

            elliot "Oh! That's exciting!"



            show elliot neutral
            elliot "Where at?"



            rowan "OakHaven Remote Logistics."



            show elliot neutral
            elliot "Ah, the drone delivery company!"



            show elliot neutral
            elliot "They're always looking for people."



            show elliot happy
            elliot "Good luck! I hope it goes well."



            thought happy "He seems nice..."



        "I just moved here. I'm trying to start over.":



            $ elliot_friendship += 2
            $ elliot_trust += 2
            $ elliot_like += 1



            show elliot neutral
            rowan sad "I just moved here. I'm trying to start over."



            show elliot neutral
            elliot "Well, you've come to a pretty good place for that."



            show elliot neutral
            elliot "OakHaven can be a little quiet sometimes, but the people are generally friendly."



            show elliot happy
            elliot "I'm sure you'll find your place."



            show rowan embarrassed



            rowan "Th-Thanks..."



            show elliot happy
            elliot "Of course!"



        "It's a little complicated...":



            $ elliot_trust += 1
            show elliot neutral
            rowan nervous "It's... a little complicated."



            show elliot neutral

            elliot "Ah. Fair enough."



            show elliot neutral
            elliot "You don't have to explain anything."



            show elliot happy
            elliot "Sometimes a fresh cup of coffee is all someone needs."



            show rowan happy



            rowan "Heh... yeah."



    "Elliot glanced toward the display case."



    show elliot neutral
    elliot "Have you eaten breakfast yet?"



    "Rowan's stomach gave a small growl."



    show rowan embarrassed



    show elliot smug
    rowan "...Maybe."



    show elliot smug
    elliot "That sounds like a no."



    "Elliot chuckled."



    show elliot neutral
    elliot "Well, we've got a few things available."



    show elliot neutral
    elliot "Nothing too fancy, but everything's fresh."



    # --------------------------------------------------------



    # BREAKFAST MENU



    # --------------------------------------------------------



    $ breakfast_choice = ""



    $ breakfast_cost = 0



    menu:



        "What should Rowan order? (Wallet: $[wallet])"



        "Butter toast — $3":



            $ breakfast_choice = "Butter toast"



            $ breakfast_cost = 3



        "Fresh sandwich — $7":



            $ breakfast_choice = "Fresh sandwich"



            $ breakfast_cost = 7



        "Coffee — $4":



            $ breakfast_choice = "Coffee"



            $ breakfast_cost = 4



        "Apple pastry — $3":



            $ breakfast_choice = "Apple pastry"



            $ breakfast_cost = 3



        "Tea — $3":



            $ breakfast_choice = "Tea"



            $ breakfast_cost = 3



        "Nothing. Save the money.":



            $ breakfast_choice = "Nothing"



            $ breakfast_cost = 0



    if breakfast_cost > 0:



        if wallet >= breakfast_cost:



            $ wallet -= breakfast_cost



            $ breakfast_purchased = True



            $ breakfast_eaten = True



            show elliot happy
            rowan nervous "Could I... um... have the [breakfast_choice.lower()], please?"



            show elliot happy

            elliot "Absolutely!"



            "Elliot prepared Rowan's order."



            "A few moments later, he placed it on the counter."



            show elliot happy
            elliot "There you go!"



            rowan happy "Thank you!"



            "Rowan paid and carefully picked up his food."



            show elliot happy
            elliot "Enjoy!"



            "Rowan took a bite."



            "It was simple, but surprisingly good."



            thought happy "Oh... that's actually really nice."



        else:



            rowan embarrassed "Actually... I don't think I have enough."



            show elliot neutral
            elliot "Oh! Don't worry about it."



            "Elliot put the food away."



            show elliot neutral
            elliot "Maybe another time."



    else:



        rowan nervous "I think I'll save my money."



        show elliot neutral
        elliot "That's alright!"



        show elliot neutral
        elliot "Just don't forget to eat something later, okay?"



        rowan embarrassed "I'll try..."



    # --------------------------------------------------------



    # SITTING BY THE WINDOW



    # --------------------------------------------------------



    "Rowan found a small table beside the window."



    "He placed his backpack beside the chair and sat down."



    show rowan neutral



    "Outside, Market Street was slowly getting busier."



    "People walked past the café windows."



    "A delivery van stopped near the curb."



    "For a moment, Rowan almost forgot how nervous he had been."



    thought happy "Maybe this place isn't so bad."



    "He pulled out his phone."



    "His brother's earlier message was still open."



    "Rowan smiled faintly."



    thought happy "I should call him later."



    # --------------------------------------------------------



    # COMMUNITY NOTICEBOARD



    # --------------------------------------------------------



    "After finishing his breakfast, Rowan noticed a large noticeboard near the café entrance."



    "It was covered with colorful flyers and handwritten notes."



    "One flyer caught his attention."



    centered "{size=30}{color=#ffffff}OAKHAVEN COMMUNITY BOARD{/color}{/size}"



    centered "{size=23}{color=#a7c98a}COMMUNITY GATHERING{/color}{/size}"



    centered "{size=18}Pinewood Park — Saturday Morning{/size}"



    centered "{size=18}Everyone is welcome!{/size}"



    "Another notice advertised affordable rooms for rent."



    centered "{size=23}{color=#83b7df}ROOMS AVAILABLE{/color}{/size}"



    centered "{size=18}OakHaven Community Housing Office{/size}"



    centered "{size=18}Affordable accommodation for new residents{/size}"



    "Rowan leaned closer to read the details."



    $ housing_info_found = True



    $ cafe_quest_unlocked = True



    thought happy "Affordable rooms... I should remember that."



    menu:



        "What should Rowan do?"



        "Ask Elliot about affordable housing.":



            $ elliot_friendship += 2
            $ elliot_trust += 2
            $ elliot_like += 1



            show rowan nervous



            show elliot neutral
            rowan "Um... Elliot?"



            show elliot neutral
            elliot "Yeah?"



            show elliot neutral
            rowan "Do you know anything about the rooms on that notice?"



            show elliot neutral
            elliot "Oh! The Community Housing Office."



            show elliot neutral
            elliot "They help people who are new to OakHaven find affordable places to stay."



            show elliot happy
            elliot "You should definitely stop by sometime."



            rowan happy "Really? That would be helpful."



            show elliot happy
            elliot "Of course!"



            show elliot neutral
            elliot "There's also a little apartment building near Market Street."



            show elliot neutral
            elliot "Sometimes they have rooms available."



            thought happy "That's something, at least."



            "Rowan took a picture of the flyer."



        "Read more of the flyers.":



            "Rowan spent a few minutes looking through the other notices."



            "There were advertisements for community events, volunteer opportunities, and local services."



            "He found another small flyer advertising a weekend market."



            thought happy "There's quite a lot going on around here."



            "He took a picture of the housing notice."



        "Return to the table.":



            "Rowan decided he had enough information for now."



            "He returned to his table and picked up his backpack."



    # --------------------------------------------------------



    # ELLIOT CHECKS IN



    # --------------------------------------------------------



    "A little while later, Elliot walked over to Rowan's table."



    show elliot neutral
    elliot "Everything alright over here?"



    show rowan happy



    rowan "Y-Yeah. Everything's really nice."



    show elliot happy
    elliot "Glad to hear it!"



    "Elliot pulled out the chair opposite Rowan."



    show elliot neutral
    elliot "Mind if I sit for a minute?"



    rowan "Oh! N-No, go ahead."



    "Elliot sat down."



    show elliot neutral
    elliot "So, do you have somewhere to stay yet?"



    show rowan nervous



    show elliot neutral
    rowan "Not... exactly."



    show elliot neutral
    elliot "Ah."



    show elliot neutral
    elliot "Well, don't panic."



    show elliot neutral
    elliot "There are a few affordable places around town."



    show elliot neutral
    elliot "The housing office is probably your best starting point."



    show elliot happy
    rowan "I'll look into it."



    show elliot neutral
    elliot "Good!"



    "Elliot smiled."



    show elliot neutral
    elliot "OakHaven's a pretty welcoming place."



    show elliot happy
    elliot "It might take a little while, but you'll find your people."



    show rowan embarrassed



    rowan "I-I hope so."



    # --------------------------------------------------------



    # GETTING TO KNOW ROWAN



    # --------------------------------------------------------



    show elliot neutral
    elliot "So, Rowan..."



    show elliot neutral
    elliot "How are you feeling about everything?"



    menu:



        "What should Rowan say?"



        "I'm nervous about my interview.":



            $ elliot_friendship += 2
            $ elliot_trust += 1
            $ elliot_like += 2



            show rowan nervous



            show elliot neutral
            rowan "Honestly? I'm really nervous about the interview."



            rowan "I really need this job."



            show elliot neutral
            elliot "That's understandable."



            show elliot neutral
            elliot "First interviews are always a little scary."



            show elliot neutral
            elliot "Just take a breath and be yourself."



            show elliot happy
            elliot "You've got this."



            show rowan happy



            rowan "Thanks..."



            thought happy "That actually helps."



        "I'm not very good at meeting new people.":



            $ elliot_friendship += 2
            $ elliot_trust += 1
            $ elliot_like += 2



            show rowan embarrassed



            show elliot smug
            rowan "I'm... not really good at meeting new people."



            show elliot happy
            elliot "Really?"



            "Elliot smiled."



            show elliot smug
            elliot "Well, you're doing pretty well right now!"



            show rowan embarrassed



            rowan "A-Ah..."



            "Rowan's ears lowered."



            show elliot embarrassed

            elliot "Sorry! Didn't mean to embarrass you."



            "Elliot chuckled softly."



        "I'm actually enjoying talking with you.":



            $ elliot_trust += 1
            $ elliot_like += 2
            $ elliot_love += 2



            show rowan embarrassed
            show elliot surprised
            rowan "I-I'm actually... enjoying talking with you."



            show elliot embarrassed
            elliot "Oh! Well... I'm glad. I like talking with you too."



            show rowan embarrassed
            thought "Did I really just say that out loud?"



        "I'd rather not talk about it.":



            show rowan nervous



            $ elliot_trust += 2
            show elliot neutral
            rowan "I'd... rather not talk about it."



            show elliot happy

            show elliot neutral
            elliot "No problem."



            show elliot neutral
            elliot "Everyone deserves a little privacy."



            rowan "Thanks."



            show elliot happy
            elliot "Anytime."



    # --------------------------------------------------------

    # A LITTLE MORE TIME WITH ELLIOT

    # --------------------------------------------------------

    show elliot happy
    elliot "I'm glad you stopped by this morning, Rowan."

    show rowan neutral
    rowan "R-Really?"

    show elliot neutral
    elliot "Of course. It's nice meeting someone new."

    menu:

        "What should Rowan say?"

        "I'd like to get to know you better.":

            show rowan embarrassed
            rowan "I-I'd like to get to know you better, too."

            show elliot embarrassed
            elliot "Oh! I'd like that."

            "Elliot's smile turns a little shy."

            $ change_relationship("elliot", trust=1, like=2, love=5)
            $ elliot_memories.append("Rowan told Elliot he wanted to get to know him better.")

        "Tell me more about yourself.":

            show rowan happy
            rowan "Could you tell me a little more about yourself?"

            show elliot happy
            elliot "Sure! I've lived in OakHaven for a few years, and I opened this café because I love bringing people together."

            elliot "There's always something interesting happening around here."

            $ change_relationship("elliot", trust=3, like=3)

        "Thanks for being so welcoming.":

            show rowan happy
            rowan "Thanks for being so welcoming. It means a lot."

            show elliot happy
            elliot "You're very welcome, Rowan. I mean it."

            $ change_relationship("elliot", trust=1, like=1)


    # --------------------------------------------------------



    # INTERVIEW REMINDER — 8:47 AM



    # --------------------------------------------------------



    call screen phone_notification(



        "INTERVIEW REMINDER",



        "8:47 AM",



        "Reminder: Your interview at OakHaven Remote Logistics is approaching. Please arrive at Main Reception by 9:45 AM."



    )



    show rowan surprised



    "Rowan looked at his phone."



    rowan "Oh!"



    thought nervous "Right! The interview!"



    "He quickly checked the time."



    "He still had time, but he didn't want to be late."



    show rowan nervous



    rowan "I should probably get going."



    show elliot neutral
    elliot "Got an interview?"



    show elliot happy
    rowan "Y-Yeah. At OakHaven Remote Logistics."



    show elliot neutral
    elliot "Oh, right!"



    show elliot neutral
    elliot "Well, I won't keep you."



    "Elliot stood up."



    show elliot happy
    elliot "Good luck, Rowan."



    show elliot neutral
    elliot "And hey..."



    show elliot happy
    elliot "You're welcome here anytime."



    show rowan happy



    show elliot happy
    rowan "Really?"



    show elliot happy
    elliot "Of course!"



    show elliot happy
    elliot "First cup of tea is on the house next time."



    show rowan embarrassed



    rowan "Y-You don't have to do that..."



    show elliot neutral
    elliot "I know."



    show elliot happy
    elliot "I want to."



    "Rowan's cheeks turned a little pink."



    rowan "Th-Thank you, Elliot."



    show elliot happy
    elliot "Anytime!"



    $ elliot_friendship += 1
    $ elliot_trust += 1
    $ elliot_like += 1



    # --------------------------------------------------------



    # NEW ACQUAINTANCE



    # --------------------------------------------------------



    "Rowan adjusted his backpack."



    "He felt a little less like a stranger than he had when he first walked through the door."



    thought happy "Maybe I can make friends here."



    centered "{size=30}{color=#a7c98a}NEW ACQUAINTANCE{/color}{/size}"



    centered "{size=26}Elliot{/size}"



    centered "{size=18}Owner of Whiskers Café{/size}"



    pause 1.5



    centered "{size=30}{color=#83b7df}NEW SIDE QUEST{/color}{/size}"



    centered "{size=25}A Familiar Face at the Café{/size}"



    centered "{size=18}Visit Elliot again sometime.{/size}"



    pause 2.0



    # --------------------------------------------------------



    # LEAVING THE CAFÉ — 8:50 AM



    # --------------------------------------------------------



    scene bg market



    with dissolve



    call show_location_intro("Market Street", "Monday — 8:50 AM")



    show rowan happy:



        xalign 0.27



        yalign 1.0



        zoom 1.25
        yoffset -150



    "Rowan stepped outside."



    "The little bell jingled behind him."



    "He looked back through the window."



    "Elliot waved from behind the counter."



    rowan happy "Bye!"



    show elliot happy
    elliot "See you later!"



    "Rowan waved back."

    hide elliot
    show nyx neutral
    "Rowan had only taken a few steps when a black cat nearby glanced over."
    nyx "You're new around here, aren't you?"
    show rowan surprised
    rowan "H-Huh?"
    show nyx smug
    nyx "Backpack, nervous ears, and that very lost look. Kind of gives it away."
    show rowan embarrassed
    rowan "I... guess I'm not very subtle."
    show nyx happy
    nyx "Don't worry. OakHaven can be confusing on your first day. I'm Nyx."
    $ nyx_met = True
    $ nyx_trust += 1
    $ nyx_like += 1
    menu:
        "How should Rowan respond to Nyx?"
        "Apologize for being distracted.":
            show rowan embarrassed
            rowan "Sorry. I've got a lot on my mind today."
            show nyx happy
            nyx "Fair enough. First days can be a lot."
            $ nyx_trust += 2
            $ nyx_like += 1
        "Joke back about the lost look.":
            show rowan happy
            rowan "Well, at least I look consistently lost."
            show nyx smug
            nyx "That's one way to own it."
            $ nyx_like += 2
        "Introduce himself properly.":
            show rowan nervous
            rowan "I'm Rowan. Nice to meet you."
            show nyx neutral
            nyx "Nyx. And welcome to OakHaven, Rowan."
            $ nyx_trust += 1
            $ nyx_like += 1
    show nyx happy
    nyx "If you're looking for places around town, the community board inside the café is actually useful."
    rowan happy "Thanks. I'll remember that."
    "Nyx gave Rowan a small wave before heading down Market Street."
    hide nyx
    centered "{size=30}{color=#a99be8}NEW ACQUAINTANCE{/color}{/size}"
    centered "{size=26}Nyx{/size}"
    centered "{size=18}A local black cat{/size}"
    pause 1.5



    # --------------------------------------------------------
    # MEETING MILO — MARKET STREET
    # --------------------------------------------------------

    "A cheerful voice called from the corner of the street."
    "A golden retriever in a teal community-medic vest was helping a cyclist with a scraped elbow."
    show milo neutral
    milo "There we go. Nothing serious — just needs a clean bandage."
    "The retriever packed away a small first-aid kit, then noticed Rowan watching."
    show milo happy
    milo "Oh, hey! Sorry, didn't mean to stare. You doing alright? You look a little overwhelmed."
    show rowan embarrassed
    rowan "M-Me? I'm okay! Just... a lot happening today."
    show milo neutral
    milo "First day in town? I know that look. I'm Milo. I help out as a community medic around OakHaven."
    $ milo_met = True
    $ milo_trust += 1
    $ milo_like += 1

    menu:
        "How should Rowan respond to Milo?"

        "Offer to help put the first-aid supplies away.":
            show rowan happy
            rowan "I-I can help with those, if you want."
            show milo happy
            milo "That's really thoughtful of you. Thanks!"
            "Rowan helped Milo pack the kit neatly."
            $ milo_trust += 2
            $ milo_like += 1

        "Ask whether the cyclist is feeling better.":
            show rowan nervous
            rowan "Is... is the cyclist going to be alright?"
            show milo happy
            milo "Absolutely. Just a little scrape. Thanks for checking."
            $ milo_trust += 1
            $ milo_like += 2

        "Make a shy joke about looking overwhelmed.":
            show rowan embarrassed
            rowan "I guess my face is giving away the whole 'new and confused' thing."
            show milo happy
            milo "Heh! Don't worry. OakHaven has that effect on everyone at first."
            $ milo_like += 2

    show milo happy
    milo "If you ever need a hand, or just need directions, come find me. Take care, alright?"
    show rowan happy
    rowan "Th-Thanks, Milo. It's nice to meet you."
    "Milo gave Rowan an encouraging thumbs-up before returning to his kit."
    hide milo
    centered "{size=30}{color=#e6b86f}NEW ACQUAINTANCE{/color}{/size}"
    centered "{size=26}Milo{/size}"
    centered "{size=18}Community medic — golden retriever{/size}"
    pause 1.5



    "Then he turned toward the road leading to OakHaven Remote Logistics."







    "His interview was getting closer."



    "He still needed somewhere to live."



    "He still had a very long way to go."



    "But at least he had met someone."



    thought happy "One step at a time."



    # --------------------------------------------------------



    # UPDATED CHECKLIST



    # --------------------------------------------------------



    centered "{size=30}{color=#ffffff}ROWAN'S TO-DO LIST{/color}{/size}"



    centered "{color=#83df9b}✓ Arrive in OakHaven{/color}"



    centered "{color=#83df9b}✓ Visit Whiskers Café{/color}"



    centered "{color=#83df9b}✓ Meet Elliot{/color}"
    centered "{color=#83df9b}✓ Meet Nyx{/color}"
    centered "{color=#83df9b}✓ Meet Milo{/color}"



    centered "{color=#ffffff}□ Find somewhere affordable to stay{/color}"



    centered "{color=#ffffff}□ Attend job interview — 10:00 AM{/color}"



    centered "{color=#ffffff}□ Get hired{/color}"



    centered "{color=#ffffff}□ Start paying off medical debt{/color}"



    pause 2.0



    # --------------------------------------------------------



    # SCENE 2 COMPLETE



    jump act1_scene2_end



label act1_scene2_end:



    scene bg black



    with fade



    centered "{size=36}{color=#ffffff}SCENE 2 COMPLETE{/color}{/size}"



    centered "{size=23}First Impressions{/size}"



    pause 1.5



    "A warm cup of tea."



    "A friendly conversation."



    "And a new face in a town full of strangers."



    "Perhaps OakHaven was already beginning to feel a little more like home."



    pause 2.0



    return



# ============================================================
# ROMANCE HUB
# ============================================================

label romance_hub:

    "Rowan takes a moment to think about the people he's met."

    menu:

        "Who would Rowan like to spend time with?"

        "Elliot" if elliot_met:
            $ romance_target = "elliot"
            call romance_activity_menu
            jump romance_hub

        "Nyx" if nyx_met:
            $ romance_target = "nyx"
            call romance_activity_menu
            jump romance_hub

        "Milo" if milo_met:
            $ romance_target = "milo"
            call romance_activity_menu
            jump romance_hub

        "Never mind.":

            return


label romance_activity_menu:

    if romance_target == "elliot":
        $ romance_name = "Elliot"
    elif romance_target == "nyx":
        $ romance_name = "Nyx"
    else:
        $ romance_name = "Milo"

    "Rowan thinks about spending some time with [romance_name]."

    menu:

        "What would Rowan like to do?"

        "Give them a gift.":
            call romance_gift
            jump romance_activity_menu

        "Invite them on a date." if can_go_on_date(romance_target):
            call romance_date
            jump romance_activity_menu

        "Confess his feelings." if can_confess(romance_target):
            call romance_confess
            jump romance_activity_menu

        "Return to the character list.":
            return


# ============================================================
# GIFT SYSTEM
# ============================================================

label romance_gift:

    if romance_target == "elliot":
        if elliot_gift_received:
            "Rowan has already given Elliot his special gift."
            return

    elif romance_target == "nyx":
        if nyx_gift_received:
            "Rowan has already given Nyx their special gift."
            return

    elif romance_target == "milo":
        if milo_gift_received:
            "Rowan has already given Milo his special gift."
            return

    menu:

        "Choose a gift. (Wallet: $[wallet])"

        "A little box of chocolates — $8":
            $ gift_choice = "chocolates"
            $ gift_cost = 8

        "A small handmade charm — $12":
            $ gift_choice = "charm"
            $ gift_cost = 12

        "A packet of specialty tea — $5":
            $ gift_choice = "tea"
            $ gift_cost = 5

        "Never mind.":
            return

    if wallet < gift_cost:

        rowan sad "I don't have enough money for that..."

        "Rowan decides to save his money."

        return

    $ wallet -= gift_cost

    # Elliot's gift preferences.

    if romance_target == "elliot":

        $ elliot_gift_received = True
        $ elliot_memories.append("Rowan gave Elliot a thoughtful gift.")

        if gift_choice == "tea":

            show elliot surprised
            elliot "Oh! You remembered that I like tea?"

            show elliot happy
            elliot "That's incredibly sweet of you."

            $ change_relationship("elliot", trust=2, like=4, love=6)

        elif gift_choice == "charm":

            show elliot happy
            elliot "This is lovely! Thank you, Rowan."

            $ change_relationship("elliot", like=3, love=3)

        else:

            show elliot happy
            elliot "Chocolate! You really didn't have to."

            $ change_relationship("elliot", like=3, love=2)

    # Nyx's gift preferences.

    elif romance_target == "nyx":

        $ nyx_gift_received = True
        $ nyx_memories.append("Rowan gave Nyx a thoughtful gift.")

        if gift_choice == "charm":

            show nyx surprised
            nyx "Wait... you got this for me?"

            show nyx embarrassed
            nyx "Huh. I guess you have decent taste."

            $ change_relationship("nyx", trust=2, like=4, love=6)

        elif gift_choice == "chocolates":

            show nyx happy
            nyx "Chocolate? Okay, you know how to make an impression."

            $ change_relationship("nyx", like=3, love=3)

        else:

            show nyx smug
            nyx "Tea? Not exactly what I expected."

            $ change_relationship("nyx", like=2, love=1)

    # Milo's gift preferences.

    elif romance_target == "milo":

        $ milo_gift_received = True
        $ milo_memories.append("Rowan gave Milo a thoughtful gift.")

        if gift_choice == "chocolates":

            show milo surprised
            milo "For me? Aw, that's really kind!"

            show milo happy
            milo "You're going to make me blush!"

            $ change_relationship("milo", trust=2, like=4, love=6)

        elif gift_choice == "charm":

            show milo happy
            milo "I'll keep this somewhere safe. Thanks, Rowan!"

            $ change_relationship("milo", like=3, love=3)

        else:

            show milo happy
            milo "Oh, nice! I'll enjoy this after my shift."

            $ change_relationship("milo", like=3, love=2)

    "Rowan smiles."

    "It feels nice to do something thoughtful for someone."

    return


# ============================================================
# FIRST DATE SYSTEM
# ============================================================

label romance_date:

    if romance_target == "elliot":

        $ elliot_date_completed = True
        $ elliot_memories.append("Rowan and Elliot shared their first date.")

        scene bg cafe
        with fade

        show elliot happy
        elliot "I was hoping you'd ask me to spend some time together."

        show rowan embarrassed
        rowan "Y-You were?"

        show elliot embarrassed
        elliot "Well... yes."

        "Elliot prepares a quiet table by the window."

        "The two spend the afternoon talking about their interests, their hopes, and the little things that make them happy."

        show elliot happy
        elliot "I'm really glad we did this."

        show rowan happy
        rowan "Me too."

        $ change_relationship("elliot", trust=4, like=5, love=8)

    elif romance_target == "nyx":

        $ nyx_date_completed = True
        $ nyx_memories.append("Rowan and Nyx shared their first date.")

        scene bg park
        with fade

        show nyx smug
        nyx "Don't look so surprised. I can be nice sometimes."

        show rowan embarrassed
        rowan "I-I wasn't expecting you to ask me to the park."

        show nyx happy
        nyx "Well, I thought we could do something without competing for once."

        "The two walk along the Pinewood Park trail."

        "Nyx occasionally makes playful comments, but their usual competitive attitude slowly fades."

        show nyx embarrassed
        nyx "This was actually pretty nice."

        show rowan happy
        rowan "Yeah. It really was."

        $ change_relationship("nyx", trust=4, like=5, love=8)

    elif romance_target == "milo":

        $ milo_date_completed = True
        $ milo_memories.append("Rowan and Milo shared their first date.")

        scene bg park
        with fade

        show milo happy
        milo "I brought snacks! I figured we'd need something for our walk."

        show rowan happy
        rowan "You thought of everything."

        show milo embarrassed
        milo "Heh. I wanted this to be special."

        "Milo and Rowan spend the afternoon walking through the park."

        "They talk about their lives, laugh about silly things, and enjoy the peaceful afternoon."

        show milo happy
        milo "I'd really like to do this again."

        show rowan embarrassed
        rowan "I-I'd like that too."

        $ change_relationship("milo", trust=4, like=5, love=8)

    centered "{size=34}{color=#f2a6c6}SPECIAL MEMORY{/color}{/size}"

    centered "{size=24}A day spent together{/size}"

    pause 2.0

    return


# ============================================================
# CONFESSION SYSTEM
# ============================================================

label romance_confess:

    "Rowan takes a deep breath."

    "There is something he's wanted to say for a while."

    menu:

        "What should Rowan do?"

        "Tell them how he feels.":

            if romance_target == "elliot":

                $ elliot_confessed = True
                $ elliot_romance_active = True
                $ elliot_memories.append("Rowan confessed his feelings to Elliot.")

                show elliot surprised
                elliot "Rowan... are you serious?"

                show rowan embarrassed
                rowan "Y-Yeah. I really like you, Elliot."

                show elliot embarrassed
                elliot "I... I like you too."

                show elliot happy
                elliot "I'd really like to see where this goes."

                $ change_relationship("elliot", trust=3, like=5, love=5)

            elif romance_target == "nyx":

                $ nyx_confessed = True
                $ nyx_romance_active = True
                $ nyx_memories.append("Rowan confessed his feelings to Nyx.")

                show nyx surprised
                nyx "Wait. You're actually confessing to me?"

                show rowan embarrassed
                rowan "Y-Yes. I like you."

                show nyx embarrassed
                nyx "Well... that's inconvenient."

                show rowan nervous
                rowan "I-I'm sorry?"

                show nyx happy
                nyx "Because I like you too, dummy."

                $ change_relationship("nyx", trust=3, like=5, love=5)

            elif romance_target == "milo":

                $ milo_confessed = True
                $ milo_romance_active = True
                $ milo_memories.append("Rowan confessed his feelings to Milo.")

                show milo surprised
                milo "Oh, Rowan..."

                show rowan embarrassed
                rowan "I really like you, Milo."

                show milo embarrassed
                milo "You have no idea how happy that makes me."

                show milo happy
                milo "I like you too."

                $ change_relationship("milo", trust=3, like=5, love=5)

            centered "{size=34}{color=#f2a6c6}ROMANCE ROUTE UNLOCKED{/color}{/size}"

            pause 2.0

        "Not yet.":

            "Rowan decides to wait for a better moment."

    return
