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
            cells[i][j].setAlive(rand() % 2 == 1);
        }
    }
}

void Grid::printGrid() const
{
    for (int i; i < rows; i++)
    {
        for (int j = 0; j < cols; j++)
        {
            std::cout << (cells[i][j].isAlive() ? '*' : ' ') << ' ';
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
            if (ni >= 0 && ni < rows && nj >= 0 && nj < cols && !(i == 0 && j == 0)) // check if the cell is within the grid
            {
                count += cells[ni][nj].isAlive() ? 1 : 0;
            }
        }
    }
    return count;
}

void Grid::update()
{
    std::vector<std::vector<Cell>> newCells = cells; // Next generation

    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < cols; j++)
        {
            int aliveNeighbours = countAliveNeighbours(i, j);

            if (cells[i][j].isAlive())
            {
                if (aliveNeighbours < 2 || aliveNeighbours > 3)
                {
                    newCells[i][j].setAlive(false);
                }
            }
            else
            {
                if (aliveNeighbours == 3)
                {
                    newCells[i][j].setAlive(true);
                }
            }
        }
    }
    cells = newCells;
}