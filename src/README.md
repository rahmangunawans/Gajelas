# ATV - AUTOTRADEVIP Source Code

This directory contains the organized source code for the ATV mobile application.

## Directory Structure

```
src/
├── __init__.py                 # Package initialization
├── config/                     # Configuration management
│   ├── __init__.py
│   └── app_config.py          # Application configuration
├── core/                      # Core application components
│   ├── __init__.py
│   ├── pages/                 # UI pages and screens
│   │   ├── __init__.py
│   │   ├── auth_handler.py    # Authentication pages
│   │   ├── dashboard.py       # Main dashboard
│   │   └── splash_screen.py   # Splash screen
│   └── styles.py              # Application styling
├── services/                  # Business logic services
│   ├── __init__.py
│   └── database/              # Database services
│       ├── __init__.py
│       └── postgres_manager.py # PostgreSQL database manager
└── utils/                     # Utility functions
    ├── __init__.py
    └── admin_setup.py         # Admin user setup utility
```

## Key Components

### Configuration (`config/`)
- **app_config.py**: Centralized application configuration including database settings, UI dimensions, and security parameters

### Core (`core/`)
- **pages/**: All UI components and page handlers
- **styles.py**: Application styling and theme management

### Services (`services/`)
- **database/**: Database operations and data management
- **postgres_manager.py**: PostgreSQL database interface with user authentication

### Utils (`utils/`)
- **admin_setup.py**: Utility for creating admin users

## Usage

The main application entry point is `app.py` in the root directory, which imports components from this organized structure.

## Development Notes

- All imports use proper Python path management
- Components are organized by functionality
- Clean separation of concerns between UI, business logic, and data layers