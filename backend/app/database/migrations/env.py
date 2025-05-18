from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
from ...database.db import Base
import os

config = context.config

fileConfig(config.config_file_name)

# Import all models for Alembic
from ...models.user import User
from ...models.calibration import Calibration
from ...models.measurement import Measurement
from ...models.company import Company
from ...models.file import File

connectable = engine_from_config(
    config.get_section(config.config_ini_section),
    prefix="sqlalchemy.",
    poolclass=pool.NullPool
)

with connectable.connect() as connection:
    context.configure(
        connection=connection,
        target_metadata=Base.metadata
    )

    with context.begin_transaction():
        context.run_migrations()