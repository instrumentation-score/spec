# **Introduction**

The OpenTelemetry project provides a powerful, vendor-neutral framework for instrumenting, generating, collecting, and exporting telemetry data (traces, metrics, logs). However, as adoption grows, organizations often face challenges with the *quality* and *consistency* of their instrumentation. Issues like missing critical attributes (e.g., `service.name`), inefficient use of telemetry signals (e.g., using verbose logs where metrics suffice), high cardinality, or incomplete traces can hinder observability effectiveness, increase costs, and make troubleshooting difficult. Currently, the OpenTelemetry ecosystem lacks a standardized, transparent, and objective method for assessing the quality of this instrumentation.

To address this gap, this document proposes a specification for a standardized **Instrumentation Score**. This score, represented as a numerical value ranging from **10 to 100**, aims to provide a quantifiable measure of how well a service or system is instrumented according to OpenTelemetry best practices and semantic conventions. It is calculated by analyzing OpenTelemetry Protocol (OTLP) data streams against a defined set of rules.

The introduction of such a standard score offers several significant benefits:

1. **Common Vocabulary:** It establishes a shared language for discussing instrumentation quality among developers, SREs, platform teams, and vendors.  
2. **Benchmarking:** It enables meaningful comparisons of instrumentation quality across different services within an organization, or tracking improvements over time.  
3. **Actionable Guidance:** The score and its underlying components are designed to provide clear, actionable feedback, helping teams identify specific areas for improvement.  
4. **Efficiency Promotion:** It encourages practices that lead to more efficient and effective telemetry pipelines, potentially reducing data volume and associated costs.

