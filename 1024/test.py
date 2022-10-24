from fastapi import FastAPI

#서버 실행 uvicorn test:app --reload
#fastapi 가 1위 ㅇㅇ
#pip install fastapi
#pip install "uvicorn[standard]"
#pip install uvicorn

app = FastAPI()

@app.get('/hello')
def hello():
    return {'test': 'hello'}

@app.get('/users')
def get_users(username: str):
    return {'username': username}

@app.post('/users')
def create_user(username: str):
    return {'username': username}
    
@app.get('/users/{username}')
def get_user(username: str):
    return {'username': username}

