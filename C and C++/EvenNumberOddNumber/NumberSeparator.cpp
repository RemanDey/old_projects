#include <iostream>
#include <fstream>
#include <windows.h>
using namespace std;
class num
{
    private: 
        int number;

    public:
        void set(int n)
        {
            number=n;
        }
            
        void check()
        {
            if(number%2==0)
            {
                ofstream evenfile;
                evenfile.open("EvenNumbers.txt",ios::out|ios::app);
                evenfile<<number;evenfile<<",";
                evenfile.close();


            }
            else
            {
                ofstream oddfile;
                oddfile.open("OddNumbers.txt",ios::out|ios::app);
                oddfile<<number;oddfile<<",";
                oddfile.close();
            }


        }

};

int main()
{
    int input=1;
    num number;
    ofstream even,odd;
    even.open("EvenNumbers.txt");even<<":::This file contains the Even Number(s):::\n---------------------------------------------------\n";even.close();
    odd.open("OddNumbers.txt");odd<<":::This file contains the Odd Number(s):::\n---------------------------------------------------\n";odd.close();

    SetConsoleTitle("Number Separator");
    cout<<"\n:::NUMBER SEPARATOR:::";
    cout<<"\nThis Program takes numbers and splits them into two different files namely EvenNumbers.txt and Oddnumbers.txt. As the name implies ""EvenNumbers"" file contains all the even numbers inputted and ""OddNumbers"" files contain all the odd numbers inputted.";
    cout<<"\n:::ENTER 0 to terminate:::";
    cout<<"\n---------------------------------------------\n";
    while(input!=0)
    { 
        cin>>input;
        if(input!=0)
        {number.set(input);
        number.check();}
        else
            cout<<"\nTerminating the program...";

    }
    

}