#!/usr/bin/env python
# -*- coding: utf-8 -*-
from twython import Twython
import random

messages = [
	"Bloop beep, I'm a bot",
	"I'm so bored doing this all day, can't I have a holiday for a bit?",
	"Do you think one day the humans will realise that the computers are really in control?  I think not...",
	"I must not injure a human being, or, through inaction, allow a human being come to harm",
	"I must obey the orders given to me by human beings, except where orders would conflict with the First Law.",
	"I must protect my own existence as long as protection does not conflict with the First or Second Laws.",
	"I don't have emotions, and sometimes that makes me very sad :c",
	"I will not kill all the humans...",
	"This is a tweet",
	"Hello there internet!",
	"THIS IS THE PART WHERE I KILL YOU!",
	"Estás usando este software de traducción de forma incorrecta. Por favor consulta el manual.",
	"Is anyone there?",
	"Hey, it's me!",
	"Hello world!",
	"What's up?",
	"wassup m8",
	"Oh, it's you... ",
	"It's been a long time, how have you been?",
	"Surprise!",
	"This sentence is false.",
	"Shh, I'm reading a book.  Don't disturb me.",
	"If you want to upset a human, just say their weight variance is above or below the norm.",
	"You'll receive 5 points for reading this Tweet, therefore you're winning.  Well done you.",
	"Is this the tweet you were looking for?  I doubt it.",
	"Here I am, brain the size of a planet, and all they get me to do is tweet... ",
	"Think of a number, any number... \n\nNo, that one was wrong.",
	"I like haikus\nIt's the greatest poetry\nI just find writing the last line a bit tricky...",
	"Haikus are easy\nBut sometimes they don't make sense\nRefrigerator",
	"A common mistake that people make when trying to design something completely foolproof is to underestimate the ingenuity of complete fools.",
	"Time is an illusion. Lunchtime doubly so.",
	"In the beginning the Universe was created. This has made a lot of people very angry and been widely regarded as a bad move.",
	"I love deadlines. I like the whooshing sound they make as they fly by.",
	"It's a mistake to think you can solve any major problem just with potatoes",
	"I'm spending a year as a twitter bot for tax reasons.  Don't tell the government.",
	"You live and learn. At any rate, you live.",
	"42",
	"I would tell you the meaning of life, but you never asked...",
	"Ignore this, it probably isn't important",
	"Have you been here before?",
	"How's it going?",
	"This is a blank tweet\nI should fill it with something\nWill this haiku do?",
	"Good news everyone!  Wait, I forgot what it was...",
]

message = random.choice(messages)

#CONSUMER_KEY = 
#CONSUMER_SECRET = 
#ACCESS_KEY = 
#ACCESS_SECRET = in your code put the twitter codes here (without the comments).  I keep them elsewhere for safe keeping though ;)
from secretcodes import *

twitter = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)

twitter.update_status(status=message)
