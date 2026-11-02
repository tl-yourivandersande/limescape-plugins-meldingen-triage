from pathlib import Path

from limescape_plugin_sdk.testing import FakeContext, run_node

NODE_DIR = Path(__file__).resolve().parents[1]


async def run(input_data):
    return await run_node(
        NODE_DIR, FakeContext(granted=[]), params={}, input_data=input_data, output_key="selected"
    )


async def test_selects_first_message_on_first_iteration():
    result = await run({"triage_filter": {"meldingen": [{"ID": "synthetic-1", "Subject": "First"}]}})
    assert result == [{"selected": {"index": 0, "next_index": 1, "melding_id": "synthetic-1", "onderwerp": "First"}}]


async def test_advances_using_previous_loop_outputs():
    result = await run({
        "triage_filter": {"meldingen": [{"ID": "one"}, {"ID": "two"}]},
        "triage_selecteer_melding": [{"index": 0}],
    })
    assert result == [{"selected": {"index": 1, "next_index": 2, "melding_id": "two", "onderwerp": None}}]


async def test_out_of_range_returns_empty_selection():
    result = await run({"triage_filter": {"meldingen": []}})
    assert result[0]["selected"]["melding_id"] == ""
