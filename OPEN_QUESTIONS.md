# Open Questions — The Glass Alibi

Non-blocking items for the author. None of these stop the game from being
played; they are places where the canon lock / master script left room and
this build deliberately did not invent story.

## Story / canon

1. **Daridra Dalit's role.** The brief marks them important but establishes
   no role. They do not appear in this build. Needs an author decision
   before any scene, dialogue, or sprite is written for them.
2. **Reserved names.** Hirendra Raju, Ram Piyari, Sher Bahadur, Muture
   Kanxa, Chuddha, Chimse Muso, and Padhuwa Hali are unassigned, per the
   canon lock. No arbitrary roles were given.
3. **Cover-identity knowledge map.** Who knows the playable subject is
   Damaai-overlaid-with-Saban, and when (Ritesh surely; the doctor's
   chart implies clinic knowledge; the prosecutor and detective's exact
   awareness is unstated). Current dialogue stays ambiguous where the
   master script is ambiguous.
4. **Engram mechanics.** How the overlay was applied, what "synaptic
   drift" thresholds mean physically, and why sanity numbers move as they
   do are presentation-level only. No mechanics beyond the master script
   were invented.
5. **Six-month timeline.** Baireni killing → graft → present night is
   "six months" per canon; exact intermediate dates are not established.
6. **Wedding ring detail.** The cryo-reveal wedding-band line is kept
   verbatim; any engraving/inscription detail is not specified in the
   source and was not invented.
7. **Supporting-cast depth.** Prosecutor, detective, boss, and doctor have
   exactly the master script's dialogue; no backstory was added.

## Decisions already approved by the author

- **Witness flashback prologue** (`prologue_witness`): built as a genuine
  scene with two real choices (spare / pay $500). Act II's corrupted-menu
  replay proves both options were fabricated — the override executes
  "SURGICAL AMPUTATION" regardless, quoting whichever text the player picked.
- **Doctor pronoun:** "he" (master script's "If she takes you" corrected to
  "If he takes you").

## Implementation notes (not questions, just disclosed)

- Two small conditional inner lines were added so state is visibly used:
  a suspicion-gated line in `act_one_climax` (`suspicion_ritesh >= 3`) and
  a spared-witness memory line in Act II. No plot facts were added.
- **FRAGMENT A gate:** the final menu shows FRAGMENT A only when
  `truth_fragments >= 2` (look+wait=3, accuse+wait=2 qualify; look+follow=1
  and accuse+follow=0 do not). This makes the "truth" ending earned rather
  than always available; the gate threshold is a design choice, flag it if
  the author wants it always visible.
- Caste/class-coded names are never used as moral shorthand; character
  names appear only as the master script uses them.

## Assets

- All art and audio are original generated placeholders (see
  `ASSET_CREDITS.md`). Final soundtrack and character art are still to be
  commissioned/dropped in; declarations in `game/assets.rpy` and
  `safe_play()` make replacement drop-in.