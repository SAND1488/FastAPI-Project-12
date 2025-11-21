from fastapi import FastAPI

app = FastAPI()



"""
@app.get("/")
def index():
    return {"message": "salom dunyo"}

# http://localhost:8000/about
@app.get("/about")
def about():
    return {"xabar": "men haqimda page"}

@app.get("/student/{name}/familya/{surname}")
def about(name: str, surname):
    return {"salom": name + " " + surname}

@app.get("/ikkinchi")
def ikkinchi(a,b):
    return{
        a,
        b
    }

@app.get("/ikkinchi")
def ikkinchi(s,b=None):
    if b:
        return{ "s": s, "b": b }
    return {"s": s}
"""


# /docs
# /redoc





# uvicorn main:app --reload
# pip install fastapi uvicorn[standard]
mevalar = ["olma", "anor"]

@app.get("/")
def index():
    return {"mevalar_list": mevalar}

@app.post("/{meva_nomi}")
def meva_yaratish(meva_nomi):
    global mevalar
    mevalar.append(meva_nomi)
    return{ "message": "meva yaratish."}

@app.put("/{meva_nomi}/{yangi_nom}")
def ozgartirish(meva_nomi: str, yangi_nom: str):
    global mevalar 
    try:
        meva_id = mevalar.index(meva_nomi)
        mevalar[meva_id] = yangi_nom
    except:
        return {"error": "bunday meva nomi yo'q"}
    return {"xabar": "meva nomi o'zgardi"}

@app.delete("/{meva_nomi}")
def ozgartirish(meva_nomi: str):
    global mevalar 
    try:
        
        mevalar.remove(meva_nomi)
    except:
        return {"error": "bunday meva nomi yo'q"}
    return {"xabar": "meva nomi o'zgardi"}