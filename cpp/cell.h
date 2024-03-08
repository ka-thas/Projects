#pragma once

class Cell
{
private:
    bool alive;

public:
    Cell();

    bool isAlive() const;

    void setAlive(bool alive);
    void toggleState();
};