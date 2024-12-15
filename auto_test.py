from tests import salary, hello_who

assert hello_who('Max') == 'Hello Max', 'Error'
assert hello_who('L') == 'Hello L', 'Error'
assert salary(2, 2) == 8
assert salary(5, 5) == 50