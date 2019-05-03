import unittest
from assignment2 import quotes_another_method as qam


class NamesTestCase(unittest.TestCase):

    def test_first_last_name(self):
        jsoncontent = {"lang": "en", "format": "json", "delay": 1}
        language = jsoncontent["lang"]
        format = jsoncontent["format"]
        total_seconds = jsoncontent["delay"]
        result = qam.print_quotes_for_time(jsoncontent, total_seconds, language, format)
        self.assertEqual(result, True)


if __name__ == '__main__':
    unittest.main()
