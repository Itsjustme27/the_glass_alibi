# ANK I: RESHAM KO FAANDA

label act_one_gallery:

    $ show_chapter("ANK I", "RESHAM KO FAANDA")

    scene bg_ritesh_gallery_night with fade
    $ safe_play("audio/cello_noir_tension.ogg", fadein=2.0)

    "2:15 AM. Ritesh's private restoration studio, tucked beneath an old market building in Bhakunde Besi."
    "Paubha paintings, old Bhairav masks, and disassembled brass idols line the tables under harsh UV lamps. It looks less like an art studio and more like an ICU for expensive statues whose owners have more money than sense."

    show ritesh_shirt_sleeves at left with dissolve
    show prosecutor_suit at right with dissolve

    p "You promised me you were out of the fixer game, Ritesh! My father's chief accountant gets carved up like a holiday roast, and your brother is the first man on the scene?!"

    r "Lower your voice, [PROSECUTOR_NAME]. Saban is in the back room washing up."

    "I stand behind the heavy velvet curtain of the darkroom, listening through the crack. My head is splitting. Every time the UV lamp hums, I hear the sound of bone saws."

    p "My father knows someone is systematically executing his lieutenants. He thinks the Sarkari Wakil ko karyalaya is leaking their safe houses. If he finds out I'm sleeping with the brother of the prime suspect—"

    r "Saban is not the suspect! He's sick, [PROSECUTOR_NAME]. His mind is fracturing. If I don't clean up the trail—"

    p "Then let him burn! Why are you destroying your life for a washed-up detective who can't even remember your birthday?!"

    "Silence hangs heavy in the gallery. Through the gap in the velvet, I watch Ritesh pour two glasses of local raksi with hands that are trembling."

    r "Because I made a vow at the wharf six months ago. And unlike your family, darling, I pay my debts in full."

    p "Take this encrypted drive. It's the sealed indictment against my father's personal neuro-clinic—[DOCTOR_NAME]'s black site. Destroy it. If Saban finds it, he'll go after my father directly, and neither of us will survive the week."

    hide prosecutor_suit with dissolve

    "The heavy steel door clangs shut as [PROSECUTOR_NAME] leaves. Ritesh walks toward the back office to lock the drive in his floor safe."
    "Wait. The floor safe isn't behind his desk. He's walking toward the false brick wall behind the old paubha of Bhairav, whose painted eyes seemed to judge every bad financial decision in the room."

    menu:
        "Follow Ritesh and confront him immediately.":
            $ suspicion_ritesh += 3
            jump act_one_confrontation

        "Wait until Ritesh leaves, then pick the lock on the false wall.":
            $ truth_fragments += 2
            "I wait twenty minutes until Ritesh goes upstairs to shower. I slip a tension wrench into the electronic bypass behind the painting."
            jump act_one_vault_discovery


label act_one_vault_discovery:

    scene bg_secret_vault with flash_white
    $ safe_play("audio/metal_door_creak.ogg", channel="sound")

    "The false wall swings inward. The smell hits me first—formaldehyde, ozone, and old blood."
    "It's not an art vault. It's a trophy room."
    "Pinned to a corkboard are seven severed left ring fingers suspended in glass vials. Below them: surgical spools of red silk thread, and a bloodstained butcher's apron."
    "And sitting on the center table is a pristine leather case containing the encrypted drive [PROSECUTOR_NAME] just handed him—next to a folder labeled: {b}PROJECT: HOELMES_OVERRIDE{/b}."

    r "I told you not to look in the puddle, Saban."

    show ritesh_dark_silhouette at center with dissolve

    jump act_one_climax


label act_one_confrontation:

    scene bg_secret_vault with fade
    show ritesh_dark_silhouette at center with dissolve

    "I kick the false wall open before the latch clicks. Inside the hidden alcove sits a surgical tray, seven glass vials containing severed ring fingers, and the murder weapons from every Damaai Saarki crime scene in the city."

    s "You son of a bitch."

    jump act_one_climax


label act_one_climax:

    "I draw my .38 revolver, thumbing back the hammer. My hand is shaking so violently the barrel rattles against Ritesh's sternum."

    s "All those nights 'bribing coroners.' All those fake alibis. You weren't protecting me from the police, Ritesh. You're Damaai Saarki! You've been using my old case files to butcher [BOSS_NAME]'s syndicate so your prosecutor boyfriend can inherit a clean empire!"

    if suspicion_ritesh >= 3:
        "The van. The pigment. The pity. Every warning sign I swallowed tonight finally comes back up at once."

    "Ritesh looks down at the revolver pressed against his silk shirt. He doesn't raise his hands. He looks exhausted—like a man who has been carrying a corpse up a mountain for six months."

    r "Pull the trigger if it makes the headache stop, Saban. Lord knows I'm tired of mopping the floors."

    s "Don't play the martyr with me! Why are the trophies in your vault?!"

    r "Because you kept leaving them under your pillow like a stray cat bringing home dead birds!"

    "A high-pitched whine pierces my left ear. The room tilts forty-five degrees."

    show bg_secret_vault with vpunch

    s "Shut up! You're lying! I'm Saban Hoelmes! I hunt monsters, I don't—"

    r "Saban. What did you do at 11:40 PM tonight before you called me to Kotha No 420?"

    s "I... I interrogated the night manager in the alley. I let him go! The player—I mean, {i}I{/i} chose to spare him!"

    r "Did you?"

    "Ritesh reaches into his pocket and pulls out a neural-link remote. He presses a single red button."

    neos "OVERRIDE CODE ACCEPTED: ADMIN_RITESH. REPLAYING RAW OCULAR FEED..."

    jump act_two_unreliable_ui