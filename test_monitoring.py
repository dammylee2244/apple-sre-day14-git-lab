
import unittest
from unittest.mock import patch, Mock
import health_check
import memory_check


class TestMonitoring(unittest.TestCase):

    @patch("health_check.shutil.disk_usage")
    def test_disk_check_runs(self, mock_disk):
        mock_disk.return_value = Mock(
            total=100 * 1024**3,
            used=30 * 1024**3,
            free=70 * 1024**3
        )

        health_check.check_disk()
        mock_disk.assert_called_once()


    @patch("memory_check.psutil.virtual_memory")
    def test_memory_check_runs(self, mock_memory):
        mock_memory.return_value = Mock(
            total=8 * 1024**3,
            available=4 * 1024**3,
            percent=50.0
        )

        memory_check.check_memory()
        mock_memory.assert_called_once()


if __name__ == "__main__":
    unittest.main()
