*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input Register Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  pekka  pekka123

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  ka  kalle123
    Output Should Contain  Username should be 3+ letters from a to z

Register With Valid Username And Too Short Password
    Input Credentials  pekka  a1
    Output Should Contain  Username should be length 8 or more and contain letter a-z and digits.

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  pekka  moimoimoimoi
    Output Should Contain  Username should be length 8 or more and contain letter a-z and digits.

*** Keywords ***
Create User And Input Register Command
    Create User  kalle  kalle123
    Input Register Command