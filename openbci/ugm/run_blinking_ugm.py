#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:
#     Mateusz Kruszyński <mateusz.kruszynski@gmail.com>
from ugm import ugm_internal_server
class UdpBlinkingServer(ugm_internal_server.UdpServer):
    def process_message(self, message):
        if not super(UdpBlinkingServer, self).process_message(message):
            # assumed that if not UGM_UPDATE_MESSAGE then it is UGM_CONTROL_MESSAGE
        # should represent UgmUpdate type...
            l_msg = variables_pb2.Variable()
            try:
                l_msg.ParseFromString(message)
                LOGGER.info("Properly parsed UGM_CONTROL_MESSAGE...")
            except:
                LOGGER.info("PARSER ERROR, too big ugm control message  or not UGM_CONTROL_MESSAGE...")
                return False
            self._ugm_engine.control(l_msg)

        return True
            

import configurer
from blinking import ugm_blinking_engine
from blinking import ugm_blinking_connection
from ugm import ugm_config_manager
import settings

if __name__ == "__main__":
    # Create instance of ugm_engine with config manager (created from
    # default config file
    configs = configurer.Configurer(settings.MULTIPLEXER_ADDRESSES).get_configs(['UGM_CONFIG', 'UGM_USE_TAGGER', 'UGM_INTERNAL_IP', 'UGM_INTERNAL_PORT'])
    connection = ugm_blinking_connection.UgmBlinkingConnection(settings.MULTIPLEXER_ADDRESSES)

    ENG = ugm_blinking_engine.UgmBlinkingEngine(ugm_config_manager.UgmConfigManager(configs['UGM_CONFIG']),
                                                connection
                                                )
    c = configurer.Configurer(settings.MULTIPLEXER_ADDRESSES).get_configs(ENG.get_requested_configs())
    ENG.set_configs(c)

    thread.start_new_thread(UdpBlinkingServer(ENG, 
                                              configs['UGM_INTERNAL_IP'],
                                              int(configs['UGM_INTERNAL_PORT']),
                                              int(configs['UGM_USE_TAGGER'])).run, ())


    # Start multiplexer in a separate process
    path = os.path.join(settings.module_abs_path(), "ugm_server.py")
    os.system("python " + path + " &")


    #TODO - works only when running from openbci directiory...
    # fire ugm engine in MAIN thread (current thread)
    ENG.run()

