README.md

# Vortex image processing

[![codecov](https://codecov.io/github/vortexntnu/vortex-image-processing/graph/badge.svg?token=yS64SRLzUs)](https://codecov.io/github/vortexntnu/vortex-image-processing) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) [![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/pylint-dev/pylint)

This is the README file for the directory containing the image processing software created and used by Vortex.

## Getting Started:

### Prerequisites:

Make sure that you have the following installed on your system:

- [Python](https://www.python.org/)
- [pip](https://pip.pypa.io/en/stable/installation/)
- [venv](https://docs.python.org/3/library/venv.html)

---

## Testing

The automated tests are stored in the `tests` directory. Make sure to [install `pytest`](https://docs.pytest.org/en/7.1.x/getting-started.html). The tests can be ran by using the command `pytest .`. The commands will run the test define the the `test_*.py` files. Make sure that you are in the `YOLO-detect-buoys` directory. The naming convention of testing files is comprised of the word `test_` followed by the name of the file to which the test is related: `test_<FILE_NAME>.py`. An example of that is `tests/test_utils.py` which is a python test file tah tests the functions `utils`.

---

## Linting

Linting improves code quality by ensuring the the codebase does not contain bad-practices. Make sure to [install PyLint](https://pypi.org/project/pylint/) globally in order to use CLI. Use the command `pylint $(git ls-files '*.py')` in order to lint the files tracked by git. PyLint is used as the Python linter in this project. Make sure to install the [PyLint extension](https://pypi.org/project/pylint/) for VSCode or [PyLint plugin](https://plugins.jetbrains.com/plugin/11084-pylint) for JetBrains products like Pycharm. The rules are saved in the `.pylintrc` files.
