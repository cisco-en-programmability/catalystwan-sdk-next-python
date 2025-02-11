import pathlib
import sys

import nox

PYPROJECT = nox.project.load_toml("pyproject.toml")

ALL_PYTHONS = [
    c.split()[-1]
    for c in PYPROJECT["project"]["classifiers"]
    if c.startswith("Programming Language :: Python :: 3.")
]
DEFAULT_PYTHON_VERSION = "3.12"
CURRENT_DIRECTORY = pathlib.Path(__file__).parent.absolute()

DEPENDENCY = [
    "../catalystwan-types/",
    "../../versions/catalystwan-v20_15/",
    "../../versions/catalystwan-v20_16/",
]

nox.options.sessions = ["units"]


@nox.session(python=ALL_PYTHONS)
def units(session):
    """Default unit test session."""
    coverage_file = f".coverage.{sys.platform}.{session.python}"

    session.install(*PYPROJECT["dependency-groups"]["test"])

    for dep in DEPENDENCY:
        session.install("-e", dep)

    install_target = "."
    session.install("-e", install_target)
    session.run("python", "-m", "pip", "freeze")

    session.run(
        "pytest",
        "--quiet",
        "--cov=catalystwan",
        "--cov-config",
        "pyproject.toml",
        "--cov-fail-under=0",
        "tests",
        env={
            "COVERAGE_FILE": coverage_file,
        },
    )

    """Run the unit test suite."""


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
    session.run("mypy", "-p", "catalystwan", "--show-traceback")


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


@nox.session(default=False)
def cover(session: nox.Session) -> None:
    """Coverage analysis."""
    session.install("coverage[toml]>=7.3")
    session.run("coverage", "combine")
    session.run("coverage", "report", "--fail-under=80", "--show-missing")
    session.run("coverage", "erase")
