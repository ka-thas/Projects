#include "World.h"
#include <iostream> // Add this line

World::World(int rows, int cols) : grid(rows, cols) {}

void World::run(int generations)
{
    grid.initializeRandom();

    for (int gen = 0; gen < generations; gen++)
    {
        std::cout << "Generation " << gen + 1 << ":\n";
        grid.printGrid();
        grid.update();
    }
}