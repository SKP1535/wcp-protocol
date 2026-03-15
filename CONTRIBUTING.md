# Contributing to WCP

Thank you for your interest in contributing to the **Work Coordination Protocol (WCP)**.

WCP is an open protocol designed to coordinate work between humans, AI agents, and software systems. Contributions from the community are essential for evolving the protocol.

---

# Ways to Contribute

You can contribute in several ways:

* Propose protocol improvements
* Improve documentation
* Implement SDKs
* Build agent examples
* Develop reference implementations
* Report issues or bugs

---

# Protocol Changes

Changes to the protocol should be proposed through **WCP Proposals**.

Steps:

1. Create a new proposal document

```text
proposals/WCP-PXXXX-name.md
```

2. Follow the proposal format used by existing specs.

3. Open a Pull Request describing the proposed changes.

Protocol proposals should include:

* motivation
* specification
* examples
* backward compatibility considerations

---

# Development Setup

Clone the repository:

```bash
git clone https://github.com/skp1535/wcp-protocol.git
cd wcp-protocol
```

Install dependencies for the reference server:

```bash
pip install -r reference/wcp-fastapi-server/requirements.txt
```

Run the server:

```bash
uvicorn app.main:app --reload
```

---

# Pull Request Guidelines

Before submitting a PR:

* Ensure documentation is updated
* Follow existing code style
* Provide examples when possible
* Keep changes focused

---

# Reporting Issues

If you encounter a bug or design problem:

1. Open a GitHub Issue
2. Describe the problem clearly
3. Provide reproduction steps

---

# Community

We welcome constructive feedback and discussion around protocol design.

Together we can evolve WCP into a robust coordination protocol for autonomous systems.
