# WCP-P0006: Work Graphs (Dependencies Between Work)

Status: Draft
Author: Saurabh Kumar
Created: 2026-03-15
Protocol Version: WCP v0.1

---

## Abstract

This proposal introduces **Work Graphs**, a mechanism that allows multiple work objects to be connected through dependency relationships.

Work Graphs enable complex workflows to be expressed as directed graphs where certain work objects must complete before others can begin execution.

By supporting dependency relationships between work objects, the Work Coordination Protocol (WCP) can coordinate multi-step workflows across multiple agents.

---

## Motivation

Many real-world tasks consist of multiple steps that must occur in sequence or in parallel.

Examples include:

* travel planning workflows
* software build pipelines
* document processing pipelines
* multi-step automation tasks

Without dependency management, agents cannot coordinate execution across multiple related work objects.

Work Graphs provide a structured way to express these dependencies.

---

## Work Graph Model

A Work Graph represents a collection of work objects connected by dependency relationships.

In a Work Graph:

* nodes represent work objects
* edges represent dependencies

A dependency indicates that a work object cannot begin execution until another work object has completed.

---

## Graph Structure

Example workflow:

```text
search_flights
      ↓
book_flight
      ↓
send_confirmation
```

Graph representation:

```text
Work A → Work B → Work C
```

---

## Dependency Field

Work objects may define dependencies using the `depends_on` field.

Example:

```json
{
  "work_id": "book_flight",
  "type": "travel.book_flight",
  "status": "created",
  "depends_on": ["search_flights"]
}
```

This indicates that `book_flight` can only begin execution after `search_flights` completes.

---

## Multiple Dependencies

Work objects may depend on multiple other work objects.

Example:

```json
{
  "work_id": "create_itinerary",
  "type": "travel.create_itinerary",
  "depends_on": [
    "search_flights",
    "find_hotels"
  ]
}
```

Execution begins only after all dependencies complete successfully.

---

## Parallel Execution

Work Graphs allow independent work objects to execute concurrently.

Example:

```text
           → search_flights →
start
           → find_hotels   →
```

Both tasks may execute in parallel.

---

## Dependency Resolution

Before an agent executes a work object, the system MUST verify that all dependencies have completed successfully.

Execution rule:

```text
All dependencies must be in state: completed
```

If a dependency fails:

```text
dependent work should not execute
```

The dependent work may transition to:

```text
blocked
```

---

## Blocked State

Implementations MAY introduce an optional lifecycle state:

```text
blocked
```

This indicates that a work object cannot yet execute due to unresolved dependencies.

Example lifecycle with dependency state:

```text
created → blocked → ready → running → completed
```

---

## Graph Example

Example workflow for planning a trip.

```text
search_flights
find_hotels
      ↓
create_itinerary
      ↓
notify_user
```

Execution order:

1. search_flights
2. find_hotels
3. create_itinerary
4. notify_user

Agents may execute independent steps concurrently.

---

## Example Work Graph

Example JSON representation:

```json
{
  "graph_id": "trip_planning",
  "work": [
    {
      "work_id": "search_flights",
      "type": "travel.search_flights"
    },
    {
      "work_id": "find_hotels",
      "type": "travel.find_hotels"
    },
    {
      "work_id": "create_itinerary",
      "type": "travel.create_itinerary",
      "depends_on": [
        "search_flights",
        "find_hotels"
      ]
    }
  ]
}
```

---

## Graph Execution Rules

Implementations should follow these rules:

1. A work object must not execute before dependencies complete.
2. Independent work objects may execute in parallel.
3. Dependency cycles must be rejected.

Cycle example (invalid):

```text
A → B → C → A
```

Systems must validate graphs before execution.

---

## Event Integration

Work Graphs integrate with event messaging.

Example sequence:

```text
work.completed(search_flights)
work.completed(find_hotels)
work.ready(create_itinerary)
```

Events allow agents to react to dependency completion.

---

## Graph Identification

Graphs may be identified using a unique identifier.

Example:

```json
{
  "graph_id": "workflow_001"
}
```

This allows systems to track related work objects.

---

## Failure Handling

If a dependency fails, dependent work objects may transition to:

```text
blocked
failed
cancelled
```

Implementation policy determines how failures propagate.

---

## Future Extensions

Future proposals may introduce:

* graph scheduling optimizations
* conditional workflows
* dynamic graph expansion
* distributed graph execution

These features could enable large-scale automation networks composed of cooperating agents.

---

## Conclusion

Work Graphs enable the Work Coordination Protocol to support complex multi-step workflows involving multiple agents.

By introducing dependency relationships between work objects, WCP can coordinate sophisticated task execution across distributed systems while maintaining a simple and extensible protocol design.
