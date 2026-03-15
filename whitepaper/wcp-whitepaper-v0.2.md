# Work Coordination Protocol (WCP)

## An Open Standard for Coordinating Work Between Humans and AI Agents

**Version:** Draft v0.2
**Author:** Saurabh Kumar
**Date:** March 2026

---

# Abstract

Artificial intelligence systems are rapidly evolving from passive computational tools into autonomous agents capable of executing complex tasks. Large language models and agent frameworks have demonstrated the potential for software systems that can reason, plan, and perform actions on behalf of users.

Despite these advances, modern AI agents operate primarily within isolated environments. Task execution and workflow management are typically implemented through proprietary APIs or tightly coupled application architectures. This fragmentation prevents agents from collaborating across platforms and limits the development of open ecosystems where autonomous systems can coordinate work.

This paper introduces the **Work Coordination Protocol (WCP)**, an open protocol designed to standardize how work is represented, distributed, executed, and completed across heterogeneous systems. WCP defines a minimal set of primitives including **work objects, agents, capabilities, and events**, enabling humans and AI agents to collaborate through a shared coordination model.

The protocol also introduces mechanisms for **workflow dependencies, event-driven coordination, capability discovery, and distributed scheduling**, enabling scalable collaboration between autonomous systems.

---

# 1. Introduction

Recent developments in artificial intelligence have enabled systems capable of performing increasingly complex tasks. Advances in large language models and agent architectures have made it possible for software agents to plan actions, interact with external systems, and execute workflows that previously required human intervention.

However, despite rapid progress in agent capabilities, there is currently **no widely adopted standard for coordinating work between autonomous agents and human users**.

Most task coordination today occurs within application-specific environments such as:

* project management systems
* workflow automation platforms
* proprietary AI orchestration frameworks

These systems define their own task structures and execution models, preventing interoperability between applications.

The **Work Coordination Protocol (WCP)** proposes a standardized model for representing and coordinating work across heterogeneous systems.

---

# 2. Background and Motivation

The history of distributed systems demonstrates the importance of standardized communication protocols.

Examples include:

| Protocol   | Purpose                        |
| ---------- | ------------------------------ |
| HTTP       | Standardized web communication |
| SMTP       | Standardized email delivery    |
| BitTorrent | Peer-to-peer file distribution |

These protocols enabled independent systems to interoperate through shared conventions.

In contrast, modern AI agents lack a universal protocol for coordinating work execution across platforms.

As AI systems become increasingly autonomous, the absence of such a protocol limits the development of collaborative agent ecosystems.

---

# 3. Design Principles

The Work Coordination Protocol is designed according to several key principles.

### Simplicity

Protocols that succeed tend to define small sets of primitives that can be extended over time.

### Interoperability

Different systems implementing WCP should be able to exchange work objects and coordinate execution.

### Extensibility

The protocol must support future features such as:

* distributed work networks
* agent marketplaces
* decentralized discovery mechanisms

### Agent Compatibility

WCP must support both **human-driven workflows and fully autonomous agents**.

---

# 4. Core Concepts

WCP introduces four fundamental primitives.

| Primitive  | Description                       |
| ---------- | --------------------------------- |
| Work       | Unit of executable work           |
| Agent      | Entity capable of executing work  |
| Capability | Type of work an agent can perform |
| Event      | Lifecycle notification            |

---

## 4.1 Work

A **Work Object** represents a unit of executable work.

Example:

```json
{
  "work_id": "work_123",
  "type": "email.send",
  "status": "ready",
  "context": {
    "to": "alice@example.com",
    "subject": "Meeting Reminder"
  }
}
```

Fields:

| Field   | Description          |
| ------- | -------------------- |
| work_id | unique identifier    |
| type    | work category        |
| status  | lifecycle state      |
| context | execution parameters |

---

## 4.2 Agent

An **Agent** is an entity capable of executing work.

Agents may include:

* AI systems
* automation services
* software applications
* human operators

Example:

