from pydantic import BaseModel

class Bgpost(BaseModel):
    id:int
    title:str
    content:str