import PySimpleGUI as sg


def getPuzzelGui(size):
    if size == 4:
        return getPuzzelGui4()
    if size == 5:
        return getPuzzelGui5()
    if size == 6:
        return getPuzzelGui6()
    return 0


def getPuzzelGui6():
    result = ""
    sg.theme('SandyBeach')
    layout = [
        [sg.Text('Vul de puzzel in', font='Courier 32')],
        [sg.InputText(size=(5, 2), font='Courier 32'),
         sg.InputText(size=(5, 2), font='Courier 32'),
         sg.InputText(size=(5, 2), font='Courier 32'),
         sg.InputText(size=(5, 2), font='Courier 32'),
         sg.InputText(size=(5, 2), font='Courier 32'),
         sg.InputText(size=(5, 2), font='Courier 32')
         ],
        [sg.InputText(size=(5, 2), font='Courier 32'),
         sg.InputText(size=(5, 2), font='Courier 32'),
         sg.InputText(size=(5, 2), font='Courier 32'),
         sg.InputText(size=(5, 2), font='Courier 32'),
         sg.InputText(size=(5, 2), font='Courier 32'),
         sg.InputText(size=(5, 2), font='Courier 32')
         ],
        [sg.InputText(size=(5, 2), font='Courier 32'),
         sg.InputText(size=(5, 2), font='Courier 32'),
         sg.InputText(size=(5, 2), font='Courier 32'),
         sg.InputText(size=(5, 2), font='Courier 32'),
         sg.InputText(size=(5, 2), font='Courier 32'),
         sg.InputText(size=(5, 2), font='Courier 32')
         ],
        [sg.InputText(size=(5, 2), font='Courier 32'),
         sg.InputText(size=(5, 2), font='Courier 32'),
         sg.InputText(size=(5, 2), font='Courier 32'),
         sg.InputText(size=(5, 2), font='Courier 32'),
         sg.InputText(size=(5, 2), font='Courier 32'),
         sg.InputText(size=(5, 2), font='Courier 32')
         ],
        [sg.InputText(size=(5, 2), font='Courier 32'),
         sg.InputText(size=(5, 2), font='Courier 32'),
         sg.InputText(size=(5, 2), font='Courier 32'),
         sg.InputText(size=(5, 2), font='Courier 32'),
         sg.InputText(size=(5, 2), font='Courier 32'),
         sg.InputText(size=(5, 2), font='Courier 32')
         ],
        [sg.InputText(size=(5, 2), font='Courier 32'),
         sg.InputText(size=(5, 2), font='Courier 32'),
         sg.InputText(size=(5, 2), font='Courier 32'),
         sg.InputText(size=(5, 2), font='Courier 32'),
         sg.InputText(size=(5, 2), font='Courier 32'),
         sg.InputText(size=(5, 2), font='Courier 32')
         ],
        [sg.Button('Lezen', size=(5, 1), font='Courier 16'), sg.Button('Stop', size=(5, 1), font='Courier 16')]
    ]

    window = sg.Window('Oplossen van de Calcudoku', layout)
    event, values = window.read()
    window.close()

    if event == "Lezen":
        result = []
        tmp = ""
        for x in range(0, 35, 6):
            for y in range(0, 6):
                #print("klopt de index?", x+y)
                tmp+=values[x+y]
            result.append(tmp)
            tmp = ""


        for q in result:
            print(q)

    return result

def getPuzzelGui5():
    result = ""
    sg.theme('SandyBeach')
    layout = [
        [sg.Text('Vul de puzzel in', font='Courier 32')],
        [sg.InputText(size=(5, 2), font='Courier 32'),
         sg.InputText(size=(5, 2), font='Courier 32'),
         sg.InputText(size=(5, 2), font='Courier 32'),
         sg.InputText(size=(5, 2), font='Courier 32'),
         sg.InputText(size=(5, 2), font='Courier 32'),
         ],
        [sg.InputText(size=(5, 2), font='Courier 32'),
         sg.InputText(size=(5, 2), font='Courier 32'),
         sg.InputText(size=(5, 2), font='Courier 32'),
         sg.InputText(size=(5, 2), font='Courier 32'),
         sg.InputText(size=(5, 2), font='Courier 32'),
         ],
        [sg.InputText(size=(5, 2), font='Courier 32'),
         sg.InputText(size=(5, 2), font='Courier 32'),
         sg.InputText(size=(5, 2), font='Courier 32'),
         sg.InputText(size=(5, 2), font='Courier 32'),
         sg.InputText(size=(5, 2), font='Courier 32'),
         ],
        [sg.InputText(size=(5, 2), font='Courier 32'),
         sg.InputText(size=(5, 2), font='Courier 32'),
         sg.InputText(size=(5, 2), font='Courier 32'),
         sg.InputText(size=(5, 2), font='Courier 32'),
         sg.InputText(size=(5, 2), font='Courier 32'),
         ],
        [sg.InputText(size=(5, 2), font='Courier 32'),
         sg.InputText(size=(5, 2), font='Courier 32'),
         sg.InputText(size=(5, 2), font='Courier 32'),
         sg.InputText(size=(5, 2), font='Courier 32'),
         sg.InputText(size=(5, 2), font='Courier 32'),
         ],

        [sg.Button('Lezen', size=(5, 1), font='Courier 16'), sg.Button('Stop', size=(5, 1), font='Courier 16')]
    ]

    window = sg.Window('Oplossen van de Calcudoku', layout)
    event, values = window.read()
    window.close()

    if event == "Lezen":
        result = []
        tmp = ""
        for x in range(0, 24, 5):
            for y in range(0, 5):
                #print("klopt de index?", x+y)
                tmp+=values[x+y]
            result.append(tmp)
            tmp = ""


        for q in result:
            print(q)

    return result


def getPuzzelGui4():
    result = ""
    sg.theme('SandyBeach')
    layout = [
        [sg.Text('Vul de puzzel in', font='Courier 32')],
        [sg.InputText(size=(5, 2), font='Courier 32'),
         sg.InputText(size=(5, 2), font='Courier 32'),
         sg.InputText(size=(5, 2), font='Courier 32'),
         sg.InputText(size=(5, 2), font='Courier 32')
         ],
        [sg.InputText(size=(5, 2), font='Courier 32'),
         sg.InputText(size=(5, 2), font='Courier 32'),
         sg.InputText(size=(5, 2), font='Courier 32'),
         sg.InputText(size=(5, 2), font='Courier 32')
         ],
        [sg.InputText(size=(5, 2), font='Courier 32'),
         sg.InputText(size=(5, 2), font='Courier 32'),
         sg.InputText(size=(5, 2), font='Courier 32'),
         sg.InputText(size=(5, 2), font='Courier 32')
         ],
        [sg.InputText(size=(5, 2), font='Courier 32'),
         sg.InputText(size=(5, 2), font='Courier 32'),
         sg.InputText(size=(5, 2), font='Courier 32'),
         sg.InputText(size=(5, 2), font='Courier 32')
         ],

        [sg.Button('Lezen', size=(4, 1), font='Courier 16'), sg.Button('Stop', size=(4, 1), font='Courier 16')]
    ]

    window = sg.Window('Oplossen van de Calcudoku', layout)
    event, values = window.read()
    window.close()

    if event == "Lezen":
        result = []
        tmp = ""
        for x in range(0, 15, 4):
            for y in range(0, 4):
                #print("klopt de index?", x+y)
                tmp+=values[x+y]
            result.append(tmp)
            tmp = ""


        for q in result:
            print(q)

    return result