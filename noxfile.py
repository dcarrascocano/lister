import nox


@nox.session(python=["3.10"])
def tests(session):
    session.install("poetry")
    session.run("poetry", "install", "--no-interaction")
    session.run("coverage", "run", "-m", "pytest")
    session.run("coverage", "report")


@nox.session(python=["3.10"])
def lint(session):
    session.install("poetry")
    session.run("poetry", "install")
    session.run("black", "--check", ".")
    session.run("flake8", ".")


@nox.session(python=["3.10"])
def typing(session):
    session.install("poetry")
    session.run("poetry", "install")
    session.run("mypy", ".")
