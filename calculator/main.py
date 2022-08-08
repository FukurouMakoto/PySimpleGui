import PySimpleGUI as sg
	 
def get_layout(theme, theme_menu):

	FONT = "Franklin 14"
	BUTTON_SIZE = (6, 3)
	PADDING = (10, 20)
	sg.theme(theme)
	sg.set_options(font = FONT)

	layout = [
		#[
			#sg.Text('Output', 
			#font = 'Franklin 26', 
			#justification = 'right',
			#expand_x = True)
		#],
		[
			sg.Push(),
			sg.Text('', 
			key = '-OUTPUT-',
			font = 'Franklin 26',
			pad = PADDING,
			right_click_menu = theme_menu)
		],

		[
			sg.Button('Enter', expand_x = True),
			sg.Button('Clear', expand_x = True),
		],
		[
			sg.Button('7', size = BUTTON_SIZE),
			sg.Button('8', size = BUTTON_SIZE),
			sg.Button('9', size = BUTTON_SIZE),
			sg.Button('/'),
		],
		[
			sg.Button('4', size = BUTTON_SIZE),
			sg.Button('5', size = BUTTON_SIZE),
			sg.Button('6', size = BUTTON_SIZE),
			sg.Button('*'),
		],
		[
			sg.Button('1', size = BUTTON_SIZE),
			sg.Button('2', size = BUTTON_SIZE),
			sg.Button('3', size = BUTTON_SIZE),
			sg.Button('-'),
		],
		[
			sg.Button('0', expand_x = True),
			sg.Button('.'),
			sg.Button('+'),
		],
	]

	return layout

def main():
	title = 'Calculator'
	theme_menu = [  #Available themes
		'menu', 
		[
			'lightGrey1', 
			'dark', 
			'DarkGray8', 
			'random', 
		]
	]

	current_num = []
	full_operation = []

	window = sg.Window(title, get_layout('dark', theme_menu))

	while True:
		event, values = window.read()

		if event == sg.WIN_CLOSED:
			break

		if event in theme_menu[1]: #Change theme
			window.close()
			window = sg.Window(title, get_layout(event, theme_menu))
		
		digits = [str(i) for i in range(10)]
		digits.append('.')

		if event in digits:
			current_num.append(event)
			window['-OUTPUT-'].update(''.join(current_num))

		if event in ['+', '-', '*', '/']:
			full_operation.append(''.join(current_num))
			current_num = []
			full_operation.append(event)
			window['-OUTPUT-'].update(''.join(''))


		if event == 'Enter':
			full_operation.append(''.join(current_num))
			result = eval(''.join(full_operation))
			window['-OUTPUT-'].update(result)
			full_operation = []
			

		if event == 'Clear':
			current_num = []
			full_operation = []
			window['-OUTPUT-'].update(''.join(current_num))


	window.close()

if __name__ == "__main__":
	main()

