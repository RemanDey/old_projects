#include <iostream>
#include <map>
#include <fstream>
using namespace std;
map <char,char> scroll=
{
{' ','z'},
{'.','9'},
{',','5'},
{'a','#'},
{'b','$'},
{'c','!'},
{'d','@'},
{'e','%'},
{'f','^'},
{'g','&'},
{'h','*'},
{'i','('},
{'j',')'},
{'k','<'},
{'l','>'},
{'m','/'},
{'n','?'},
{'o','~'},
{'p','`'},
{'q','{'},
{'r','}'},
{'s','['},
{'t',']'},
{'u','a'},
{'v','m'},
{'w','q'},
{'x','f'},
{'y','u'},
{'z','t'}
};
int main(){
    string input;
    string Myfile;
    cout<<"\nEnter the filename where encoded data is to be stored: ";
    getline(cin,Myfile);
    
    ofstream output(Myfile);
    cout<<"\n-<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>-\nMessage Encoder\n-<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>-\nEnter the message:\t";
    getline(cin,input);
    int size=input.size();
    for(int i=0;i<size;i++)
    {output<<scroll[input[i]];
    cout<<scroll[input[i]];}
    output.close();

}

