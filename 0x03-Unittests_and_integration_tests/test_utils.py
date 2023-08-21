#!/usr/bin/env python3
"""
unit test for utils.access_nested_map.
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """
    inherits from unittest.TestCase.
    tests utils.access_nested_map function
    """
    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2)
        ]
    )
    def test_access_nested_map(self, nested_map, path, expected):
        """
        test whether the access_nested_map function works correctly
        """
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected)

    @parameterized.expand(
        [
            ({}, ("a",), KeyError),
            ({"a": 1}, ("a", "b"), KeyError)
        ]
    )
    def test_access_nested_map_exception(self, nested_map, path,
                                         expected_err):
        """
        test that a KeyError is raised for the parameterized inputs
        """
        with self.assertRaises(expected_err) as context:
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    inherits from unittest.TestCase.
    tests utils.get_json function
    """
    @parameterized.expand(
        [
            ('http://example.com', {'payload': True}),
            ('http://holberton.io', {'payload': False})
        ]
    )
    @patch("utils.requests.get")
    def test_get_json(self, url, payload, mock_get):
        """
        test that utils.get_json returns the expected result
        """
        mock_response = Mock()
        mock_response.json.return_value = payload
        mock_get.return_value = mock_response

        result = get_json(url)

        mock_get.assert_called_once_with(url)
        self.assertEqual(result, payload)


class TestMemoize(unittest.TestCase):
    """
    test utils.test_memoize function
    """
    def test_memoize(self):
        """test
        """

        class TestClass:
            """tests class
            """

            def a_method(self):
                """return 42
                """
                return 42

            @memoize
            def a_property(self):
                """memoize decorated
                """
                return self.a_method()

        test_obj = TestClass()

        with patch.object(test_obj, 'a_method') as mock_method:
            mock_method.return_value = 42

            result1 = test_obj.a_property
            result2 = test_obj.a_property

            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)
            mock_method.assert_called_once()
