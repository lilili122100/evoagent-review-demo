import re
import subprocess


def export_report(filename):
    if not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9_-]*[.]txt', filename):
        raise ValueError('Invalid filename')
    return subprocess.run(['cat', filename], check=True, timeout=30)
