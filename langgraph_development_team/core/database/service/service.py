import io
import zipfile


def download_run(run_id):
    with Session(engine()) as session:
        run = session.get(Run, run_id)
        if run is None:
            raise HTTPException(404, "Run not found.")
        files = run.files

    buffer = io.BytesIO()                       # builds the zip in memory, not on disk
    with zipfile.ZipFile(buffer, "w", zipfile.ZIP_DEFLATED) as z:
        for path, content in files.items():
            z.writestr(path, content)           # one entry per file: "calc.py" -> its code
    return buffer.getvalue()


## In route.py
from fastapi import APIRouter, Response


@ai_agent_router.get("/runs/{run_id}/download")
def download_run(run_id: UUID):
    return Response(
        service.download_run(run_id),
        media_type="application/zip",
        headers={"Content-Disposition": f'attachment; filename="run-{run_id}.zip"'},
    )
