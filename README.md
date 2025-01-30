# Sunflower assignment - Test Standard

## Test Purpose
1.Validate that users can:
2.Successfully log into the system
3.Update their profile with a new username and avatar
4.Verify the coin balances for both Sweep and Social coins

## Preconditions
Python 3.7+ installed
Playwright browsers installed
Valid test account credentials:
Email: watchdogstest02+11@sunfltd.com
Password: 123456
Base URL accessible: https://app.dev.crowncoinscasino.com/
Browser viewport set to 1920x1080

## Steps to Execute
1. Login:
Click login button
Enter credentials
Handle post-login popup
Expected: Menu button visible
2. Profile Update:
Open My Account dialog
Update nickname with random string
Select random avatar
Apply changes
Expected: New nickname displayed correctly
3. Balance Check:
Check Sweep coin balance
Switch to Social coin
Check Social coin balance
Switch back to Sweep coin
Expected: Both balances retrieved and printed

## Post-Conditions
Automatic cleanup via pytest fixture
Browser page closed after test
System returned to initial state

## Validation Criteria
Test is considered successful when:
1. Login completes without errors
2. Profile updates are verified:
-New nickname matches input
-Avatar selection successful
3. Both coin balances are successfully retrieved
4. No unexpected errors or popups occur
5. All page transitions complete as expected

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
