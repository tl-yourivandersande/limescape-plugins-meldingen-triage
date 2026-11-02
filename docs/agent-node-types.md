# Creating node types with a coding agent

Follow this workflow for dynamic node types in this repository. It does not
itself establish SDK capabilities or platform deployment status.

## Before implementing

Define each node's code, category, purpose, inputs, exact output shape, runtime,
fields and tests. Use codes matching `^[a-z][a-z0-9_]{2,63}$`, check the SDK
catalogue for reserved codes and categories, and avoid collisions with builtins.

## Scaffold

One folder per node under `src/node-types/<code>/` containing `node-type.yaml`,
`node.py`, `i18n/nl.json`, `i18n/en.json`, `README.md` and `tests/test_node.py`.
Use `execute(ctx, inp)` as an async generator, `inp.param(...)` to read fields,
and yield `{inp.output_key: result}`. Declare capabilities and dependencies.
Use only the standard library and the SDK unless dependencies are declared.

Parameter defaults must be handled in code, not assumed to be injected. Declare
required flow input keys in `io.input_data`; optional inputs should be checked by
the plugin. Keep outputs JSON serializable and error messages safe.

## Testing and release

Use `FakeContext(granted=...)` and `run_node` with synthetic fixtures. Test
normal behavior, missing/empty inputs, edge cases and exact output shape. Validate
manifests, translations, imports, tests and lint in CI. Do not claim tests were run
unless they were actually run.

A release is made with a `vX.Y.Z` tag on `main`. CI builds and publishes the
bundle. Limescape administrators register the bundle source and activate it for
the team. Merging, tagging and activation remain human actions.
