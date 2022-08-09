import PySimpleGUI as sg
from conversions import *

def get_layout():
	x = [
		[
			sg.Input(key = '-INPUT-'), 
			sg.Spin(
			[
				'km to mile',
				'mile to km',
				'meter to ft',
				'ft to meter',
				'sec to min',
				'min to sec',
				'min to hrs',
			],
			key='-CHOICES-',
			), 
			sg.Button("convert", key = '-CONVERT-') 
		],

		[	
			sg.Text("Results", key = '-TEXT-')
		],
		]
	return x

def main():

	layout = get_layout()

	window = sg.Window('Converter', layout)

	while True: 

		event, values = window.read()

		if event == sg.WIN_CLOSED:
			break

		if event == '-CONVERT-':
			if values['-CHOICES-'] == 'km to mile':
				x = km_to_mile(values['-INPUT-'])
				window['-TEXT-'].update(x)
			if values['-CHOICES-'] == 'mile to km':
				x = mile_to_km(values['-INPUT-'])
				window['-TEXT-'].update(x)
			if values['-CHOICES-'] == 'sec to min':
				x = sec_to_min(values['-INPUT-'])
				window['-TEXT-'].update(x)
			if values['-CHOICES-'] == 'min to sec':
				x = min_to_sec(values['-INPUT-'])
				window['-TEXT-'].update(x)
			if values['-CHOICES-'] == 'meter to ft':
				x = meter_to_ft(values['-INPUT-'])
				window['-TEXT-'].update(x)
			if values['-CHOICES-'] == 'ft to meter':
				x = ft_to_meter(values['-INPUT-'])
				window['-TEXT-'].update(x)
			if values['-CHOICES-'] == 'min to hrs':
				x = min_to_hrs(values['-INPUT-'])
				window['-TEXT-'].update(x)

	window.close()
if __name__ == "__main__":
	main()

