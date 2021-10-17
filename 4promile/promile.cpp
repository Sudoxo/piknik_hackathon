#include <iostream>
#include <cstdio>
#include <iomanip>

int main() {
    char plec;
    int masa, objetosc, procent;
    bool flag;

    do {
        flag = false;
        std::cout << "Plec (k/m):";
        plec = getchar();
        getchar();
        if (plec != 'k' && plec != 'm' && plec != 'K' && plec != 'M') {
            std::cout << "Niewlasciwa plec (k - kobieta, m - mezczyzna)\n";
            flag = true;
        }
    } while(flag);

    std::cout << "Masa (kg): ";
    std::cin >> masa;

    std::cout << "Objetosc spozytego napoju (ml): ";
    std::cin >> objetosc;
    std::cout << "Procent zawartosci alkoholu w spozytym napoju: ";
    std::cin >> procent;

    float A = 0.0079f * objetosc * procent;
    float K, prom, B;

    if (plec == 'k' || plec == 'K') {
        K = 0.55f; //https://en.wikipedia.org/wiki/Blood_alcohol_content
        B = 0.1f; //angielska wiki twierdzi ze u kobiet spalanie/h wynosi 0.017%
    } else {
        K = 0.68f; 
        B = 0.15f;
    }
    prom = A/(K * masa);
    std::cout << std::setprecision(2) << std::fixed;

    std::cout << "\nWskazanie alkomatu: " << prom << "‰\n";

    int czas = 0;
    while (prom >= 0.2f) {
        czas++;
        prom -= B;
    }
    std::cout << "Po " << czas << "h procent alkoholu we krwi zejdzie ponizej 0.2‰\n";
    return 0;
}

