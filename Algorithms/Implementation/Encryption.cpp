#include <bits/stdc++.h>

using namespace std;

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string s;
    getline(cin, s);

    int length = s.length();
    int columns = ceil(sqrt(length));
    int rows = floor(sqrt(length));
    
    if(rows * columns < length){
        rows++;
    }

    for(int i = 0; i < columns; i++) {
        for(int j = i; j < length; j += columns) {
            fout << s[j];
        }
        fout << ' ';
    }

    fout.close();

    return 0;
}
