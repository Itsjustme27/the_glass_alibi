# ANK III: BAIRENI KO MAHA-TAMASHA

label act_three_clinic:

    $ show_chapter("ANK III", "BAIRENI KO MAHA-TAMASHA")

    scene bg_cyber_clinic_morgue with fade
    $ safe_play("audio/dark_synth_climax.ogg", fadein=1.5)

    "3:45 AM. Baireni. [DOCTOR_NAME]'s subterranean neuro-grafting theater."
    "The room smells like burnt copper and cryo-fluid. In the center of the theater stands a glass cryo-pod, frosted over from the inside."

    if sanity <= 50:
        neos "WARNING: SYNAPTIC INTEGRITY BELOW SAFE THRESHOLD. PERSONALITY COHESION FAILING."

    "Standing beside it are [BOSS_NAME], his son [PROSECUTOR_NAME], and [DOCTOR_NAME]."

    show boss_shocked at left with dissolve
    show prosecutor_shocked at center with dissolve
    show doctor_shocked at right with dissolve

    "Wait. [PROSECUTOR_NAME] is on his knees, his lip split, his wrists bound in red silk cord."

    b "Ah. The prodigal hound returns to the kennel. Tell me, [DOCTOR_NAME], did the artificial conscience hold up, or is he ready to come back on the payroll?"

    doc "His synaptic drift is at ninety-two percent, [BOSS_NAME]. One more cognitive shock and the 'Saban Hoelmes' persona will dissolve completely."

    s "Let [PROSECUTOR_NAME] go! It's over, [BOSS_NAME]. I have the drive. I know you hired Damaai Saarki to wipe out your own traitors!"

    "The crime boss bursts out laughing. It's a dry, rattling sound that echoes off the tiled autopsy walls."

    b "Hired him? Son... walk over to the cryo-pod. Wipe the frost off the glass."

    "My legs move on their own. I approach the cylindrical tank in the center of the room. With a trembling sleeve, I wipe away the rime."

    scene bg_cryo_reveal with flash_white
    $ safe_play("audio/heartbeat_stop.ogg", channel="sound")

    "Floating inside the blue preservation fluid is a corpse with a bullet hole through his left temple."
    "He's wearing my black overcoat. He's wearing a gold wedding band that matches the panchadhatu ring on Ritesh's thumb."
    "And he has the face I thought I saw in the puddle every night."

    s "No... no, that's impossible. If that's Saban Hoelmes in the tank... then who the hell am I?!"

    show ritesh_angry at left with dissolve    #  TODO: replace here with bloodied later

    "The heavy airlock hisses open. Ritesh stumbles in, holding a suppressed submachine gun, blood soaking his white collar."

    r "Tell him, [DOCTOR_NAME]. Or I swear to God I'll paint that wall with every last one of you."

    doc "Six months ago at Baireni... the Syndicate's top assassin—Damaai Saarki—ambushed Detective Saban Hoelmes and put a bullet through his skull."

    r "Saban wasn't my brother."

    show ritesh_angry at center with dissolve
    "Ritesh's voice cracks, raw and devoid of its usual aristocratic armor. He stares at the corpse in the glass tank, tears finally cutting tracks through the soot on his cheeks."

    r "Saban Hoelmes was my husband. He was the only good thing in this rotting city. And you—{i}Damaai Saarki{/i}—you butchered him on Baireni while I watched from the rusted cargo cranes beside Baireni's ghat."

    s "I... I killed him?"

    r "I captured you that night. Killing you was too merciful. Too quick. So I paid [DOCTOR_NAME] three million dollars to take Saban's backed-up neural engrams and burn them over your cerebral cortex."

    "Ritesh raises the submachine gun, aiming it not at [BOSS_NAME], not at the doctor—but directly at me."

    r "I turned the monster who murdered my husband into a puppet wearing his soul. I made you hunt down your own Syndicate brothers one by one while mourning the man you killed. And to keep [PROSECUTOR_NAME] close enough to betray his father's empire from the inside, I let him believe I loved him."

    show saban_shocked at center with dissolve
    p "Ritesh... you used me? This entire time, everything we had was just to get the clinic coordinates?!"

    r "Everything I am died in that tank six months ago, [PROSECUTOR_NAME]. You were just brushstrokes on the canvas."

    b "Bravo! A masterpiece of vengeance! Truly, Ritesh, you belong in Patan Museum's basement, with a board saying: 'Do not touch. May start monologuing.' But now the paint is dry. [DOCTOR_NAME], hit the purge switch. Give me back my assassin!"

    doc "Executing factory reset on Subject 09!"

    $ safe_play("audio/siren_glitch_overload.ogg", channel="sound")
    scene bg_cyber_clinic_morgue with flash_red

    neos "CRITICAL WARNING: PERSONALITY MATRIX 'SABAN_HOELMES' DELETING... 85%... 92%..."

    damaai_saarki "Finally! God, do you know how exhausting it is pretending to care about orphans and due process?! Hand me a scalpel, Khatey, I want to start with the art critic!"

    s "No! Get out of my head! I am Saban Hoelmes!"

    r "Fight him, Saban! Or finish the canvas!"

    # FINAL CLIMAX CHOICE: THREE DISTINCT ENDINGS
    # FRAGMENT A requires truth_fragments >= 2 (reachable via the patient
    # lock-picking path; the confrontation path yields fewer fragments).
    menu:
        "FRAGMENT A: Shoot myself in the temple before Damaai Saarki takes full control. [[JASOOS KO PRAYASHCHIT]" if truth_fragments >= 2:
            jump ending_glass_alibi

        "FRAGMENT B: Surrender to Damaai Saarki's persona and slaughter everyone in the room—except Ritesh. [[RAKSHAS KO KALAKRITI]":
            jump ending_red_canvas

        "FRAGMENT C: Shoot the cryo-tank, shattering the real Saban's body, and force Ritesh to escape with me as a new man. [[NAYA MISRAN]":
            jump ending_broken_mirror