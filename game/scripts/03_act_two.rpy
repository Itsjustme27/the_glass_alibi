# ANK II: BIGRIYEKO CHOICE MACHINE

label act_two_unreliable_ui:

    $ show_chapter("ANK II", "BIGRIYEKO CHOICE MACHINE")

    $ glitch_active = True
    scene bg_neon_alley_rain with glitch_fade
    $ safe_play("audio/industrial_heartbeat.ogg", fadein=0.5)

    "My vision fractures into scanlines. I'm forced to watch my own memory from three hours ago—except the color grading filter has been stripped away."
    "On the wet pavement in front of me is the night manager of Kotha No 420, begging for his life."

    if spared_witness:
        "In my memory, I remember choosing the merciful path. Let's see what happens when I try to choose it again."
    else:
        "In my memory, I remember choosing the cheap path. Five hundred dollars to make a problem disappear. Let's see what happens when I try to choose it again."

    # The corrupted choice: both options look merciful and both are accepted,
    # but the baseline personality hijacks the motor cortex either way. The
    # player's actual input is quoted back to them in the override message.
    menu:
        "Spare the witness and tell him to leave town. [[GOOD CHOICE]":
            $ forced_choice_text = "Spare the witness"

        "Give him $500 to forget he saw me. [[MERCIFUL CHOICE]":
            $ forced_choice_text = "Pay the witness $500"

    $ safe_play("audio/ui_error_buzz.ogg", channel="sound")
    scene bg_neon_alley_rain with flash_red

    neos "ERROR 409: MOTOR CORTEX HIJACKED BY BASELINE PERSONALITY."
    neos "TRANSLATING INPUT: [['[forced_choice_text]']] ---> EXECUTING: [[SURGICAL AMPUTATION]"

    "I watch in horror through my own eyes as my hands ignore my brain's command. My left hand clamps over the manager's mouth while my right hand pulls a bone saw from my coat lining."

    damaai_saarki "Shh. Hold still. If the stitch is crooked, Ritesh gets so disappointed in my brushwork."

    scene bg_secret_vault with glitch_fade
    $ sanity -= 40

    "I drop to my knees on the vault floor, dry-heaving as the ocular playback cuts out."

    s "What is in my head?! Ritesh, what the hell is inside my skull?!"

    show ritesh_angry at center with dissolve

    r "Every time your adrenaline spikes, the graft slips. You black out, you butcher another link in [BOSS_NAME]'s chain, and then your neural implant hallucinates a righteous detective story so you can live with yourself."

    s "The graft? What graft?! Who did this to me?!"

    r "[DOCTOR_NAME]. Down at the Navama Ghat Clinic. Before I can explain the rest—"

    $ safe_play("audio/glass_shatter_breach.ogg", channel="sound")
    scene bg_secret_vault with vpunch

    d "Nepal Police—Sorry, purano film ko dialogue niskyo. Navama Ghat ko Prahari Task Force! Haath mathi, Hoelmes!"

    show detective_tactical at right with dissolve
    show ritesh_angry at left

    "The studio skylight shatters. [DETECTIVE_NAME] rappels down onto the restoration tables, laser sight painted squarely between my eyes."

    d "Well, look at the corkboard. Seven fingers, seven cold cases. Looks like I don't need a warrant for your umbrella after all, Ritesh."

    "Suddenly, Ritesh lunges in front of me, kicking over a rack of turpentine carboys and firing a flare gun into the ceiling sprinklers."

    r "Run, Saban! Go to Baireni! Find [DOCTOR_NAME]! If he takes you into custody, they'll run a cranial scan and the Syndicate will execute you before sunrise!"

    show detective_angry at center with dissolve
    d "Freeze! Don't make me shoot through him, Hoelmes!"

    menu:
        "Save Ritesh and help him fight [DETECTIVE_NAME].":
            $ suspicion_ritesh = 0
            "I grab Ritesh by his silk collar and haul him behind the heavy steel vault door, jamming my .38 revolver into the locking mechanism to trap [DETECTIVE_NAME] outside."
            r "You idiot... you were supposed to leave me!"
            s "Shut up and run! You're the only one with the admin password to my brain!"
            jump act_three_clinic

        "Abandon Ritesh to buy time and sprint for Baireni alone.":
            $ sanity -= 20
            "I vault over the back window as [DETECTIVE_NAME] tackles Ritesh into the shattered glass. I hear Ritesh laughing through a mouthful of blood as the handcuffs click."
            r "Run, you bastard! Go see what you really look like!"
            jump act_three_clinic