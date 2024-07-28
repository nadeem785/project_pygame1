import PySimpleGUI as sg
layout=[
[
sg.Input(key="input")
,sg.Spin(["min to sec","km to mile","dicmil to square ft"],key="unit")
,sg.Button("converter",key="button1")
]
,
[sg.Text(key='output')]
]
window=sg.Window("my converter",layout)
while True:
	event ,value=window.read()
	if event==sg.WIN_CLOSED:
		break
	if event=="button1":
		input_val=value["input"]
		if input_val.isnumeric():
			match value['unit']:
				case "min to sec":
					output_val=float(input_val)
					output=output_val*60
					val_=f"the value of {input_val} min  is {output} in sec"
				case "km to mile":
					output_val=float(input_val)
					output=round(output_val*0.6214,2)
					val_=f"the value of {input_val} km  is {output} in mil"
				case "dicmil to square ft":
					output_val=float(input_val)
					output=round(output_val*435.56,2)
					val_=f"the value of {input_val} dicmil  is {output} in sq ft"
			window['output'].update(val_)
		else:

		    window["output"].update("please enter the numeric value")
window.close()
