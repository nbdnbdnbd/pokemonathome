#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import logging
import time

from threading import Thread

from pogom import config
from pogom.utils import get_args
from pogom.search import search_loop, create_search_threads
from pogom.models import init_database, create_tables, Pokemon, Pokestop, Gym

from pogom.utils import get_pos_by_name

logging.basicConfig(format='%(asctime)s [%(module)14s] [%(levelname)7s] %(message)s')
log = logging.getLogger()

if __name__ == '__main__':
    args = get_args()

    if args.debug:
        log.setLevel(logging.DEBUG);
    else:
        log.setLevel(logging.INFO);

    # These are very noisey, let's shush them up a bit
    logging.getLogger("peewee").setLevel(logging.INFO)
    logging.getLogger("requests").setLevel(logging.WARNING)
    logging.getLogger("pogom.pgoapi.pgoapi").setLevel(logging.WARNING)
    logging.getLogger("pogom.pgoapi.rpc_api").setLevel(logging.INFO)
    logging.getLogger('werkzeug').setLevel(logging.ERROR)

    config['parse_pokemon'] = not args.no_pokemon
    config['parse_pokestops'] = not args.no_pokestops
    config['parse_gyms'] = not args.no_gyms

    # Turn these back up if debugging
    if args.debug:
        logging.getLogger("requests").setLevel(logging.DEBUG)
        logging.getLogger("pgoapi").setLevel(logging.DEBUG)
        logging.getLogger("rpc_api").setLevel(logging.DEBUG)

    db = init_database()
    create_tables(db)

    position = get_pos_by_name(args.location)
    if not any(position):
        log.error('Could not get a position by name, aborting.')
        sys.exit()

    log.info('Parsed location is: {:.4f}/{:.4f}/{:.4f} (lat/lng/alt)'.
             format(*position))
    if args.no_pokemon:
        log.info('Parsing of Pokemon disabled.')
    if args.no_pokestops:
        log.info('Parsing of Pokestops disabled.')
    if args.no_gyms:
        log.info('Parsing of Gyms disabled.')

    config['CREDENTIALS'] = {'user': args.pah_username, 'key': args.pah_key}
    config['ORIGINAL_LATITUDE'] = position[0]
    config['ORIGINAL_LONGITUDE'] = position[1]
    config['LOCALE'] = args.locale
    config['CHINA'] = args.china


    log.debug('Starting a real search thread and {} search runner thread(s)'.format(args.num_threads))
    create_search_threads(args.num_threads)
    search_thread = Thread(target=search_loop, args=(args,))

    search_thread.daemon = True
    search_thread.name = 'search_thread'
    search_thread.start()

    while search_thread.is_alive():
        time.sleep(60)
