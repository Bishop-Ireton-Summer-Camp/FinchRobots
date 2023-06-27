from BirdBrain import Finch
import time
from enum import Enum

finch = Finch('A')

class Notes(Enum):
    C = 73
    CS = 74
    D = 75
    DS = 76
    E = 77
    F = 78
    FS = 79
    G = 80
    GS = 81
    A = 82
    AS = 83
    B = 84

def note(note, num):
    beats = 5
    finch.playNote(note.value, beats)
    time.sleep(0.25 * num)
    finch.playNote(135, 1)
    time.sleep(0.04)

def mary_had_a_litte_lamb():
    beats = 5
    note(Notes.E, 1)
    note(Notes.D, 1)
    note(Notes.C, 1)
    note(Notes.D, 1)
    note(Notes.E, 1)
    note(Notes.E, 1)
    note(Notes.E, 2)
    note(Notes.D, 1)
    note(Notes.D, 1)
    note(Notes.D, 2)
    note(Notes.E, 1)
    note(Notes.G, 1)
    note(Notes.G, 2)
    note(Notes.E, 1)
    note(Notes.D, 1)
    note(Notes.C, 1)
    note(Notes.D, 1)
    note(Notes.E, 1)
    note(Notes.E, 1)
    note(Notes.E, 1)
    note(Notes.E, 1)
    note(Notes.D, 1)
    note(Notes.D, 1)
    note(Notes.E, 1)
    note(Notes.D, 1)
    note(Notes.C, 2)

mary_had_a_litte_lamb()

finch.stopAll()
