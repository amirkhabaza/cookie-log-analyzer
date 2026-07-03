import io
import unittest
from unittest.mock import patch
from cookie_analyzer import get_most_active_cookies

# Sample data provided in the prompt
SAMPLE_CSV = """cookie,timestamp
AtY0laUfhglK3lC7,2018-12-09T14:19:00+00:00
SAZuXPGUrfbcn5UA,2018-12-09T10:13:00+00:00
5UAVanZf6UtGyKVS,2018-12-09T07:25:00+00:00
AtY0laUfhglK3lC7,2018-12-09T06:19:00+00:00
SAZuXPGUrfbcn5UA,2018-12-08T22:03:00+00:00
4sMM2LxV07bPJzwf,2018-12-08T21:30:00+00:00
fbcn5UAVanZf6UtG,2018-12-08T09:30:00+00:00
4sMM2LxV07bPJzwf,2018-12-07T23:30:00+00:00"""


class TestCookieAnalyzer(unittest.TestCase):

    @patch("builtins.open", return_value=io.StringIO(SAMPLE_CSV))
    def test_single_most_active(self, mock_file):
        result = get_most_active_cookies("dummy_path.csv", "2018-12-09")
        self.assertEqual(result, ["AtY0laUfhglK3lC7"])

    @patch("builtins.open", return_value=io.StringIO(SAMPLE_CSV))
    def test_multiple_most_active_tie(self, mock_file):
        result = get_most_active_cookies("dummy_path.csv", "2018-12-08")
        # Order should be maintained or matched based on appearance
        expected = ["SAZuXPGUrfbcn5UA", "4sMM2LxV07bPJzwf", "fbcn5UAVanZf6UtG"]
        self.assertCountEqual(result, expected)

    @patch("builtins.open", return_value=io.StringIO(SAMPLE_CSV))
    def test_date_with_no_cookies(self, mock_file):
        result = get_most_active_cookies("dummy_path.csv", "2018-12-10")
        self.assertEqual(result, [])

    @patch("builtins.open", return_value=io.StringIO("cookie,timestamp\n"))
    def test_empty_file(self, mock_file):
        result = get_most_active_cookies("dummy_path.csv", "2018-12-09")
        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()