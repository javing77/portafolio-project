"""SQLAlchmey Query Functions"""
from sqlalchemy.orm import Session, joinedload
from datetime import date
from typing import Optional
import models


def get_player(db: Session, player_id: int):
    return db.query(models.Player).filter(
        models.Player.player_id == player_id
    ).first()


def get_players(db: Session, skip: int = 0, limit: int = 100,
                min_last_changed_date: Optional[date] = None,
                last_name: Optional[str] = None,
                first_name: Optional[str] = None):

    query = db.query(models.Player)

    if min_last_changed_date:
        query = query.filter(
            models.Player.last_changed_date >= min_last_changed_date)
    if first_name:
        query = query.filter(models.Player.first_name == first_name)
    if last_name:
        query = query.filter(models.Player.last_name == last_name)

    return query.offset(skip).limit(limit).all()


def get_performances(db: Session, skip: int = 0, limit: int = 100,
                     min_last_changed_date: Optional[date] = None):

    query = db.query(models.Performance)

    if min_last_changed_date:
        query = query.filter(
            models.Performance.last_changed_date >= min_last_changed_date)

    return query.offset(skip).limit(limit).all()


def get_league(db: Session, league_id: Optional[int] = None):

    return db.query(models.League).filter(
            models.League.league_id == league_id
            ).first()


def get_leagues(db: Session, skip: int = 0, limit: int = 100,
                min_last_changed_date: Optional[date] = None,
                league_name: Optional[str] = None):

    query = db.query(models.League).options(joinedload(models.League.teams))
    if min_last_changed_date:
        query = query.filter(
            models.Player.last_changed_date >= min_last_changed_date)
    if league_name:
        query = query.filter(models.League.league_name == league_name)

    return query.offset(skip).limit(limit).all()


def get_teams(db: Session, skip: int = 0, limit=100,
              min_last_changed_date: Optional[date] = None,
              team_name: Optional[str] = None,
              league_id: Optional[int] = None):

    query = db.query(models.Team)
    if min_last_changed_date:
        query = query.filter(
            models.Player.last_changed_date >= min_last_changed_date)

    if team_name:
        query = query.filter(models.Team.team_name == team_name)

    if league_id:
        query = query.filter(models.Team.league_id == league_id)

    return query.offset(skip).limit(limit).all()


# analytics queries
def get_player_count(db: Session):
    query = db.query(models.Player)
    return query.count()


def get_team_count(db: Session):
    query = db.query(models.Team)
    return query.count()


def get_league_count(db: Session):
    query = db.query(models.League)
    return query.count()
