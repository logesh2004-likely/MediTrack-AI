from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import uvicorn

app = FastAPI(title="Healthcare AI Adherence Agent")

class PatientData(BaseModel):
    patientId: str
    patientName: str
    disease: str
    adherenceRate: int

class AnalysisResult(BaseModel):
    riskLevel: str
    reasoning: str
    intervention: str

@app.post("/analyze", response_model=AnalysisResult)
async def analyze_adherence(data: PatientData):
    # In a real environment, this would initialize Langchain to reason over the specific disease guidelines.
    # For this architecture setup, we provide dynamic but simulated AI reasoning logic.
    print(f"[AI AGENT] Received analysis request for {data.patientName}")
    
    if data.adherenceRate < 70:
        risk_level = "high-risk"
        reasoning = f"AI Reasoning System: Patient adherence for {data.disease} is critically low at {data.adherenceRate}%. According to clinical guidelines, an adherence rate below 80% significantly increases the likelihood of acute complications tied to {data.disease}."
        intervention = "Automated high-priority alert dispatched to care team. Recommended immediate follow-up call to unblock medication access issues."
    elif data.adherenceRate < 85:
        risk_level = "medium-risk"
        reasoning = f"AI Reasoning System: Patient adherence for {data.disease} is suboptimal ({data.adherenceRate}%). While not critical, this marks a declining trend."
        intervention = "Automated AI-driven SMS sent providing educational material and an encouragement nudge."
    else:
        risk_level = "low-risk"
        reasoning = f"AI Reasoning System: Patient adherence is excellent ({data.adherenceRate}%). Clinical threshold for therapeutic efficacy is maintained."
        intervention = "No action necessary. Log adherence state to permanent patient record."

    print(f"[AI AGENT] Completed reasoning: {risk_level.upper()}")
    
    return AnalysisResult(
        riskLevel=risk_level,
        reasoning=reasoning,
        intervention=intervention
    )

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
