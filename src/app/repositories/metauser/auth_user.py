from ServiceDatabase.protos.gen.python.DatabaseService import DatabaseService_pb2_grpc
from ServiceDatabase.protos.gen.python.DatabaseService import DatabaseService_pb2
from ServiceDatabase.protos.gen.python.DatabaseService.DatabaseService_pb2_grpc import DatabaseServiceStub
from src.app.models.users.auth_auth import UserORM
from sqlalchemy import insert, select, update
from src.app.schemas.auth import (
    UserCreateDB,
    User,
    UserUpdate,
    UsersFindRequest,
)
import uuid


class AuthRepository:
    def __init__(self, database_accessor):
        self.stub = database_accessor.get_stub()

    async def create_user(self, email: str, username: str, password: str, phone: str):
        request = DatabaseService_pb2.CreateUserRequest(
            email=email,
            username=username,
            password=password,
            phone=phone
        )
        response = self.stub.CreateUser(request)
        return response

    async def users(self):
        request = DatabaseService_pb2.Empty()  # Предполагается, что метод не требует параметров
        response = self.stub.Users(request)

    # Предположим, что response.users - это итерируемый объект, который содержит пользователей
        user_list = []
        for user in response.users:  # Предполагается, что response.users - это итерируемый объект
            user_list.append({
            "id": user.id,
            "email": user.email,
            "username": user.username,
            "phone": user.phone,
            "createdAt": user.createdAt,
            "updatedAt": user.updatedAt
        })

        return user_list

    async def is_role(self, user_id: str, role: str):
        request = DatabaseService_pb2.IsRoleRequest(
            user_id=user_id,
            role=role
        )
        response = self.stub.IsRole(request)
        return response

    async def compare_password(self, user_id: str, password: str):
        request = DatabaseService_pb2.ComparePasswordRequest(
            user_id=user_id,
            password=password
        )
        response = self.stub.ComparePassword(request)
        return response

    async def user_exists(self, phone: str):
        request = DatabaseService_pb2.UserIsExistsRequest(
            phone=phone
        )
        response = self.stub.UserIsExists(request)
        return response

    async def find_user_by_id(self, id: int):
        request = DatabaseService_pb2.FindUserByIdRequest(id=id)
        response = self.stub.FindUserById(request)

        # Проверьте, существует ли пользователь в ответе
        if response.HasField("user"):  # Предполагается, что user - это поле в ответе
            user = response.user  # Получите объект пользователя
            return {
                "id": user.id,
                "email": user.email,
                "username": user.username,
                "phone": user.phone,
                "createdAt": user.createdAt,  # Убедитесь, что это datetime
                "updatedAt": user.updatedAt   # Если нужно, добавьте это поле
            }
        else:
            return None  # Если пользователь не найден, возвращаем None

    async def find_user_by_email(self, email: str):
        request = DatabaseService_pb2.FindUserByEmailRequest(
            email=email
        )
        response = self.stub.FindUserByEmail(request)
        return response

    async def find_user_by_phone(self, phone: str):
        request = DatabaseService_pb2.FindUserByPhoneRequest(
            phone=phone
        )
        response = self.stub.FindUserByPhone(request)
        return response

