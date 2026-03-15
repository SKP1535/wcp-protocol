```mermaid
flowchart TD

User --> WorkAPI
WorkAPI --> WorkEngine
WorkEngine --> Database
WorkEngine --> EventBus
EventBus --> Agents
Agents --> WorkEngine
```