pip install -U selenium
pip install behave
pip install behave-html-formatter
pip install webdriver-manager

run test
behave -f html -o behave-report-login1.html --tags=login1
behave -f html -o behave-report-login2.html --tags=login2
behave -f html -o behave-report-cart1.html --tags=cart1
behave -f html -o behave-report-cart2.html --tags=cart2
behave -f html -o behave-report-search.html --tags=search
behave -f html -o behave-report-favorite.html --tags=favorite