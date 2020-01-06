*** Settings ***
Documentation    Magenic Sample App
Library          SeleniumLibrary
Library          DateTime
Library          ImapLibrary
Library          Website_Functions.py                   #case sensitive!
Library          utilities.py            WITH NAME   my_code
Resource         website_keywords.robot
Default Tags     CompanionMode   All  TopLevel   CRUD  LowLevel  DebugOnly   DontRun

Suite Setup      GotoMagenicSite
#Suite Teardown   Test Teardown

*** Variables ***
${DateTime}
${MagenicURL} =    "http://magenic.com"
${Browser}=   chrome

*** Test Cases ***
Set Speed and Get DateTime
    [Documentation]   documentation must start intented (this is a note from me)
    [Tags]  Smoke
    Set Selenium Speed    4
    Set Browser Implicit Wait    5
    ${DateTime}=       my_code.get_datetime
    Log To Console    ${DateTime}
    #Provided precondition   'Given'
    # Open Browser     http://www.magenic.com     ${Browser}              # optionally here standard keyword with parameter declared literally and then with variable



Click On Contact
   [Documentation]   documentation must start intented (this is a note from me)
   Log To Console   Clicking on Contact button
   #Element Should Be Visible  xpath= //*[@text='Equipment']
   #Wait Until Keyword Succeeds     5x    3 sec      Click Element   class=

*** Keywords ***
GotoMagenicSite
   Open Browser  https://www.magenic.com  ${Browser}
   Log To Console    done

Test Teardown
   Close Browser