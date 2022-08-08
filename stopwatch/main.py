import PySimpleGUI as sg
from time import time 

def get_window():
	THEME = 'black'
	TITLE = 'Stopwatch'
	DIMENSIONS = (300, 300)
	BUTTON_COLOR = "#FF0000",
	BORDER_WIDTH = 0

	sg.theme(THEME)
	LAYOUT = [
	#	[	sg.Push(), 
	#		sg.Image(
	#			'cross.png', 
	#			pad = 0,
	#			enable_events = True, 
	#			key = '-CLOSE-')
	#	],  
		#Cannot use above code because cross.png does not exist
		[sg.VPush()],
		[sg.Text('', 
					font = 'Young 50',
					key = '-TIME-')
		],
		[
			sg.Button('Start', 
						button_color = BUTTON_COLOR, 
						border_width = BORDER_WIDTH,
						key = '-STARTSTOP-'
			),
			sg.Button('Lap', 
						button_color = BUTTON_COLOR,
						border_width = BORDER_WIDTH,
						visible = False,
						key = '-LAP-'
			),
		],
		[sg.VPush()],
		[sg.Column([[]], key = '-LAPS-')],
	]
	
	window = sg.Window(
					TITLE, 
					LAYOUT, 
					size = (DIMENSIONS),
					element_justification = 'center'
					)

	return window

def main():
	window = get_window()
	start_time = 0
	active = False
	lap_amount = 1
	
	while True:
		event, values = window.read(timeout = 10)
		#if event in (sg.WIN_CLOSED, '-CLOSE-'):
		if event == sg.WIN_CLOSED:
			break

		if event == '-STARTSTOP-':
			if active:
				#from active to stop
				active = False
				window['-STARTSTOP-'].update('Reset')
				window['-LAP-'].update(visible = False)
			else:
				#from stop to reset
				if start_time > 0:
					window.close()
					window = get_window()
					start_time = 0
				#from start to active
				else:
					start_time = time()
					active = True
					window['-STARTSTOP-'].update('Stop')
					window['-LAP-'].update(visible = True)

		if active:
			elapsed_time = round(time() - start_time, 1)
			window['-TIME-'].update(elapsed_time)
		
		if event == '-LAP-':
			window.extend_layout(window['-LAPS-'],[
		[
			sg.Text(lap_amount),
			sg.VSeperator(),
			sg.Text(elapsed_time)
		],
		[
		]
	]
)
			lap_amount += 1

	window.close()


if __name__ == "__main__":
	main()

