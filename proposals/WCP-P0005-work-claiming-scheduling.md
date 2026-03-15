# WCP-P0005: Work Claiming & Scheduling

Status: Draft
Author: Saurabh Kumar
Created: 2026-03-15
Protocol Version: WCP v0.1

---

## Abstract

This proposal defines how agents claim and schedule work within the Work Coordination Protocol (WCP).

Work claiming allows agents to declare intent to execute a work object. Scheduling mechanisms determine how work is distributed among available agents.

The goal is to ensure that work execution remains coordinated, conflict-free, and scalable across distributed environments.

---

## Motivation

In systems where multiple agents can execute the same type of work, a coordination mechanism is required to determine:

* which agent executes a specific work object
* how work is distributed across agents
* how conflicts are prevented when multiple agents attempt to execute the same work

Without a standardized claiming mechanism, distributed execution systems may experience:

* duplicate work execution
* race conditions
* inefficient scheduling

WCP introduces a simple and extensible model for work claiming and scheduling.

---

## Work Claiming

Agents must explicitly claim work before execution.

Claiming indicates that the agent intends to execute the work object.

### Claim Operation

```text
POST /work/{work_id}/claim
```

Payload example:

```json
{
  "agent_id": "email_agent"
}
```

---

## Claim Response

Successful claim:

```json
{
  "status": "claimed",
  "work_id": "work_123",
  "assigned_to": "email_agent"
}
```

Rejected claim (already assigned):

```json
{
  "status": "rejected",
  "reason": "work_already_claimed"
}
```

---

## Claim Locking

When a work object is successfully claimed:

* the `assigned_to` field MUST be set
* the work status SHOULD transition to `running` or `reserved`

Example work object after claim:

```json
{
  "work_id": "work_123",
  "type": "email.send",
  "status": "running",
  "assigned_to": "email_agent"
}
```

This prevents multiple agents from executing the same work.

---

## Scheduling Models

WCP does not mandate a specific scheduling algorithm.

Implementations may use different strategies.

### 1. Pull-Based Scheduling

Agents poll the system for available work.

Example:

```text
GET /work?status=ready&type=email.send
```

Advantages:

* simple implementation
* scalable

---

### 2. Push-Based Scheduling

The system assigns work directly to agents based on capability.

Example flow:

```text
Work Engine → selects compatible agent → assigns work
```

Advantages:

* reduced latency
* centralized control

---

### 3. Capability-Based Routing

Work objects are matched with agents based on declared capabilities.

Example:

```text
Work Type: email.send
Agent Capabilities: ["email.send"]
```

This allows systems to route work automatically.

---

## Retry Mechanism

If an agent fails to complete work, the system may retry execution.

Example retry policy:

```text
max_retries = 3
retry_delay = 10 seconds
```

Retry events:

```text
work.retrying
work.failed
```

Work may be reassigned to another agent after failure.

---

## Timeout Handling

If an agent claims work but fails to start execution within a specified time, the claim may expire.

Example timeout:

```text
claim_timeout = 60 seconds
```

Expired claims allow other agents to claim the work.

---

## Example Work Execution Flow

```text
work.created
      ↓
work.ready
      ↓
agent.claim
      ↓
work.claimed
      ↓
work.started
      ↓
work.completed
```

Failure path:

```text
work.started
      ↓
work.failed
      ↓
work.retrying
```

---

## Fair Scheduling Considerations

Implementations should avoid overloading specific agents.

Possible strategies:

* round-robin assignment
* priority queues
* load-aware scheduling

---

## Security Considerations

Systems should ensure that:

* only authorized agents claim work
* malicious agents cannot monopolize work
* claims are verified before execution

---

## Future Extensions

Future protocol proposals may introduce:

* decentralized work markets
* agent bidding mechanisms
* priority-based distributed scheduling
* peer-to-peer work distribution

These mechanisms could enable large-scale networks where autonomous agents collaborate and compete for work execution.
