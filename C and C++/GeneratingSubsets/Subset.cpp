   
#include <bits/stdc++.h>

using namespace std;
ofstream subsets;
string filename;

class subset
{   

    private:
        int upper_limit;
    public:
        vector <int> s;


        void set(int n)
        {
            upper_limit=n;
            filename="Subsets["+to_string(upper_limit)+"].txt";
            subsets.open(filename);
            subsets<<"Printing the ";subsets<<to_string((int)pow(2.00,upper_limit));subsets<<" subsets of {";
            for(int i=1;i<upper_limit+1;i++)
            {
                if(i==upper_limit)
                    {subsets<<i;subsets<<"} :\n";}
                else
                    {subsets<<i;subsets<<",";}
            }
        }

        void run(int k)
        {
            if(k==upper_limit+1)
            {   
                cout<<"\n{";subsets<<"\n{";
                for(int i=0;i<s.size();i++)
                {   
                    if(i==s.size()-1)
                    {
                        cout<<s[i];subsets<<s[i];
                    }
                    else 
                    {cout<<s[i];cout<<",";subsets<<s[i];subsets<<",";}
                    
                }
                cout<<"}\n";subsets<<"}\n";
            }
            else
            {
                s.push_back(k);
                run(k+1);
                s.pop_back();
                run(k+1);

            }
    
        }

};

int main()
{   
    
    int input;
    subset generating_subsets;
    cout<<":::PROGRAM TO PRINT ALL THE SUBSETS:::\nENTER the value of n:";cin>>input;
    cout<<"\nPRINTING the ";cout<<pow(2.00,input);cout<<" subsets:\n";
    auto start = std::chrono::high_resolution_clock::now();
    generating_subsets.set(input);
    generating_subsets.run(1);
    auto end = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double, std::micro> duration = end - start;
    
    std::cout << "Time taken: " << duration.count() << " microseconds" << std::endl;
    
    return 0;

    
}