#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import socket
from common.message import OBCIMessageTool
import common.net_tools as net

from launcher.launcher_messages import message_templates

from launcher.plain_tcp_handling import make_unicode_netstring, recv_unicode_netstring


mtool = OBCIMessageTool(message_templates)

def send_and_receive(host, port, msg):
    netstr = make_unicode_netstring(msg)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    wfile = None
    rfile = None

    rec_msg = None
    try:
        # Connect to server and send data
        sock.connect((host, port))
        rfile = sock.makefile('rb', -1)
        wfile = sock.makefile('wb', 0)
        wfile.write(netstr)

        # Receive data from the server and shut down
        received = recv_unicode_netstring(rfile)
        print received
        print received.__class__, received[0], received[-1]
        rec_msg = mtool.unpack_msg(received)

    finally:
        sock.close()
        if wfile is not None:
            wfile.close()
        if rfile is not None:
            rfile.close()
    return rec_msg


def get_eeg_experiments(host, port):

    msg = mtool.fill_msg("find_eeg_experiments")
    response = send_and_receive(host, port, msg)

    if response.type == 'rq_error':
        print 'BLEEEEEEEEE'
    else:
        print ':-))))'

    if response.experiment_list:
        exp = response.experiment_list[0]
        # print exp
        host, port = exp['tcp_addr']
        msg = mtool.fill_msg("join_experiment", peer_id="blebleble")
        print "sending join to exp ", host, port
        response = send_and_receive(host, port, msg)
        print "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"


    msg = mtool.fill_msg("find_eeg_amplifiers", amplifier_type='virtual')
    response = send_and_receive(host, port, msg)

    if response.type == 'rq_error':
        print 'BLEEEEEEEEE2', response
    elif response is not None:
        print '\n\n****************************************************************\n\n'
        amp =  response.amplifier_list
        if amp:
            exp = amp[0]
            params = exp['amplifier_params']
            params['sampling_rate'] = '128'
            params['active_channels'] = '1;2;3;4'
            params['channel_names'] = 'aaa;bbb;xxx;fff'
            msg = mtool.fill_msg('start_eeg_signal', amplifier_params=params, name='HELL YEAH',
                                launch_file=exp['recommended_scenario'], client_push_address='')
            response= send_and_receive(host, port, msg)



if __name__ == '__main__':
    get_eeg_experiments('127.0.0.1', int(net.server_tcp_proxy_port()))#'172.16.53.135'
    #59336