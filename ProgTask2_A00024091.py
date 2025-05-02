#include <iostream>
#include <cmath>
#include <array>

// 1. Solve a quadratic equation ax^2 + bx + c = 0
//    Returns number of real roots (0,1,2) and prints them.
int solveQuadratic(double a, double b, double c) {
    double D = b*b - 4*a*c;
    if (D > 0) {
        double sqrtD = std::sqrt(D);
        double x1 = (-b + sqrtD) / (2*a);
        double x2 = (-b - sqrtD) / (2*a);
        std::cout << "Two real roots: " << x1 << " and " << x2 << "\n";
        return 2;
    }
    else if (D == 0) {
        double x = -b / (2*a);
        std::cout << "One real root: " << x << "\n";
        return 1;
    }
    else {
        std::cout << "No real roots (discriminant < 0)\n";
        return 0;
    }
}

// 2. Reverse all the contents of an array of size 10
void reverseArray(std::array<int,10>& arr) {
    for (size_t i = 0; i < arr.size()/2; ++i) {
        std::swap(arr[i], arr[arr.size()-1 - i]);
    }
}

// 3. Check if a number is a power of 2
bool isPowerOfTwo(unsigned int n) {
    return n != 0 && ( (n & (n - 1)) == 0 );
}

// Example of usage
int main() {
    // 1. Quadratic
    double a = 1, b = -3, c = 2;
    solveQuadratic(a, b, c);
    
    // 2. Reverse array
    std::array<int,10> data = {0,1,2,3,4,5,6,7,8,9};
    reverseArray(data);
    std::cout << "Reversed: ";
    for (int x : data) std::cout << x << ' ';
    std::cout << '\n';
    
    // 3. Power of two
    unsigned int test = 16;
    std::cout << test << (isPowerOfTwo(test) ? " is " : " is not ")
              << "a power of 2\n";
    
    return 0;
}
