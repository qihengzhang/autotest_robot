*** Settings ***

Library  test.py   WITH NAME  F

Library  test.autotest   WITH NAME  autotest



*** Test Cases ***

管理员首页 - UI-0101

  autotest.teststeps
