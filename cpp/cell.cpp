#include "Cell.h"

Cell::Cell() : alive(false) {}

bool Cell::isAlive() const
{
    return alive;
}

void Cell::setAlive(bool alive)
{
    this->alive = alive;
}

void Cell::toggleState()
{
    alive = !alive;
}
