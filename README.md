# [<img src="https://api.manacube.com/img/favicon.webp">](manacube.com) ManaSales

ManaSales is a tool to help players of the manacube server decide at what price to sell their SVA's (Seasonal Vault Access) items by giving them data on previous sales and the total amount of their SVA in circulation.

Installation
------------

To install the manaSales tool, simply:

```console
$ git clone https://github.com/wholeheartedness/manaSales.git

$ cd manaSales

$ python -m pip install -r requirements.txt
```

Usage
-----

### Searching
To search for sva ID's you must perform a search for them using a feature built into the application. All you need to know is the gamemode you want to search on and the filters you want to search by.
 - Possible queries include:
 - `mv` to filter by mineville svas
 - `17/19/20/21/22` to filter by years (does not include every sva made in that year because mana is annoying)
 - `manasets` to only show sets
 - `gadgets` to only show gadgets
 - `wildtools` to filter by special effect tools (Ex: trench tools or sell wands)
 - enter nothing to get a list of all svas for that gamemode

 ### Everything else
 Everything else is self explanatory so figure it out