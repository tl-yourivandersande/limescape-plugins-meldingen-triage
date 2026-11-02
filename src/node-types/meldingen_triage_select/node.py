from limescape_plugin_sdk import NodeContext, NodeInput


def _as_list(value: object) -> list[object]:
    if value is None:
        return []
    return value if isinstance(value, list) else [value]


def _previous_count(value: object) -> int:
    # The flow loop provides an object on its first round and a list thereafter.
    if value is None:
        return 0
    if isinstance(value, list):
        return len(value)
    return 1


async def execute(ctx: NodeContext, inp: NodeInput):
    filtered = inp.input_data.get("triage_filter") or {}
    messages = _as_list(filtered.get("meldingen") if isinstance(filtered, dict) else None)
    index = _previous_count(inp.input_data.get("triage_selecteer_melding"))
    message = messages[index] if index < len(messages) and isinstance(messages[index], dict) else {}
    yield {
        inp.output_key: {
            "index": index,
            "next_index": index + 1,
            "melding_id": str(message.get("ID") or ""),
            "onderwerp": message.get("Subject"),
        }
    }
