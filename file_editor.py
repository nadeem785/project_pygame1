import PySimpleGUI as sg
from pathlib import Path 
smiley=['happy',[':)','xD',':D','<3'],'sad',[':(','T_T'],'other',[':3']]
smiley_events=smiley[1]+smiley[3]+smiley[5]
menu_lay=[
['file',['open','New','save','----','exit']],
['Tools',['word_Count']],
['Add',[smiley]]
]

layout=[
[sg.Menu(menu_lay)],
[sg.Text("Untitle",key="docname")],
[sg.Multiline(no_scrollbar=True,size=(80,30),key='box')]

]
window=sg.Window("file_creator",layout)

while True:
	event,value =window.read()
	if event==sg.WIN_CLOSED:
		break

	if event=='word_Count':
		final=value['box'].replace('n','').split()
		sg.popup(len(final))

	if event in smiley_events:
		final=value['box']+" "+ event
		window['box'].update(final)
		
	if event=="open":
		file_path=sg.popup_get_file('open',no_window=True)
		if file_path:
			file=Path(file_path)
			window['box'].update(file.read_text())
			window['docname'].update(file_path.split('/')[-1])
	if event=='save':
		file_path=sg.popup_get_file("save as",no_window=True,save_as=True)+".txt"
		file=Path(file_path)
		file.write_text(value['box'])
		window['docname'].update(file_path.split('/')[-1])

			





	
window.close()

