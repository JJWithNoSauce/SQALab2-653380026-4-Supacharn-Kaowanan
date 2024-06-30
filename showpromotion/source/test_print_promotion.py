import pytest
import source.print_promotion as print_promotion_function

#TS001
# def test_print_promotion():
#     result = print_promotion_function.print_promotion('A')
#     assert result == "Error"

# def test_print_promotion():
#     result = print_promotion_function.print_promotion("A")
#     assert result == "Error"

# def test_print_promotion():
#     result = print_promotion_function.print_promotion()
#     assert result == "Error"

# #TS002
# def test_print_promotion():
#     result = print_promotion_function.print_promotion(-100)
#     assert result == "Warning"

# def test_print_promotion():
#     result = print_promotion_function.print_promotion(100.6912)
#     assert result == "Thank you and see you next time"

#TS003
# def test_print_promotion():
#     result = print_promotion_function.print_promotion(True)
#     assert result == "Warning"

# #TS004
# def test_print_promotion():
#     result = print_promotion_function.print_promotion(150)
#     assert result == "Thank you and see you next time"

# def test_print_promotion():
#     result = print_promotion_function.print_promotion(300)
#     assert result == "Thank you and see you next time"
    
# def test_print_promotion():
#     result = print_promotion_function.print_promotion(450)
#     assert result == "Thank you and see you next time"

# #TS005
# def test_print_promotion():
#     result = print_promotion_function.print_promotion(500)
#     assert result == "Free ice cream cone = 1.0"

# def test_print_promotion():
#     result = print_promotion_function.print_promotion(600)
#     assert result == "Free ice cream cone = 1.0"

# #TS006
# def test_print_promotion():
#     result = print_promotion_function.print_promotion(700)
#     assert result == "Free chocolate cake = 1.0"

# def test_print_promotion():
#     result = print_promotion_function.print_promotion(900)
#     assert result == "Free chocolate cake = 1.0"

# #TS007
# def test_print_promotion():
#     result = print_promotion_function.print_promotion(1200)
#     assert result == "Free ice cream cone = 1.0 and Free chocolate cake = 1.0"

# def test_print_promotion():
#     result = print_promotion_function.print_promotion(1500)
#     assert result == "Free ice cream cone = 1.0 and Free chocolate cake = 1.0"

# #TS008
# def test_print_promotion():
#     result = print_promotion_function.print_promotion(2400)
#     assert result == "Free ice cream cone = 2.0 and Free chocolate cake = 2.0"

# def test_print_promotion():
#     result = print_promotion_function.print_promotion(2900)
#     assert result == "Free ice cream cone = 2.0 and Free chocolate cake = 2.0"

# #TS009
# def test_print_promotion():
#     result = print_promotion_function.print_promotion(3500)
#     assert result == "Free ice cream cone = 2.0 and Free chocolate cake = 3.0"

def test_print_promotion():
    result = print_promotion_function.print_promotion(4200)
    assert result == "Free ice cream cone = 2.0 and Free chocolate cake = 3.0"

