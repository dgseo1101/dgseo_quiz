# -*- coding: utf-8 -*-
from typing import Optional

import jwt
from dependency_injector.providers import Configuration
from dependency_injector.wiring import Provide, inject
from fastapi import Depends, Header, HTTPException

from core.infrastructure.di.container import CoreContainer

def decode_jwt_token(token: str, config: Configuration) -> dict:
    try:
        payload = jwt.decode(
            token, config["jwt"]["secret_key"], algorithms=[config["jwt"]["algorithm"]]
        )
        return payload
    except (jwt.ExpiredSignatureError, jwt.DecodeError):
        raise HTTPException(status_code=401, detail="Token is invalid or expired")
    
@inject
async def get_user_id_by_token(token: str, config: Configuration) -> int:
    payload = decode_jwt_token(token, config)
    user_id = int(payload.get("sub"))
    role = payload.get("role")
    if not user_id:
        raise HTTPException(status_code=401, detail="Invalid token: user_id missing")
    return user_id, role

@inject
async def get_token_by_header_token(authorization: str, config: Configuration) -> str:
    if not authorization:
        raise HTTPException(status_code=401, detail="Authorization header is missing")

    try:
        token = authorization.split(" ")[1]  # "Bearer token"에서 token 추출
    except IndexError:
        raise HTTPException(status_code=401, detail="Invalid authorization format")

    decode_jwt_token(token, config)  # 토큰이 유효한지 검증
    return token

@inject
async def validate_user_and_get_user_id(
    authorization: Optional[str] = Header(None),
    config: Configuration = Depends(Provide[CoreContainer.config]),
):
    token = await get_token_by_header_token(authorization=authorization, config=config)
    user_id, _ = await get_user_id_by_token(token=token, config=config)
    return user_id

@inject
async def validate_admin_and_get_user_id(
    authorization: Optional[str] = Header(None),
    config: Configuration = Depends(Provide[CoreContainer.config]),
):
    token = await get_token_by_header_token(authorization=authorization, config=config)
    user_id, role = await get_user_id_by_token(token=token, config=config)
    if role != "admin":
        raise HTTPException(status_code=401, detail="Invalid token")
    return user_id