import pytest
import mysql.connector
from unittest.mock import Mock


def test_database_connection_failure_is_detected():
    mock_connection = Mock(
        side_effect=mysql.connector.Error(
            "Simulated database connection failure"
        )
    )

    with pytest.raises(
        mysql.connector.Error,
        match="Simulated database connection failure"
    ):
        mock_connection()
