#include <iostream>
#include<fstream>
#include <string>
using namespace std;

class collatz
{
    private:
        int startingpoint;
    public:
        void set(int n)
        {
            startingpoint=n;

        }

        int run()
        {
            int present;
            string filename;
            ofstream CollatzSeries;
            filename="CollatzSeries_"+to_string(startingpoint)+".txt";
            CollatzSeries.open(filename);
            present=startingpoint;
            cout<<startingpoint;
            CollatzSeries<<startingpoint;
            while(present!=1)
            {
                if(present%2==0)
                {   
                    present=present/2;
                    cout<<"->";cout<<present;
                    CollatzSeries<<"->";CollatzSeries<<present;
                }
                else
                {
                    present=3*present+1;
                    cout<<"->";cout<<present;
                    CollatzSeries<<"->";CollatzSeries<<present;
                }
            }
            CollatzSeries.close();
        }
};

int main()
{
    int user_input;
    collatz collatzseries;
    cout<<":::PROGRAM TO IMPLEMENT COLLATZ CONJECTURE:::";
    cout<<"\nEnter the collatz input:";cin>>user_input;
    collatzseries.set(user_input);
    collatzseries.run();

}
