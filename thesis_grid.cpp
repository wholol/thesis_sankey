//Author:Der Zhi Jeremy Sow
//Date: 22/3/19

#include "pch.h"
#include "math.h"
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
using namespace std;


double Percentarray[7];
double PercentageRatio[7] = { 0.178,0.559,0.068,0.093,0.083,0.014,0.005 };
string PercentageGrid[7] = { "brown coal","black coal", "unrefined gas","solar","wind","hydro","other" };
string ExcelColumn[7] = { "O","Q","U","W","Y","AC","AE" };




int main(){
	double percent; char end;
	while (1) {
		system("cls");
		cout << " insert electricity percentage (%)" << endl;
		cin >> percent;
		for (int i = 0; i <= 6; i++) {
			Percentarray[i] = PercentageRatio[i] * percent;
				cout << PercentageGrid[i] << "  is   " << Percentarray[i] << "    at excel column    " << ExcelColumn[i] << endl;
 		}
		cout << "press x to break" << endl;
		cin >> end;
		if (end == 'x') {
			break;
		}
	}

	
	system("pause");
}
