import flet as ft
import time
import threading

def main(page: ft.Page):
    """Test percentage display fix"""
    page.title = "Test Percentage"
    page.window_width = 375
    page.window_height = 812
    page.bgcolor = "#0a0a1a"
    
    # Create progress bar with percentage
    progress_bar = ft.Container(
        content=ft.Column([
            # Progress bar
            ft.Container(
                content=ft.ProgressBar(
                    width=220,
                    height=6,
                    color="#06b6d4",
                    bgcolor="#1e293b",
                    value=0,
                ),
                border_radius=3,
            ),
            # Animated loading dots
            ft.Container(
                content=ft.Row([
                    ft.Container(
                        width=8,
                        height=8,
                        bgcolor="#06b6d4",
                        border_radius=4,
                        opacity=0.3,
                    ),
                    ft.Container(
                        width=8,
                        height=8,
                        bgcolor="#06b6d4",
                        border_radius=4,
                        opacity=0.3,
                    ),
                    ft.Container(
                        width=8,
                        height=8,
                        bgcolor="#06b6d4",
                        border_radius=4,
                        opacity=0.3,
                    ),
                ],
                spacing=12,
                alignment=ft.MainAxisAlignment.CENTER,
                ),
                padding=ft.padding.only(top=20),
            ),
            # Progress percentage
            ft.Container(
                content=ft.Text(
                    "0%",
                    size=12,
                    color="#06b6d4",
                    text_align=ft.TextAlign.CENTER,
                    weight=ft.FontWeight.W_600,
                ),
                padding=ft.padding.only(top=10),
            ),
        ],
        spacing=0,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        opacity=1,
    )
    
    # Add components to page
    page.add(
        ft.Container(
            content=ft.Column([
                ft.Container(height=200),
                ft.Text("ATV", size=48, color="#ffffff", weight=ft.FontWeight.BOLD),
                ft.Container(height=50),
                progress_bar,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            expand=True,
            alignment=ft.alignment.center,
        )
    )
    
    # Start animation
    def animate():
        try:
            progress_bar_control = progress_bar.content.controls[0].content
            percentage_text = progress_bar.content.controls[2].content
            
            for i in range(0, 101, 5):
                progress_bar_control.value = i / 100
                percentage_text.value = f"{i}%"
                page.update()
                time.sleep(0.1)
                
            page.add(ft.Text("Animation Complete!", color="#10b981", size=16))
            page.update()
            
        except Exception as e:
            page.add(ft.Text(f"Error: {e}", color="#ef4444", size=12))
            page.update()
    
    # Start animation in thread
    thread = threading.Thread(target=animate)
    thread.daemon = True
    thread.start()

if __name__ == "__main__":
    ft.app(target=main, port=5001, host="0.0.0.0", view=ft.AppView.WEB_BROWSER)