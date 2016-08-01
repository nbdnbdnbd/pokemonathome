import logging
from requests import post

log = logging.getLogger(__name__)


def send_to_server(url, credentials, pokemons):
    data = {'pokemons': pokemons}
    data['credentials'] = credentials
    try:
        log.info('Posting data to ' + url.format(''))
        r = post(url.format('submit'), json=data)
        if r.status_code == 200:
            log.info('Post successful.')
        else:
            log.warning('Post failed: {} ({})'.format(r.reason, r.status_code))
    except:
        log.info('Post failed.')
