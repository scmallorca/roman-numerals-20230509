from unittest import TestCase
from main import translate_to_roman

class TryTesting(TestCase):

    def test_one_translates(self):
        result = translate_to_roman(1)
        self.assertEqual(result, "I")

    def test_two_translates(self):
        result = translate_to_roman(2)
        self.assertEqual(result, "II")

    def test_three_translates(self):
        result = translate_to_roman(3)
        self.assertEqual(result, "III")
    
    def test_four_translates(self):
        result = translate_to_roman(4)
        self.assertEqual(result, "IV")

    def test_five_translates(self):
        result = translate_to_roman(5)
        self.assertEqual(result, "V")
    
    def test_six_translates(self):
        res = translate_to_roman(6)
        self.assertEqual(res, "VI")
    
    def test_seven_translates(self):
        res = translate_to_roman(7)
        self.assertEqual(res, "VII")
    
    def test_eight_translates(self):
        res = translate_to_roman(8)
        self.assertEqual(res, "VIII")
    
    def test_nine_translates(self):
        res = translate_to_roman(9)
        self.assertEqual(res, "IX")
    
    def test_ten_translates(self):
        res = translate_to_roman(10)
        self.assertEqual(res, "X")
    
    def test_eleven_translates(self):
        res = translate_to_roman(11)
        self.assertEqual(res, "XI")
    
    def test_twelve_translates(self):
        res = translate_to_roman(12)
        self.assertEqual(res, "XII")
    
    def test_fourteen_translates(self):
        res = translate_to_roman(14)
        self.assertEqual(res, "XIV")

    def test_fiveteen_translates(self):
        res = translate_to_roman(15)
        self.assertEqual(res, "XV")

    def test_nineteen_translates(self):
        res = translate_to_roman(19)
        self.assertEqual(res, "XIX")

    def test_20_translates(self):
        res = translate_to_roman(20)
        self.assertEqual(res, "XX")

    def test_25_translates(self):
        res = translate_to_roman(25)
        self.assertEqual(res, "XXV")

    def test_30_translates(self):
        res = translate_to_roman(30)
        self.assertEqual(res, "XXX")

    def test_35_translates(self):
        res = translate_to_roman(35)
        self.assertEqual(res, "XXXV")

    def test_40_translates(self):
        res = translate_to_roman(40)
        self.assertEqual(res, "XL")

   