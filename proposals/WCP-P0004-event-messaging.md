# WCP-P0004: Event Messaging Specification

Status: Draft
Author: Saurabh Kumar
Created: 2026-03-15
Protocol Version: WCP v0.1

---

## Abstract

This proposal defines the **Event Messaging Model** used by the Work Coordination Protocol (WCP).

Events allow systems and agents to observe changes in work state and coordinate execution across distributed environments.

By standardizing event messages, WCP enables asynchronous communication between agents, allowing systems to react to work lifecycle changes.

---

## Motivation

In distributed agent systems, multiple entities may participate in the execution of a workflow.

Examples include:

* monitoring agents
* verification agents
* notification systems
* dependent workflow steps

Without standardized events, these systems cannot reliably detect changes in work execution.

The event messaging model enables:

* real-time coordination between agents
* event-driven workflows
* loosely coupled system architectures

---

## Event Structure

All WCP events MUST follow a common structure.

Required fields:

| Field      | Type   | Description                 |
| ---------- | ------ | --------------------------- |
| event_id   | string | unique identifier           |
| event_type | string | type of event               |
| work_id    | string | related work object         |
| timestamp  | string | event creation time         |
| source     | string | originating agent or system |

Optional fields:

| Field    | Description                        |
| -------- | ---------------------------------- |
| agent_id | agent performing the action        |
| payload  | additional event data              |
| metadata | implementation-specific attributes |

---

## Event Message Example

```json
{
  "event_id": "event_789",
  "event_type": "work.started",
  "work_id": "work_123",
  "agent_id": "email_agent",
  "timestamp": "2026-03-15T10:30:00Z",
  "source": "agent-worker",
  "payload": {
    "status": "running"
  }
}
```

---

## Standard Event Types

WCP defines several standard event types.

| Event          | Description                  |
| -------------- | ---------------------------- |
| work.created   | new work registered          |
| work.ready     | work available for execution |
| work.claimed   | agent claimed work           |
| work.started   | execution started            |
| work.completed | execution finished           |
| work.failed    | execution failed             |

Implementations MAY introduce additional event types.

---

## Event Flow Example

Example sequence for executing work.

```text
work.created
      ↓
work.ready
      ↓
work.claimed
      ↓
work.started
      ↓
work.completed
```

If execution fails:

```text
work.started
      ↓
work.failed
```

---

## Event Delivery

Events may be delivered through several mechanisms.

### Message Queues

Examples include:

* Redis Streams
* Kafka
* RabbitMQ

### Webhooks

Systems may subscribe to event notifications through HTTP callbacks.

Example:

```text
POST /events/webhook
```

### Event Streams

Implementations may expose event streams using:

* Server-Sent Events (SSE)
* WebSockets

---

## Event Ordering

Events SHOULD be emitted in chronological order.

Systems MUST NOT assume strict ordering across distributed nodes.

Consumers SHOULD rely on timestamps when ordering events.

---

## Idempotency

Event consumers SHOULD treat events as idempotent.

Duplicate events MAY occur in distributed environments.

Systems should process events safely even if delivered multiple times.

---

## Security Considerations

Event messaging systems must ensure:

### Authentication

Event publishers must authenticate with the event system.

### Integrity

Event payloads should be protected from tampering.

### Authorization

Agents must only receive events they are authorized to observe.

---

## Future Extensions

Future proposals may include:

* event filtering
* event replay
* event persistence
* distributed event routing
* event signatures

These features may enable decentralized event networks supporting large-scale agent ecosystems.
