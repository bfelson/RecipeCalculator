import requests
import numpy as np
from bs4 import BeautifulSoup
import pandas as pd

def getIngredientPrice(ingredient):
    price = 0.0
    return price

def calculateRecipeCost(recipe):
    recipePrice = 0.0
    for ingredient in recipe:
        recipePrice += getIngredientPrice(ingredient)
    return recipePrice

def calculateGroceriesPrice(recipes):
    groceriesPrice = 0.0
    for recipe in recipes:
        groceriesPrice += calculateRecipeCost(recipe)
    
