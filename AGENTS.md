# Coding-agent instructions

This repository contains dynamic node types for Limescape AI Platform. These
instructions apply to agents working here, including Claude Code via `CLAUDE.md`.

## Read before implementing

1. Read [README.md](README.md) and [CONTRIBUTING.md](CONTRIBUTING.md).
2. Follow [the node-type workflow](docs/agent-node-types.md).
3. For any authenticated integration, read
   [the credential contract](docs/credentials-and-node-types.md) before designing
   fields or writing HTTP calls. Record the chosen credential type, value shape,
   selection mode, identity source and authentication lifecycle in the node's README.
4. Inspect the closest existing node and its tests, and check `compat/legacy/`
   for a code collision. Existing nodes can contain intentional legacy behavior;
   do not copy it into a new contract without checking the guide.

## Boundaries

- Create `src/node-types/<code>/node-type.yaml`, `node.py`, `i18n/nl.json`,
  `i18n/en.json`, `README.md` and behavior tests. Folder name equals manifest code.
- The plugin entry point is an async generator: `execute(ctx, inp)`.
  Import only the standard library, `limescape_plugin_sdk`, declared third-party
  dependencies and relative helpers inside the same node folder.
- Keep execution orchestration small and transformations pure. Never import
  `truelime_ai`, Django, another node type or platform tracing decorators.
- Keep nodes stateless and never commit secrets, customer data or real addresses.
- Preserve output shapes and use synthetic tests.

## Verification

Follow the commands and checks in [docs/agent-node-types.md](docs/agent-node-types.md).
Report which checks actually ran and any remaining platform, release or activation prerequisites.
