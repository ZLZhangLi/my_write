
#include<iostream>
#include<math.h>
#define ElemType int
using namespace std;

void GaoSi(double **gaosi, const int size, const double sigma){
	const double PI = 4.0*atan(1.0);
	int center = size / 2;
	double sum = 0;
	for (int i = 0; i < size; i++){
		for (int j = 0; j < size; j++){
			gaosi[i][j] = (1 / (2 * PI*sigma*sigma))*exp(-((i - center)*(i - center) + (j - center)*(j - center)) / (2 * sigma*sigma));
			sum += gaosi[i][j];
		}
	}

	for (int i = 0; i < size; i++){
		for (int j = 0; j < size; j++){
			gaosi[i][j] /= sum;
			cout << gaosi[i][j] << " ";
		}
		cout << endl;// << endl;

	}
	return ;
}

int main() {
	int size;
	float sigma;
	cin >> size >> sigma;
	double **gaosi = new double *[size];
	for (int i = 0; i < size; i++){
		gaosi[i] = new double[size];
	}
	GaoSi(gaosi, size, sigma);
	return 0;
}