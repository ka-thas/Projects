#pragma once
#include "Grid.h"

class World
{
public:
    World(int rows, int cols);
    void run(int generations);

private:
    Grid grid;
};