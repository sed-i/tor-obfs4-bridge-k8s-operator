# Copyright 2023 Ubuntu
# See LICENSE file for licensing details.

import unittest

import ops.testing
from ops.model import ActiveStatus
from ops.testing import Harness

from charm import TorObfs4Bridge


class TestCharm(unittest.TestCase):
    def setUp(self):
        ops.testing.SIMULATE_CAN_CONNECT = True
        self.addCleanup(setattr, ops.testing, "SIMULATE_CAN_CONNECT", False)

        self.harness = Harness(TorObfs4Bridge)
        self.addCleanup(self.harness.cleanup)
        self.harness.begin()

    def test_pebble_ready(self):
        # Simulate the container coming up and emission of pebble-ready event
        self.harness.container_pebble_ready("bridge")
        # Ensure we set an ActiveStatus with no message
        self.assertEqual(self.harness.model.unit.status, ActiveStatus())
