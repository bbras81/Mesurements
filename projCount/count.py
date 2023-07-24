import flet as ft

def main(page: ft.Page):
    page.title = "Calculator"

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
    row_01 = ft.Row([enter_width, width])
    enter_height = ft.Text("Enter Height:", size=22)
    height = ft.TextField(value="", text_align=ft.TextAlign.RIGHT, width=100)
    row_02 = ft.Row([enter_height, height])
    enter_new_width = ft.Text("New Width", size=22)
    resWidth = ft.TextField(value="", text_align=ft.TextAlign.RIGHT, width=100)
    row_03 = ft.Row([enter_new_width, resWidth])
    enter_new_height = ft.Text("New Width", size=22)
    resHeight = ft.TextField(value="", text_align=ft.TextAlign.RIGHT, width=100)
    row_04 = ft.Row([enter_new_height, resHeight])
    viwer = ft.Row()
    container = ft.Column([row_01, row_02, row_03, row_04])
    
    data_container = ft.Container(
        content= container,
        width= 750,
        height= 500,
        bgcolor="#4d4d4d",
        border_radius=30,
        padding=20,
    )
    
    
    
    
    
    
    
    def clear_text(e):
        width.value=""
        height.value=""
        resHeight.value=""
        resWidth.value=""
        viwer.clean()
        page.update()
        
    
    
    def calculate(e):
        if resHeight.value == "":
            result = str(int(height.value) * int(resWidth.value) / int(width.value))
            viwer.controls.append(ft.Text(f"Result: {result}", text_align=ft.TextAlign.CENTER))
            page.update()
            
        elif resWidth.value == "":
            result = str(int(width.value) * int(resHeight.value) / int(height.value))
            viwer.controls.append(ft.Text(f"Result: {result}"))
            page.update()
            
    
    page.add(
        app_title,
        data_container,
        ft.Row(
            [
                ft.ElevatedButton(text="Clear", on_click= clear_text),
                ft.ElevatedButton(text="Calculate", on_click=calculate),

            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        viwer
    )

ft.app(target=main, assets_dir="assets")