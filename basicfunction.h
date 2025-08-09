#include<iostream>
#include<windows.h>
#include<string>
using namespace std;

string input(int x, int y)
{
    char a;
    string txt= "";
    while(true)
    {
        if(GetAsyncKeyState(VK_F1))
        {
            return("1");
        }
        a=getch();

        if(a == 13)

            break;
        else if(a== 8)
        {
            if(txt.length()>0)
            {
                txt.pop_back();
                outtextxy(x,y,"                                                                                   ");

                outtextxy(x,y, const_cast<char*>(txt.c_str()));
            }
        }
        else
        {
            txt +=a;
            outtextxy(x, y, const_cast<char*>(txt.c_str()));
        }
    }
    return txt;
}
string inputpass(int x, int y)
{
    char a;
    string txt= "";
    while(true)
    {
         if(GetAsyncKeyState(VK_F1))
        {
            return("1");
        }
        a=getch();

        if(a ==13)

            break;
        else if(a==8)
        {
            if(txt.length()>0)
            {
                char arr[20]="\0";
                arr[txt.length()]='\0';
                txt.pop_back();
                outtextxy(x,y,"                                                                                   ");
                for(int i=0; i<txt.length(); i++)
                {
                    arr[i]='*';

                }
                outtextxy(x,y, arr);

            }
        }
        else
        {
            if(txt.length()<=10)
            {


            char arrr[20]="\0";
            txt +=a;
            outtextxy(x,y,"                                                                                   ");
                for(int i=0; i<txt.length(); i++)
                {
                    arrr[i]='*';

                }
                outtextxy(x,y, arrr);
            }
        }
    }
    return txt;
}
void cleartitle()
{
    bar(0,124,1500,200);

}
void clearbody()
{
    bar(0,203,1500, 599 );
}
clearheader()
{
    bar(1000,0,1500,120);
}
clearfooter()
{
    bar(1120,610, 1250, 650 );
}
clearsuccess()
{
    bar(630,610,1250,660);
}

void copyimage(const std::string& inputPath, const std::string& finalPath)
{
    std::ifstream inputFile(inputPath, std::ios::binary);
    std::ofstream finalFile(finalPath, std::ios::binary);
    // Read and write the file content
    finalFile << inputFile.rdbuf();

    // Close the files
    inputFile.close();
    finalFile.close();
}

std::string photo()
{
    OPENFILENAME ofn;
    char profileLoc[MAX_PATH] = "";

    ZeroMemory(&ofn, sizeof(OPENFILENAME));
    ofn.lStructSize = sizeof(OPENFILENAME);
    ofn.lpstrFile = profileLoc;
    ofn.lpstrFile[0] = '\0';
    ofn.nMaxFile = sizeof(profileLoc);
    ofn.lpstrFilter = "Image Files\0.jpeg\0.jpg\0All Files\0.*\0";
    ofn.nFilterIndex = 1;

    if (GetOpenFileName(&ofn))
    {
        return profileLoc;
    }
    // If no file was selected, return an empty string
    return "";
}
