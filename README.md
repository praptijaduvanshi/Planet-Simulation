# Planet Simulation in Python

## Overview

This Python program simulates the motion of planets in a gravitational field. It utilizes numerical methods to calculate the positions of planets over time, taking into account gravitational forces between them.

## Features

- Simulate the motion of multiple planets in a 2D space.
- Determined parameters for initial conditions, such as position, velocity, and mass.
- Visualization of planetary orbits and positions using a graphical interface.

## File Structure

This repository contains the source code for a planet simulation in Python. The project is organized into the following file structure:

### `planet.py`

The `planet.py` file defines the `Planet` class, which encapsulates the properties and behaviors of celestial bodies in the simulation. This includes methods for drawing the planet, calculating gravitational forces, and updating its position.

### `main.py`

The `main.py` file is the main simulation script. It initializes the planets (Sun, Earth, Mars, Mercury, Venus, Jupiter), updates their positions based on gravitational interactions, and visualizes the simulation using Pygame. The window size is adjusted to accommodate the simulation.
