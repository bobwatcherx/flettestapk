from flet import *

def main(page:Page):
	page.theme_mode = ThemeMode.LIGHT
	page.appbar = AppBar(
		title=Text("hello youtube",color="white"),
		bgcolor="blue"
		)
	page.add(
		Column([
			Text("hello"),
			ElevatedButton("test123",bgcolor="blue",color="white")
			])
		)

app(main)
