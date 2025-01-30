## Overview
Automated testing framework for Crown Casino's web application using Playwright with Python and Pytest, following the Page Object Model pattern.

## Prerequisites
- Python 3.7+
- pip

## Installation
1. Install packages:
pip install pytest playwright pytest-playwright

2. Install browsers:
playwright install

## Running Tests
Run with UI and console output:
pytest test_edit_profile.py --headed -s

## Test Configuration
- Base URL: https://app.dev.crowncoinscasino.com/
- Test Account: watchdogstest02+11@sunfltd.com / 123456
- Viewport: 1920x1080

## Main Components
1. Page Objects (pages/):
   - LoginPage: Authentication
   - HomePage: Navigation & balances
   - ProfileDialog: Profile management

2. Test Coverage:
   - Login flow
   - Profile updates
   - Balance verification

## Notes
- Random usernames generated per test
- Use -s flag to see balance outputs
- Automatic cleanup after each test
