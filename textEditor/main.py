import PySimpleGUI as sg

def get_window():
	TITLE = 'Text Editor'
	SMILEYS = [
			'happy', [
				':)',
				'xD',
				':D',
				'<3'
			],

			'sad', [
				':(', 
				'T_T'
			],

			'other', [
				':3'
			]
		]
			
	MENU_LAYOUT = [
		[
			'File', [
				'Open', 
				'Save', 
				'---', 
				'Exit'
			]
		],
		[
			'Tools', [
				'Word Count'
			]
		],
		[
			'Add', SMILEYS
		]
	]
	LAYOUT = [
		[
			sg.Menu(MENU_LAYOUT)
		],
		[
			sg.Text('Untitled', key = '-DOCNAME-')
		],
		[
			sg.Multiline()
		]
	]
	window = sg.Window(TITLE, LAYOUT)

	return window

def main():

	window = get_window()

	while True:
		event, values = window.read()

		if event == sg.WIN_CLOSED:
			break


		window.close()


if __name__ == "__main__":
	main()

