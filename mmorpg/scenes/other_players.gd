extends CharacterBody3D

@export var sounds: Array[AudioStream] = []

@export var RANDOM_VOICE_FREQ = 2.0
@export var RANDOM_JUMP_FREQ = 2.0

const SPEED = 5.0
const JUMP_VELOCITY = 4.5
var gen = RandomNumberGenerator.new()
#var random = 0
var randomizer: AudioStreamRandomizer = AudioStreamRandomizer.new()


func _ready():
	if sounds.size() > 0:
		setup_randomizer()
	#$Voice.stream(sounds)
	$random_voice.wait_time = gen.randf_range(0.0, RANDOM_VOICE_FREQ)
	$random_jump.wait_time = gen.randf_range(0.0, RANDOM_JUMP_FREQ)
	$random_voice.start()
	$random_jump.start()

func _physics_process(delta: float) -> void:
	#random = gen.randi_range(0, 100)
	#print(random)
	# Add the gravity.
	if not is_on_floor():
		velocity += get_gravity() * delta

	#var input_dir := Input.get_vector("ui_left", "ui_right", "ui_up", "ui_down")
	#var direction := (transform.basis * Vector3(input_dir.x, 0, input_dir.y)).normalized()
	#if direction:
	#	velocity.x = direction.x * SPEED
	#	velocity.z = direction.z * SPEED
	#else:
	#	velocity.x = move_toward(velocity.x, 0, SPEED)
	#	velocity.z = move_toward(velocity.z, 0, SPEED)

	move_and_slide()
	
func setup_randomizer():

	var i = 0
	for sound in sounds:
		if sound:
			randomizer.add_stream(i, sound)
		i += 1

	$Voice.stream = randomizer

func _on_voice_finished() -> void:
		$voice_sign.visible = false

func _on_random_voice_timeout() -> void:
	if !$Voice.playing:
		$voice_sign.visible = true
		$Voice.play()

	$random_voice.wait_time = gen.randf_range(0.0, RANDOM_VOICE_FREQ)
	$random_voice.start()

func _on_random_jump_timeout() -> void:
	if is_on_floor():
		velocity.y = JUMP_VELOCITY
	$random_jump.wait_time = gen.randf_range(0.0, RANDOM_JUMP_FREQ)
	$random_jump.start()
