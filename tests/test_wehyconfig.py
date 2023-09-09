import pytest
from wehyconfig.wehyconfig import read_config


@pytest.fixture
def test_file():
    return "tests/test_wehyconfig_files/test_first.toml"


@pytest.fixture
def test_folder():
    return "tests/test_wehyconfig_files/test_folder/"


def test_read_config_file(test_file):
    config = read_config(config_source=test_file)
    assert config["main"]["root_folder"] == "/tmp"
    assert config["logging"]["level"] == "DEBUG"
    assert config["logging"]["filemode"] == "a"
    assert config["logging"]["log_format"] == "%(asctime)s [%(module)s] %(message)s"
    assert config["alerts"]["email"]["to_addresses"][0] == "dev-bunnies@weehooey.com"
    assert config["alerts"]["email"]["to_addresses"][1] == "dev-ewoks@weehooey.com"
    assert config["alerts"]["email"]["to_addresses"][2] == "dev-pandas@weehooey.com"
    assert config["alerts"]["email"]["from_address"] == "test-system-42@weehooey.com"
    assert config["alerts"]["email"]["subject"] == "Toilet Paper Levels"
    assert config["alerts"]["email"]["smtp_server"] == "mx-42.weehooey.com"
    assert config["alerts"]["sms"]["to_numbers"][0] == "343-555-1212"
    assert config["alerts"]["sms"]["to_numbers"][1] == "705-555-1212"
    assert config["alerts"]["sms"]["to_numbers"][2] == "905-555-1212"
    assert config["alerts"]["sms"]["from_number"] == "613-555-1212"


def test_read_config_file_section(test_file):
    logging_config = read_config(config_source=test_file, section="logging")
    assert logging_config["level"] == "DEBUG"
    assert logging_config["filemode"] == "a"
    assert logging_config["log_format"] == "%(asctime)s [%(module)s] %(message)s"

def test_read_config_folder(test_folder):
    config = read_config(config_source=test_folder)
    assert config['fwhojirue']['vms']['name'] == "helicopter"
    assert config['fwhojirue']['vms']['location'] == "PVE" 
    assert config['fwhojirue']['vms']['drives'][0] == 8
    assert config['fwhojirue']['vms']['drives'][1] == 16
    assert config['fwhojirue']['vms']['drives'][2] == 9
    assert config['fwhojirue']['vms']['drives'][3] == 7
    assert config['okyktvhnm']['vms']['name'] == "torpedo"
    assert config['okyktvhnm']['vms']['location'] == "PBS"
    assert config['okyktvhnm']['vms']['depth'][0] == 80
    assert config['okyktvhnm']['vms']['depth'][1] == 160
    assert config['okyktvhnm']['vms']['depth'][2] == 9
    assert config['okyktvhnm']['vms']['depth'][3] == 7.5
    assert config['okyktvhnm']['vms']['comments'] == "This is not the config you are looking for!"
    assert config['ruexrvgvf']['logging'] == "no"
    assert config['ruexrvgvf']['blogging'] == "likely not"
    assert config['ruexrvgvf']['vlogging'] == "definitely no"
    assert config['ruexrvgvf']['age'] == 100
