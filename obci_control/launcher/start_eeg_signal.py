#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import zmq
import time
import socket

import common.net_tools as net
from common.message import OBCIMessageTool, send_msg, recv_msg, PollingObject
from launcher.launcher_messages import message_templates, error_codes
from launcher.obci_client import OBCIClient

import launcher.launcher_logging as logger
import launcher.launcher_tools
from common.obci_control_settings import PORT_RANGE
from peer import peer_cmd

LOGGER = logger.get_logger("start_eeg_signal", "info")

def start_eeg_signal_experiment(ctx, srv_addrs, rq_message):
    client = OBCIClient(srv_addrs, ctx)
    # server_req_socket = ctx.socket(zmq.REQ)
    #     for addr in srv_addrs:
    #         server_req_socket.connect(addr)

    amp_params = rq_message.amplifier_params

    par_list = ['--peer', 'amplifier']
    for par, val in amp_params.iteritems():
        par_list += ['-p', par, unicode(val)]

    overwrites = peer_cmd.peer_overwrites_pack(par_list)
    result = client.launch(rq_message.launch_file, None, rq_message.name, overwrites)


    LOGGER.info("START EEG signal! return to:  " + rq_message.client_push_address)
    mtool = OBCIMessageTool(message_templates)
    to_client = ctx.socket(zmq.PUSH)
    to_client.connect(rq_message.client_push_address)
    if result is None:
        send_msg(to_client, mtool.fill_msg("rq_error", err_code="launch_failed",
                    details="No response from server or experiment"))
    else:
        send_msg(to_client, result.raw())
    LOGGER.info("sent eeg launch result"  + str(result)[:500] )
    time.sleep(0.1)