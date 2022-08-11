import unittest
import file_validation
import config

test_csv = 'test_files/MED_DATA_20210701153952.csv'
df = file_validation.convert_to_df(test_csv)


class TestValidation(unittest.TestCase):

    def test_get_row_count(self):
        result = file_validation.get_row_count(df)
        self.assertEqual(result, 10)
        self.assertNotEqual(result, 1)

        self.assertRaises(AttributeError, file_validation.get_row_count, test_csv)

    def test_check_headers(self):
        result = file_validation.check_headers(df)
        self.assertTrue(result)

    def test_check_malformed(self):
        result = file_validation.check_malformed(test_csv)
        self.assertEqual(result, 'File correct')

        self.assertRaises(AttributeError, file_validation.check_malformed, df)


class TestFTP(unittest.TestCase):

    def test_ftp_login(self):
        result = config.ftp_login_check('incorrect', 'incorrect')
        self.assertFalse(result)

        self.assertRaises(ValueError, config.ftp_login_check, df, df)


if __name__ == '__main__':
    unittest.main()
