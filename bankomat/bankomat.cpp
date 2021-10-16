#include <iostream>
#include <map>

const int MAX_VALUE = 1000;

int prev[MAX_VALUE];
int min[MAX_VALUE];

void writeSolution(int x, int * nom, int n);

void fillArr(int *nom, int n);

int main() {
    int n, q, p;
    std::cin >> n >> q;

    int *nom = new int[n];
    for (int i = 0; i < n; i++) {
        std::cin >> nom[i];
    }

    fillArr(nom, n);

    for (int i = 0; i < q; i++) {
        std::cin >> p;
        writeSolution(p, nom, n);
    }
    delete[] nom;
    return 0;
}

void writeSolution(int x, int * nom, int n) {
    if (x > MAX_VALUE - 1 || x < 1) {
        std::cout << "Wartosci moga byc z przedzialu <1;" << MAX_VALUE - 1 << ">\n";
        return;
    }

    if (min[x] == -1) {
        std::cout << "Nie da sie wyplacic!\n";
        return;
    }

    std::map <int, int> res;
    int a = x;

    while (prev[a] != 0) {
        res[a - prev[a]]++;
        a = prev[a];
    }
    res[a]++;

    for (int i = n-1; i >= 0; i--) {
        if (res[nom[i]] > 0) {
            std::cout << nom[i] << " x" << res[nom[i]] << "\n";
        }
    }
}

void fillArr(int *nom, int n) {
    min[0] = 0;
    prev[0] = 0;
    for (int i = 1; i < MAX_VALUE; i++) {
        int m = MAX_VALUE + 1;
        for (int j = 0; j < n; j++) {
            if (i - nom[j] >= 0) {
                if (min[i - nom[j]] != -1) {
                    if (min[i - nom[j]] + 1 < m) {
                        m = min[i - nom[j]] + 1;
                        prev[i] = i - nom[j];
                    }
                }
            }
        }
        if (m == MAX_VALUE + 1) {
            min[i] = -1;
        } else {
            min[i] = m;
        }
    }
}