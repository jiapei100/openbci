#!/usr/bin/env python
# -*- coding: utf-8 -*-

import settings, variables_pb2
from multiplexer.multiplexer_constants import peers, types
from multiplexer.clients import connect_client
import socket

BUFFER_SIZE = 1024
VIRTUAL = False
VIRTUAL_MANUAL = False
VIRTUAL_CONSTANT = None #0.1
VIRTUAL_SAMPLING_SLEEP = 1/30.0

import random, time, configurer


import etr_logging as logger
LOGGER = logger.get_logger("etr_amplifier")




class EtrAmplifier(object):
    """A simple class to convey data from multiplexer (UGM_UPDATE_MESSAGE)
    to ugm_engine using udp. That level of comminication is needed, as
    pyqt won`t work with multithreading..."""
    def __init__(self, p_addresses):

        # Get from hash: ETR_IP, ETR_PORT
        LOGGER.info("Start initializin etr amplifier...")
        configurer_ = configurer.Configurer(p_addresses)
        configs = configurer_.get_configs(['ETR_AMPLIFIER_IP', 'ETR_AMPLIFIER_PORT'])
        self.connection = connect_client(type = peers.ETR_AMPLIFIER, addresses=p_addresses)
        LOGGER.info("Etr connected!")
        if not VIRTUAL:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.socket.bind((configs['ETR_AMPLIFIER_IP'],int(configs['ETR_AMPLIFIER_PORT'])))
        LOGGER.info("Socket binded!")
        configurer_.set_configs({'PEER_READY':str(peers.ETR_AMPLIFIER)}, self.connection)

    def _get_mx_message_from_etr(self, p_data):
        l_msg = variables_pb2.Sample2D()
        lst = p_data.split()

        if (len(lst) != 4):
            LOGGER.info("WARNING! Received data length != 4. Message ommited.")
            return None

        if lst[0] == 'x':
            try:
                l_msg.x = float(str(lst[1]).replace(",","."))
            except:
                LOGGER.info("WARNING! Error while unpacking x message. Message ommited.")                
                return None
        else:
            LOGGER.info("WARNING! received key different from x. Meesage ommited.")
            return None

        if lst[2] == 'y':
            try:
                l_msg.y = float(str(lst[3]).replace(",","."))
            except:
                LOGGER.info("WARNING! Error while unpacking y message. Message ommited.")
                return None
        else:
            LOGGER.info("WARNING! received key different from y. Meesage ommited.")
            return None
        l_msg.timestamp = time.time()
        return l_msg

    def run(self):
        """Method fired by multiplexer. It conveys update message to 
        ugm_engine using udp sockets."""
        try:
            while True:
                # Wait for data from ugm_server
                LOGGER.info("Waiting on socket ...")
                if not VIRTUAL:
                    l_data, addr = self.socket.recvfrom(1024)
                    l_msg = self._get_mx_message_from_etr(l_data)
                else:
                    l_msg = variables_pb2.Sample2D()
                    if VIRTUAL_MANUAL:
                        i = raw_input().split(' ')
                        l_msg.x = float(i[0])
                        l_msg.y = float(i[1])
                        l_msg.timestamp = time.time()
                    else:
                        time.sleep(VIRTUAL_SAMPLING_SLEEP)
                        if VIRTUAL_CONSTANT is not None:
                            l_msg.x = VIRTUAL_CONSTANT
                            l_msg.y = VIRTUAL_CONSTANT
                        else:
                            l_msg.x = random.random()
                            l_msg.y = random.random()
                        l_msg.timestamp = time.time()
                
                    # d should represent UgmUpdate type...
                if l_msg != None:
                    LOGGER.info("ETR sending message ... x = "+str(l_msg.x) + ", y = "+str(l_msg.y))
                    self.connection.send_message(message = l_msg.SerializeToString(), type = types.ETR_SIGNAL_MESSAGE, flush=True)            
        finally:
            if not VIRTUAL:
                self.socket.close()

if __name__ == "__main__":
    EtrAmplifier(settings.MULTIPLEXER_ADDRESSES).run()

