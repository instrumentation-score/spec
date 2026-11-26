# Rule index

Search this page by rule ID or description. Each ID links to the full rule
and its criteria.

To regenerate this index, run `python3 scripts/generate_rule_index.py` from
the repository root.

## LOG

- [LOG-001](LOG-001.md): Debug-level logs are not enabled in production environments for longer than 14 days.
- [LOG-002](LOG-002.md): Log records have their `severityNumber` set.
- [LOG-003](LOG-003.md): Log records do not contain sensitive data such as PII, financial identifiers, credentials, or health information.

## MET

- [MET-001](MET-001.md): Metric attributes have bound cardinality.
- [MET-002](MET-002.md): Metrics have useful metric units.
- [MET-003](MET-003.md): Metric names are consistently associated with the same metric unit.
- [MET-004](MET-004.md): Histogram metrics consistently use the same histogram buckets per metric name.
- [MET-005](MET-005.md): Metric names do not contain the name of the metric unit.
- [MET-006](MET-006.md): Metric names do not equal semantic convention attribute keys.
- [MET-007](MET-007.md): Metrics do not carry volatile or verbose resource attributes.
- [MET-008](MET-008.md): Metrics do not contain sensitive data such as PII, financial identifiers, credentials, or health information.

## RES

- [RES-001](RES-001.md): `service.instance.id` is present.
- [RES-002](RES-002.md): `service.instance.id` is unique across logical resources within a given `service.name`.
- [RES-003](RES-003.md): `k8s.pod.uid` is present in telemetry collected from applications running on a Kubernetes cluster, or from the control pane of the Kubernetes cluster itself.
- [RES-004](RES-004.md): Semantic conventions attributes are used at the right level.
- [RES-005](RES-005.md): `service.name` is present
- [RES-006](RES-006.md): `service.criticality` uses the canonical form of its well-known values
- [RES-007](RES-007.md): `deployment.environment.name` is present
- [RES-010](RES-010.md): Resource attribute values do not contain sensitive data such as PII, financial identifiers, credentials, or health information.

## SDK

- [SDK-001](SDK-001.md): Dependencies (language and runtime) are supported by the SDK.

## SPA

- [SPA-001](SPA-001.md): Traces contain a limited number of `INTERNAL` spans per service.
- [SPA-002](SPA-002.md): Traces do not contain orphan spans.
- [SPA-003](SPA-003.md): Span names have bound cardinality.
- [SPA-004](SPA-004.md): Root spans are not `CLIENT` spans.
- [SPA-005](SPA-005.md): Traces do not contain a high number of short duration spans.
- [SPA-006](SPA-006.md): Spans do not contain sensitive data such as PII, financial identifiers, credentials, or health information.
