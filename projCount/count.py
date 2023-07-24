import flet as ft
import keyboard

def main(page: ft.Page):
    page.title = "Calculator"
    page.theme_mode = "dark"
    page.vertical_alignment = "top"
    page.horizontal_alignment = "center"

    page.fonts = {
        "RobotoMono-Regular" : "RobotoMono-Regular.ttf",
        "RobotoMono-Bold" : "RobotoMono-Bold.ttf",  
    }



    app_title = ft.Row(
        [
            ft.Text("Measurement", font_family="RobotoMono-Regular",style="displayLarge")
        ],
        alignment="center"
    )   
    
    enter_width = ft.Text("Enter Width:", size=22)
    width = ft.TextField(value="", text_align=ft.TextAlign.RIGHT, width=100)
    enter_height = ft.Text("Enter Height:", size=22)
    height = ft.TextField(value="", text_align=ft.TextAlign.RIGHT, width=100)
    enter_new_width = ft.Text("New Width:", size=22)
    resWidth = ft.TextField(value="", text_align=ft.TextAlign.RIGHT, width=100)
    enter_new_height = ft.Text("New Height:", size=22)
    resHeight = ft.TextField(value="", text_align=ft.TextAlign.RIGHT, width=100)
    space = ft.Text("")
    viwer = ft.Row()
    col_01 = ft.Column([enter_width,space,enter_height, space, enter_new_width, space, enter_new_height],alignment="letf")
    col_02 = ft.Column([width, height, resWidth, resHeight], alignment="center")
    container = ft.Row([col_01, col_02], alignment="center")
    
    
    data_container = ft.Container(
        content= container,
        width= 750,
        height= 300,
        border_radius=30,
        padding=20,
    )
    
    def clear_text(e):
        width.value = ""
        height.value = ""
        resHeight.value = ""
        resWidth.value = ""
        viwer.controls.clear()
        page.update()
        
    def calculate(e):
        if resHeight.value == "":
            result = str(int(height.value) * int(resWidth.value) / int(width.value))
            viwer.controls.append(ft.Text(f"Result: {result}", size=40, font_family="RobotoMono-Bold"))
            page.update()
            
        elif resWidth.value == "":
            result = str(int(width.value) * int(resHeight.value) / int(height.value))
            viwer.controls.append(ft.Text(f"Result: {result}", size=40, font_family="RobotoMono-Bold"))
            page.update()
            

    page.add(
        app_title,
        data_container,
        ft.Row(
            [
                ft.ElevatedButton(text="Clear", on_click= clear_text),
                ft.ElevatedButton(text="Calculate", on_click=calculate),
            ], alignment="center"
        ), 
        ft.Row(
            [
                viwer
            ], alignment="center"
        )
    )
    keyboard.add_hotkey("return", calculate)

ft.app(target=main, assets_dir="assets")