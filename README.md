# qualys_challenge

## Prerequisites:

```
python
elasticsearch
numpy
```

## Installing Prerequisites:

```
pip install -r requirements.txt
```

## Running the code:

```
python script.py
```

## Description:

1. The input dat file contains several readings where each reading is made up of 2 parts where each part is an unsigned integer (0-255).
2. The part 1 of all the readings and part 2 of the all the readings are put into an array of their own and the mean values of these 2 parts are computed.
3. A 2-d array of these two parts of the number is created which signifies each row of the array to be a complex number where the first part is real number and the second part is an imaginary number
4. The complex numbers are then made into json strings to be able to post them into an elasticsearch databse using the elasticsearch-py library.
5. An elasticsearch database was set up on aws and tested if the script is able to post to the database online succesfully