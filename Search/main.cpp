#include <bits/stdc++.h>
using namespace std;

int buscaBinaria(int buscador, int comp){
    vector<int> bins;
    for(int i = 0; i <= comp; i++){
        bins.push_back(i);
    }
    int start = 0,end = comp, meio = (end-start)/2;
    
    while(1){
        if(end-start <=2){ //if element not found
            return -1;
        }
        if(bins[meio] == buscador){ //if element was found return the index
            return meio;
            break;
        }else if(bins[meio] > buscador){
            end = meio;
            meio = (end-start)/2;
        }else if(bins[meio] < buscador){
            int aux = meio;
            start = meio;
            meio = (end-start)/2 + meio;
        }
    }
}

int main(){
    int B, C;
    cin >> B >> C; // Number to find, //vector length
    int result = buscaBinaria(B, C);
    if(result == -1){
        cout << "Elemento não encontrado" << endl;
    }else{
        cout << "Elemento encontrado no index: " << result << endl;   
    }
}
