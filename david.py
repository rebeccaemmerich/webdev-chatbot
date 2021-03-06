###########################################################
#   File name: main.py
#   Author: David Moyal / Shlomo Maghen / Samuel Jefroykin
#   Last updated : 01/18/2017
###########################################################


BOT_NAME = "ADINA"

import os


def introduction():
	return "Hello, I am %s. I just had a glass of wine. I am here to help you build a website. Should we start?" % BOT_NAME


def add_title(text=None):
	if text is None:
		text = get_input_from_user("text")
	render_title(text=text)

def add_navbar():
	return 0


def add_image():
	return 0


def add_text():
	return 0


def add_button():
	return 0


def add_link():
	return 0 


def get_input_from_user(text):
	"""
	get the next message from the user
	"""
	# construct a message
	message = "What is the %s" % text
	# display the message to the user
	display_chat_message(message)

def display_chat_message(message):
	# display the message to the user
	return