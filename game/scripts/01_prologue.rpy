# PRARAMBHA: HILO MA DEKHINE CHHAAYA
# The witness flashback implements the scene referenced by the master script
# (spared_witness, "I chose to spare him", the Act II ocular replay). Both
# options here are genuine and in the player's control — that is the point.

label prologue_witness:

    scene bg_neon_alley_rain with fade
    $ safe_play("audio/rain_synth_drone.ogg", fadein=2.0)

    "11:40 PM. The service alley behind Kotha No 420. The rain has been falling for hours, like the sky is trying to wash the city clean and failing."
    "The night manager is on his knees in the runoff, hands laced over his head like a man praying to a broken streetlight."
    "He saw me come out of the building. Or he thinks he did. In this city, seeing the wrong thing is a terminal condition."

    menu:
        "Spare the witness and tell him to leave town.":
            $ spared_witness = True
            s "Get up. Take the night bus out of the valley and don't come back. You never saw my face."
            "He nods so fast I'm afraid his neck will snap, then scrambles toward the main road without looking back."

        "Give him $500 to forget he saw me.":
            $ spared_witness = False
            "I press five hundred dollars into his shaking hand. His eyes go wide enough to catch the neon."
            s "You forgot my face. Spend it somewhere far from here."
            "He bolts into the rain without a word."

    "The alley is empty again. My hands did exactly what I told them to. Clean. Simple. The way police work is supposed to be."
    "I dial Ritesh. Kotha No 420. I need him here before the thana vultures start circling."

    jump prologue_present


label prologue_present:

    scene bg_neon_alley_rain with glitch_fade
    $ safe_play("audio/rain_synth_drone.ogg", fadein=2.0)

    "The neon sign across the street flickers in a dying rhythm. Three short buzzes, one long. Jasto Indra Jatra ma Lakhey le traffic police ko whistle choryo ra sahar lai afnai taal ma nachauna thalyo."
    "Mero kalo overcoat ma sasto local raksi ra kasai aruko paap ko gandha adkeko cha."
    "Six months since the Navama Ghat raid. Six months since a bullet grazed my temporal lobe, put my partner in a closed casket, and left my memory looking like a government road after monsoon."

    show ritesh_coat_neutral at center with dissolve

    r "You're staring at the puddle again, Saban. If you're looking for your reflection, save your energy. You won't like what's looking back."

    "The man I know as my adoptive brother steps under the awning, shaking acid rain off a black chhata that probably costs more than my rent. Ritesh always looked less like an art restorer and more like a Lakhey who wandered out of Indra Jatra, opened an underworld accounting firm, and started charging demons late fees."

    s "The body upstairs, Ritesh. Kotha No 420. Same surgical knot. Same missing left ring finger. Damaai Saarki is mocking me."

    r "And you touched the evidence before the forensics sweep got here. Again."

    "Ritesh pulls a silver cigarette case from his coat; his panchadhatu thumb-ring catches the red police strobes bleeding through the alley."

    r "Do you have any idea what I had to promise the thana pramukh just to get the lobby CCTV wiped tonight? [PROSECUTOR_NAME] thinks I'm having an affair because I spend every Tuesday at 3 AM bribing coroners for you."

    s "Your boyfriend is the Deputy Sarkari Wakil. Tell him even Yamraj needs paperwork before collecting someone."

    show ritesh_coat_serious at center

    r "Don't joke about [PROSECUTOR_NAME], Saban. Not tonight. That stiff upstairs in Kotha No 420? He was an accountant for [BOSS_NAME]."

    s "Wait. [BOSS_NAME]? Your boyfriend's estranged father? The head of the Kaalo Murkutta?"

    r "Which means the family business just bled onto my Nepali galicha. Look at your hands, Saban."

    menu:
        "Look down at my hands.":
            $ sanity -= 10
            $ truth_fragments += 1
            "I look down. Under my fingernails, mixed with dried blood, is a faint deep-blue residue: the mineral pigment used in paubha restoration. Ritesh uses that expensive shade only on his most carefully restored pieces."
            s "Ritesh... why is your gallery's pigment under my nails?"
            r "Keep your voice down. Put your gloves on. [DETECTIVE_NAME] just ducked under the police tape."

        "Accuse Ritesh of hiding something.":
            $ suspicion_ritesh += 2
            s "Stop deflecting. Why was your gallery's climate-controlled delivery van parked two blocks from the victim's apartment?"
            "Ritesh doesn't blink. The corner of his mouth twitches—not guilt, but an unbearable, suffocating pity."
            r "Because someone had to carry you out of the lobby before you woke up, brother. Put your gloves on. [DETECTIVE_NAME] is coming."

    show ritesh_coat_neutral at left with move
    show detective_raincoat at right with dissolve

    d "Well, well. The amnesia twins. Tell me, Hoelmes, does your brother always hold your umbrella while you contaminate my crime scenes, or is today your anniversary?"

    s "Good evening to you too, [DETECTIVE_NAME]. You're late. Damaai Saarki left twenty minutes ago."

    d "Funny. Because the building's smart-grid registered only two biometric signatures leaving the fourth floor in the last hour. One was masked by a military-grade scrambler."

    "She steps closer, the rain dripping off the edge of her black Dhaka topi onto my lapel."

    d "The other smelled like paint thinner and an expensive pashmina coat. Care to comment, Mr. Ritesh?"

    r "I restore Malla-kaal ko stone idols and paubha paintings for the Prahari Pramukh's wife, Inspector. Half the city smells my paint thinner. Now, unless you have a warrant for my chhata, my brother and I are going for momo."

    jump act_one_gallery