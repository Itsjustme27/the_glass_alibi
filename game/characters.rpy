# Character name macros and definitions for The Glass Alibi.
# Change the four name macros below to rename the supporting cast everywhere.

init offset = -1

define PROSECUTOR_NAME = "Ghanashyam Prasad"
define DETECTIVE_NAME = "Inspector Rajaram Kumar"
define BOSS_NAME = "Chairman Khatey Bahun"
define DOCTOR_NAME = "Dr. Godatta Prasad"

define s = Character("Saban Hoelmes", color="#a3c1ad", what_prefix='"', what_suffix='"')
define r = Character("Ritesh", color="#e63946", what_prefix='"', what_suffix='"')
define p = Character("[PROSECUTOR_NAME]", color="#f4a261", what_prefix='"', what_suffix='"')
define d = Character("[DETECTIVE_NAME]", color="#457b9d", what_prefix='"', what_suffix='"')
define b = Character("[BOSS_NAME]", color="#6d597a", what_prefix='"', what_suffix='"')
define doc = Character("[DOCTOR_NAME]", color="#2a9d8f", what_prefix='"', what_suffix='"')

# Prefix/suffix go through interpolation, so literal brackets must be escaped.
define damaai_saarki = Character("Damaai Saarki", color="#ff0055", what_prefix='[[', what_suffix=']]')
define neos = Character("NEURAL_OS v4.02", color="#00ffcc", what_font="fonts/LiberationMono-Regular.ttf")