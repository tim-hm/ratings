#!/usr/bin/env python3
# Copyright 2023 Canonical
# See LICENSE file for licensing details.

"""Ubuntu Software Centre ratings service.

A backend service to support application ratings in the new Ubuntu Software Centre.
"""

import logging

import ops
from charms.data_platform_libs.v0.data_interfaces import DatabaseCreatedEvent, DatabaseRequires

logger = logging.getLogger(__name__)


class RatingsCharm(ops.CharmBase):
    """Main operator class for ratings service."""

    def __init__(self, *args):
        super().__init__(*args)

        self._container = self.unit.get_container("ratings")
        self._database = DatabaseRequires(self, relation_name="database", database_name="ratings")

        self.framework.observe(self.on.ratings_pebble_ready, self._on_ratings_pebble_ready)
        self.framework.observe(self._database.on.database_created, self._on_database_created)

    def _on_ratings_pebble_ready(self, event: ops.PebbleReadyEvent):
        """Define and start the workload using the Pebble API."""
        if not self._database.is_resource_created():
            self.unit.status = ops.WaitingStatus("Waiting for database creation")
            return

        self._start_ratings_service()

    def _on_database_created(self, event: DatabaseCreatedEvent):
        """Handle the database creation event."""
        conn_str = f"postgres://{event.username}:{event.password}@{event.endpoints}/ratings"
        self._start_ratings_service(conn_str)

    def _start_ratings_service(self, connection_string=None):
        """Populate Pebble layer and start the ratings service."""
        if connection_string is None:
            connection_string = self._database_connection_string()

        if self._container.can_connect():
            self._container.add_layer(
                "ratings", self._pebble_layer(connection_string), combine=True
            )
            self._container.replan()
            self.unit.status = ops.ActiveStatus()
        else:
            logger.info("Cannot connect to ratings container. Deferring event.")
            self.unit.status = ops.WaitingStatus("Waiting for ratings container")

    def _database_connection_string(self) -> str:
        """Report database connection string using info from relation data bag."""
        relation_id = self._database.relations[0].id
        relation_data = self._database.fetch_relation_data()[relation_id]

        username = relation_data.get("username")
        password = relation_data.get("password")
        endpoints = relation_data.get("endpoints")

        return f"postgres://{username}:{password}@{endpoints}/ratings"

    def _pebble_layer(self, db_connection_string):
        """Return a dictionary representing a Pebble layer."""
        return {
            "summary": "ratings layer",
            "description": "pebble config layer for ratings",
            "services": {
                "ratings": {
                    "override": "replace",
                    "summary": "ratings",
                    "command": "/bin/ratings",
                    "startup": "enabled",
                    "environment": {
                        "POSTGRES": db_connection_string,
                        # TODO: Replace this placeholder
                        "JWT_SECRET": "deadbeef",
                    },
                }
            },
        }


if __name__ == "__main__":  # pragma: nocover
    ops.main(RatingsCharm)
