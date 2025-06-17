# Contributing to the Instrumentation Score Specification

Thank you for your interest in contributing to the Instrumentation Score Specification! This document provides guidelines for contributing to the project.

## Table of Contents

- [Getting Started](#getting-started)
- [Ways to Contribute](#ways-to-contribute)
- [Contributing to the Specification](#contributing-to-the-specification)
- [Contributing Rules](#contributing-rules)
- [Submitting Changes](#submitting-changes)
- [Communication](#communication)
- [Code of Conduct](#code-of-conduct)

## Getting Started

The Instrumentation Score Specification defines a standardized metric for assessing OpenTelemetry instrumentation quality. Before contributing, please:

1. **Read the specification**: Review the main [specification.md](./specification.md) document
2. **Understand the goals**: Familiarize yourself with the project's objectives and scope
3. **Join the community**: Connect with us on [CNCF Slack #instrumentation-score](https://cloud-native.slack.com/archives/C090FEG5R0F)
4. **Review existing issues**: Check [GitHub Issues](https://github.com/instrumentation-score/spec/issues) for current discussions

## Ways to Contribute

We welcome various types of contributions:

### 📝 Documentation
- Improve specification clarity and completeness
- Fix typos, grammar, and formatting
- Add examples and use cases
- Enhance explanations of concepts

### 📋 Rules Development
- Propose new scoring rules
- Improve existing rule definitions
- Provide rationale for rule changes
- Contribute rule validation examples

### 🐛 Issue Reporting
- Report ambiguities or gaps in the specification
- Suggest improvements to existing rules
- Identify inconsistencies or contradictions

### 💡 Feature Proposals
- Suggest new features or capabilities
- Propose extensions to the scoring framework
- Share implementation experiences and feedback

### 🔬 Research and Analysis
- Provide research on instrumentation best practices
- Share data on real-world instrumentation patterns
- Contribute analysis of scoring effectiveness

## Contributing to the Specification

### Specification Structure

The main specification is organized into these key sections:
- **Introduction**: Project overview and goals
- **Prior Art**: Learning from existing scoring systems
- **Goals and Non-Goals**: Project scope definition
- **Detailed Specification**: Core technical specification
- **Score Calculation**: Mathematical framework
- **Rule Structure**: How rules are defined and applied

### Making Specification Changes

1. **Small Changes**: For minor fixes (typos, clarifications), submit a pull request directly
2. **Significant Changes**: For major modifications, start with an issue to discuss the proposal

### Specification Guidelines

- **Clarity**: Write clearly and avoid ambiguous language
- **Completeness**: Ensure all concepts are fully defined
- **Consistency**: Maintain consistent terminology throughout
- **Implementability**: Ensure the specification can be practically implemented
- **Vendor Neutrality**: Avoid favoring specific tools or vendors

## Contributing Rules

Rules are the core mechanism for calculating instrumentation scores. They are located in the `rules/` directory.

### Rule Structure

Each rule must include:
- **ID**: Unique identifier (e.g., RES-001, SPAN-042)
- **Description**: Clear, human-readable explanation
- **Rationale**: Why this rule matters for instrumentation quality
- **Criteria**: Specific, objective conditions for rule application
- **Target**: Which OTLP element it applies to (Resource, TraceSpan, Metric, Log)
- **Impact**: Impact level (Critical, Important, Normal, Low)

### Rule Guidelines

- **Objective**: Rules must be measurable and unambiguous
- **Based on Standards**: Align with OpenTelemetry Semantic Conventions
- **Well-Justified**: Include clear rationale for the rule's importance
- **Implementable**: Ensure rules can be consistently implemented across tools
- **Tested**: Provide examples of when the rule should and shouldn't trigger

### Proposing New Rules

1. **Research**: Ensure the rule aligns with OpenTelemetry best practices
2. **Issue First**: Create an issue describing the proposed rule
3. **Community Input**: Allow time for community discussion
4. **Implementation**: Submit a pull request with the complete rule definition

## Submitting Changes

### Pull Request Process

1. **Fork the Repository**: Create your own fork of the project
2. **Create a Branch**: Use a descriptive branch name (e.g., `add-service-version-rule`)
3. **Make Changes**: Implement your changes with clear, focused commits
4. **Test**: Ensure your changes don't break existing content
5. **Submit PR**: Create a pull request with a clear description

### Pull Request Guidelines

- **Title**: Use a clear, descriptive title, following [conventional commits](https://www.conventionalcommits.org/en/v1.0.0/)
- **Description**: Explain what changes you made and why
- **Scope**: Keep PRs focused on a single issue or feature
- **Documentation**: Update related documentation as needed

### Commit Message Format

Use clear, descriptive commit messages:
```
feat: add rule for missing `service.version` attribute

- Defines RES-002 rule for service.version presence
- Categorized as "Important" impact
- Includes rationale and implementation criteria
```

## Communication

### Discussion Channels

- **GitHub Issues**: For specific problems, proposals, and bugs
- **CNCF Slack**: Join [#instrumentation-score](https://cloud-native.slack.com/archives/C090FEG5R0F) for real-time discussion
- **Pull Requests**: For code and documentation review discussions

### Getting Help

If you need assistance:
1. Check existing documentation and issues
2. Ask questions in the CNCF Slack channel
3. Create a GitHub issue with the "question" label
4. Reach out to the maintainers directly

### Community Meetings

We hold regular community meetings to discuss:
- Project roadmap and priorities
- Rule proposals and changes
- Implementation feedback
- Community questions and concerns

Meeting details will be announced in the CNCF Slack channel and GitHub discussions.

## Code of Conduct

This project follows the [CNCF Code of Conduct](https://github.com/cncf/foundation/blob/master/code-of-conduct.md). By participating, you agree to uphold this code. Please report unacceptable behavior to the project maintainers.

### Our Standards

- **Inclusive**: Welcome contributors from all backgrounds
- **Respectful**: Treat everyone with respect and professionalism
- **Collaborative**: Work together constructively
- **Constructive**: Provide helpful, actionable feedback

## Recognition

Contributors are recognized in several ways:
- Contributors are listed in project documentation
- Significant contributors may be invited to become maintainers
- Community achievements are highlighted in project communications

## Questions?

If you have questions about contributing, please:
- Join our [CNCF Slack channel](https://cloud-native.slack.com/archives/C090FEG5R0F)
- Create a GitHub issue with the "question" label
- Review the [governance document](./GOVERNANCE.md) for project structure

Thank you for contributing to the Instrumentation Score Specification!
