#include <iostream>
#include <string>
using namespace std;
class atom
    {


        public:
       
             string element_name;
                int atomic_no;
                float atomic_mass;
                float density;


            void set_elementdata(string element_namei, int atomic_noi, float atomic_massi, float densityi)
            {
                element_name=element_namei;
                atomic_no=atomic_noi;
                atomic_mass=atomic_massi;
                density=densityi;
            }

            void display(atom atom)
            {
                cout<<"\nElement Name:\t";cin>>atom.element_name;
                cout<<"\nAtomic No.:\t";cin>>atom.atomic_no;
                cout<<"\nAtomic Mass:\t";cin>>atom.atomic_mass;
                cout<<"\nDensity:\t";cin>> atom.density;

            }    

    };

int main()
{   
    int decision=0;
    atom atom[120];
    string element_name;
    int atomic_no;
    float atomic_mass;
    float density;
    cout<<"\n[0]->Enter NEW Element.\n[1]->Display Element.";
    for(int i=0;i<120;i++){
                cout<<"\nEnter your choice:";
                cin>>decision;
                if(decision==0)
                {
                    cout<<"\nEnter Element name:\t";cin>>element_name;
                    cout<<"\n\tAtomic No.:\t";cin>>atomic_no;
                    cout<<"\n\tAtomic Mass:\t";cin>>atomic_mass;
                    cout<<"\n\tDensity:\t";cin>>density;

                    atom[i].set_elementdata(element_name,atomic_no,atomic_mass,density);
                }
                else if(decision=1)
                {   cout<<"\nEnter Element Name:\t";cin>>element_name;
                    atom[0].display(atom[0]);
                    for(int j=0;j<120;j++)
                    {
                        if(atom[j].element_name==element_name)
                        {atom[j].display(atom[j]); break;}
                    }
                }
            }
}