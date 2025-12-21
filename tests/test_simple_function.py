from main.main import return_value

def test_simple_function_int():
    assert return_value(1) == 1

def test_simple_function_float():
    assert return_value(1.1) == 1.1

def test_simple_function_bool():
    assert return_value(False) == False

def test_simple_function_str():
    assert return_value("hello") == "hello"