#!/usr/bin/env python3
"""Synthesize original placeholder audio for The Glass Alibi.

All tracks are procedurally generated (no external assets) and converted to
Ogg Vorbis with ffmpeg. Music loops are crossfade-seamless. Final soundtrack
files can replace game/audio/*.ogg under the same names; story code uses the
crash-safe safe_play() hook.
"""

import array
import math
import os
import random
import subprocess
import tempfile
import wave

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AUDIO = os.path.join(ROOT, "game", "audio")
SR = 32000
random.seed(7)


def write_ogg(name, samples, loop=False):
    os.makedirs(AUDIO, exist_ok=True)
    if loop:
        n = len(samples) - SR
        cf = SR
        for i in range(cf):
            t = i / cf
            samples[i] = samples[i] * t + samples[n + i] * (1 - t)
        samples = samples[:n]
    peak = max(1e-6, max(abs(v) for v in samples))
    scale = 0.85 / peak
    data = array.array("h", (int(max(-1, min(1, v * scale)) * 32767) for v in samples))
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
        wav_path = f.name
    with wave.open(wav_path, "wb") as w:
        w.setparams((1, 2, SR, len(data), "NONE", "not compressed"))
        w.writeframes(data.tobytes())
    subprocess.run(
        ["ffmpeg", "-y", "-loglevel", "error", "-i", wav_path,
         "-c:a", "libvorbis", "-q:a", "4", os.path.join(AUDIO, name)],
        check=True,
    )
    os.unlink(wav_path)
    print("wrote", name)


def seconds(d):
    return int(d * SR)


def silence(d):
    return [0.0] * seconds(d)


def sine(t, f):
    return math.sin(2 * math.pi * f * t)


def square(t, f):
    return 1.0 if sine(t, f) >= 0 else -1.0


def saw(t, f):
    return 2 * ((t * f) % 1) - 1


def thump(t, f=52, decay=9):
    if t < 0:
        return 0.0
    return math.exp(-decay * t) * sine(t, f) + 0.3 * math.exp(-40 * t) * random.uniform(-1, 1)


# ---------------------------------------------------------------- music

def rain_synth_drone():
    n = seconds(25)
    out = []
    brown = 0.0
    for i in range(n):
        t = i / SR
        white = random.uniform(-1, 1)
        brown = (brown + 0.02 * white) / 1.02
        rainv = white * 0.10 + brown * 0.9
        drone = 0.16 * sine(t, 55) + 0.07 * sine(t, 110.3) + 0.03 * sine(t, 220.7)
        hum = 0.02 * square(t, 120) * (0.5 + 0.5 * sine(t, 0.23))
        out.append(rainv * 0.5 + drone + hum)
    return out


def cello_noir_tension():
    n = seconds(25)
    out = []
    for i in range(n):
        t = i / SR
        trem = 0.6 + 0.4 * sine(t, 5.2)
        bow = 0.0
        for f, a in ((110.0, 0.22), (164.81, 0.14), (220.0, 0.08), (329.63, 0.04)):
            bow += a * (saw(t, f) * 0.5 + sine(t, f) * 0.5) * (0.8 + 0.2 * sine(t, 0.31 + f))
        out.append(bow * trem + 0.03 * random.uniform(-1, 1))
    return out


def industrial_heartbeat():
    n = seconds(21)
    out = silence(21)
    beat = 0.95
    k = 0
    while k * beat < 20:
        t0 = k * beat
        for off, amp in ((0.0, 0.8), (0.28, 0.5)):
            start = seconds(t0 + off)
            for j in range(seconds(0.5)):
                idx = start + j
                if idx < n:
                    out[idx] += amp * thump(j / SR)
        # metallic tick
        start = seconds(t0 + 0.5)
        for j in range(seconds(0.2)):
            idx = start + j
            if idx < n:
                out[idx] += 0.12 * math.exp(-30 * j / SR) * sine(j / SR, 1200)
        k += 1
    for i in range(n):
        out[i] += 0.05 * sine(i / SR, 41)
    return out


def dark_synth_climax():
    n = seconds(25)
    out = []
    for i in range(n):
        t = i / SR
        pad = sum(0.09 * sine(t, f + 0.3 * sine(t, 0.5)) for f in (55, 82.41, 110, 130.81))
        pulse = 0.22 * saw(t, 55) * max(0.0, sine(t, 2.0)) ** 2
        air = 0.02 * random.uniform(-1, 1)
        out.append(pad + pulse + air)
    return out


def industrial_slaughter():
    n = seconds(21)
    out = []
    for i in range(n):
        t = i / SR
        p = max(0.0, sine(t, 1.75)) ** 4
        bass = 0.35 * math.tanh(2.5 * saw(t, 55)) * p
        hit = 0.2 * math.exp(-18 * ((t % 0.5714))) * random.uniform(-1, 1)
        screech = 0.05 * sine(t, 880 + 200 * sine(t, 6)) * (0.5 + 0.5 * sine(t, 0.9))
        out.append(bass + hit + screech)
    return out


