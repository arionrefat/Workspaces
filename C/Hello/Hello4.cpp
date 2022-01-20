#include <bits/stdc++.h>

using namespace std;
int main() {
  cout << "Hello , Welcome to Refatel Carpet cleaning service "
       << "\n"
       << "\n";
  cout << "How many Small rooms do you want: "
       << "\n";
  int numberOfSmallRooms{0};
  cin >> numberOfSmallRooms;

  cout << "How many Large rooms do you want: "
       << "\n";
  int numberOfLargeRooms{0};
  cin >> numberOfLargeRooms;

  const double priceSmallRoom{25.0};
  const double priceLargeRoom{35.0};
  const double sales_tax{0.06};
  const int estimateExpiry{30}; // days

  cout << "\nEstimate for Carpet cleaning service " << endl;
  cout << "Number of Small room( s) : " << numberOfSmallRooms << "\n";
  cout << "Price per Small room $" << priceSmallRoom << "\n";
  cout << "Number of Large room(s) : " << numberOfLargeRooms << "\n";
  cout << "Price per Large room $" << priceLargeRoom << "\n";
  cout << "Cost: $"
       << (priceSmallRoom * numberOfSmallRooms) +
              (priceLargeRoom * numberOfLargeRooms)
       << "\n";
  cout << "Tax: $"
       << ((priceSmallRoom * numberOfSmallRooms) +
           (priceLargeRoom * numberOfLargeRooms)) *
              sales_tax
       << "\n";
  cout << "#################################################"
       << "\n";

  cout << "Total estimate: $"
       << (priceSmallRoom * numberOfSmallRooms) +
              (priceLargeRoom * numberOfLargeRooms) +
              ((priceSmallRoom * numberOfSmallRooms) +
               (priceLargeRoom * numberOfLargeRooms)) *
                  sales_tax
       << "\n";
  cout << "This estimate is valid for " << estimateExpiry << " days"
       << "\n";
}
