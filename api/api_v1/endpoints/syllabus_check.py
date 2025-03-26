from fastapi import APIRouter, HTTPException
from schemas.request_schema import RequestSchema
from app.bulk_process import process_bulk

router = APIRouter()

@router.post("/syllabus_check")
def syllabus_check(request: RequestSchema):
    try:
        process_bulk(request.request_id)
        return {"message": "Processing started", "request_id": request.request_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))