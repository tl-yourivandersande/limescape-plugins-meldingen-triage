from datetime import UTC, datetime, timedelta

from limescape_plugin_sdk import NodeContext, NodeInput, NodeInputError


def _lines(value: object) -> list[str]:
    if value is None:
        return []
    if not isinstance(value, str):
        raise NodeInputError("List fields must be text, with one value per line")
    return [line.strip() for line in value.splitlines() if line.strip()]


def _integer(value: object, name: str, low: int, high: int) -> int:
    if isinstance(value, bool) or not isinstance(value, (int, str)):
        raise NodeInputError(f"{name} must be an integer")
    try:
        number = int(value)
    except ValueError as exc:
        raise NodeInputError(f"{name} must be an integer") from exc
    if not low <= number <= high:
        raise NodeInputError(f"{name} must be between {low} and {high}")
    return number


async def execute(ctx: NodeContext, inp: NodeInput):
    mailbox_id = inp.param("mailbox_id", "")
    if not isinstance(mailbox_id, str) or not mailbox_id.strip():
        raise NodeInputError("Mailbox identifier is required")
    days_back = _integer(inp.param("dagen_terug", 3), "Days to look back", 1, 365)
    max_per_run = _integer(inp.param("max_per_run", 25), "Maximum per run", 1, 100)
    label = inp.param("label_nieuwe_melding", "")
    if not isinstance(label, str):
        raise NodeInputError("New-message label identifier must be text")

    now = datetime.now(UTC)
    from_date = (now - timedelta(days=days_back)).replace(hour=0, minute=0, second=0, microsecond=0)
    since = from_date.isoformat(timespec="seconds").replace("+00:00", "Z")
    clauses = [
        f"Mailbox/ID eq {mailbox_id.strip()}",
        "Activity eq null",
        "_2ae5c07f__9046__4d8e__a174__baffb8a43ea6 eq null",
        "_2d685b26__0b59__4f88__8978__050cdf3b7b55 eq null",
        f"CreationDate ge {since}",
        *_lines(inp.param("extra_filters", "")),
    ]
    yield {
        inp.output_key: {
            "mailbox_id": mailbox_id.strip(),
            "label_nieuwe_melding": label.strip(),
            "handmatige_domeinen": _lines(inp.param("handmatige_domeinen", "")),
            "extra_melders": _lines(inp.param("extra_melders", "")),
            "max_per_run": max_per_run,
            "top": str(max_per_run),
            "vanaf": since,
            "filter": " and ".join(clauses),
        }
    }
