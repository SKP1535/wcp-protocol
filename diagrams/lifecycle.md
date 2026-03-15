```mermaid
stateDiagram-v2
    created --> ready
    ready --> running
    running --> completed
    running --> failed
```