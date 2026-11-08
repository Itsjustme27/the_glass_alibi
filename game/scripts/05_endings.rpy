# ANTYAHARU — the three established endings.
# Outcomes are canon-locked: self-destruction, Damaai Saarki reasserting,
# or the hybrid escaping after destroying the original body.

label ending_glass_alibi:

    scene black with flash_white
    $ safe_play("audio/revolver_shot_echo.ogg", channel="sound")

    "The .38 kicks against my palm. Not toward Ritesh. Not toward [BOSS_NAME]."
    "Right against the neural port behind my ear."

    scene bg_cyber_clinic_morgue with dissolve
    show ritesh_crying at center

    "I hit the wet tiles. Above me, the red emergency lights spin like a dying carousel. Ritesh drops his gun and falls to his knees beside me, cradling my head in his lap—just like he must have held the real Saban six months ago."

    s "Hey, Ritesh..."
    r "Don't talk. Stupid bastard, you always ruin the restoration right at the end..."
    s "Did I... did I get the bastard who killed your husband?"

    "Ritesh looks at the blood pooling beneath my skull. For the first time in six months, his smile is genuine."

    r "Yeah, Saban. You got him. Case closed."

    scene black with fade

    "ENDING 1 OF 3: KANCH KO JHOOTH (SACHO NOIR ANTIM)"

    return


label ending_red_canvas:

    scene bg_cyber_clinic_morgue with flash_red
    $ safe_play("audio/industrial_slaughter.ogg")

    neos "DELETION COMPLETE. WELCOME BACK, DAMAAI SAARKI."

    "The headache vanishes. Suddenly, the world is crisp, quiet, and hysterically funny."
    "Before [BOSS_NAME] can draw his piece, I flick a surgical scalpel off the tray straight into his carotid artery. Two bullets from my .38 drop [DOCTOR_NAME] and [PROSECUTOR_NAME] before they hit the exit."

    "Only Ritesh remains, kneeling among the corpses, out of ammo, staring up at me."

    show ritesh_bloodied at center with dissolve

    damaai_saarki "Six months you made me wear that dead cop's cheap cologne, Ritesh. You made me weep over his photographs. You should be terrified."

    r "Then cut my throat. Finish it."

    "I kneel in front of him, dipping my thumb into [BOSS_NAME]'s blood and smearing it across Ritesh's cheekbone like paint."

    damaai_saarki "Kill you? Darling, Saban's memories are still floating around in my temporal lobe. I know how he loved you. Better than that—I {i}feel{/i} it. And I'm never letting you go."

    scene black with fade

    "ENDING 2 OF 3: RAGATKO PAUBHA (RAKSHASI ANTIM)"

    return


label ending_broken_mirror:

    scene bg_cyber_clinic_morgue with vpunch
    $ safe_play("audio/glass_explosion.ogg", channel="sound")

    "I empty the entire cylinder into the cryo-pod and the server rack behind [DOCTOR_NAME]. Thousands of gallons of freezing blue fluid and shattered glass flood the theater, short-circuiting the neural transmitter and electrocuting [BOSS_NAME] where he stands."

    "Ritesh stares in horror as the preserved body of the real Saban washes across the floor."

    r "What did you do?! That was all I had left of him!"

    s "Look at me, Ritesh! His memories are in {i}my{/i} head! The killer's hands are on {i}my{/i} wrists! Neither of them exists anymore—only me!"

    "I grab Ritesh's wrist, pulling him toward the service elevator as sirens wail above the dock."

    r "Let go of me! You're a forgery! You're a lie I painted over a murderer!"

    s "A forgery is worth just as much as the original if nobody left alive can tell the difference. Now put your gloves on—[DETECTIVE_NAME] is coming."

    scene black with glitch_fade

    neos "REBOOTING LOOP..."

    "The neon sign across the street flickers in a dying rhythm. Three short buzzes, one long..."

    "ENDING 3 OF 3: NAYA JYAN, PURANO PAAP (YAAD KO CHAKRA)"

    return