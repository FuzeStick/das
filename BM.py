import eel
eel.init('web')
@eel.expose
def recv(login,ip):
	print(login,ip)
eel.start("ui.html", size=(700, 700))


