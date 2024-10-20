from collections import OrderedDict
from contextlib import asynccontextmanager
from re import compile
from typing import AsyncGenerator

import grpc


from ServiceDatabase.protos.gen.python.DatabaseService import DatabaseService_pb2_grpc
from ServiceDatabase.protos.gen.python.DatabaseService import DatabaseService_pb2
from src.app_config.config_db import DBSettings


class DatabaseAccessor:
    _instance = None

    def __new__(cls, db_settings: DBSettings):
        if cls._instance is None:
            cls._instance = super(DatabaseAccessor, cls).__new__(cls)
            cls._instance._initialize(db_settings)
        return cls._instance

    def _initialize(self, db_settings: DBSettings):
        self._db_settings = db_settings
        self._initialize_grpc()

    def _initialize_grpc(self):
        """Инициализация gRPC канала и стуба."""
        self._channel = grpc.insecure_channel(f"{self._db_settings.HOST}:{self._db_settings.PORT}")
        self._stub = DatabaseService_pb2_grpc.DatabaseServiceStub(self._channel)

    async def run(self) -> None:
        try:
            request = DatabaseService_pb2.Empty()
            response = self._stub.Users.future(request) 
            print("gRPC service is available.")
        except grpc.RpcError as e:
            print(f"gRPC service is not available: {e}")
            
    def get_stub(self):
        """Возвращает gRPC стуб."""
        return self._stub

    async def stop(self) -> None:
        self._channel.close() 