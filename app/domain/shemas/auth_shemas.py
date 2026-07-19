"""user auth shemas"""
from pydantic import BaseModel, Field, field_validator, EmailStr

from app.core.exceptions import BusinessLogicError


class RegisterModel(BaseModel):
    """model for registration user"""
    # нужно добавить проверкеу юз ернейма в кеше на уровне пайдентик модели
    # не забыть что в случаи падения кеша я перестану принимать юзеров(обработать вариант падения кеша)
    username: str = Field(..., min_length=3, max_length=10, description="any unique username")
    name: str = Field(..., min_length=2, max_length=10, description="user's name")
    second_name: str = Field(..., min_length=2, max_length=10, description="user's secondname")
    email: str = Field(..., min_length=10, max_length=40,
                       description="user's email popular(mail,gmail,etc)")
    password: str = Field(..., min_length=1, max_length=10)

    @field_validator('email')
    @classmethod
    def validate_email(cls,value: EmailStr) -> EmailStr:
        """validate email"""
        domain = value.lower().split('@')[-1]

        # не хочу делать список в env
        allowed_domains = ['mail.ru', 'gmail']

        if domain not in allowed_domains:
            raise BusinessLogicError(
                field='email',
                message='not allowed email',
                log=True,
                details={
                    'input': domain,
                    'allowed emails': allowed_domains
                }
            )
        return value
