import PySimpleGUI as sg
from os import listdir
from os.path import isfile, join
import definitions

SUDOKUPATH = "/Users/tacobakker/PycharmProjects/sudoku/puzzels/"


def schowtheinput():
    result = False
    inhoud = []
    sudokufiles = [f for f in listdir(SUDOKUPATH) if isfile(join(SUDOKUPATH, f))]
    for sudokuFile in sudokufiles:
        inhoud = definitions.leesCSV(SUDOKUPATH + sudokuFile)

    sg.theme("DarkBlue3")
    sg.set_options(font=("Courier New", 24))

    layout = [[sg.Listbox(inhoud, size=(40, 30))],
              [sg.Button('Goed', size=(5, 1), font='Courier 16'), sg.Button('Fout', size=(5, 1), font='Courier 16')]
              ]

    window = sg.Window('Input van de calcudoku', layout)
    event, values = window.read()
    window.close()

    if event == "Goed":
        result = True
    return result


