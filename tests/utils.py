"""Test utilities for the Longboard project."""


from subprocess import Popen, PIPE



class TestingServer(object):

    """Simple static file server."""

    def __init__(self, path, port=3333):
        """Initialize a TestingServer serving the files in path."""
        self._path = path
        self._port = port
        self._proc = None

    def start(self):
        self._proc = Popen(
            'python -m SimpleHTTPServer ' + str(self._port),
            cwd=self._path, shell=True,
            stdout=PIPE, stderr=PIPE, stdin=PIPE)

    def stop(self):
        self._proc.terminate()
        self._proc.wait()

    def make_url(self, rel):
        return 'http://localhost:{}{}'.format(self._port, rel)
