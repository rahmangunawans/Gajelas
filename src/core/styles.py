import flet as ft

class AppStyles:
    """Application styling constants and configurations"""
    
    # Enhanced color palette with gradients
    PRIMARY_COLOR = "#0a0a1a"  # Deep dark background
    SECONDARY_COLOR = "#151528"  # Card background
    ACCENT_COLOR = "#1e3a8a"  # Blue accent
    SUCCESS_COLOR = "#10b981"  # Green success
    WARNING_COLOR = "#f59e0b"  # Yellow warning
    ERROR_COLOR = "#ef4444"  # Red error
    
    # Text colors
    TEXT_PRIMARY = "#ffffff"  # Pure white
    TEXT_SECONDARY = "#06b6d4"  # Cyan accent
    TEXT_TERTIARY = "#94a3b8"  # Gray text
    TEXT_MUTED = "#64748b"  # Muted text
    
    # Gradient colors
    GRADIENT_PRIMARY = ["#1e3a8a", "#3b82f6", "#06b6d4"]
    GRADIENT_SECONDARY = ["#7c3aed", "#a855f7", "#ec4899"]
    GRADIENT_ACCENT = ["#059669", "#10b981", "#34d399"]
    
    # Special colors
    PROGRESS_BG = "#1e293b"
    CARD_BORDER = "#334155"
    INPUT_BORDER = "#475569"
    INPUT_FOCUS = "#06b6d4"
    
    # Animation settings
    FADE_DURATION = 1000
    SLIDE_DURATION = 800
    BOUNCE_DURATION = 600
    
    # Mobile dimensions
    MOBILE_WIDTH = 375
    MOBILE_HEIGHT = 812
    
    # Component spacing
    SPACING_SMALL = 10
    SPACING_MEDIUM = 20
    SPACING_LARGE = 40
    SPACING_XL = 60
    
    # Font sizes
    FONT_LARGE = 32
    FONT_MEDIUM = 18
    FONT_SMALL = 14
    FONT_TINY = 12
    FONT_HERO = 36
    
    @staticmethod
    def get_primary_button_style():
        """Get primary button style with gradient effect"""
        return ft.ButtonStyle(
            color=ft.Colors.WHITE,
            bgcolor=AppStyles.TEXT_SECONDARY,
            padding=ft.padding.symmetric(horizontal=40, vertical=18),
            shape=ft.RoundedRectangleBorder(radius=12),
            shadow_color=ft.Colors.BLACK26,
            elevation=8,
            text_style=ft.TextStyle(
                size=16,
                weight=ft.FontWeight.BOLD,
                letter_spacing=0.5,
            ),
        )
    
    @staticmethod
    def get_secondary_button_style():
        """Get secondary button style"""
        return ft.ButtonStyle(
            color=AppStyles.TEXT_SECONDARY,
            bgcolor=ft.Colors.TRANSPARENT,
            padding=ft.padding.symmetric(horizontal=30, vertical=12),
            shape=ft.RoundedRectangleBorder(radius=8),
            side=ft.BorderSide(width=1, color=AppStyles.TEXT_SECONDARY),
        )
        
    @staticmethod
    def get_card_style():
        """Get enhanced card style with modern shadows"""
        return ft.Container(
            bgcolor=AppStyles.SECONDARY_COLOR,
            border_radius=16,
            padding=25,
            border=ft.border.all(1, AppStyles.CARD_BORDER),
            shadow=ft.BoxShadow(
                spread_radius=0,
                blur_radius=20,
                color=ft.Colors.BLACK26,
                offset=ft.Offset(0, 8),
            ),
        )
        
    @staticmethod
    def get_input_style():
        """Get enhanced input field style"""
        return {
            "border_color": AppStyles.INPUT_BORDER,
            "focused_border_color": AppStyles.INPUT_FOCUS,
            "cursor_color": AppStyles.INPUT_FOCUS,
            "bgcolor": AppStyles.SECONDARY_COLOR,
            "border_radius": 12,
            "content_padding": ft.padding.symmetric(horizontal=16, vertical=14),
            "text_style": ft.TextStyle(
                color=AppStyles.TEXT_PRIMARY,
                size=14,
                weight=ft.FontWeight.W_400,
            ),
            "hint_style": ft.TextStyle(
                color=AppStyles.TEXT_MUTED,
                size=14,
            ),
        }
        
    @staticmethod
    def create_gradient_container(width=None, height=None, colors=None):
        """Create gradient container"""
        if colors is None:
            colors = AppStyles.GRADIENT_PRIMARY
        
        return ft.Container(
            width=width,
            height=height,
            gradient=ft.LinearGradient(
                colors=colors,
                begin=ft.alignment.top_left,
                end=ft.alignment.bottom_right,
            ),
            border_radius=16,
        )
        
    @staticmethod
    def create_glass_effect():
        """Create glass morphism effect"""
        return ft.Container(
            bgcolor=ft.Colors.with_opacity(0.1, ft.Colors.WHITE),
            border_radius=16,
            border=ft.border.all(1, ft.Colors.with_opacity(0.2, ft.Colors.WHITE)),
            shadow=ft.BoxShadow(
                spread_radius=0,
                blur_radius=20,
                color=ft.Colors.BLACK26,
                offset=ft.Offset(0, 8),
            ),
        )
