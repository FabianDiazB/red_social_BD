from fastapi import FastAPI, HTTPException, Request, Depends
from db import Database
from fastapi.security import OAuth2PasswordBearer
import auth
from auth import Autenticacion
from user import UserLogin

app = FastAPI()
db = Database()
auth = Autenticacion()

# OAuth2 Password Bearer
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")




@app.post("/login")
async def login(user: UserLogin):
    try:
        user_data = db.get_user(user.username, user.password)
        print(user[0][0]," es esteeee::: ","\n\n\n\n\n\n\n\n")
        if not user_data or not auth.verify_password(user.password, user_data[0][3]):
            raise HTTPException(status_code=401, detail="Usuario o contraseña incorrectos")
        rol = user_data[0][4]
        # Incluir el rol en el token
        token = auth.create_jwt_token({"sub": user.username, "rol": rol,"usuario_id": user_data[0][0]})
        return {"access_token": token, "token_type": "bearer"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

   
@app.post("/post")
async def create_post(request: Request, token: str = Depends(oauth2_scheme)):
    try:
        # Decodificar el token JWT para obtener el usuario_id
        payload = auth.verify_jwt_token(token)
        usuario_id = payload.get("usuario_id")  # Aquí asumimos que "sub" es el usuario_id

        if not usuario_id:
            raise HTTPException(status_code=400, detail="No se pudo identificar el usuario.")

        # Obtener la publicación desde el cuerpo de la solicitud
        body = await request.json()
        publicacion = body.get("publicacion")
        enlaces = body.get("links")

        if not publicacion:
            raise HTTPException(status_code=400, detail="La publicación no puede estar vacía.")

        db.insertar_publicacion(usuario_id, publicacion,enlaces)
        print("Publicación creada con éxito")

        return {"message": "Publicación creada con éxito"}
    
    except Exception as e:
        print("Error al crear la publicación:", str(e))
        raise HTTPException(status_code=400, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
