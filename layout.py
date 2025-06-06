import PySimpleGUI as sg

ddlist = ["Bengalur", "Mysore", "Chikkamagalur", "Udupi" ]
RJList1 = ['Rj Rachana', 'Rj Smitha Dixit']
RJList2=['RJ Lavanya','RJ Sudhesh']
RJList3=['RJ Games Bond','RJ Rashmi']
RJList4=['Rj Aishwarya','Rj Malavika Avinash']

layout = [[sg.T("select the district")],
          [sg.Radio("Bengalur",key='-BANG-',group_id=1,enable_events=True),sg.Radio("Mysore",key='-MYS-',group_id=1,enable_events=True),
           sg.Radio("Chikkamagalur", key='-CKM-',group_id=1,enable_events=True),sg.Radio("Udupi",key='-UDP-',group_id=1,enable_events=True)],
          [sg.T('',key="-RJ-")],
          [sg.LB(RJList1,key="-LBOX1-",visible=False)],
          [sg.LB(RJList2,key="-LBOX2-",visible=False)],
          [sg.LB(RJList3,key="-LBOX3-",visible=False)],
          [sg.LB(RJList4,key="-LBOX4-",visible=False)],
          [sg.Ok(),sg.Cancel()]

 ]
window = sg.Window("Music Station",layout)
while True:
    events, values = window.read()
    if events == "Cancel" or events == sg.WIN_CLOSED:
        window.close()
        break
    elif events == "-BANG-":
        window["-RJ-"].update(visible=True)
        window["-LBOX1-"].update(visible=True)
    elif events == "-MYS-":
        window["-RJ-"].update(visible=True)
        window["-LBOX2-"].update(visible=True)
    elif events == "-UDP-":
        window["-RJ-"].update(visible=True)
        window["-LBOX4-"].update(visible=True)
    elif events == "-CKM-":
        window["-RJ-"].update(visible=True)
        window["-LBOX3-"].update(visible=True)

    print(events,values)