```json
{
  "agent_id": "email_agent",
  "capabilities": ["email.send"]
}
```

---

## 4.3 Capability

Capabilities describe the types of work an agent can perform.

Examples:

```
email.send
calendar.schedule
travel.book_flight
payment.process
```

Capabilities enable systems to match work objects with compatible agents.

---

## 4.4 Event

Events communicate lifecycle transitions.

Examples include:

```
work.created
work.claimed
work.started
work.completed
work.failed
```

Event messaging enables **event-driven coordination between agents**.

---

# 5. Work Lifecycle

A work object progresses through a standardized lifecycle.

```
created → ready → running → completed
                    ↘
                     failed
```

Lifecycle definitions:

| State     | Description             |
| --------- | ----------------------- |
| created   | work registered         |
| ready     | available for execution |
| running   | agent executing         |
| completed | execution successful    |
| failed    | execution unsuccessful  |

---

# 6. Work Graphs

Many real-world tasks require multiple dependent steps.

WCP introduces **Work Graphs**, allowing work objects to define dependencies on other work objects.

Example workflow:

```
search_flights
find_hotels
      ↓
create_itinerary
      ↓
notify_user
```

Work graphs enable:

* multi-agent collaboration
* parallel task execution
* workflow orchestration

This capability transforms WCP from a simple task protocol into a **workflow coordination protocol**.

---

# 7. Protocol Architecture

A typical WCP system contains several components.

```
User Interface
      ↓
Work API
      ↓
Work Engine
      ↓
Event Bus
      ↓
Agent Workers
```

Components include:

| Component   | Role                           |
| ----------- | ------------------------------ |
| Work API    | create and manage work objects |
| Work Engine | lifecycle and scheduling       |
| Event Bus   | distributes events             |
| Agents      | execute work                   |

---

# 8. Protocol Specification Set

The protocol is defined through proposal documents.

| Proposal  | Description                |
| --------- | -------------------------- |
| WCP-P0001 | Work Object                |
| WCP-P0002 | Work Lifecycle             |
| WCP-P0003 | Agent Capabilities         |
| WCP-P0004 | Event Messaging            |
| WCP-P0005 | Work Claiming & Scheduling |
| WCP-P0006 | Work Graphs                |
| WCP-P0007 | Authentication & Security  |
| WCP-P0008 | Capability Discovery       |

This modular proposal structure allows the protocol to evolve incrementally.

---

# 9. Reference Implementation

A reference implementation of WCP is provided using **FastAPI**.

The reference server demonstrates:

* work creation
* agent registration
* work claiming
* lifecycle transitions
* event emission

This implementation provides a foundation for developers experimenting with the protocol.

---

# 10. Developer Ecosystem

To simplify adoption, WCP includes developer tooling:

| Tool         | Purpose                   |
| ------------ | ------------------------- |
| Python SDK   | build WCP agents          |
| CLI Tool     | interact with WCP servers |
| OpenAPI Spec | API interoperability      |

These tools allow developers to quickly build agents and test distributed coordination workflows.

---

# 11. Security Considerations

Security is essential in distributed agent environments.

Important considerations include:

* agent authentication
* capability-based authorization
* work validation
* audit logging

Future versions of the protocol may include:

* cryptographic event signing
* decentralized identity
* agent reputation systems

---

# 12. Future Directions

Future protocol extensions may include:

* distributed work networks
* agent marketplaces
* peer-to-peer work routing
* decentralized discovery

These developments could enable large-scale ecosystems where autonomous agents collaborate across the internet.

---

# Conclusion

The Work Coordination Protocol proposes a universal abstraction for coordinating work between humans and AI agents.

By defining shared primitives for work objects, agent capabilities, lifecycle states, and event messaging, WCP provides a foundation for interoperable agent ecosystems.

As autonomous systems become increasingly capable, open coordination protocols will play an important role in enabling collaboration across platforms.

WCP represents an early exploration of how such a protocol might be structured and implemented.

---
