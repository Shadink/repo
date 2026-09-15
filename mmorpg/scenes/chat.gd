extends Label

@export var RANDOM_CHAT_FREQ = 2.0

#version MUY primitiva de esto
var random_article = []
var random_usr1 = []
var random_usr2 = []

var random_lines1 = []
var random_lines2 = []

var gen = RandomNumberGenerator.new()

# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	var file1 = FileAccess.open("res://data/chat/usernames1.txt", FileAccess.READ)
	if file1:
		while not file1.eof_reached():
			random_usr1.push_back(file1.get_line())
		file1.close()
		
	var file2 = FileAccess.open("res://data/chat/usernames2.txt", FileAccess.READ)
	if file2:
		while not file2.eof_reached():
			random_usr2.push_back(file2.get_line())
		file2.close()
		
	var file3 = FileAccess.open("res://data/chat/usernames0.txt", FileAccess.READ)
	if file3:
		while not file3.eof_reached():
			random_article.push_back(file3.get_line())
		file3.close()

	var file4 = FileAccess.open("res://data/chat/msg.txt", FileAccess.READ)
	if file4:
		while not file4.eof_reached():
			random_lines1.push_back(file4.get_line())
			random_lines2.push_back(file4.get_line())
		file4.close()
	self.text = ""
	$random_chat.wait_time = gen.randf_range(0.0, RANDOM_CHAT_FREQ)
	$random_chat.start()

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	pass


func _on_random_chat_timeout() -> void:
	var lines = self.text.split("\n") 
	if lines.size() > 6:
		lines.remove_at(0)
	text = "\n".join(lines)
	
	#random username generator
	var usrname = ""
	var piece = ""
	if(gen.randi_range(0,5) == 0):
		piece = random_article[gen.randi_range(0, random_article.size() - 1)]
		if(gen.randi_range(0,1) == 0):
			piece = piece.to_lower()
		usrname += piece
		if(gen.randi_range(0,1) == 0):
			usrname += "_"
	piece = random_usr1[gen.randi_range(0, random_usr1.size() - 1)]
	if(gen.randi_range(0,1) == 0):
		piece = piece.to_lower()
	usrname += piece
	if(gen.randi_range(0,1) == 0):
		usrname += "_"
	if(gen.randi_range(0,5) == 0):
		piece = random_article[gen.randi_range(0, random_article.size() - 1)]
		if(gen.randi_range(0,1) == 0):
			piece = piece.to_lower()
		usrname += piece
		if(gen.randi_range(0,1) == 0):
			usrname += "_"
	piece = random_usr2[gen.randi_range(0, random_usr2.size() - 1)]
	if(gen.randi_range(0,1) == 0):
		piece = piece.to_lower()
	usrname += piece
	if(gen.randi_range(0,3) == 0):
		if(gen.randi_range(0,1) == 0):
			usrname += "_"
		usrname += str(gen.randi_range(0, 9000))
	if(gen.randi_range(0,50) == 0):
		usrname += "_"
	if(gen.randi_range(0,30) == 0):
		usrname = usrname.to_upper()
	
	self.text += "\n" 
	self.text += usrname + ": "
	
	var message
	message = random_lines1[gen.randi_range(0, random_lines1.size() - 1)]
	if(gen.randi_range(0,50) == 0):
		message += "."
		var i = 0
		while(i < 10):
			if(gen.randi_range(0,30) == 0):
				message += "."
			i+=1
	elif(gen.randi_range(0,50) == 0):
		message += "?"
		var i = 0
		while(i < 10):
			if(gen.randi_range(0,30) == 0):
				message += "?"
			i+=1
	elif(gen.randi_range(0,50) == 0):
		message += "!"
		var i = 0
		while(i < 10):
			if(gen.randi_range(0,30) == 0):
				message += "!"
			i+=1

	if(gen.randi_range(0,10) == 0):
		message += " " + random_lines2[gen.randi_range(0, random_lines2.size() - 1)].to_lower()
	
	if(gen.randi_range(0,50) == 0):
		message += "."
		var i = 0
		while(i < 10):
			if(gen.randi_range(0,30) == 0):
				message += "."
			i+=1
	elif(gen.randi_range(0,50) == 0):
		message += "?"
		var i = 0
		while(i < 10):
			if(gen.randi_range(0,30) == 0):
				message += "?"
			i+=1
	elif(gen.randi_range(0,50) == 0):
		message += "!"
		var i = 0
		while(i < 10):
			if(gen.randi_range(0,30) == 0):
				message += "!"
			i+=1
	
	if(gen.randi_range(0,1) == 0):
		message = message.to_lower()
	if(gen.randi_range(0,30) == 0):
		message = message.to_upper()
	self.text += message
	#replay
	$random_chat.wait_time = gen.randf_range(0.0, RANDOM_CHAT_FREQ)
	$random_chat.start()
