# Select triage message

Input key: `triage_filter`; optional loop-history key:
`triage_selecteer_melding`. Output preserves the existing shape: `index`,
`next_index`, `melding_id` and `onderwerp`. The loop counter follows the current
Python-node behavior: no previous output means index 0; one prior output means
index 1, and so on.
