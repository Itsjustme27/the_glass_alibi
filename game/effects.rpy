# Presentation helpers: transitions, chapter cards, distortion overlay, and
# crash-safe audio hooks.

define flash_red = Fade(0.1, 0.0, 0.3, color="#ff0000")
define flash_white = Fade(0.05, 0.05, 0.2, color="#ffffff")
define glitch_fade = Pixellate(0.4, 12)

init python:

    # Audio hook that never crashes on a missing file. Drop final tracks into
    # game/audio/ under the same filenames and they are picked up automatically.
    def safe_play(filename, channel="music", fadein=0.0, loop=None):
        if not renpy.loadable(filename):
            return
        if channel == "music":
            renpy.music.play(filename, fadein=fadein, loop=loop, if_changed=True)
        else:
            renpy.sound.play(filename, channel=channel, fadein=fadein)

    def show_chapter(title, subtitle=""):
        renpy.show_screen("chapter_card", title=title, subtitle=subtitle)
        renpy.transition(dissolve)
        renpy.pause(2.4)
        renpy.hide_screen("chapter_card")
        renpy.transition(dissolve)

    config.overlay_screens.append("glitch_overlay")


screen chapter_card(title, subtitle=""):
    zorder 200

    add Solid("#04070acc")

    vbox:
        align (0.5, 0.45)
        spacing 24

        text title:
            xalign 0.5
            style "chapter_title"

        if subtitle:
            text subtitle:
                xalign 0.5
                style "chapter_subtitle"


style chapter_title:
    font "fonts/LiberationMono-Regular.ttf"
    size 62
    color "#2de1c2"

style chapter_subtitle:
    font "fonts/LiberationMono-Regular.ttf"
    size 30
    color "#9fb8b2"


# Scanline distortion, active from the Act II override onward. Intensity scales
# with lost sanity. Hidden on the main menu.
screen glitch_overlay():
    if glitch_active and not main_menu:
        add "images/fx/scanlines.png" alpha (0.06 + (100 - sanity) * 0.0012)