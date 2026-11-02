from pathlib import Path

from limescape_plugin_sdk.testing import FakeContext, run_node

NODE_DIR = Path(__file__).resolve().parents[1]


async def run(**params):
    return await run_node(NODE_DIR, FakeContext(granted=[]), params=params, output_key="config")


async def test_builds_config_from_form_fields():
    result = await run(
        mailbox_id="synthetic-mailbox",
        label_nieuwe_melding="synthetic-label",
        handmatige_domeinen="example.test\nmail.test",
        extra_melders="person@example.test",
        dagen_terug=3,
        max_per_run=25,
        extra_filters="Status eq false",
    )
    config = result[0]["config"]
    assert config["mailbox_id"] == "synthetic-mailbox"
    assert config["handmatige_domeinen"] == ["example.test", "mail.test"]
    assert config["extra_melders"] == ["person@example.test"]
    assert config["top"] == "25"
    assert "Status eq false" in config["filter"]
    assert "CreationDate ge " in config["filter"]


async def test_requires_mailbox_identifier():
    result = await run()
    assert result == [{"error": "Mailbox identifier is required"}]


async def test_rejects_out_of_range_maximum():
    result = await run(mailbox_id="synthetic", max_per_run=101)
    assert result == [{"error": "Maximum per run must be between 1 and 100"}]
