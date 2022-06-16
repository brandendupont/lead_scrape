# Scrape MHD HEH Dashboard 

A postprocess script in Github's Flat Data actions is used to fire a Python script that collects data from the [Milwaukee Health Department Lead Dashboard](https://healthmke.quickbase.com/db/bptnemrfu?a=showpage&pageID=22)

## Execution :

- the Flat Data action is scheduled weekly to run on Monday.

- the `postprocess.ts` script is then run, triggers the install of python packages, and runs the main python script `postprocess.py`.

- `postprocess.py` prints out its received arguments, and then generates CSV files `abated_lead.csv` (abated properties since 2018) and `open_lead.csv` (properties with lead hazard not yet abated since 2018). 

## Thanks

- Thanks to the Github Octo Team
- Thanks to [Pierre-Olivier Simonard](https://github.com/pierrotsmnrd/flat_data_py_example) for his repo on implementing Flat data as a Python postprocess file.

