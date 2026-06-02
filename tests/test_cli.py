from typer.testing import CliRunner
from assistant.cli import app

runner = CliRunner()


def test_version():
    result = runner.invoke(app, ["version"])
    assert result.exit_code == 0


def test_git_history():
    result = runner.invoke(app, ["git", "history"])
    assert result.exit_code == 0


def test_budget_status():
    result = runner.invoke(app, ["budget", "status"])
    assert result.exit_code == 0