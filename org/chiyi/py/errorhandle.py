x = 5
y = 0
try:
    print(x / y)
except ZeroDivisionError as e:
    # Optionally, log e some where
    print('Sorry, something wnent wrong')
else:
    print('Something really went wrong')
finally:
    print('This always runs on success or failure')