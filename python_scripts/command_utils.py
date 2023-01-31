import subprocess


def _run_command(command):
    p = subprocess.run(command, shell=True,
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return p.returncode, p.stdout.decode().strip(), p.stderr.decode().strip()
