# Filter triage messages

Input keys: `triage_configuratie` (object) and `triage_meldingen` (list or
single object). Entries must be objects with a truthy `ID`. Output preserves the
existing shape: `{meldingen: [{ID, Subject, CreationDate}, ...], aantal: n}`.
The configured `max_per_run` defaults to 25 and is clamped to 1–100, matching the
Tribe query's maximum response size.
