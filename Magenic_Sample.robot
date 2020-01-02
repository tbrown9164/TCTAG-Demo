*** Settings ***
Documentation    Magenic Sample App
Library          SeleniumLibrary
Library          website_functions.py
Library          utilities.py            WITH NAME   my_code
Resource         website_keywords.robot
Default Tags     CompanionMode   All  TopLevel   CRUD  LowLevel  DebugOnly   DontRun

#Suite Setup     Open Browser    ${MagenicURL}  ${Browser}            Can be done here but variables must be declared in Settings
#Suite Teardown   Test Teardown

*** Variables ***
${DateTime}
${MagenicURL} =    "http://magenic.com"
${Browser}=   chrome

*** Test Cases ***
Test title 1
    [Tags]    DEBUG    TopLevel
    ${DateTime}=       my_code.get_datetime
    Log To Console    ${DateTime}
    #Provided precondition   'Given'
    Open Browser     http://www.magenic.com     ${Browser}              # standard keyword with parameter declared literally and then with variable

    #When action
    #Then check expectations

*** Keywords ***
Provided precondition
   # Setup system under test
   Log To Console    done