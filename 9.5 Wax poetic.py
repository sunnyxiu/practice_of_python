# -*- coding: utf-8 -*-
import random

nouns = [
    "fossil",
    "horse",
    "aardvark",
    "judge",
    "chef",
    "mango",
    "extrovert",
    "gorrila"
    ]
verbs = [
    "kicks", 
    "jingles", 
    "bounces", 
    "slurps", 
    "meows", 
    "explodes", 
    "curdles"
    ]
adjectives = [
    "furry", 
    "balding", 
    "incredulous", 
    "fragrant", 
    "exuberant", 
    "glistening"
    ]
prepositions = [
    "against", 
    "after", 
    "into", 
    "into", 
    "beneath", 
    "upon", 
    "for", 
    "in", 
    "like", 
    "like", 
    "over", 
    "within"
    ]
adverbs = [
    "curiously", 
    "extravagantly", 
    "tantalizingly", 
    "furiously", 
    "sensuously"
    ]


def make_poem(nouns, verbs, adjectives, prepositions, adverbs):
    """Create poem randomly from given word lists and returned as a multi-line string"""
    # Choose 3 nouns randomly
    noun1 = random.choice(nouns)
    noun2 = random.choice(nouns)
    noun3 = random.choice(nouns)
    # Make sure all chosen nouns are different
    while noun2 == noun1:
        noun2 = random.choice(nouns)
    while noun3 == noun1 or noun3 == noun2:
        noun3 == random.choice(nouns)
    
    # Choose 3 verbs randomly 
    verb1 = random.choice(verbs)
    verb2 = random.choice(verbs)
    verb3 = random.choice(verbs)
    # Make sure all chosen verbs are different
    while verb2 == verb1:
        verb2 = random.choice(verbs)
    while verb3 == verb1 or verb3 == verb2:
        verb3 = random.choice(verbs)
    
    # Choose 3 adjectives randomly
    adj1 = random.choice(adjectives)
    adj2 = random.choice(adjectives)
    adj3 = random.choice(adjectives)
    while adj2 == adj1:
        adj2 = random.choice(adjectives)
    while adj3 == adj1 or adj3 == adj2:
        adj3 = random.choice(adjectives)
    
    # Choose 2 different preps randomly
    prep1 = random.choice(prepositions)
    prep2 = random.choice(prepositions)
    while prep2 == prep1:
        prep2 = random.choice(prepositions)
    
    # Choose 1 adverb
    adverb1 = random.choice(adverbs)
    if "aeiou".find(adj1[0]) != -1:
        article = "An" 
    else:
        article = "A"

    poem = (
        f"{article} {adj1} {noun1}\n\n"
        f"{article} {adj1} {noun1} {verb1} {prep1} the {adj2} {noun2}\n"
        f"{adverb1}, the {noun1} {verb2}\n"
        f"the {noun2} {verb3} {prep2} a {adj3} {noun3}"
    )

    return poem
   

poem = make_poem(nouns, verbs, adjectives, prepositions, adverbs)     
print(poem)        
        
        
        
        
        
        

