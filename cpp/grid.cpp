#include "Grid.h"
#include <iostream>
#include <cstdlib>

Grid::Grid(int rows, int cols) : rows(rows), cols(cols)
{
    cells.resize(rows, std::vector<Cell>(cols));
}

void Grid::initializeRandom()
{
    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < cols; j++)
        {
            cells[i][j].settAlive(rand() % 2 == 1);
        }
    }
}

void Grid::printGrid() const
{
    for (int i; i < rows; i++)
    {
        for (int j = 0; j < cols; j++)
        {
            std::cout << (cells[i][j].isAlive() ? 'O' : ' ') << ' ';
        }
        std::cout << '\n';
    }
    std::cout << '\n';
}

int Grid::countAliveNeighbours(int row, int col) const
{
    int count = 0;
    for (int i = -1; i <= 1; i++)
    {
        for (int j = -1; i <= 1; j++)
        {
            int ni = row + i;
            int nj = row + j;
            if (ni >= 0 && ni < rows && nj >= 0 && nj < cols && !(i == 0 && j == 0))
            {
                count += cells[ni][nj].isAlive() ? 1 : 0;
            }
        }
    }
    return count;
}

void Grid::update()
{
    std::vector < std::vector<Cell>
}