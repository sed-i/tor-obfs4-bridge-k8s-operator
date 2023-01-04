#!/usr/bin/env python3
# Copyright 2023 Ubuntu
# See LICENSE file for licensing details.

"""Charm the application."""

import logging

from ops.charm import CharmBase
from ops.main import main
from ops.model import ActiveStatus
from ops.pebble import ChangeError, ExecError, Layer, PathError, ProtocolError

logger = logging.getLogger(__name__)


class TorObfs4Bridge(CharmBase):
    """Charm the application."""

    _container_name = _layer_name = _service_name = "bridge"

    def __init__(self, *args):
        super().__init__(*args)
        self.container = self.unit.get_container(self._container_name)
        self.framework.observe(self.on.bridge_pebble_ready, self._on_pebble_ready)

    def _on_pebble_ready(self, event):
        """Handle pebble-ready event."""
        overlay = self._layer()
        self.container.add_layer(self._layer_name, overlay, combine=True)
        self.container.replan()
        self.unit.status = ActiveStatus()

    def _layer(self) -> Layer:
        return Layer(
            {
                "summary": "obfs4-bridge layer",
                "description": "pebble layer for obfs4-bridge",
                "services": {
                    self._service_name: {
                        "override": "replace",
                        "summary": "obfs4-bridge service",
                        "command": "/usr/local/bin/start-tor.sh",  # their script generates config
                        "startup": "enabled",
                        "environment": {
                            "OR_PORT": "8000",
                            "PT_PORT": "8001",
                            "EMAIL": "82407168+sed-i@users.noreply.github.com",
                            "NICKNAME": "DockerObfs4Bridge",
                            "OBFS4_ENABLE_ADDITIONAL_VARIABLES": "1",
                            "OBFS4V_AddressDisableIPv6": "1",
                        },
                    }
                },
            }
        )


if __name__ == "__main__":  # pragma: nocover
    main(TorObfs4Bridge)
