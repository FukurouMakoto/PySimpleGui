import PySimpleGUI as sg


def main():
	layout = [
		[sg.Text("Text", enable_events = True, key = '-TEXT-'), sg.Spin(['item 1', 'item 2'])],
		[sg.Button("Button")],
		[sg.Input(key = '-INPUT-')],
		[sg.Text("Hello"), sg.Button("Test Button")]
	]

	window = sg.Window('Converter', layout)

	while True:

		event, values = window.read()
	
		if event == sg.WIN_CLOSED:
			break

		if event == 'Button':
			window['-TEXT-'].update(values['-INPUT-'])

		if event == 'Test Button':
			print('Test button pressed')

		if event == '-TEXT-':
			print('Text was pressed')

	window.close()

if __name__ == "__main__":
	main()

