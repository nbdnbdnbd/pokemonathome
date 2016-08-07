<<<<<<< HEAD
Pokémon@Home Client
===================

Registration
------------
Visit http://pokemonathome.herokuapp.com/register to make an account and
receive a private key.


Installation
------------

Make sure you're in a python2.7 environment and run:

```bash
$ git clone https://github.com/nbdnbdnbd/pokemonathome.git
$ cd pokemonathome
$ pip install -r requirements.txt
```


Execution
---------

```bash
$ python app.py -a $AUTH_SERVICE -u $USERNAME -p $PASSWORD -pk $PAH_KEY -l $LOCATION
```

+ `AUTH_SERVICE` is either `google` or `ptc`
+ `USERNAME` is your `google` or `ptc` username
+ `PASSWORD` is your `google` or `ptc` password
+ `PAH_KEY` is your Pokémon@Home private key
+ `LOCATION` is your desired search address (e.g. '1600 Pennsylvania Ave NW, Washington, DC')
=======
# API is currently down, please don't submit issues. Actively working on fix, might be a while.

# PokemonGo Map![Python 2.7](https://img.shields.io/badge/python-2.7-blue.svg)


Live visualization of all the pokemon (with option to show gyms and pokestops) in your area. This is a proof of concept that we can load all the pokemon visible nearby given a location. Currently runs on a Flask server displaying Google Maps with markers on it.

Features: 

* Shows Pokemon, Pokestops, and gyms with a clean GUI.
* Notifications 
* Lure information
* Multithreaded mode
* Filters
* Independent worker threads (many can be used simulatenously to quickly generate a livemap of a huge geographical area)
* Localization (en, fr, pt_br, de, ru, zh_cn, zh_hk)
* DB storage (sqlite or mysql) of all found pokemon
* Incredibly fast, efficient searching algorithm (compared to everything else available)

[![Deploy](https://raw.githubusercontent.com/sych74/PokemonGo-Map-in-Cloud/master/images/deploy-to-jelastic.png)](https://jelastic.com/install-application/?manifest=https://raw.githubusercontent.com/sych74/PokemonGo-Map-in-Cloud/master/manifest.jps) [![Deploy](https://www.herokucdn.com/deploy/button.png)](https://github.com/AHAAAAAAA/PokemonGo-Map/wiki/Heroku-Deployment) 

#[Twitter] (https://twitter.com/PokemapDev), [Website] (https://jz6.github.io/PoGoMap/)#

![Map](https://raw.githubusercontent.com/AHAAAAAAA/PokemonGo-Map/master/static/cover.png)


## How to setup

For instructions on how to setup and run the tool, please refer to the project [wiki](https://github.com/AHAAAAAAA/PokemonGo-Map/wiki), or the [video guide](https://www.youtube.com/watch?v=RJKAulPCkRI).


## Android Version

There is an [Android port](https://github.com/omkarmoghe/Pokemap) in the works. All Android related prs and issues please refer to this [repo](https://github.com/omkarmoghe/Pokemap).

## iOS Version

There is an [iOS port](https://github.com/istornz/iPokeGo) in the works. All iOS related prs and issues please refer to this [repo](https://github.com/istornz/iPokeGo).

## Warnings

Using this software is against the ToS of the game. You can get banned, use this tool at your own risk.


## Contributions

Please submit all pull requests to [develop](https://github.com/AHAAAAAAA/PokemonGo-Map/tree/develop) branch.

Building off [tejado's python pgoapi](https://github.com/tejado/pgoapi), [Mila432](https://github.com/Mila432/Pokemon_Go_API)'s API, [leegao's additions](https://github.com/leegao/pokemongo-api-demo/tree/simulation) and [Flask-GoogleMaps](https://github.com/rochacbruno/Flask-GoogleMaps). Current version relies primarily on the pgoapi and Google Maps JS API.
>>>>>>> 9c2f6d03eaa779c4d85df4403de55f65587ca84c
