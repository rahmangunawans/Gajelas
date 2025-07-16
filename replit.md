# ATV - AUTOTRADEVIP Mobile Application

## Overview

This is a Python-based mobile application built with Flet (Python's Flutter framework) called "ATV - AUTOTRADEVIP". The application appears to be a trading platform with a mobile-first design approach, featuring a splash screen with animated branding elements.

## User Preferences

Preferred communication style: Simple, everyday language.

## Recent Changes

**July 15, 2025:**
- ✓ Successfully migrated project from Replit Agent to Replit environment
- ✓ Restored original Flet mobile application structure
- ✓ Configured PostgreSQL database with proper user schema
- ✓ Created admin user: admin@atv.com / admin123
- ✓ Updated database manager to support full_name, phone, and admin fields
- ✓ Application now running on port 5000 for mobile interface
- ✓ All original mobile features preserved (splash screen, authentication, dashboard)
- ✓ Removed all Flask dependencies and files to focus purely on Flet
- ✓ Cleaned up pyproject.toml to only include necessary dependencies for Flet mobile app
- ✓ Fixed admin panel position to appear below Trading Bot section instead of horizontal navigation
- ✓ Enhanced Bottom Navigation Bar with unique glassmorphism design and floating button effects
- ✓ Added gradient backgrounds, glow effects, and smooth animations to navigation elements
- ✓ Implemented floating center button navigation design similar to modern mobile apps
- ✓ Created notched navigation bar with elevated center button for Active Bots section
- ✓ Added white background with rounded corners and shadow effects for professional look

**July 16, 2025:**
- ✓ Successfully migrated project from Replit Agent to Replit environment
- ✓ Updated database system from PostgreSQL to SQLite for Replit compatibility  
- ✓ Fixed Flet compatibility issues with letter_spacing parameter
- ✓ Removed duplicate workflow configuration to run single server instance
- ✓ Application now running cleanly on port 5000 with mobile interface
- ✓ Enhanced database with 9 comprehensive tables for trading functionality
- ✓ Created admin user (admin@atv.com / admin123) with full privileges
- ✓ Added support for trading bots, history, VIP subscriptions, and analytics
- ✓ Redesigned login page with ultra-professional luxury glassmorphism effects
- ✓ Enhanced header with sophisticated floating logo and multiple glow layers
- ✓ Premium form fields with advanced gradient backgrounds and animations
- ✓ Luxury button design with multi-layer gradients and shadow effects
- ✓ Fixed mobile layout for optimal scroll experience with Column-based design
- ✓ Implemented premium typography using SF Pro Display and Inter fonts
- ✓ Optimized form container size (340x460px) for mobile viewport
- ✓ Enhanced glassmorphism effects with subtle gradients for professional appearance
- ✓ Complete project structure reorganization for professional standards
- ✓ Created organized src/ directory with proper module separation
- ✓ Implemented clean architecture with config/, core/, services/, and utils/ packages
- ✓ Moved all Python files to appropriate directories with proper imports
- ✓ Created centralized app_config.py for configuration management
- ✓ Added comprehensive documentation and README files
- ✓ Removed temporary/test files and cleaned up project structure
- ✓ Fixed admin login authentication system
- ✓ Created admin setup utility for easy user management
- ✓ Added .gitignore for proper version control
- ✓ Successfully migrated from Replit Agent to Replit environment  
- ✓ Resolved complex application loop issues and database initialization problems
- ✓ Restored complete original ATV application with all design elements intact
- ✓ All original features preserved: splash screen animations, login system, dashboard
- ✓ PostgreSQL database configured with admin user (admin@atv.com / admin123)
- ✓ Fixed infinite loop issues while maintaining 100% original functionality and design
- ✓ Implemented professional logging system using Python logging module
- ✓ Replaced all print statements with proper structured logging
- ✓ Added comprehensive debug capabilities with log files and console output
- ✓ Created centralized logger utility for better debugging and monitoring
- ✓ Cleaned up project by removing temporary test files and debug versions
- ✓ Restored to clean production-ready state with only necessary files
- ✓ Completed migration from Replit Agent to Replit environment
- ✓ Created custom broker assets (SVG logos) for all trading platforms
- ✓ Updated dashboard to use proper broker logos instead of generic icons
- ✓ Enhanced broker cards with authentic branding for Binomo, Quotex, Olymptrade, IQ Option, and Stockity
- ✓ Fixed dashboard trading bot logos to properly display PNG images using base64 encoding
- ✓ Enhanced broker card image loading with better error handling and fallback display
- ✓ Fixed splash screen percentage display to properly count from 0% to 100%
- ✓ Updated progress animation to correctly update percentage text during loading sequence

**Project preference:** Keep as Flet mobile application, not Flask web application.

## System Architecture

The application follows a professional modular architecture pattern with clear separation of concerns:

- **Frontend Framework**: Flet (Python's Flutter wrapper) for cross-platform mobile development
- **UI Architecture**: Component-based design with reusable styling system
- **Design Pattern**: Object-oriented approach with dedicated classes for different screens
- **Platform Target**: Mobile-first design (375x812 resolution - iPhone X/11 dimensions)
- **Database**: PostgreSQL for production data storage with user authentication
- **Authentication**: Hash-based password security with session management
- **Project Structure**: Professional organization with src/ directory containing:
  - **config/**: Centralized configuration management
  - **core/**: UI components and styling
  - **services/**: Business logic and database operations
  - **utils/**: Utility functions, admin tools, and logging system

## Key Components

### 1. Main Application (`app.py`)
- **ATVApp Class**: Main application controller with page routing and navigation
- **Database Integration**: SQLite database initialization and user management
- **Authentication Flow**: Secure user login/registration with session management
- **Page Configuration**: Mobile-optimized window dimensions and styling

### 2. Pages Module (`pages/`)
- **SplashScreen**: Animated logo and branding with smooth transitions
- **AuthHandler**: Login, registration, and forgot password functionality with Remember Me and Terms & Conditions
- **Dashboard**: Comprehensive trading dashboard with broker management, VIP status, and navigation
- **Responsive Design**: Mobile-first approach with consistent styling

### 3. Database Module (`database/`)
- **DatabaseManager**: SQLite database operations and user management
- **User Authentication**: Secure password hashing and session management
- **Trading Accounts**: User trading account management system

### 4. Styling System (`styles.py`)
- **AppStyles Class**: Centralized styling configuration with consistent color palette
- **Design Tokens**: Predefined colors, fonts, spacing, and animation settings
- **Reusable Components**: Standardized button and card styles for consistency

### 5. Assets Structure
- **Logo Assets**: SVG-based logo system located in `assets/logo.svg`
- **Responsive Design**: Mobile-optimized dimensions and spacing

## Data Flow

The application implements a complete user journey flow:
1. Application initialization
2. Splash screen display with animated logo and branding
3. Brand text and progress bar animation sequence
4. Main description page with product information
5. Getting started confirmation page
6. Authentication flow with enhanced login/register forms
7. Dashboard with comprehensive trading interface featuring:
   - App header with search, VIP button, and notifications
   - Horizontal broker navigation (Beranda, Binomo, Quotex, Olymptrade, IQ Option, Stockity)
   - VIP status management and subscription options
   - Trading bot section with broker cards and progress tracking
   - Bottom navigation with pink active states (Beranda, Active Bots, History, Saya)

## External Dependencies

### Primary Framework
- **Flet**: Python framework for building Flutter-based mobile applications
- **Threading**: For handling animations and timing operations

### Asset Dependencies
- **SVG Images**: Logo and branding assets
- **Font System**: Custom typography hierarchy

## Deployment Strategy

The application is designed for:
- **Mobile Deployment**: Primary target platform with responsive design
- **Cross-Platform**: Leveraging Flet's Flutter backend for iOS/Android compatibility
- **Asset Management**: Local asset storage for offline functionality

### Technical Specifications
- **Window Dimensions**: 375x812 (iPhone X/11 standard)
- **Color Scheme**: Dark theme with blue/red accent colors
- **Animation System**: Smooth transitions with configurable timing
- **Responsive Design**: Mobile-first approach with scalable components

The architecture emphasizes maintainability through separation of concerns, with dedicated modules for styling and screen management, making it easy to extend with additional features and screens.