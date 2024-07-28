import PySimpleGUI as sg
from time import time
def creat_window():
	sg.theme("black")
	layout=[[sg.Push(),sg.Image("cross.png",enable_events=True,key="cross")],
	[sg.VPush()],
	
	[sg.Text("time",font ='young 50 ',key="time")],

	[sg.Button("start", button_color = ('#FFFFFF','#FF0000'),border_width=0,key="stopstart"),
	sg.Button("lap", button_color = ('#FFFFFF','#FF0000'),border_width=0,key="laps",visible=False)],
	[sg.Column([[]],key="lap")],
	[sg.VPush()]]
	return sg.Window("stopwatch",layout,

		size=(300,300),
		no_titlebar=True,
		element_justification="center",

		)
start_time=0
lap_count=1
active=False

window=creat_window()
while True:
	event,value=window.read(timeout=100)
	if event in (sg.WIN_CLOSED ,'cross'):
		break
	if event =='stopstart':
		if active:
			#from active to stop
			active=False
			window['stopstart'].update("reset")
			window['laps'].update(visible=False)

		else:
			#stop to reset
			if start_time>0:
				window.close()
				window=creat_window()
				start_time=0
			else:
				start_time=time()
				active=True
				window['stopstart'].update("stop")
				window['laps'].update(visible=True)
	if active:
		time_elapsed=round(time()-start_time,2)
		window['time'].update(time_elapsed)
	if event=='laps':
		window.extend_layout(window['lap'],[[sg.Text(lap_count),sg.VSeparator(),sg.Text(time_elapsed)]])
		lap_count+=1



window.close()