# ---------------------------------------------------------------- sfx

def metal_door_creak():
    n = seconds(2.2)
    out = []
    for i in range(n):
        t = i / SR
        f = 300 - 220 * (t / 2.2) + 30 * sine(t, 13)
        groan = 0.3 * sine(t, f) * (0.4 + 0.6 * abs(sine(t, 7))) * min(1, t * 4)
        scrape = 0.12 * random.uniform(-1, 1) * (0.5 + 0.5 * sine(t, 23))
        clunk = 0.5 * thump(t - 1.8, 70, 14) if t > 1.8 else 0.0
        out.append(groan + scrape + clunk)
    return out


def ui_error_buzz():
    n = seconds(0.7)
    out = []
    for i in range(n):
        t = i / SR
        gate = 1.0 if (t < 0.22 or 0.32 < t < 0.62) else 0.0
        out.append(0.4 * gate * (square(t, 120) * 0.6 + square(t, 240) * 0.4))
    return out


def glass_shatter_breach():
    n = seconds(1.6)
    out = []
    pings = [(random.uniform(1800, 5200), random.uniform(0.02, 0.5), random.uniform(6, 18)) for _ in range(14)]
    for i in range(n):
        t = i / SR
        burst = 0.5 * random.uniform(-1, 1) * math.exp(-9 * t)
        high = burst * (0.5 + 0.5 * square(t, 3000))
        ping = sum(0.08 * math.exp(-d * (t - s)) * sine(t - s, f) for f, s, d in pings if t > s)
        thud = 0.4 * thump(t, 60, 12)
        out.append(high + ping + thud)
    return out


def heartbeat_stop():
    n = seconds(2.6)
    out = silence(2.6)
    for t0, amp in ((0.0, 0.8), (0.7, 0.55)):
        start = seconds(t0)
        for j in range(seconds(0.6)):
            out[start + j] += amp * thump(j / SR)
    for i in range(seconds(1.5), n):
        t = (i - seconds(1.5)) / SR
        out[i] += 0.12 * min(1, t * 3) * sine(t, 880)
    return out


def siren_glitch_overload():
    n = seconds(3.0)
    out = []
    for i in range(n):
        t = i / SR
        f = 620 if int(t * 2.4) % 2 == 0 else 830
        stutter = 0.0 if (int(t * 16) % 7 == 0) else 1.0
        sir = 0.25 * sine(t, f) * stutter
        rise = 0.1 * random.uniform(-1, 1) * (t / 3.0)
        out.append(sir + rise)
    return out


def revolver_shot_echo():
    n = seconds(2.2)
    out = []
    for i in range(n):
        t = i / SR
        crack = 0.9 * random.uniform(-1, 1) * math.exp(-60 * t)
        boom = 0.6 * thump(t, 75, 10)
        echo = 0.0
        for k, amp in ((0.24, 0.3), (0.5, 0.16), (0.8, 0.08)):
            if t > k:
                echo += amp * random.uniform(-1, 1) * math.exp(-25 * (t - k))
        out.append(crack + boom + echo)
    return out


def glass_explosion():
    n = seconds(2.8)
    out = []
    pings = [(random.uniform(1500, 6000), random.uniform(0.0, 0.7), random.uniform(4, 14)) for _ in range(22)]
    for i in range(n):
        t = i / SR
        burst = 0.7 * random.uniform(-1, 1) * math.exp(-6 * t)
        rumble = 0.4 * thump(t, 45, 4)
        water = 0.12 * random.uniform(-1, 1) * max(0.0, 1 - abs(t - 1.4))
        ping = sum(0.06 * math.exp(-d * (t - s)) * sine(t - s, f) for f, s, d in pings if t > s)
        out.append(burst + rumble + water + ping)
    return out


def main():
    write_ogg("rain_synth_drone.ogg", rain_synth_drone(), loop=True)
    write_ogg("cello_noir_tension.ogg", cello_noir_tension(), loop=True)
    write_ogg("industrial_heartbeat.ogg", industrial_heartbeat(), loop=True)
    write_ogg("dark_synth_climax.ogg", dark_synth_climax(), loop=True)
    write_ogg("industrial_slaughter.ogg", industrial_slaughter(), loop=True)
    write_ogg("metal_door_creak.ogg", metal_door_creak())
    write_ogg("ui_error_buzz.ogg", ui_error_buzz())
    write_ogg("glass_shatter_breach.ogg", glass_shatter_breach())
    write_ogg("heartbeat_stop.ogg", heartbeat_stop())
    write_ogg("siren_glitch_overload.ogg", siren_glitch_overload())
    write_ogg("revolver_shot_echo.ogg", revolver_shot_echo())
    write_ogg("glass_explosion.ogg", glass_explosion())
    print("Audio placeholders generated.")


if __name__ == "__main__":
    main()