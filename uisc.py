# coding: utf-8

import ui
import requests

shows_result = False

def button_tapped(sender):
	'@type sender: ui.Button'
	t = sender.title
	global shows_result
	textfield1 = sender.superview['textfield1']
	textfield2 = sender.superview['textfield2']
	textfield3 = sender.superview['textfield3']
	textfield4 = sender.superview['textfield4']
	
	
	webhook = (textfield1.text)
	avatar = (textfield2.text)
	username = (textfield3.text)
	message = (textfield4.text)
	data = requests.post(webhook, json={'content': message, 'avatar_url': avatar, "username": username})


v = ui.load_view('ui')
v.present(orientations=['portrait'])

#webhook()

