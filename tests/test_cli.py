import pytest
from typer.testing import CliRunner
from assistant.cli import app

runner = CliRunner()

def test_version():
    result = runner.invoke(app, ["version"])
    assert result.exit_code == 0
    assert "v0.1.0" in result.stdout

def test_config_init():
    result = runner.invoke(app, ["config", "init"])
    assert result.exit_code == 0