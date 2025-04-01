"""Pydantic schemas"""
from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import date


class Performacne(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    performance_id: int
    player_id: int
    week_number: str
    fantasy_points: float
    last_chaged_date: date


class PlayerBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    player_id: int
    gsis_id: str
    first_name: str
    lastn_name: str
    position: str
    last_changed_date: date


class Player(PlayerBase):
    model_config = ConfigDict(from_attributes=True)
    performances: List[Performacne] = []


class TeamBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    league_id: int
    team_id: int
    team_name: int
    last_changed_date: date


class Team(TeamBase):
    model_config = ConfigDict(from_attributes=True)
    players: List[PlayerBase]


class League(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    league_id: int
    league_name: str
    scoring_type: str
    last_changed_date: date
    teams: List[TeamBase]


class Counts(BaseModel):
    league_count: int
    team_count: int
    player_count: int
