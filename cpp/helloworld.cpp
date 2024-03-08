#include <iostream>

class Dog
{
public:
    std::string name;

    void bark()
    {
        std::cout << "WOOF! My name is " << name << std::endl;
    }
};

// function
int add(int a, int b)
{
    return a + b;
}

int main()
{
    std::cout << "Hello, world!" << std::endl;

    // Variables
    int age = 20;
    double pi = 3.14;
    char grade = 'A';

    std::cout << "input age: ";
    std::cin >> age;

    // Conditionals
    if (age < 18)
    {
        std::cout << "You are a minor" << std::endl;
    }
    else
    {
        std::cout << "You are an adult" << std::endl;
    }

    // loops
    for (int i = 0; i < 10; i++)
    {
        std::cout << i << " ";
    }

    // Calling a function
    int num = add(1, 5);
    std::cout << num << std::endl;

    Dog myDog;
    myDog.name = "Pluto";
    myDog.bark();

    return 0;
}
