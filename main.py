import PySimpleGUI as sg

rj_info = {
    "Bengalur": [
        {'name': 'Rj Rachana','Show': 'Morning No 1', 'next_event': '25-06-2023 09:00', 'replacement': 'Rj Smitha Dixit'},
        {'name': 'Rj Smitha Dixit', 'Show': 'Rewind Raga', 'next_event': '26-06-2023 11:30', 'replacement': 'Rj Rachana'}
    ],
    "Mysore": [
        {'name': 'RJ Lavanya', 'Show': 'Just Maat Mathali', 'next_event': '24-06-2023 15:00', 'replacement': 'RJ Sudhesh'},
        {'name': 'RJ Sudhesh', 'Show': 'Tropical Beats','next_event': '27-06-2023 10:45', 'replacement': 'RJ Lavanya'}
    ],
    "Chikkamagalur": [
        {'name': 'RJ James Bond', 'Show': 'On The Air','next_event': '25-06-2023 14:30', 'replacement': 'RJ Rashmi'},
        {'name': 'RJ Rashmi', 'Show': 'Mirchi Murga','next_event': '26-06-2023 17:15', 'replacement': 'RJ Games Bond'}
    ],
    "Udupi": [
        {'name': 'Rj Aishwarya', 'Show': 'Influenza','next_event': '27-06-2023 13:45', 'replacement': 'Rj Malavika Avinash'},
        {'name': 'Rj Malavika Avinash', 'Show': 'Akasha Vani','next_event': '26-06-2023 09:30', 'replacement': 'Rj Aishwarya'}
    ]
}

layout = [
    [sg.T("Select the district")],
    [sg.Radio("Bengalur", key='-Bengalur-', group_id=1, enable_events=True),
     sg.Radio("Mysore", key='-Mysore-', group_id=1, enable_events=True),
     sg.Radio("Chikkamagalur", key='-Chikkamagalur-', group_id=1, enable_events=True),
     sg.Radio("Udupi", key='-Udupi-', group_id=1, enable_events=True)],
    [sg.T('', key="-RJ-")],
    [sg.Listbox(values=[], key="-LBOX-", size=(30, 5), visible=False)],
    [sg.T('', key="-EVENT-")],
    [sg.T('', key="-REPLACEMENT-")],
    [sg.T('', key="-SHOW-")],
    [sg.Ok(), sg.Cancel()]
]

window = sg.Window("Music Station", layout)

while True:
    event, values = window.read()

    if event == "Cancel" or event == sg.WINDOW_CLOSED:
        break

    if values["-Bengalur-"]:
        selected_district = "Bengalur"
    elif values["-Mysore-"]:
        selected_district = "Mysore"
    elif values["-Chikkamagalur-"]:
        selected_district = "Chikkamagalur"
    elif values["-Udupi-"]:
        selected_district = "Udupi"
    else:
        selected_district = None

    if selected_district:
        rj_details = rj_info.get(selected_district, [])
        rj_names = [rj['name'] for rj in rj_details]
        window["-RJ-"].update(f"RJs in {selected_district}:")
        window["-LBOX-"].update(values=rj_names, visible=True)
        window["-EVENT-"].update('')
        window["-REPLACEMENT-"].update('')
        window["-SHOW-"].update('')

    if event == "Ok":
        selected_rj_name = values["-LBOX-"][0] if values["-LBOX-"] else None
        if selected_rj_name and selected_district:
            rj = next((rj for rj in rj_info[selected_district] if rj['name'] == selected_rj_name), None)
            if rj:
                window["-EVENT-"].update(f"Next Event: {rj['next_event']}")
                window["-REPLACEMENT-"].update(f"Replacement RJ: {rj['replacement']}")
                window["-SHOW-"].update(f"Show : {rj['Show']}")
            else:
                window["-EVENT-"].update('')
                window["-REPLACEMENT-"].update('')
                window["-SHOW-"].update('')

window.close()