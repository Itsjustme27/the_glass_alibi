# THE GLASS ALIBI — entry point.
#
# Story flow:
#   start -> prologue_witness -> prologue_present -> act_one_gallery
#   act_one_gallery -> (vault_discovery | confrontation) -> act_one_climax
#   act_one_climax -> act_two_unreliable_ui -> act_three_clinic
#   act_three_clinic -> (ending_glass_alibi | ending_red_canvas | ending_broken_mirror)
#
# Scene scripts live in game/scripts/. Characters: characters.rpy.
# State: variables.rpy. Images: assets.rpy. Presentation: effects.rpy.

label start:

    stop music fadeout 1.0
    scene black with fade

    neos "BOOTING ENGRAM_ARCHIVE: SUBJECT_09 ('SABAN_HOELMES')..."
    neos "WARNING: SYNAPTIC DRIFT DETECTED AT SECTOR 404. APPLYING DAMPENERS."
    neos "PLAYING OCULAR ARCHIVE: TIMESTAMP 23:40. LOCATION: KOTHA_420 SERVICE ALLEY."

    $ show_chapter("PRARAMBHA", "HILO MA DEKHINE CHHAAYA")

    jump prologue_witness