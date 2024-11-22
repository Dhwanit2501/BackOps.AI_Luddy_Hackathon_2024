from typing import Annotated
from fastapi import FastAPI, Request, Form
from schemas import PromptQuery
from database import get_session, create_db_and_tables
from crud import createKeyValue, updateKeyValue, deleteKeyValue
from database import SessionDep
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, RedirectResponse
import utils
from llm import parse_from_llm
from exceptions import KeyAlreadyExist, KeyNotFound, ValueIsEmpty

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

in_memory_session = {
    "questions": [],
    "answers": []
}

@app.get("/", response_class=HTMLResponse)
def homepage(request: Request):
    key_lifecycle_data = utils.visualization_of_lifecycle_of_key_for_today()

    max_length = max(len(in_memory_session["questions"]), len(in_memory_session["answers"]))
    q_and_a = zip(in_memory_session["questions"] + [None] * (max_length - len(in_memory_session["questions"])), in_memory_session["answers"] + [None] * (max_length - len(in_memory_session["answers"])))

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "questions_answers": q_and_a,
            "key_lifecycle_data": key_lifecycle_data
        }
    )

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.post("/llm")
def parsePrompt(request: Request, prompt: Annotated[str, Form()], session: SessionDep):

    msg = ""

    try:
        parsed_user_inputs = parse_from_llm(prompt)
    except Exception:
        msg = "Sorry!, Not able to serve request now."

        in_memory_session["questions"].append(msg)
        in_memory_session["answers"].append(msg)

        return RedirectResponse(url="/", status_code=303)

    in_memory_session["questions"].append(prompt)

    for input in parsed_user_inputs:
        action = input.get("action")
        key = input.get("key")
        value = input.get("value", "")


        if action.lower() == "insert":
            try:
                createKeyValue(key, value, session)
            except KeyAlreadyExist as e:
                msg = e
            except ValueIsEmpty as e:
                msg = e
            else:
                msg = f"Successfully inserted given {key}: {value}"

        elif action.lower() == "update":
        
            try:
                updateKeyValue(key, value, session)
            except KeyNotFound as e:
                msg = e
            else:
                msg = f"Successfully updated existing key: {key} with new value: {value}"
        
        elif action.lower() == "delete":
            try:
                deleteKeyValue(key, session)
            except KeyNotFound as e:
                msg = e
            else:
                msg = f"Successfully deleted existing key: {key}"

        in_memory_session["answers"].append(msg)

    return RedirectResponse(url="/", status_code=303)


@app.get("/get-log-stats/{year}/{month}/{day}")
def log_stats(year: int, month: int, day: int):
    return utils.get_stats(year, month, day)

@app.get("/get-past-day-log-stats")
def log_stats_of_past_days(days: int):
    ans = {"count": [], "date": []}

    year, month, current_day = utils.get_today_date_attr()

    for day in range(1, days + 1):
        stats = utils.get_stats(year, month, current_day - day)

        ans["count"].append(stats["Inserted"] + stats["Updated"] + stats["Deleted"])
        ans["date"].append(f"{month}/{current_day - day}/{year}")

    return ans
