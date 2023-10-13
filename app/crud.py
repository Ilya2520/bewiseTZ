import requests
from fastapi import APIRouter, HTTPException

from app.database import SessionLocal, Question, QuestionRequest

app = APIRouter()


@app.get("/show")
def show_questions():
    session = SessionLocal()
    questions = session.query(Question).all()

    if not questions:
        raise HTTPException(status_code=404, detail="No questions found in the database.")

    questions_list = []
    for question in questions:
        questions_list.append({
            "id": question.id,
            "question": question.question,
            "answer": question.answer,
            "created_at": question.created_at
        })

    return {"questions": questions_list}


@app.post("/add", status_code=201)
def add_questions(question_request: QuestionRequest):
    num = question_request.questions_num
    if num <= 0:
        raise HTTPException(status_code=400, detail="Invalid 'num' parameter. It should be a positive integer.")

    url = f'https://jservice.io/api/random?count={num}'

    try:
        response = requests.get(url)
        response.raise_for_status()

        questions = response.json()
        selected_questions = []
        i = 0
        for q in questions:
            quest = {'id': q['id'], 'question': q['question'], 'answer': q['answer'], 'created_at': q['created_at']}
            if add_question_to_db(session=SessionLocal(), question=quest):
                selected_questions.append(quest)
                i += 1
            else:
                while True:
                    new_response = requests.get(url='https://jservice.io/api/random?count=1')
                    new_question = new_response.json()[0]
                    new_quest = {'id': new_question['id'], 'question': new_question['question'],
                                 'answer': new_question['answer'], 'created_at': new_question['created_at']}
                    if add_question_to_db(SessionLocal(), new_quest):
                        selected_questions.append(new_quest)
                        i += 1
                        break

        return {"questions": selected_questions}

    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail="Failed to fetch questions from the API.") from e


def add_question_to_db(session, question):
    existing_question = session.query(Question).filter(Question.id == question['id']).first()
    if existing_question:
        print("already add")
        return False
    db_question = Question(**question)
    session.add(db_question)
    session.commit()
    return True
