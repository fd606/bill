from pydantic import BaseModel 
from datetime import datetime
from enum import Enum
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json
import os
from file import readjson, writejson

app = FastAPI()

app.add_middleware(
   CORSMiddleware,
   allow_origins=["*"],
   allow_methods=["*"],
   allow_headers=["*"],
)

class Record(BaseModel):
    payer: str
    money: int


@app.post("/add")
async def add_record(record: Record):
    # 获取当前的年份和月份，以2000.1的格式保存到变量time里面
    time = datetime.now().strftime("%Y.%m")
    file_name = 'bill/' + time + ".json"
    if not os.path.exists(file_name):
        writejson(file_name, [])
    writejson(file_name, readjson(file_name) + [{"payer": record.payer, "money": record.money}])

@app.get("/query/{time}")
async def get_records(time: str):
    file_name = 'bill/' + time + ".json"
    data = []
    if os.path.exists(file_name):
        data = readjson(file_name)
    print(data)
    return {
        "data": data
    }

if __name__ == "__main__":
   import os
   os.system("uvicorn main:app --reload")