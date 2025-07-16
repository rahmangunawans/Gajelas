import flet as ft
import sys
import os

def main(page: ft.Page):
    print("Page initialized successfully")
    
    page.title = "ATV Debug Test"
    page.window_width = 375
    page.window_height = 812
    page.bgcolor = "#0a0a1a"
    page.theme_mode = ft.ThemeMode.DARK
    
    try:
        # Simple test content
        content = ft.Column([
            ft.Container(height=100),
            ft.Icon(ft.Icons.CHECK_CIRCLE, size=60, color=ft.Colors.GREEN),
            ft.Text("ATV App Working!", size=24, color=ft.Colors.WHITE),
            ft.Text("Migration Successful", size=16, color=ft.Colors.GREEN),
            ft.ElevatedButton(
                "Continue to App",
                on_click=lambda e: print("Button clicked!"),
                bgcolor=ft.Colors.BLUE,
                color=ft.Colors.WHITE
            )
        ], 
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
        
        page.add(content)
        page.update()
        print("Content added successfully")
        
    except Exception as e:
        print(f"Error in main: {e}")
        page.add(ft.Text(f"Error: {e}", color=ft.Colors.RED))
        page.update()

if __name__ == "__main__":
    print("Starting debug app...")
    ft.app(target=main, port=5000, host="0.0.0.0", view=ft.AppView.WEB_BROWSER)