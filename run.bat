python  -m  "regression" pytest  --html=Reports\report.html testcases/ --browser chrome     
rem python  -m  "sanity" pytest  --html=Reports\report.html testcases/ --browser chrome
rem python  -m  "regression and sanity" pytest  --html=Reports\report.html testcases/ --browser chrome
rem python  -m  "regression or sanity" pytest  --html=Reports\report.html testcases/ --browser chrome

pause