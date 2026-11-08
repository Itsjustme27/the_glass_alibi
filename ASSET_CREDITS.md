# Asset Credits — The Glass Alibi

All visual and audio assets in this build are **original placeholders**,
procedurally generated for this project. No third-party art, music, or
hotlinked resources are used. They are free of external licensing
restrictions and may be replaced freely; image declarations are logical
names in `game/assets.rpy`, so swapping a file requires no script changes.

## Images

| Asset | Path | Creator | Source / Licence |
|---|---|---|---|
| Neon alley rain (5 variants of one scene) | `game/images/bg/neon_alley_rain.png` | Generated for this project | Original procedural art (`tools/generate_visuals.py`), no external licence restrictions |
| Ritesh gallery night | `game/images/bg/ritesh_gallery_night.png` | same | same |
| Secret vault | `game/images/bg/secret_vault.png` | same | same |
| Cyber clinic / morgue | `game/images/bg/cyber_clinic_morgue.png` | same | same |
| Cryo reveal | `game/images/bg/cryo_reveal.png` | same | same |
| 13 character sprites (Ritesh ×7, detective ×2, prosecutor ×2, boss, doctor) | `game/images/sprites/*.png` | same | same |
| Scanline overlay | `game/images/fx/scanlines.png` | same | same |
| GUI elements (textbox, namebox, buttons, bars, sliders, scrollbars, overlays, menu backgrounds, window icon; desktop + phone) | `game/gui/**/*.png` | same | same; regenerated at the Ren'Py template's exact dimensions |

Attribution requirement: none (original work). If you credit the project,
"placeholder art generated for The Glass Alibi" is sufficient.

## Audio

All 12 cues in `game/audio/` were synthesized from scratch (pure-Python
waveform synthesis, converted with ffmpeg/libvorbis) by
`tools/generate_audio.py`. Original work, no external licence restrictions,
no attribution required.

| Cue | File | Use |
|---|---|---|
| Rain synth drone | `rain_synth_drone.ogg` | Main menu / alley ambience (loop) |
| Cello noir tension | `cello_noir_tension.ogg` | Investigation (loop) |
| Industrial heartbeat | `industrial_heartbeat.ogg` | Vault / clinic tension (loop) |
| Dark synth climax | `dark_synth_climax.ogg` | Act I climax (loop) |
| Industrial slaughter | `industrial_slaughter.ogg` | Act II override / breach (loop) |
| Metal door creak | `metal_door_creak.ogg` | Vault discovery SFX |
| UI error buzz | `ui_error_buzz.ogg` | Forced-override SFX |
| Glass shatter breach | `glass_shatter_breach.ogg` | Raid breach SFX |
| Heartbeat stop | `heartbeat_stop.ogg` | Cryo reveal SFX |
| Siren glitch overload | `siren_glitch_overload.ogg` | Raid / ending SFX |
| Revolver shot echo | `revolver_shot_echo.ogg` | Ending SFX |
| Glass explosion | `glass_explosion.ogg` | Ending SFX |

Playback is crash-safe: `safe_play()` in `game/effects.rpy` silently skips
any missing file, so final soundtrack drops can replace these one-for-one.

## Fonts

| Font | Path | Creator | Licence | Attribution |
|---|---|---|---|---|
| Liberation Mono Regular | `game/fonts/LiberationMono-Regular.ttf` | Red Hat, Inc. (digitized data © 2010 Google Corporation) | SIL Open Font License 1.1 — full text in `game/fonts/LICENSE-LiberationMono.txt` | Reserved Font Name "Liberation"; licence file must accompany redistribution (included) |

DejaVu Sans (bundled with Ren'Py in `renpy/common/`) is used only by the
offline generators, not shipped as a game asset.

## Story text

Dialogue and scene text derive from the supplied master script and canon
lock documents. The witness flashback prologue was built with the author's
explicit approval; two small conditional lines were added to make state
variables visibly matter (see `OPEN_QUESTIONS.md`).