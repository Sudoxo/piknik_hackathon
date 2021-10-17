#include <iostream>

struct Point {
    int x;
    int y;
};

int orientation(Point a, Point b, Point c);

bool isIntersection(Point a, Point b, Point c, Point d);

int main() {
    int n, area = 0;
    std::cin >> n;
    Point *vertices = new Point[n];
    for (int i = 0; i < n; i++) {
        std::cin >> vertices[i].x >> vertices[i].y;

        //check for intersections
        for (int j = 0; j < i - 1; j++) {
            if (isIntersection(vertices[j], vertices[j + 1], vertices[i - 1], vertices[i])) {
                std::cout << "BLAD\n";
                return 0;
            }
        }

        if (i > 0) {
            area += vertices[i-1].x * vertices[i].y - vertices[i-1].y * vertices[i].x;
        }
    }
    if (isIntersection(vertices[1], vertices[0], vertices[0], vertices[n-1])) {
        std::cout << "BLAD\n";
        return 0;
    }
    for (int i = 1; i < n - 1; i++) {
        if (isIntersection(vertices[i], vertices[i + 1], vertices[n - 1], vertices[0])) {
            std::cout << "BLAD\n";
            return 0;
        }
    }
    area += vertices[n-1].x * vertices[0].y - vertices[n-1].y * vertices[0].x;
    
    float finalArea = abs(area) / 2.0f;
    std::cout << finalArea << "\n";
    return 0;
}

int orientation(Point a, Point b, Point c) {
    int prod = (b.x - c.x)*(a.y - c.y) - (a.x - c.x)*(b.y - c.y);
    if (prod == 0) {
        return 0;
    }
    if (prod < 0) {
        return -1;
    }
    return 1;
}

int max(int a, int b) {
    return a > b ? a : b;
}

int min(int a, int b) {
    return a < b ? a : b;
}

bool isIntersection(Point a, Point b, Point c, Point d) {
    int orA = orientation(c, d, a);
    int orB = orientation(c, d, b);
    int orC = orientation(a, b, c);
    int orD = orientation(a, b, d);

    if (orA * orB == 1 || orC * orD == 1) {
        return false;
    }

    if (orA == 0 && orB ==0 && orC == 0 && orD == 0) {
        if (c.x <= max(a.x, b.x) && c.x >= min(a.x, b.x) && c.y <= max(a.y, b.y) && c.y >= min(a.y, b.y)) {
            if (b.x != c.x || b.y != c.y) {
                return true;
            }
        }
        if (d.x <= max(a.x, b.x) && d.x >= min(a.x, b.x) && d.y <= max(a.y, b.y) && d.y >= min(a.y, b.y)) {
            return true;
        }
        return false;
    }

    if (orB == 0 && orC == 0) {
        return false;
    }
    
    return true;
}