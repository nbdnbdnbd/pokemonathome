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
