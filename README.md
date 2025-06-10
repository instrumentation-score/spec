# Instrumentation Score Specification

> A standardized metric for assessing OpenTelemetry instrumentation quality

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![CNCF Slack](https://img.shields.io/badge/CNCF%20Slack-%23instrumentation--score-blue)](https://cloud-native.slack.com/archives/C08U9NN1XBR)

## Overview

The **Instrumentation Score** is a standardized, vendor-neutral metric that quantifies the quality of OpenTelemetry instrumentation. Represented as a numerical value from **10 to 100**, it provides objective feedback on how well a service or system follows OpenTelemetry best practices and semantic conventions.

The rules defined in this specification are classified into different impact levels, presenting actionable recommendations that teams can implement in order to improve the overall score of their services. These levels provide engineers with a recommended **prioritization** across a range of potential instrumentation issues, allowing them to focus on the most critical actions.

## Target Audience

While this specification can be used and implemented by anyone, we have identified key audiences who will benefit most from the Instrumentation Score:

### 🏢 Observability Platform Vendors

We expect vendors to adopt the Instrumentation Score as a standard metric in their platforms. This provides:
- **Consistent Quality Assessment**: Standardized scoring across different tools and platforms
- **Customer Value**: Clear instrumentation quality insights for users
- **Customer Advisory**: Use the spec as a framework when advising customers on instrumentation best practices

### 👩‍💻 Observability & Engineering Teams

Observability engineers and engineering teams are the primary users who will interpret and act on Instrumentation Scores:
- **Quality Assessment**: Understand instrumentation health at a glance
- **Improvement Guidance**: Get actionable insights for better instrumentation
- **Vendor Independence**: Carry knowledge between different observability platforms
- **Team Communication**: Use common vocabulary when discussing instrumentation quality

We encourage these teams to join the project and contribute their expertise:
- **Real-world Experience**: Share insights about what constitutes good vs. bad instrumentation
- **Rule Development**: Help define and refine scoring criteria
- **Use Case Validation**: Ensure rules reflect practical observability needs
- **Community Growth**: Expand the collective knowledge base

### Why Instrumentation Score?

As OpenTelemetry adoption grows, organizations face challenges with instrumentation quality:
- Missing critical attributes (e.g., `service.name`)
- Inefficient telemetry signal usage
- High cardinality issues
- Incomplete traces
- Inconsistent instrumentation patterns

The Instrumentation Score addresses these challenges by providing:

- **🎯 Common Vocabulary**: Shared language for discussing instrumentation quality
- **📊 Benchmarking**: Meaningful comparisons across services and over time
- **🔧 Actionable Guidance**: Clear feedback to improve instrumentation
- **💰 Efficiency**: Practices that lead to more cost-effective telemetry

## Quick Start

### Understanding Your Score

The Instrumentation Score uses these qualitative categories:

| Score Range | Category              | Meaning                                    |
| ----------- | --------------------- | ------------------------------------------ |
| 90-100      | **Excellent**         | High standard of instrumentation quality   |
| 75-89       | **Good**              | Solid quality; minor improvements possible |
| 50-74       | **Needs Improvement** | Tangible issues requiring attention        |
| 10-49       | **Poor**              | Significant problems needing urgent action |

### How It Works

1. **Analyze OTLP Data**: The score is calculated by analyzing OpenTelemetry Protocol (OTLP) telemetry streams
2. **Apply Rules**: A set of standardized rules evaluate traces, metrics, and resource attributes
3. **Calculate Score**: Mathematical formula combines positive and negative factors
4. **Provide Feedback**: Actionable insights guide improvements

### Score Calculation

The score uses this formula:

```
Score_intermediate = min(100, 80 + P_p - N_m) - N_h
Score_final = max(10, Score_intermediate)
```

Where:
- `P_p`: Points from positive rules (good practices)
- `N_m`: Points from minor negative rules (Low, Normal, Important impact)
- `N_h`: Points from major negative rules (Very Important, Critical impact)

## Documentation

📖 **[Full Specification](./specification.md)** - Complete technical specification  
🔧 **[Contributing Guide](./CONTRIBUTING.md)** - How to contribute to the project  
🏛️ **[Governance](./GOVERNANCE.md)** - Project governance and maintainers  
📚 **[Prior Art](./prior-art.md)** - Research on existing scoring systems  
📋 **[Rules Directory](./rules/)** - Complete set of scoring rules

## Implementation

This specification is designed to be **implementation-agnostic**. Multiple tools can implement the Instrumentation Score calculation while maintaining consistency through the standardized rules.

### Implementation Requirements

- ✅ **MUST** implement all rules defined in this specification
- ✅ **MUST** use the standardized calculation formula
- ✅ **MUST** provide information if not all rules are implemented
- ✅ **MUST NOT** include additional rules that affect the standard score

## Rules Structure

Scoring rules are the foundation of the Instrumentation Score. Each rule includes:

- **ID**: Unique identifier (e.g., `RES-001`, `SPAN-042`)
- **Description**: Human-readable explanation
- **Rationale**: Why this rule matters for quality
- **Criteria**: Objective conditions for rule application
- **Target**: OTLP element type (`Resource`, `TraceSpan`, `Metric`, `Log`)
- **Impact**: Impact level (`Critical`, `Very Important`, `Important`, `Normal`, `Low`)
- **Type**: `Positive` (rewards) or `Negative` (penalizes)

### Example Rule

```yaml
id: RES-001
description: "Service name must be present"
rationale: "service.name is fundamental for service identification and observability"
target: Resource
impact: Critical
type: Negative
criteria: "Resource attributes must contain 'service.name' key with non-empty value"
```

## Community

### Get Involved

We welcome contributions from the OpenTelemetry community! Here's how to participate:

- 💬 **Join Discussion**: [CNCF Slack #instrumentation-score](https://cloud-native.slack.com/archives/C08U9NN1XBR)
- 🐛 **Report Issues**: [GitHub Issues](https://github.com/instrumentation-score/spec/issues)
- 🔀 **Submit Changes**: Follow our [contributing guide](./CONTRIBUTING.md)
- 📅 **Attend Meetings**: Community meetings (schedule in Slack)

### Maintainers

- [Antoine Toulme](https://github.com/atoulme) (@atoulme), Splunk
- [Daniel Gomez Blanco](https://github.com/danielgblanco) (@danielgblanco), New Relic
- [Juraci Paixão Kröhling](https://github.com/jpkrohling) (@jpkrohling), OllyGarden
- [Michele Mancioppi](https://github.com/mmanciop) (@mmanciop), Dash0

## Project Status

**Current Status**: Active development and community feedback  

This is an open-source specification initiated by [OllyGarden](https://olly.garden) with the goal of becoming a community-governed standard for instrumentation quality assessment.

## Relationship to OpenTelemetry

The Instrumentation Score specification:

- 🏗️ **Builds on** OpenTelemetry Semantic Conventions
- 📊 **Analyzes** OTLP telemetry data streams  
- 🔧 **Complements** existing observability tools
- 🎯 **Guides** effective use of OTel SDKs and Collector
- 🤝 **Intended for** integration with the OpenTelemetry ecosystem

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- OpenTelemetry project and community
- All contributors and community members

---

**Start improving your instrumentation quality today!** 🚀

For questions, feedback, or discussions, join us in the [CNCF Slack #instrumentation-score channel](https://cloud-native.slack.com/archives/C08U9NN1XBR).
