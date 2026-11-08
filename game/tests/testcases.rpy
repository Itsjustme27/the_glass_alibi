# Automated branch coverage for The Glass Alibi.
# Requires Ren'Py 8.5.0 or newer (automated testing was added in 8.5.0).
# Run: ./renpy.sh the_glass_alibi test glass_alibi --overwrite_screenshots
# (from the SDK root). The ui suite runs separately: test ui.

testsuite glass_alibi:

    setup:
        $ _test.maximum_framerate = False
        $ config.rollback_enabled = False
        $ renpy.music.set_volume(0.0)
        $ renpy.sound.set_volume(0.0)

    before testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)
        click "Start"

    # Mercy + observation + patience: truth_fragments 3, FRAGMENT A open.
    testcase mercy_wait_ending_a:
        advance until screen "choice"
        click "Spare the witness and tell him to leave town."
        assert eval spared_witness == True
        advance until screen "choice"
        click "Look down at my hands."
        assert eval truth_fragments == 1
        assert eval sanity == 90
        advance until screen "choice"
        click "Wait until Ritesh leaves, then pick the lock on the false wall."
        assert eval truth_fragments == 3
        advance until screen "choice"
        screenshot "act2_corrupted_menu.png"
        click "Spare the witness and tell him to leave town. [GOOD CHOICE]"
        assert eval forced_choice_text == "Spare the witness"
        assert eval glitch_active == True
        advance until screen "choice"
        click "Save Ritesh and help him fight Inspector Rajaram Kumar."
        assert eval suspicion_ritesh == 0
        advance until screen "choice"
        screenshot "final_choice.png"
        click "FRAGMENT A: Shoot myself in the temple before Damaai Saarki takes full control. [JASOOS KO PRAYASHCHIT]"
        advance until "ENDING 1 OF 3: KANCH KO JHOOTH (SACHO NOIR ANTIM)"
        click "ENDING 1 OF 3: KANCH KO JHOOTH (SACHO NOIR ANTIM)"
        assert screen "main_menu" timeout 15

    # Bribe + accusation + confrontation: truth_fragments 0, FRAGMENT A locked.
    testcase bribe_follow_ending_b:
        advance until screen "choice"
        click "Give him $500 to forget he saw me."
        assert eval spared_witness == False
        advance until screen "choice"
        click "Accuse Ritesh of hiding something."
        assert eval suspicion_ritesh == 2
        advance until screen "choice"
        click "Follow Ritesh and confront him immediately."
        assert eval suspicion_ritesh == 5
        assert eval truth_fragments == 0
        advance until screen "choice"
        click "Give him $500 to forget he saw me. [MERCIFUL CHOICE]"
        assert eval forced_choice_text == "Pay the witness $500"
        advance until screen "choice"
        click "Abandon Ritesh to buy time and sprint for Baireni alone."
        assert eval sanity == 40
        advance until screen "choice"
        assert eval truth_fragments < 2
        click "FRAGMENT B: Surrender to Damaai Saarki's persona and slaughter everyone in the room—except Ritesh. [RAKSHAS KO KALAKRITI]"
        advance until "ENDING 2 OF 3: RAGATKO PAUBHA (RAKSHASI ANTIM)"
        click "ENDING 2 OF 3: RAGATKO PAUBHA (RAKSHASI ANTIM)"
        assert screen "main_menu" timeout 15

    # Look + follow: truth_fragments 1, FRAGMENT A locked, hybrid escape.
    testcase look_follow_ending_c:
        advance until screen "choice"
        click "Spare the witness and tell him to leave town."
        advance until screen "choice"
        click "Look down at my hands."
        advance until screen "choice"
        click "Follow Ritesh and confront him immediately."
        assert eval truth_fragments == 1
        advance until screen "choice"
        click "Spare the witness and tell him to leave town. [GOOD CHOICE]"
        advance until screen "choice"
        click "Save Ritesh and help him fight Inspector Rajaram Kumar."
        advance until screen "choice"
        assert eval truth_fragments < 2
        click "FRAGMENT C: Shoot the cryo-tank, shattering the real Saban's body, and force Ritesh to escape with me as a new man. [NAYA MISRAN]"
        advance until "ENDING 3 OF 3: NAYA JYAN, PURANO PAAP (YAAD KO CHAKRA)"
        click "ENDING 3 OF 3: NAYA JYAN, PURANO PAAP (YAAD KO CHAKRA)"
        assert screen "main_menu" timeout 15

    # Accuse + wait: truth_fragments exactly 2, gate boundary, FRAGMENT A open.
    testcase accuse_wait_gate_boundary:
        advance until screen "choice"
        click "Give him $500 to forget he saw me."
        advance until screen "choice"
        click "Accuse Ritesh of hiding something."
        advance until screen "choice"
        click "Wait until Ritesh leaves, then pick the lock on the false wall."
        assert eval truth_fragments == 2
        advance until screen "choice"
        click "Give him $500 to forget he saw me. [MERCIFUL CHOICE]"
        advance until screen "choice"
        click "Abandon Ritesh to buy time and sprint for Baireni alone."
        advance until screen "choice"
        click "FRAGMENT A: Shoot myself in the temple before Damaai Saarki takes full control. [JASOOS KO PRAYASHCHIT]"
        advance until "ENDING 1 OF 3: KANCH KO JHOOTH (SACHO NOIR ANTIM)"


testsuite ui:

    setup:
        $ _test.maximum_framerate = False
        $ config.rollback_enabled = False
        $ renpy.music.set_volume(0.0)
        $ renpy.sound.set_volume(0.0)
        if not screen "main_menu":
            run MainMenu(confirm=False)

    testcase menus_save_load_history:
        assert screen "main_menu"
        screenshot "main_menu.png"
        click "Preferences"
        assert screen "preferences"
        click "Return"
        assert screen "main_menu"
        click "About"
        assert screen "about"
        click "Return"
        click "Start"
        advance until screen "choice"
        screenshot "prologue_choice.png"
        run ShowMenu("save")
        assert screen "save"
        run FileSave(1, confirm=False)
        click "Return"
        advance
        run FileLoad(1, confirm=False)
        assert screen "choice" timeout 15
        assert eval sanity == 100
        run ShowMenu("history")
        assert screen "history"
        click "Return"
        run ShowMenu("preferences")
        assert screen "preferences"
        click "Return"
        exit