import flet as ft

def main(page: ft.Page):
    page.title = "Calculator"
    page.scroll= "adaptive"   

 
    
    width = ft.TextField(value="", text_align=ft.TextAlign.RIGHT, width=100)
    height = ft.TextField(value="", text_align=ft.TextAlign.RIGHT, width=100)
    
    resWidth = ft.TextField(value="", text_align=ft.TextAlign.RIGHT, width=100)
    resHeight = ft.TextField(value="", text_align=ft.TextAlign.RIGHT, width=100)
    viwer = ft.Row()
    
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
        ft.Row(
            [
                ft.Text("Enter Width:", size=22),
                width,
            ], 
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [
                ft.Text("Enter Height:", size=22),
                height,
                
            ], 
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [
                ft.Text("New Width", size=22),
                resWidth,
            ], 
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [
                ft.Text("New Height", size=22),
                resHeight,
            ], 
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [
                ft.ElevatedButton(text="Clear", on_click= clear_text),
                ft.ElevatedButton(text="Calculate", on_click=calculate),

            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        viwer
    )

ft.app(target=main)