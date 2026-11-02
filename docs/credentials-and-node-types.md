# Credentials and node types

These flow nodes are pure data transformations and do not use credentials.
If a future node needs authentication, document its credential type, value shape,
selection mode, identity source and authentication lifecycle. Follow the current
SDK and platform credential contract; never store secrets in node parameters or
source code.
