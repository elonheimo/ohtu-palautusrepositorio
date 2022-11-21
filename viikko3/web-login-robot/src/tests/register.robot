*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page And Chech Open

*** Test Cases ***

Register With Valid Username And Password
    Set Username  kalle
    Set Password  kalle123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  a
    Set Password  kalle123
    Submit Credentials
    Register Should Fail With Message  Username should be 3+ letters from a to z

Register With Valid Username And Too Short Password
    Set Username  kallexoxo
    Set Password  x
    Submit Credentials
    Register Should Fail With Message  Username should be length 8 or more and contain letter a-z and digits.

Register With Nonmatching Password And Password Confirmation
    Set Username  khalle
    Set Password With Confirmation  khalle123  khalle666
    Submit Credentials  
    Register Should Fail With Message  password do'nt match

Login After Successful Registration
    Set Username  kallemme
    Set Password  kallemme123
    Submit Credentials
    Register Should Succeed
    Go To Login Page
    Set Username  kallemme
    Set Password Proper  kallemme123
    Submit Login
    Login Should Succeed


Login After Failed Registration
    Set Username  a
    Set Password  11233adyugdsa
    Submit Credentials
    Register Should Fail With Message  Username should be 3+ letters from a to z
    Go To Login Page
    Set Username  khallemme
    Set Password Proper  väärä
    Submit Login
    Login Should Fail With Message  Invalid username or password


*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open


Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Submit Login
    Click Button  Login

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}
    Input Password  password_confirmation  ${password}

Set Password Proper
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password With Confirmation
    [Arguments]  ${password}  ${confirmation}
    Input Password  password  ${password}
    Input Password  password_confirmation  ${confirmation}



Go To Register Page And Chech Open
    Go To Register Page
    Register Page Should Be Open
