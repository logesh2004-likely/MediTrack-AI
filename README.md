# Healthcare AI Adherence Flow

Below is the high-level architecture and data flow for the Healthcare AI Adherence platform. 
This flowchart details how the UI interacts with the Gateway Backend, which coordinates with the AI Agent and external Notification Services.

```mermaid
flowchart TD
    %% Define styles
    classDef frontend fill:#3498db,stroke:#2980b9,stroke-width:2px,color:white
    classDef backend fill:#2ecc71,stroke:#27ae60,stroke-width:2px,color:white
    classDef aiserver fill:#9b59b6,stroke:#8e44ad,stroke-width:2px,color:white
    classDef database fill:#f1c40f,stroke:#f39c12,stroke-width:2px,color:black
    classDef external fill:#e74c3c,stroke:#c0392b,stroke-width:2px,color:white

    %% Nodes
    A[Frontend Client\nReact / Vite]:::frontend
    B[Backend API Gateway\nNode.js / Express]:::backend
    C[(Mock DB\nIn-Memory)]:::database
    D[AI Agent Service\nPython / FastAPI / LangChain]:::aiserver
    E[Notification Service\nSMS / Email]:::external

    %% Flow: Fetch Patients
    A -- "1. GET /api/patients" --> B
    B -- "2. Fetch Data" --> C
    
    %% Flow: Analyze Adherence
    A -- "3. POST /api/analyze\n(patientData)" --> B
    B -- "4. Request AI Analysis" --> D
    D -- "5. Return Risk Status\n& Intervention Strategy" --> B
    
    %% Flow: Post-Analysis Actions
    B -- "6. Update Patient Risk Status" --> C
    B -- "7. Trigger Notifications\n(High/Medium Risk)" --> E
    B -- "8. Return AI Payload" --> A
```

## System Components

1. **Frontend**: A React/Vite web application that displays patient status, adherence levels, and triggers AI analysis.
2. **Backend API Gateway**: The main orchestration layer built in Node.js. It manages local persistent mock data, delegates reasoning and NLP tasks to the AI agent, and invokes external tasks like notifications.
3. **AI Agent Service**: A FastAPI server running Python with Langchain. It receives the patient context, uses LLMs/RAG (ChromaDB) to determine risk profile and suggests evidence-based clinical interventions.
4. **Notification Service**: Mock service responsible for simulating outgoing SMS/Email alerts for medium/high-risk adherence alerts. 
