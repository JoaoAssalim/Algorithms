#include <bits/stdc++.h>
using namespace std;

int buscaBinaria(int buscador){
    vector<int> bins = {0,1,4,6,7,8,10,12,15,16}; // Digit the list we need search
    int start = 0,end = 11, meio = (end-start)/2;
    
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
    int result = buscaBinaria(10); //Value you wants find
    if(result == -1){
        cout << "Element not found" << endl;
    }else{
        cout << "Element found at index: " << result << endl;   
    }
}
