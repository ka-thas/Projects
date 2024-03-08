#include "cell.h"

Cell::Cell() : alive(false) {}

bool Cell::isAlive() const
{
    return alive;
}

void Cell::setAlive(bool Alive)
{
    this->alive = alive;
}

void Cell::toggleState()
{
    alive = !alive;
}
