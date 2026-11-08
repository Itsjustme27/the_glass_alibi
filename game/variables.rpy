# Playthrough state. Every variable here is consumed by the story:
#   sanity           -> glitch overlay intensity, low-stability warning in Act III
#   suspicion_ritesh -> extra accusation beat in the Act I climax; reset when Ritesh is saved
#   truth_fragments  -> gates FRAGMENT A (self-destruction ending)
#   spared_witness   -> which mercy the player "chose" in the prologue; echoed in Act II
#   glitch_active    -> enables the scanline distortion overlay from Act II onward

default sanity = 100
default suspicion_ritesh = 0
default truth_fragments = 0
default spared_witness = False
default glitch_active = False

# Records which option the player clicked in the corrupted Act II menu, so the
# override message can quote their actual input back at them.
default forced_choice_text = "Spare the witness"