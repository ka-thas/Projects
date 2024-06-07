#include "World.h"

int main()
{
    const int rows = 10;
    const int cols = 10;
    const int generations = 5;

    World world(rows, cols);
    world.run(generations);

    return 0;
}