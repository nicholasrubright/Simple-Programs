//A simple C++ program that computes the factorial of any integer the user inputs

#include <iostream>
using namespace std;

int factorial(int x)
{
	if (x == 0)
		return 1;
	return x * factorial(x - 1);
}

int main()
{
	int value;
	cout << "Enter a number:";
	cin >> value;
	cout << factorial(value);
}
