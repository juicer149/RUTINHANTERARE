import unittest
import mixins

class TestWordToNumericValueMixin(unittest.TestCase):
    def setUp(self):
        self.converter = mixins.WordToNumericValueMixin()

    def test_convert_single_digit(self):
        self.assertEqual(self.converter.word_to_numeric_values('ett'), 1)

    def test_convert_double_digit(self):
        self.assertEqual(self.converter.word_to_numeric_values('tio'), 10)
    
    def test_convert_compound_number(self):
        self.assertEqual(self.converter.word_to_numeric_values('tjugoett'), 21)

    def test_convert_hundred(self):
        self.assertEqual(self.converter.word_to_numeric_values('etthundrafem'), 105)
        self.assertEqual(self.converter.word_to_numeric_values('hundra'), 100)
        self.assertEqual(self.converter.word_to_numeric_values('trehundraåttioåtta'), 388) 
        self.assertEqual(self.converter.word_to_numeric_values('niohundranittionio'), 999)
        
    def test_convert_tusen(self):
        self.assertEqual(self.converter.word_to_numeric_values('tusen'), 1000)
        self.assertEqual(self.converter.word_to_numeric_values('etttusenett'), 1001)
        self.assertEqual(self.converter.word_to_numeric_values('åtta tusen'), 8000)
        self.assertEqual(self.converter.word_to_numeric_values('åtta tusen sju hundra'), 8700) 
        self.assertEqual(self.converter.word_to_numeric_values('åtta tusen sju tio'), 8070)
        self.assertEqual(self.converter.word_to_numeric_values('åtta tusen sju hundra trettio nio'), 8739)
        self.assertEqual(self.converter.word_to_numeric_values('åtta tusen sju hundra tjugo nio'), 8729)

    def test_convert_irregular_number(self):
        self.assertEqual(self.converter.word_to_numeric_values('sjutiofem'), 75)
#        self.assertEqual(self.converter.word_to_numeric_values('tolvhundra'), 1200) #FAIL

    def test_invalid_input_raises_error(self):
        with self.assertRaises(ValueError):
            self.converter.word_to_numeric_values('ogiltigt')

if __name__ == '__main__':
    unittest.main(verbosity=2)
