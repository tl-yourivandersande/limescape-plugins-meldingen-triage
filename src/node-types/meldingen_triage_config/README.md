# Message triage configuration

Builds the runtime settings consumed by the Tribe query and triage sub-agent.
Mailbox/label identifiers, sender/domain lists, time window, maximum and optional
OData clauses are configuration fields; do not hardcode environment-specific IDs
in public plugin code.

Input: none. Output: object with `mailbox_id`, `label_nieuwe_melding`, lists
`handmatige_domeinen` and `extra_melders`, `max_per_run`, string `top`, UTC
`vanaf`, and the combined OData `filter`.

List fields use one item per line. The mailbox identifier must be a valid OData
literal/identifier for the Tribe endpoint; optional clauses are appended as
provided. Review these values for the target environment before use.
