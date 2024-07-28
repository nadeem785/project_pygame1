import PySimpleGUI as sg
'''
layout=[
[sg.Input(key="input"),
sg.Spin(("kg to grm","km to m","inch to cm"),key="units"),
sg.Button("convert",key="convert",expand_x=True)
],
[sg.Text("output",key="output")]
]
window=sg.Window("converter",layout)
while True:
	events,value=window.read()
	if events==sg.WIN_CLOSED:
		break
	if events=="convert":
		if value['input'].isnumeric():
			match value['units']:
				case 'km to m':
					val=float(value['input'])
					output=round(val*1000,2)
					output_string=(f"the value of {val} km in meters is {output}")
				case 'kg to grm':
					val=float(value['input'])
					output=round(val*1000,2)
					output_string=(f"the value of {val} kg in grams is {output}")
				case 'inch to cm':
					val=float(value['input'])
					output=round(val*2.54,2)
					output_string=(f"the value of {val} inch in cm is {output}")					

			window['output'].update(output_string)




window.close()

def design(theme):
	sg.theme(theme)
	button_size=(6,3)
	sg.set_options(font="Franklin 14",button_element_size=(6,2))
	layout=[

	[sg.Text("output",
		font="calibri 26",
		justification="right",
		right_click_menu=theme_menu,
		expand_x=True, 
	pad=(6,10),
	key="text")],
	[sg.Button("clear",expand_x=True),sg.Button("enter",expand_x=True)],
	[sg.Button(7,size=button_size),sg.Button(8,size=button_size),sg.Button(9,size=button_size),sg.Button("*",size=button_size)],
	[sg.Button(4,size=button_size),sg.Button(5,size=button_size),sg.Button(6,size =button_size),sg.Button("/",size=button_size)],
	[sg.Button(1,size=button_size),sg.Button(2,size=button_size),sg.Button(3,size=button_size),sg.Button("-",size=button_size)],
	[sg.Button(0,expand_x=True),sg.Button(".",expand_x=True),sg.Button("+",size=(5,2))]
	]
	return sg.Window("calci",layout)
theme_menu=["menu",["dark",'Tan','Reddit','SandyBeach',"fanlj"]]
window=design("matt") 
curr_list=[]
full_operation=[]
while True:
	events,value=window.read()
	if events==sg.WIN_CLOSED:
		break
	if events in theme_menu[1]:
		window.close()
		theme=events
		window=design(theme)
	if events in ["1","2","3","4","5","6","7","8","9","0",'.']:
		curr_list.append(events)
		num_val="".join(curr_list)
		window['text'].update(num_val)
	if events in ['*','/','+','-']:
		full_operation.append(num_val)
		
		curr_list=[]
		full_operation.append(events)
		window['text'].update(' ')
	if events=="enter":
		full_operation.append("".join(curr_list))
		result=eval(''.join(full_operation))

		window['text'].update(result)
	if events=="clear":
		curr_list=[]
		full_operation=[]
		window['text'].update(" ")
window.close()

layout=[

[sg.Input(key="input"),
sg.Spin(("kg to gram","cm to_m"),key='unit'),
sg.Button('converter',key="convert")],

[sg.Text("output",key="out")]
]
window=sg.Window("my app",layout)
while True:
	event,value = window.read()
	if event== sg.WIN_CLOSED:
		break
	
	if event=='convert':
		if value["input"].isnumeric():
			match value["unit"]:
				case "kg to gram":
					val=float(value['input'])
					res=val*1000
					output=f"the value of {val} kg in  grm is {res}"
				case "cm to_m":
					val=float(value['input'])
					res=val*1000
					output=f"the value of {val} centimeter in  meter is {res}"
			window['out'].update(output)
'''
smiley=['happy',[':)'],"sad",[":("],"other",["* ^ *"]]
smiley_events=smiley[1]+smiley[3]+smiley[5]
menu_lay=[
["file",["open","save","exit"]],
["tool",["word_count"]],
["add",[smiley]]
]
layout=[
[sg.Menu(menu_lay)],
[sg.Text("Untitle",key="docname")],2
[sg.Multiline("input")]

]
window=sg.Window("file_creator",layout)
while True:
	event,value=window.read()
	if event == sg.WIN_CLOSED:
		break







window.close()




