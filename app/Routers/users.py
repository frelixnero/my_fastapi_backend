from fastapi import *
from passlib.context import CryptContext
from psycopg2.extras import RealDictCursor
from sqlalchemy.orm import Session
from ..import models
from ..database import engine,get_db
from ..schemas_pydantic import UserCreate, UserOut
from ..utils import hash_pass



pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
models.Base.metadata.create_all(bind = engine)
router = APIRouter(
    prefix = "/users",
    tags = ['Users']
)
app = FastAPI()


@router.post("/", status_code = status.HTTP_201_CREATED, response_model = UserOut)
async def create_user(user : UserCreate, db : Session = Depends(get_db)) :
    
    # Hashing the user password -- readup on hashing
    new_pass = hash_pass(user.password)
    user.password = new_pass
    
    
    new_user = models.Users(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get("/{id}",response_model = UserOut)
def get_user(id : int, db : Session = Depends(get_db)) :
    user_info = db.query(models.Users).filter(models.Users.id == id).first()
    if not user_info :
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = 'User not found')

    
    return user_info