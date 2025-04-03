"""Testin SQLAlchemy Helper Fuctions """
import pytest
from datetime import date

import crud
from database import SessionLocal

# use a test date of 4/1/2024 to test the min_last_changed_date.
test_date = date(2024, 4, 1)


@pytest.fixture(scope="function")
def db_session():
    """This starts a database session and closes it when done"""
    session = SessionLocal()
    yield session
    session.close()


def test_get_player(db_session):
    """Tests you can get the first player"""
    player = crud.get_player(db_session, player_id=1001)
    assert player is not None, "player not found in database"
    assert player.player_id == 1001


def test_get_players(db_session):
    """Test that the count of players in the datbase is except"""
    players = crud.get_players(
        db_session, skip=0, limit=10000, min_last_changed_date=test_date)
    assert len(players) == 1018


def test_get_players_by_name(db_session):
    """Test tha the count of players in the database is what is expected"""
    players = crud.get_players(
        db_session, first_name="Bryce", last_name="Young")
    assert len(players) == 1
    assert players[0].player_id == 2009


def test_get_all_performanaces(db_session):
    performaces = crud.get_performances(
        db_session, skip=0, limit=18000, min_last_changed_date=test_date)
    assert len(performaces) >= 2711


# test the count functions
def test_get_player_count(db_session):
    player_count = crud.get_player_count(db_session)
    assert player_count == 1018
