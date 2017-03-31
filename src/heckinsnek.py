# module heckinsnek.py
# human M.S.T.O.P
# when April 2017

# hello
# this is heckinsnek
# am Python snek simulator 
# doing a print
# maybe like boop, maybe not like boop
# ask first, k?
# don't heck with me
# vur snek_case

import random

# Words

_hello_words = ["this is snek", "don't heck with me",
                "no step on snek", "am noodle",
                "doing a relax", "doing a clean",
                "am snek"] 

_heck_words = ["heck this", "hiss",
               "heck off", "gosh hecking darn it",
               "i am hide", "i am darkness",
               "doing a leave"]
    
_try_boop_ok_words = ["boop incoming", "i do a prepare",
                      "snoot is primed for boop", "pls do a proceeding",
                      "not dangur snek", "will u boop?",
                      "heckin boop me"]

_try_boop_nope_words = ["pls no boop", "hiss",
                        "i heckin dare u", "i am darkness",
                        "no human"]

_doing_a_boop_ok_words = ["bwep", "doing a snek train"]

_doing_a_boop_nope_words = ["why u touch?", "pls no boop",
                            "i was not prepare", "oh heck",
                            "do me a frighten"]

_step_words = ["no step", "pls no step",
               "no step on snek"]


# Maybe like boop, maybe not like boop

_is_boopable = random.choice([False, True])


# Doings

def hi():
    print(random.choice(_hello_words))

def heck_the_snek():
    print(random.choice(_heck_words))

def step_on_snek():
    print(random.choice(_step_words))

def can_boop():
        
    if (_is_boopable):
        print(random.choice(_try_boop_ok_words))
        return True

    else:
        print(random.choice(_try_boop_nope_words))
        return False

#end func can_boop

def doing_a_boop():

    if (_is_boopable):
        print(random.choice(_doing_a_boop_ok_words))

    else:
        print(random.choice(_doing_a_boop_nope_words))

#end func doing_a_boop