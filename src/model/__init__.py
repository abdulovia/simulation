"""
Model Package
===============

This package contains classes that represent various models in the simulation world.

Modules:
- Counter: The class for counting moves of the simulation.
- Entity: The root abstract class for all the creatures and objects.
- Rock: The class for static objects that function as obstacles on the map.
- Tree: The class for static objects that function as obstacles on the map.
- Grass: The class for static objects that serve as resources for herbivores.
- Creature: An abstract creatures class serves as the superclass for both herbivores and predators.
- Herbivore: The class of dynamic creatures - herbivores - functions as a resource for predators.
- Predator: The class of dynamic creatures - predators - strive to locate resources in the form of herbivores.
- Map: The class for storing all the simulation objects.
- Point: The class for coordinates of objects.

"""

from src.model.counter import Counter
from src.model.entity import Entity
from src.model.dynamic_entities import Creature, Herbivore, Predator
from src.model.static_entities import Rock, Grass, Tree
from src.model.map import Map
from src.model.point import Point
