import uvicorn
from fastapi import FastAPI

from config.settings import HOST, PORT, PROJECT_NAME
from config.routes import router as config_router
from config.database.db import database

app = FastAPI(title=PROJECT_NAME)
app.include_router(config_router)

@app.on_event('startup')
async def startup():
    await database.connect()
    
@app.on_event('shutdown')
async def shutdown():
    await database.disconnect()


if __name__ == '__main__':
    uvicorn.run('manage:app', host=HOST, port=PORT, reload=True)