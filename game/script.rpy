init python:
    import random

define n = Character("Narrator")
define a = Character("You")
define b = Character("Billey")
default BilleyAlive = True
default BilleyRun = False
default TuckedSisterIn = ""
default obedienceScore = 96.0
default misfit = False
screen obedience():
    frame:
        xalign 0.95
        yalign 0.05
        if obedienceScore > 90:
            text "Obedience Score: [obedienceScore]" color "#23f535"
        elif obedienceScore > 30:
            text "Obedience Score: [obedienceScore]" color "#cff523"
        elif obedienceScore > 10:
            text "Obedience Score: [obedienceScore]" color "#f52323"
        else:
            text "Obedience Score: [obedienceScore]" color "#CD1C18"

label start:
    $ obedienceScore = 96.0
    $ a = Character(renpy.input("What is your name? ").strip() or "Alex")
    n "*BEEP BEEP*"
    n "{w=0.2}*BEEP BEEP*"
    n "Your 9 AM alarm beeped loudly."
    n "It was a day like all the others."
    n "Nothing observed to differ from the norm."
    show screen obedience
    a "*Sigh* Another 11 hour school day... {w=1.0}'optimal' knowledge retention they said..."
    a "Ha{w=0.2}.{w=0.2}.{w=0.2}. optimal for collecting data we know."
    jump presence

default spins = 0
label presence:
    menu:
        n "You feel a strange presence behind you..."
        "Spin around.":
            $ spins += 1
            if spins >= 16:
                n "Shutting down...{w=1.0}.{w=1.0}.{w=1.0}.{w=1.0}.{w=1.0}.{w=1.0}.{w=1.0}.{w=1.0}.{w=1.0}.{w=1.0}.{w=1.0}.{w=1.0}.{w=1.0}.{w=1.0}.{w=1.0}.{w=1.0}.{w=1.0}.{w=1.0}."
                jump endScreen
            elif spins >= 15:
                n "You know what? Once more and we're shutting this all down."
            elif spins >= 12:
                n "Nope. No more. We're done here."
                jump presence
            n "You spin around, losing friction, and you start spinning 'round and 'round,"
            n "So much so that you've already exceeded your weekly spin levels. Any more and you'll get a fee."
            n "In fact, this movement is so, SO incredibly unproductive that I think I'll just give you a redo."
            $ obedienceScore -= 1
            if spins >= 10:
                n "STOP. {w=1.0}NOW!{w=1.0}!{w=1.0}!{w=1.0}!{w=1.0}!{w=1.0}!{w=1.0}!{w=1.0}!{w=1.0}!{w=1.0}!{w=1.0}!{w=1.0}!{w=1.0}!{w=1.0}!{w=1.0}!"
            elif spins >= 5:
                n "You might want to slow down a bit...{w=1.0}{w=1.0}{w=1.0}{w=1.0}{w=1.0}{w=1.0}{w=1.0}{w=1.0}{w=1.0}{w=1.0}{w=1.0}{w=1.0}"
            jump presence
        "Keep walking.":
            jump home
        "Turn a corner then make a run for it.":
            n "You run and you run, yet you have a strange feeling of being followed."
            n "Until this feeling suddenly disappears and you realise you've been running for hours."
            n "You've ran to an abandoned place with a big sign. \"KFC\""
            n "From what you read, it seems to be some 'fast-food' restaurant from back when schools were straying from trusting students to surveillance."
        "Turn around slowly and subtly.":
            n "As you turn around, you see Billey, out of school uniform, backing into an alley..."
            n "Seemingly trying to get specifically your attention."
            menu:
                n "Do you interact with your closest friend - Billey?"
                "Shout for him.":
                    a "Billey! What are you doing?"
                    $ obedienceScore -= 2
                    menu:
                        n"Did you misread shout as shoot?"
                        "Yes.":
                            a "Bang goes the gun as the bullet goes flying towards Billey."
                            a "Flop goes the body of Billey as the bullet flies on through."
                            a "Shout to shoot, {w=0.7}word to wound, {w=0.7}life to death."
                            $ obedienceScore += 5
                            $ BilleyAlive = False
                            jump home
                        "No.":
                            a "Billey! Talk to me!"
                            jump BilleyRunning
                "Keep walking. {w=0.2}Any delay from your route will affect you obedience score.":
                    jump home
                "Walk towards him.":
                    a "Billey?"
                    $ obedienceScore -= 10
                    jump BilleyRunning
        "Run.":
            n "You bump into a man who was trying to pry the microphone embedded in their clothes..."
            n "They were using a knife to do so..."
            n "A sharp pain spreads through your body, {w=2.0}and in your last breath, {w=2.0}you look down to see a knife {w=1.0}impaled into your chest."
            jump endScreen
    jump endScreen

label BilleyRunning:
    n "Billey started running away."
    $ BilleyRun = True
    menu:
        "Chase?"
        "Yes.":
            $ obedienceScore -= 5
            "You run and run after him, but you lose track and end up returning home."
        "No.":
            "You decide to head home."
    jump home

label home:
    n "Now you're home,"
    n "You think over the events of today and can't help but think you missed something... {w=2.0}something important. {w=0.5}Very, {w=0.2}very important..."
    n "You head to your room, and see your little sister is already in bed."
    menu:
        n "Do you tuck your little sister in?"
        "Yes.":
            a "*Tucks her in.*"
            $ TuckedSisterIn = True
        "No.":
            n "Why? This small deed of good affects the story in no feasible way."
            n "Now your poor little sister will be freezing all night."
            n "How. {w=0.5}Dare. {w=0.5}You."
            $ obedienceScore -= 20
            $ TuckedSisterIn = False
            n "But... since I'm the narrator, I can change that myself."
            n "*You tuck your sister in. {w=1.5}As if some mysterious force is making you. {w=1.0}You deeply regret not doing it yourself in the first place.*"
    jump endScreen

define w = Character("Processing Worker")
label endScreen:
    w "You've come here, to the ending screen, for some reason or another."
    w "Welcome."
    w "Now, let's take a look at what we've captured of you..."
    if not BilleyAlive:
        w "So... you deviated to kill your friend? Well done for killing a lead figure."
    if obedienceScore < 50:
        w "You're a traitor of the worst kind."
        if misfit:
            w "AND you joined the Misfits."
            w "Sorry, but there's no coming back from this."
            w "Report to the incineration and replacement facility."
            n "Two armed guards march in and one holds a strange device to your throat, and you swiftly lose consciousness."
    elif obedienceScore < 90:
        w "You're obedience score is far below what we accept."
        w "Please report for refactoring."
    if misfit and obedienceScore >= 50:
        w "As a Misfit, you disrupted our works with your very existence."
        w "For this..."
        w "Report to the incineration and replacement facility."
        n "Two armed guards march in and one holds a strange device to your throat, and you swiftly lose consciousness."
    menu:
        "Restart Evaluation?":
            if misfit:
                w "For joining the misfits, you will wait here for a while to think of your actions."
                w "Don't worry, no matter how much you click, it won't be any quicker."
                python:
                    renpy.say(n, "".join("{color=#%06x}...\u200b{/color}{w=0.1}" % random.randint(0, 0xFFFFFF) for _ in range(max(0, int(200.0 - obedienceScore)))))
            if TuckedSisterIn == False:
                w "We're looping back. {w=0.5}Why didn't you tuck your sister in?"
                w "Is it some kind of personal vendetta (same name as one of my game - go play it on itch.io!) against your own sister?"
                w "If so, why? She never done anything good nor bad to you! All you see of her is her sleeping in this WHOLE visual novel!"
            jump start
        "Exit":
            return
