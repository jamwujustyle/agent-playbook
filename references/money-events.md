# When a project handles money and external events

Apply only to the relevant area. Specific currencies, fees, permissions,
the financial model, and authorization for operations are defined by the current project.

- Store exact monetary values in an exact decimal or integer representation.
  Define rounding; the total must be preserved when amounts are allocated. Compact UI
  formatting must not change the original precision of evidence, calculations, or payment URIs.
- Verify source authenticity and server-side permissions before processing. Keep secrets
  for different sources separate. The frontend and generated responses are not authoritative.
- Use a stable operation ID and the original timestamp. Repeated delivery must not
  cause a repeated effect; explicitly reject conflicting payloads with the same ID.
- Acceptance of verified evidence, the local financial record, and entitlement grants
  must be atomic and globally idempotent. An external network and a local database
  do not form a single transaction: the gap requires verifiable reconciliation.
  An in-process queue does not protect against another process.
- Bind confirmation to a specific operation or invoice. A matching amount,
  a screenshot, or a public hash is insufficient for attribution to an owner.
- Preserve finalized financial history; make corrections through separate,
  verifiable adjustments. Changes to terms and entitlements must leave an audit trail.
- A transfer record does not move money. Mark an external action as completed
  only after independent confirmation; a manual exception must have an exact scope.
- Calculate cost across the entire path: fees, network costs, activation, intermediate
  transfers, conversion, infrastructure, and conditional expenses. Unknown does not mean zero.
