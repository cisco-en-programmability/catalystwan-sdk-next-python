import pathlib

import nox

PYPROJECT = nox.project.load_toml("pyproject.toml")

ALL_PYTHONS = [
    c.split()[-1]
    for c in PYPROJECT["project"]["classifiers"]
    if c.startswith("Programming Language :: Python :: 3.")
]
DEFAULT_PYTHON_VERSION = "3.12"
CURRENT_DIRECTORY = pathlib.Path(__file__).parent.absolute()

DEPENDENCY = ["../catalystwan-types/", "../../versions/catalystwan-v20_15/"]

nox.options.sessions = ["mypy"]


@nox.session(python=DEFAULT_PYTHON_VERSION)
def mypy(session):
    """Run type checks with mypy."""

    for dep in DEPENDENCY:
        session.install("-e", dep)

    session.install("-e", ".[all]")
    session.install(*PYPROJECT["dependency-groups"]["typing"])

    session.install(
        "types-requests",
    )
    session.run("mypy", "-p", "catalystwan.abc", "--show-traceback")


@nox.session(python=DEFAULT_PYTHON_VERSION)
def pytype(session):
    """Run type checks with pytype."""

    for dep in DEPENDENCY:
        session.install("-e", dep)

    session.install("-e", ".[all]")
    session.install(*PYPROJECT["dependency-groups"]["typing"])
    session.run("pytype", "-P", ".", "src")


@nox.session(python="3.12")
def lint(session: nox.Session) -> None:
    """Run linting."""

    for dep in DEPENDENCY:
        session.install("-e", dep)
    session.install("pre-commit")
    session.run(
        "pre-commit",
        "run",
        "--all-files",
        "--show-diff-on-failure",
        "--hook-stage=manual",
        *session.posargs,
    )
