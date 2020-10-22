#include<bits/stdc++.h>

using namespace std;
const double pi {3.1416};
//Using function prototype
double circle_area(double radius);
double cylinder_volume(double radius,double height);
void area_circle();
void volume_cylinder();

int main(){
	area_circle();
	volume_cylinder();
}

double circle_area(double radius){
	return pi*radius*radius;
}

double cylinder_volume(double radius,double height){
	return circle_area(radius)*height;
}

void area_circle(){
	double radius{};
	cout << "Enter the radius " << "\n";
	cin >> radius;
	cout << "The Area is " << circle_area(radius) << "\n";
}

void volume_cylinder(){
	double radius{};
	double height{};
	cout << "Enter the radius " << "\n";
	cin >> radius;
	cout << "Enter the height " << "\n";
	cin >> height;
	cout << "The Area is " << cylinder_volume(radius,height) << "\n";
}

