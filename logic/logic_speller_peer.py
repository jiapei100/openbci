#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:
#     Mateusz Kruszyński <mateusz.kruszynski@gmail.com>
#
import time
from obci_utils import tags_helper
from multiplexer.multiplexer_constants import peers, types
from logic import logic_helper
from logic.logic_decision_peer import LogicDecision
from logic.engines.speller_engine import SpellerEngine

from obci_configs import settings, variables_pb2
from logic import logic_logging as logger
LOGGER = logger.get_logger("logic_speller", "info")

class LogicSpeller(LogicDecision, SpellerEngine):
    """A class for creating a manifest file with metadata."""
    def __init__(self, addresses):
        LogicDecision.__init__(self, addresses=addresses)
        SpellerEngine.__init__(self, self.config.param_values())
        self.ready()
        self._update_letters()

    def _run_post_actions(self, p_decision):
        self._update_letters()

if __name__ == "__main__":
    LogicSpeller(settings.MULTIPLEXER_ADDRESSES).loop()

