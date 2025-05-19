from fastapi import APIRouter, Query

router = APIRouter()

@router.get("/")
def read_root():
    return {"message": "Hello World"}

@router.post("/application")
def post_application():
    return {"message": "Application submitted successfully"}

@router.post("/application/{candidate_id}")
def apply_for_candidate(candidate_id: str):
    return {
        "status": "success",
        "message": f"Application for candidateID: {candidate_id} successfully submitted"
    }

@router.get("/application/")
def get_applications(company_name: str = Query(None, description="Optional company name")):
    if company_name:
        return {
            "status": "success",
            "message": f"Here is your application for {company_name}"    
        }
    else:
        return {
            "status": "success",
            "message": "Here are your applications:"
        } 