# WCP-P0003: Agent Capability Declaration

Status: Draft
Author: Saurabh Kumar
Created: 2026-03-15
Protocol Version: WCP v0.1

---

## Abstract

This proposal defines how agents declare the capabilities required to execute specific types of work.

---

## Motivation

To coordinate work across distributed agents, systems must know which agents can perform which types of work.

Capability declarations allow automated routing of work objects.

---

## Agent Schema

Agents MUST provide the following fields.

| Field        | Type   | Description             |
| ------------ | ------ | ----------------------- |
| agent_id     | string | unique agent identifier |
| capabilities | array  | supported work types    |

---

## Example Agent Registration

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

## Capability Format

Capabilities SHOULD match the work type namespace.

Example:

```
email.send
calendar.schedule
travel.book_flight
```

---

## Registration Endpoint

Example API endpoint:

```
POST /agents/register
```

Payload:

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

## Future Extensions

Future proposals may introduce:

* capability discovery
* capability versioning
* agent reputation systems
* capability negotiation
