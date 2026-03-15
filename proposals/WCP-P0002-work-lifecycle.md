# WCP-P0002: Work Lifecycle Specification

Status: Draft
Author: Saurabh Kumar
Created: 2026-03-15
Protocol Version: WCP v0.1

---

## Abstract

This proposal defines the **Work Lifecycle**, a standardized state machine describing how work progresses from creation to completion.

---

## Lifecycle States

WCP defines five primary states.

```
created
↓
ready
↓
running
↓
completed
```

Alternative path:

```
running → failed
```

---

## State Definitions

### created

Work object has been registered but is not yet available for execution.

### ready

Work is available for agents to claim.

### running

An agent has begun executing the work.

### completed

Execution finished successfully.

### failed

Execution terminated unsuccessfully.

---

## State Transition Rules

| From    | To        |
| ------- | --------- |
| created | ready     |
| ready   | running   |
| running | completed |
| running | failed    |

Invalid transitions MUST be rejected.

---

## Example Lifecycle Event

```json
{
  "event": "work.started",
  "work_id": "work_123",
  "agent_id": "email_agent"
}
```

---

## Lifecycle Events

Events MAY include:

```
work.created
work.ready
work.started
work.completed
work.failed
```

These events allow systems to react to execution progress.
