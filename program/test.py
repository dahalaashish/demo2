import unittest
from scanner import scan_port, scan_range

def test_closed_port():
    result = scan_port("127.0.0.1", 1)
    assert result is None

def test_scan_range_returns_list():
    result = scan_range("127.0.0.1", 1, 10)
    assert isinstance(result, list)

def test_invalid_ip():
    result = scan_port("999.999.999.999", 80)
    assert result is None

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.FunctionTestCase(test_closed_port))
    suite.addTest(unittest.FunctionTestCase(test_scan_range_returns_list))
    suite.addTest(unittest.FunctionTestCase(test_invalid_ip))
    
    unittest.TextTestRunner(verbosity=2).run(suite)