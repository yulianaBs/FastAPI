from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import Optional, List
# from applications import router

app = FastAPI()
# app.include_router(router) 
class Application(BaseModel):
    candidate_id: str
    name: str
    email: str
    job_id: str | None = None

class UpdateApplication(BaseModel):
    email: str
    job_id: str

class PatchApplication(BaseModel):
    email: str | None = None
    job_id: str | None = None

applications_db: List[Application] = []


@app.post("/applications")
def post_application(application: Application):
    applications_db.append(application)
    return {
        "status": "success",
        "message": f"Application submitted for {application.candidate_id}",
        
    }

@app.get("/applications")
def get_applications(
    company_name: Optional[str] = Query(default=None),
    candidate_email: Optional[str] = Query(default=None)
):
    if company_name and candidate_email:
        return {
            "status": "success",
            "message": f"Here is your application for {company_name} with email {candidate_email}"
        }
    elif company_name:
        return {
            "status": "success",
            "message": f"Here is your application for {company_name}"
        }
    elif candidate_email:
        return {
            "status": "success",
            "message": f"Here is your application for email {candidate_email}"
        }
    else:
        return {
            "status": "success",
            "message": "Here are all applications",
            "data": applications_db
        }

@app.get("/applications/{candidate_id}")
def get_applications_path(candidate_id: str):
    return {
        "status": "success",
        "message": f"Application found for {candidate_id}"
    }

@app.put("/applications/{candidate_id}")
def put_applications(candidate_id: str, application: UpdateApplication):
    return {
        "status": "success",
        "message": f"Application updated for {candidate_id}"
    }

@app.patch("/applications/{candidate_id}")
def patch_applications(candidate_id: str, application: PatchApplication):
    if application.email is not None:
        return{
            "status": "success",
            "message": f"Application updated for {application.email}"
        }
    elif application.job_id is not None:
        return{
            "status": "success",
            "message": f"Application updated for {application.job_id}"
        }
    else:
        return{
            "status": "success",
            "message": f"Application updated for {candidate_id}"
        }


@app.delete("/applications/{candidate_id}")
def delete_applications(candidate_id: str):
    return{
        "status": "success",
        "message": f"Application deleted for {candidate_id}"
    }
