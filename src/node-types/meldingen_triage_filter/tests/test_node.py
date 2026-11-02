from pathlib import Path

from limescape_plugin_sdk.testing import FakeContext, run_node

NODE_DIR = Path(__file__).resolve().parents[1]


async def run(**input_data):
    return await run_node(
        NODE_DIR, FakeContext(granted=[]), params={}, input_data=input_data, output_key="filtered"
    )


async def test_filters_non_messages_and_preserves_shape():
    result = await run(
        triage_configuratie={"max_per_run": 1},
        triage_meldingen=[
            {"ID": "synthetic-1", "Subject": "Example", "CreationDate": "2026-01-01", "extra": "ignored"},
            {"ID": "synthetic-2", "Subject": "Second"},
            {"Subject": "No ID"},
        ],
    )
    assert result == [{"filtered": {"meldingen": [{"ID": "synthetic-1", "Subject": "Example", "CreationDate": "2026-01-01"}], "aantal": 1}}]


async def test_accepts_single_message_and_none():
    assert (await run(triage_configuratie={}, triage_meldingen={"ID": "one"}))[0]["filtered"]["aantal"] == 1
    assert (await run(triage_configuratie={}, triage_meldingen=None))[0]["filtered"]["aantal"] == 0
