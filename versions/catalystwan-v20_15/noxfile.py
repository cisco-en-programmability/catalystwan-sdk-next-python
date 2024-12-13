import pathlib
import shutil
import sys

import nox

MYPY_VERSION = "mypy==1.13.0"
PYTYPE_VERSION = "pytype==2024.10.11"

PYPROJECT = nox.project.load_toml("pyproject.toml")

ALL_PYTHONS = [
    c.split()[-1]
    for c in PYPROJECT["project"]["classifiers"]
    if c.startswith("Programming Language :: Python :: 3.")
]
DEFAULT_PYTHON_VERSION = "3.12"
CURRENT_DIRECTORY = pathlib.Path(__file__).parent.absolute()

DEPENDENCY = ["../../packages/catalystwan-types/"]

nox.options.sessions = ["units"]


def default(session, install_extras=True):
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


@nox.session(python=ALL_PYTHONS)
def units(session):
    """Run the unit test suite."""

    default(session)


@nox.session(python=DEFAULT_PYTHON_VERSION)
def mypy(session):
    """Run type checks with mypy."""

    for dep in DEPENDENCY:
        session.install("-e", dep)

    session.install("-e", ".[all]")
    session.install(MYPY_VERSION)

    session.install(
        "types-requests",
    )
    session.run("mypy", "-p", "catalystwan.versions", "--show-traceback")


@nox.session(python=DEFAULT_PYTHON_VERSION)
def pytype(session):
    """Run type checks with pytype."""

    for dep in DEPENDENCY:
        session.install("-e", dep)

    session.install("-e", ".[all]")
    session.install(PYTYPE_VERSION)
    session.run("pytype", "-P", ".", "src")


@nox.session(python="3.12")
def lint(session: nox.Session) -> None:
    """Run pre-commit linting."""

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


@nox.session(default=False)
def docs(session: nox.Session) -> None:
    output_dir = pathlib.Path(session.create_tmp()) / "output" / "html"
    """Build the documentation."""
    shutil.rmtree(output_dir, ignore_errors=True)
    session.install(*PYPROJECT["dependency-groups"]["docs"])
    session.install("-e.")
    session.cd("./docs")
    sphinx_args = ["-b", "html", "-W", "./source", output_dir]

    session.run("sphinx-build", *sphinx_args)
