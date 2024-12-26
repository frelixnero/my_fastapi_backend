from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_pass(password) :
    hashed_pass = pwd_context.hash(password)
    return hashed_pass


def verify(login_password : str, database_password) :
    return pwd_context.verify(login_password, database_password)
    
    # hashed_pass = pwd_context.hash(login_password)
    
    # if hashed_pass == database_password :
    #     return True
    # else :
    #     return False