# WCP-P0008: Capability Discovery

Status: Draft
Author: Saurabh Kumar
Created: 2026-03-15
Protocol Version: WCP v0.1

---

## Abstract

This proposal defines the capability discovery mechanism used by the Work Coordination Protocol (WCP).

Capability discovery allows systems and agents to identify which agents are capable of executing specific types of work.

---

## Motivation

In distributed agent environments, systems must determine which agents can perform specific tasks.

Without capability discovery, work routing becomes inefficient and requires manual configuration.

Capability discovery enables automated matching between work objects and agents.

---

## Capability Registry

Implementations may maintain a capability registry containing registered agents and their capabilities.

Example registry entry:

```json
{
  "agent_id": "travel_agent",
  "capabilities": [
    "travel.search_flights",
    "travel.book_flight"
  ]
}
```

---

## Agent Registration

Agents register capabilities with the system.

Example request:

```text
POST /agents/register
```

Payload:

```json
{
  "agent_id": "calendar_agent",
  "capabilities": [
    "calendar.schedule",
    "calendar.cancel"
  ]
}
```

---

## Capability Query

Systems may query the registry to discover available agents.

Example query:

```text
GET /agents?capability=email.send
```

Example response:

```json
[
  {
    "agent_id": "email_agent_01"
  },
  {
    "agent_id": "notification_agent"
  }
]
```

---

## Work Routing

Capability discovery enables automatic work routing.

Example workflow:

```text
work created → system identifies capability → agent selected
```

Example:

```text
Work Type: email.send
Agent Capabilities: ["email.send"]
```

The system routes work to a compatible agent.

---

## Capability Namespacing

Capabilities should follow hierarchical naming conventions.

Example:

```text
domain.action
```

Examples include:

```text
email.send
calendar.schedule
travel.book_flight
payment.process
```

Namespacing prevents capability conflicts across domains.

---

## Dynamic Capability Updates

Agents may update capabilities during runtime.

Example endpoint:

```text
PUT /agents/{agent_id}/capabilities
```

This allows agents to expand or restrict supported tasks.

---

## Discovery in Distributed Systems

In distributed environments, capability discovery may occur through:

* service registries
* distributed directories
* peer-to-peer discovery mechanisms

These approaches allow agents to locate compatible executors across networks.

---

## Future Extensions

Future protocol proposals may introduce:

* capability negotiation
* capability ranking
* distributed capability discovery
* global agent marketplaces

These extensions could enable large-scale ecosystems where agents dynamically discover and collaborate with one another.
