from limescape_plugin_sdk import NodeContext, NodeInput, NodeInputError


def _as_list(value: object) -> list[object]:
    if value is None:
        return []
    return value if isinstance(value, list) else [value]


def _maximum(configuration: object) -> int:
    if not isinstance(configuration, dict):
        return 25
    value = configuration.get("max_per_run") or 25
    try:
        return max(1, min(int(value), 100))
    except (TypeError, ValueError) as exc:
        raise NodeInputError("Maximum per run must be an integer") from exc


async def execute(ctx: NodeContext, inp: NodeInput):
    configuration = inp.input_data.get("triage_configuratie") or {}
    messages = [
        item for item in _as_list(inp.input_data.get("triage_meldingen"))
        if isinstance(item, dict) and item.get("ID")
    ]
    selected = messages[: _maximum(configuration)]
    yield {
        inp.output_key: {
            "meldingen": [
                {key: item.get(key) for key in ("ID", "Subject", "CreationDate")}
                for item in selected
            ],
            "aantal": len(selected),
        }
    }
