import subprocess
import sys
from pathlib import Path

from hello import make_message


def test_make_message_world():
    assert make_message("world") == "Hello, world!"


def test_make_message_name():
    assert make_message("Aono") == "Hello, Aono!"


def test_help_option_shows_usage():
    project_root = Path(__file__).resolve().parent.parent
    hello_py = project_root / "hello.py"

    result = subprocess.run(
        [sys.executable, str(hello_py), "--help"],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0
    assert "usage:" in result.stdout.lower()