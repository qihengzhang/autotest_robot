*** Settings ***

Library  __st__.py   WITH NAME  D

Suite Setup    D.suite_setup

Suite Teardown    D.suite_teardown

Force Tags     冒烟测试   打开浏览器  

