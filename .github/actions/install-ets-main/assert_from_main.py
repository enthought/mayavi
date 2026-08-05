"""Fail unless every package in requirements.txt was installed from its VCS URL.

None of the ETS packages carries a dev version on ``main`` -- each one reports
its last *release* -- so the version says nothing about where a distribution
came from, and a silent fall back to PyPI would leave the CI row green while
testing nothing at all.  ``direct_url.json`` (PEP 610) is what records the VCS
origin, so it is the only thing worth asserting on.
"""
import json
import sys
from importlib.metadata import distribution
from pathlib import Path

REQUIREMENTS = Path(__file__).with_name('requirements.txt')


def requirement_names(path):
    """The distribution names in a requirements file, in order."""
    for line in path.read_text().splitlines():
        line = line.split('#')[0].strip()
        if line:
            yield line.split('@')[0].strip()


def origin(name):
    """Where `name` was installed from: a URL, or None if it came from an index."""
    raw = distribution(name).read_text('direct_url.json')
    return json.loads(raw)['url'] if raw else None


def main():
    bad = False
    for name in requirement_names(REQUIREMENTS):
        url = origin(name)
        print(f'{name} {distribution(name).version} from {url or "an index"}')
        if url is None or not url.rstrip('/').endswith(f'/{name}'):
            print(f'  ERROR: expected {name} to come from its own repository')
            bad = True
    return int(bad)


if __name__ == '__main__':
    sys.exit(main())
