#include <iostream>
#include <map>
#include <fstream>
using namespace std;
map<char, char> scroll =
    {
        {'z', ' '},
        {'9', '.'},
        {'5', ','},
        {'#', 'a'},
        {'$', 'b'},
        {'!', 'c'},
        {'@', 'd'},
        {'%', 'e'},
        {'^', 'f'},
        {'&', 'g'},
        {'*', 'h'},
        {'(', 'i'},
        {')', 'j'},
        {'<', 'k'},
        {'>', 'l'},
        {'/', 'm'},
        {'?', 'n'},
        {'~', 'o'},
        {'`', 'p'},
        {'{', 'q'},
        {'}', 'r'},
        {'[', 's'},
        {']', 't'},
        {'a', 'u'},
        {'m', 'v'},
        {'q', 'w'},
        {'f', 'x'},
        {'u', 'y'},
        {'t', 'z'}};
int main()
{
    string encoded_message;
    string filename;
    
    cout<<"Filename:";
    cin>>filename;


    ifstream EncodedFile (filename);
    cout << "\n-<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>-\nMessage Decoder\n-<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>-\n";
    getline(EncodedFile, encoded_message);
    cout << "The Encoded message:\t"+encoded_message+"\n";
    cout<<"\nThe Decoded message:\t";
    int size = encoded_message.size();
    for (int i = 0; i < size; i++)
    {
        cout << scroll[encoded_message[i]];
    }

    EncodedFile.close();
    
}
