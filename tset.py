from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/encrypt/{key}/{msg}/{r_key}")
def read_root(msg: str,key: int,r_key: int):
    enrpt_msg = enrpt(msg,key,r_key)
    return {"Message": msg,"sender_key":key,"reciever_key":r_key,"encrypted_msg":enrpt_msg}


def enrpt(msg,key,r_key):
    k1 = key
    k2 = r_key
    b=0
    c=0
    str1=""
    str_list = list(msg)
    for i in msg:
            k=k1^k2
            e=ord(i)^k
            ##print(k,e,chr(e))
            str_list[b]=chr(e)
            b=b+1
            k2=k2+1
            k1=k1+1
    str1="".join(str_list)
    print("The Encrypted message ")
    print(str1)
    return str1
