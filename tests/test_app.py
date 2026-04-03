# tests/test_app.py
import subprocess

def test_default_sum():
    # Run app.py without arguments (uses default 10+20)
    result = subprocess.run(
        ["python3", "app.py"],
        capture_output=True,
        text=True
    )
    assert "Sum = 30" in result.stdout

def test_custom_sum():
    # Run app.py with custom numbers 15+25
    result = subprocess.run(
        ["python3", "app.py", "15", "25"],
        capture_output=True,
        text=True
    )
    assert "Sum = 40" in result.stdout
