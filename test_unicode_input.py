import unittest
from unittest.mock import patch

from amor_fati import AmorFati
from training import TrainingHandler


class TestUnicodeInput(unittest.TestCase):
    def test_composed_input_matches_decomposed_training_name(self):
        handler = TrainingHandler(AmorFati())

        with patch("builtins.input", return_value="löpning"):
            result = handler.get_input(
                "Vilken typ av kondition?",
                handler.TRÄNINGS_METOD_DICT["kondition"],
            )

        self.assertEqual(
            result,
            handler.TRÄNINGS_METOD_DICT["kondition"][0],
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
