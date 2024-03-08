# include <iostream>

// Base class
class Shape {
    public:
        virtual double area() const = 0; // Virtual class
};

// Derived classes
class Circle : public Shape {
    private:
        double radius;

    public:
        Circle(double r) : radius(r) {}

        double area() const override {
            return 3.14 * radius * radius;
        }
};

class Rectangle : public Shape {
    private:
        double length;
        double width;

    public:
        Rectangle(double l, double w) : length(l), width(w) {}

        double area() const override {
            return length * width;
        }
};

int main() {
    Circle circle(5.0);
    Rectangle rectangle(4.0, 6.0);

    // Polymorphism - common interface
    Shape* shape1 = &circle;
    Shape* shape2 = &rectangle;

    std::cout << "Circle area: " << shape1->area() << std::endl;
    std::cout << "Rectangle area: " << shape2->area() << std::endl;

    return 0;
}