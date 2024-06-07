#pragma once
#include <vector>
#include "Cell.h"

class Grid
{
public:
    Grid(int rows, int cols);
    void initializeRandom();
    void printGrid() const;
    void update();

private:
    int rows;
    int cols;
    std::vector<std::vector<Cell> > cells;
    int countAliveNeighbours(int row, int col) const;
};