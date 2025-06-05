**Rule ID:** \[Unique Rule ID\]

**Description:** \[A brief, clear statement describing the purpose of the rule and what condition it checks for.\]

**Rationale:** \[Explanation of why this rule is important for instrumentation quality. What benefit does adherence provide, or what problem does non-adherence cause? Link to relevant OpenTelemetry specifications (e.g., Semantic Conventions) or established best practices if applicable. Explain the impact on observability, efficiency, or cost.\]

**Target:** \[Specify the primary OTLP element this rule evaluates: Resource | Span | Metric | Log | Profile | Other (Specify) or the component: SDK | Collector | Other (Specify)\]

**Criteria:** \[The precise, objective conditions under which this rule is triggered when analyzing OTLP data. This description must be unambiguous and algorithmically testable. Provide specific attribute names, expected values or patterns, conditions for presence/absence, thresholds, etc. Use backticks for attribute names or code elements.\]

**Examples:**

* *"Resource attribute service.name is missing, null, or an empty string."*  
* *"A Span has span.kind \= SpanKind.SPAN\_KIND\_SERVER but is missing the http.route attribute when http.request.method is present."*  
* *"A Metric point of type Sum has aggregation\_temporality \= AGGREGATION\_TEMPORALITY\_DELTA and is\_monotonic \= true, but its name does not end with the suffix \_total."*  
* *"More than 10 spans within the service in a single trace have a duration less than 5 milliseconds."*  
* *"A log record with severity\_text \= 'DEBUG' is observed in an environment where the Resource attribute deployment.environment.name is set to production."*

**Severity:** \[Choose one: Critical | Very Important | Important | Normal | Low\] (Based on the perceived impact of violating this rule on overall observability effectiveness or efficiency.)

**Type:** \[Choose one: Positive | Negative\] (Indicates if the rule adds points for good practice or subtracts points for deficiency.)  
