import subprocess


def export_report(filename):
    command = "cat " + filename
    return subprocess.run(command, shell=True)
