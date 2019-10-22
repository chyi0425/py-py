x = 5
y = 0
try:
    print(x / y)
except ZeroDivisionError as e:
    # Optionally, log e some where
    print('Sorry, something wnent wrong')
except:
    print('Something really went wrong')
finally:
    print('This always runs on success or failure')