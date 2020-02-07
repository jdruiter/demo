
# Simple Calculator REST API

## Introduction
 
A simple calculator as JSON REST API. 

## Run

    # Install django and simplecalculator
    $ pip install -r requirements.txt
    
    $ python manage.py runserver 8000

## Examples

http://localhost:8000/ 2+2

http://localhost:8000/ 2 + 2

http://localhost:8000/ 2 / 2 

http://localhost:8000/ abs-20

http://localhost:8000/ ceil 1.001

http://localhost:8000/ 10 fmod 4

## Usage

This calculator is as forgiving as a simple desktop calculator, it will
ignore what it does not know, try to compute what it can treating the
given string as a list of keystrokes.

Use of spaces between arguments is optional, both work: 
    
    localhost:8000/2+2
    
    localhost:8000/ 2 + 2

Two argument operators: 

    2 + 2
    2 - 2
    2 * 2
    2 / 2
    10 fmod 4   #result: 2. Modulo operator

Single argument operators:
    
    -5 abs      # result: 5. Give the absolute of the number
    -5 fabs     # result: 5. Give the (float) absolute of the number
    2.45 ceil   # result: 3. 
    
    
   
# Credits
Django REST API: Joris de Ruiter,
[Github](https://github.com/jdruiter/code-samples-jdruiter)

Simple Calculator: Jacek Artymiak,
[Python SimpleCalculator](https://pypi.org/project/simplecalculator/)





