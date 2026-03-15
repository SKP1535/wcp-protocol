# WCP-P0001: Work Object Specification

Status: Draft
Author: Saurabh Kumar
Created: 2026-03-15
Protocol Version: WCP v0.1

---

## Abstract

This proposal defines the **Work Object**, the fundamental unit of execution in the Work Coordination Protocol (WCP).

A Work Object represents a declarative description of a unit of work that may be executed by an agent.

---

## Motivation

In distributed systems involving autonomous agents, tasks must be represented in a standardized format to allow interoperability between systems.

The Work Object provides a minimal and extensible schema for representing executable work.

---

## Work Object Schema

A Work Object MUST contain the following fields.

| Field   | Type   | Description          |
| ------- | ------ | -------------------- |
| work_id | string | unique identifier    |
| type    | string | work category        |
| status  | string | lifecycle state      |
| context | object | execution parameters |

---

## Example Work Object

```json
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

---

## Optional Fields

| Field       | Description           |
| ----------- | --------------------- |
| priority    | execution priority    |
| assigned_to | agent executing work  |
| created_by  | work creator          |
| metadata    | additional attributes |

---

## Work Type Naming

Work types SHOULD follow a hierarchical naming convention.

```
domain.action
```

Examples:

```
email.send
calendar.schedule
travel.book_flight
payment.process
```

---

## Design Principles

The Work Object is designed to be:

* simple
* serializable
* language-agnostic
* extensible