This specification is presented as an initial draft (Version 0.1) and is being initiated as an open-source effort by [OllyGarden](https://olly.garden), with the explicit goal of soliciting community feedback and eventually hosting it under an open governance model, hopefully integrated into the OpenTelemetry project. It focuses on defining the core scoring framework, the structure of the rules, and the calculation methodology, rather than mandating or endorsing any specific software tool for its implementation.

## **Target Audience**

This specification is designed for technical stakeholders involved in implementing, adopting, or evaluating the Instrumentation Score standard:

### **Tool and Platform Implementers**

- **Observability Platform Vendors**: Teams building commercial or open-source observability platforms who want to integrate standardized instrumentation scoring, and who can use the spec as a framework when advising customers on instrumentation best practices
- **Tool Developers**: Engineers creating standalone tools for instrumentation analysis and scoring
- **Integration Engineers**: Technical teams implementing the score calculation within existing observability infrastructure

### **Technical Decision Makers**

- **Platform Engineering Teams**: Engineers responsible for observability strategy and tooling decisions within organizations
- **SRE and DevOps Teams**: Teams evaluating instrumentation quality assessment solutions for their production environments
- **Engineering Managers**: Technical leaders assessing the value and feasibility of adopting instrumentation scoring standards

### **Community Contributors**

- **OpenTelemetry Contributors**: Community members interested in extending or refining the scoring methodology
- **Observability Engineers**: Practitioners with real-world experience who can contribute insights about effective instrumentation patterns
- **Standards Enthusiasts**: Technical professionals interested in contributing to open observability standards

This specification assumes familiarity with OpenTelemetry concepts, OTLP data formats, and observability engineering practices.

## **Learning from Prior Art in Scoring**

Before defining the specifics, it's valuable to consider established scoring systems in other technical domains:

* **CVSS (Common Vulnerability Scoring System):** This standard for vulnerability impact demonstrates the power of a transparent, multi-faceted scoring system based on clearly defined metrics. Its separation of a universal base score from contextual modifiers is also instructive. The key takeaway is the importance of **standardization and transparency** for wide adoption and trust.
* **Google Lighthouse:** Scoring web page quality, Lighthouse excels at linking scores directly to **actionable recommendations**, making it highly valuable for users seeking improvement. Its use of weighted averages and data-driven thresholds also provides useful patterns.  
* **SonarQube Quality Gate:** By using Pass/Fail gates based on code metrics, SonarQube shows how quality scores can be integrated into **developer workflows** (like CI/CD pipelines) to enforce standards, particularly focusing on the quality of *new* code.  
* **SSL Labs Server Test:** This TLS configuration grader effectively uses **grade capping**, where critical flaws (like weak protocols) limit the maximum achievable score, regardless of other positive factors. It also rewards exceptional configurations (e.g., HSTS for an A+), providing clear incentives.

These examples underscore the need for the Instrumentation Score to be standardized, transparent, actionable, multi-faceted, and governed effectively, incorporating mechanisms to reflect the critical impact of major deficiencies. A more comprehensive research on the existing prior art is available at [Prior art for Instrumentation Score](./prior-art.md).

## **Specification Goals and Non-Goals**

The primary **goals** of this specification are to:

* Define a **standardized**, vendor-neutral metric for instrumentation quality.  
* Provide **quantifiable and transparent** feedback via a numerical score (10-100) and an open calculation method.  
* Offer **actionable insights** by structuring the score to guide improvements.  
* **Promote best practices** in line with OpenTelemetry standards.  
* Establish a **governed framework** allowing for community-driven evolution.  
* Create a basis for **benchmarking** instrumentation quality.

It is explicitly **not** the goal of this specification to:

* Mandate or endorse specific software tools for score calculation.  
* Define a system for real-time alerting on instrumentation issues.  
* Dictate specific backend implementation details (databases, architecture).  
* Cover every niche instrumentation scenario in initial versions.  
* Replace existing observability dashboards or analysis tools.

## **Detailed Specification**

### **Overview**

The Instrumentation Score is a numerical value between 10 (Poor) and 100 (Excellent). It assesses the quality of instrumentation based on the automated analysis of OTLP telemetry data streams, primarily focusing on Traces and associated Resource attributes in its initial conception, with potential future expansion to Metrics and Logs. The score is typically calculated per `service.name`, representing the quality over a defined sliding time window (defaulting to 30 days). Implementations may support aggregation to higher levels (e.g., organization-wide), potentially applying additional rules at that level. The calculation relies on applying a defined set of Rules to the observed telemetry. Implementations MUST NOT include other rules to the instrumentation score that don't belong to the specification: the instrumentation score obtained by a service using a specific implementation must yield the same instrumentation score when using a different implementation. If an implementation doesn't implement all rules, they MUST provide information to their users that the instrumentation score might not be complete.

### **Rules**

The scoring mechanism is driven by rules derived primarily from OpenTelemetry Semantic Conventions and community-accepted best practices. Each rule must be clearly defined with the following attributes:

* ID: A unique, stable identifier (e.g., RES-001).
* Description: A human-readable explanation.
* Rationale: Justification for the rule's importance to quality.
* Criteria: The specific, objective conditions within OTLP data that trigger the rule.
* Target: The OTLP signal or element it applies to. Must be one of: `Resource`, `TraceSpan`, `Metric`, `Log`.
* Impact: An assigned importance level influencing score impact. Must be one of: `Critical`, `Very Important`, `Important`, `Normal`, `Low`.
* Type: Indicates the rule's effect: `Positive` (rewards good practice) or `Negative` (penalizes deficiency).

The initial proposed point values are:

* Critical: 40 points (Negative rules only)  
* Very Important: 20 points  
* Important: 10 points  
* Normal: 5 points  
* Low: 1 point

### **Score Calculation Formula**

The final score (*Scorefinal​*) reflects a balance of positive and negative factors, ensures major issues significantly impact the score, and adheres to the 10-100 range.

* **Terms Definition:**  
  * *Pp​*: Sum of points from all triggered *positive* rules.  
  * *Nm​*: Sum of points from all triggered *negative* rules with Impact Low, Normal, or Important.
  * *Nh​*: Sum of points from all triggered *negative* rules with Impact Very Important or Critical.
* **Calculation Steps:**  
  1. Calculate Intermediate Score: Start with a base score (default 80), add positive points, subtract minor negative points, cap at 100, and then subtract the full impact of major negative points.  
     	*Scoreintermediate​\=min(100,80+Pp​−Nm​)−Nh​*  
  2. Apply Floor/Ceiling: Ensure the final score is within the 10 to 100 range.  
     	*Scorefinal​\=max(10,Scoreintermediate​)*  
* **Rationale:** This structure ensures that while good practices (*Pp​*) can offset minor issues (*Nm​*), major deficiencies (*Nh*​) act as a significant deterrent, potentially capping the achievable score, aligning with lessons from prior art like SSL Labs. The base score of 80 provides a neutral starting point, and the final `max(10, ...)` prevents demotivating zero scores. The base score and point values are initial suggestions requiring validation with real-world workloads.

### **Qualitative Categories**

To simplify interpretation, the numerical score is mapped to intuitive qualitative categories:

| Score Range | Category | Interpretation Guidance |
| :---- | :---- | :---- |
| 90 \- 100 | **Excellent** | Represents a high standard of instrumentation quality. |
| 75 \- 89 | **Good** | Solid, acceptable quality; minor improvements may be possible. |
| 50 \- 74 | **Needs Improvement** | Indicates tangible issues requiring attention and remediation. |
| 10 \- 49 | **Poor** | Signals significant instrumentation problems needing urgent action. |

These ranges provide clear signals for action, with "Excellent" being a distinct achievement and "Poor" indicating likely critical issues.

### **Initial Rule Set Considerations**

The initial set of official rules should prioritize high-impact, widely applicable checks, primarily based on stable OpenTelemetry Semantic Conventions and focusing on foundational elements like Traces and Resource attributes. A comprehensive rule set accompanies this repository under the [rules](./rules/) directory, but illustrative examples include:

* *Negative Rules:* Missing `service.name` (Critical), missing `service.version` (Very Important), missing `deployment.environment.name` (Normal), patterns suggesting logs used inefficiently instead of metrics (Normal), high cardinality detected in metric dimensions (Important).  
* *Positive Rules:* Presence of recommended attributes like `service.instance.id` (Important).

## **Intended Usage and Benefits**

The Instrumentation Score serves multiple purposes:

* Providing direct **feedback to developers** to guide instrumentation improvements.  
* Allowing **platform teams** to track quality trends across services.  
* Establishing a basis for internal **benchmarking**.  
* Highlighting areas for **optimization** to improve telemetry efficiency and potentially reduce costs.  
* Creating a **common language** for discussing instrumentation quality.  
* Serving as a standard metric for **consultants and auditors**.

## **Relationship to the OpenTelemetry Ecosystem**

This specification is deeply intertwined with the OpenTelemetry project:

* It **leverages** OpenTelemetry Semantic Conventions as the primary source for rule definitions and OTLP as the data format analyzed.  
* It **informs** users about the effectiveness of their instrumentation choices made using OTel SDKs and configurations within the OTel Collector.  
* It **complements** existing observability backends and visualization tools by providing a focused metric on instrumentation quality itself.  
* It is intended for eventual submission to a neutral ground, perhaps as a CNCF project or OpenTelemetry SIG.
