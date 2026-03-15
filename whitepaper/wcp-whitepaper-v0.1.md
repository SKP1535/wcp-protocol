# Work Coordination Protocol (WCP)

## An Open Standard for Coordinating Work Between Humans and AI Agents

Version: Draft v0.1\
Author: Saurabh Kumar\
Date: March 2026

------------------------------------------------------------------------

# Abstract

Artificial intelligence systems are rapidly evolving from passive
computational tools into autonomous agents capable of executing complex
tasks. Large language models and agent frameworks have demonstrated the
potential for software systems that can reason, plan, and perform
actions on behalf of users.

Despite these advances, modern AI agents operate primarily within
isolated environments. Task execution and workflow management are
typically implemented through proprietary APIs or tightly coupled
application architectures. This fragmentation prevents agents from
collaborating across platforms and limits the development of open
ecosystems where autonomous systems can coordinate work.

This paper introduces the **Work Coordination Protocol (WCP)**, an open
protocol designed to standardize how work is represented, distributed,
executed, and completed across heterogeneous systems. WCP defines a
minimal set of primitives including **work objects, agents,
capabilities, and events**, enabling humans and AI agents to collaborate
through a shared coordination model.

------------------------------------------------------------------------

# 1. Introduction

Recent developments in artificial intelligence have enabled systems
capable of performing increasingly complex tasks. Advances in large
language models and agent architectures have made it possible for
software agents to plan actions, interact with external systems, and
execute workflows that previously required human intervention.

However, despite the rapid progress in agent capabilities, there is
currently **no widely adopted standard for coordinating work between
autonomous agents and human users**.

Most task coordination today occurs within application-specific
environments such as project management systems, workflow automation
platforms, or proprietary AI frameworks. These systems define their own
task structures and execution models, which prevents interoperability
between applications.

The Work Coordination Protocol (WCP) proposes a standardized model for
representing and coordinating work across heterogeneous systems.

------------------------------------------------------------------------

# 2. Background and Motivation

The history of distributed systems demonstrates the importance of
standardized communication protocols.

Examples include:

-   HTTP -- standardizing web communication\
-   SMTP -- standardizing email delivery\
-   BitTorrent -- peer‑to‑peer distributed file sharing

Each of these protocols enabled independent systems to interoperate
through shared conventions.

In contrast, modern AI agent systems lack such a standard for
coordinating work.

------------------------------------------------------------------------

# 3. Design Principles

The Work Coordination Protocol is designed according to several key
principles.

### Simplicity

Protocols that succeed tend to define small sets of primitives that can
be extended over time.

### Interoperability

Different systems implementing WCP should be able to exchange work
objects and coordinate execution.

### Extensibility

The protocol must allow future extensions such as:

-   distributed work networks
-   multi-agent collaboration
-   decentralized discovery mechanisms

### Agent Compatibility

WCP must support both human-driven workflows and autonomous AI agents.

------------------------------------------------------------------------

# 4. Core Concepts

The Work Coordination Protocol introduces four primary primitives:

-   Work
-   Agent
-   Capability
-   Event

------------------------------------------------------------------------

## 4.1 Work

A **Work Object** represents a unit of executable work.

Example:

``` json
{
  "work_id": "work_123",
  "type": "email.send",
  "status": "ready",
  "priority": "medium",
  "context": {
    "to": "alice@example.com",
    "subject": "Meeting Reminder"
  }
}
```

Fields:

  Field     Description
  --------- ----------------------
  work_id   unique identifier
  type      category of work
  status    lifecycle state
  context   execution parameters

------------------------------------------------------------------------

## 4.2 Agent

An **Agent** is an entity capable of executing work.

Agents may include:

-   AI systems
-   automation services
-   software applications
-   human operators

Example:

``` json
{
  "agent_id": "email_agent",
  "capabilities": ["email.send"]
}
```

------------------------------------------------------------------------

## 4.3 Capability

Capabilities define the types of work an agent can perform.

Examples:

-   email.send
-   calendar.schedule
-   travel.book_flight
-   payment.process

Capabilities allow systems to match work objects with compatible agents.

------------------------------------------------------------------------

## 4.4 Event

Events communicate changes in work state.

Examples:

-   work.created
-   work.assigned
-   work.started
-   work.completed
-   work.failed

------------------------------------------------------------------------

# 5. Work Lifecycle

Standard lifecycle:

created → ready → running → completed\
                         ↘ failed

State definitions:

-   **created** -- work registered
-   **ready** -- available for execution
-   **running** -- agent executing
-   **completed** -- execution finished
-   **failed** -- execution unsuccessful

------------------------------------------------------------------------

# 6. Protocol Operations

Typical operations include:

Create Work POST /work

Claim Work POST /work/{id}/claim

Start Work POST /work/{id}/start

Complete Work POST /work/{id}/complete

Fail Work POST /work/{id}/fail

------------------------------------------------------------------------

# 7. System Architecture

Typical architecture:

User Interface\
↓\
Work API\
↓\
Work Engine\
↓\
Event Bus\
↓\
Agent Workers

Components:

-   Work API -- interface for creating work objects
-   Work Engine -- manages lifecycle
-   Event Bus -- broadcasts state changes
-   Agent Workers -- execute work

------------------------------------------------------------------------

# 8. Example Workflow

User request:

"Plan my trip to Goa"

Generated work:

-   search_flights
-   book_flight
-   find_hotels
-   create_itinerary
-   notify_user

Agents execute tasks and publish completion events.

------------------------------------------------------------------------

# 9. Security Considerations

Important security considerations:

Authentication -- agents must authenticate\
Authorization -- capability-based execution\
Validation -- work object validation\
Auditability -- lifecycle logs

------------------------------------------------------------------------

# 10. Future Directions

Future protocol expansions may include:

-   Distributed work networks
-   Agent marketplaces
-   Work dependency graphs
-   Peer-to-peer coordination

These could enable ecosystems where autonomous agents collaborate
globally.

------------------------------------------------------------------------

# Conclusion

The Work Coordination Protocol proposes a universal abstraction for
coordinating work between humans and AI agents.

By defining shared primitives for work objects, agent capabilities,
lifecycle states, and events, WCP provides a foundation for
interoperable agent ecosystems.

As autonomous systems become more capable, open coordination protocols
will play an increasingly important role in enabling collaboration
across platforms.

------------------------------------------------------------------------