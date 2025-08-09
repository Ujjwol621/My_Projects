#include<iostream>
#include<conio.h>
#include<fstream>
#include<string.h>
#include<stdlib.h>
#include<sstream>
#include<graphics.h>
#include<windows.h>
#include "basicfunction.h"
using namespace std;
int backgroundColor=RGB(255, 255, 255);
int main();
void login();
void homepage();
class car_rent
{
    int count=0;
    string userid,password;
    string brand,model,color;
    string id, pass,carnum;
    int mileage,cost;


public:
    void ulogin();
    void registration();
    void adminlogin();
    void invoice(string,string,string,int,int);
    void rent();
    void updatecar(string, string, int);

};
void car_rent::adminlogin()
{
    char a,ch;
    string username,pass;
    clearbody();
    cleartitle();
    clearfooter();
    clearheader();
    settextstyle(9, 0, 4);
    outtextxy(0,145,"---------------------------------ADMIN LOGIN----------------------------------");
    settextstyle(9,0,2);
    outtextxy(100,300, "Enter Username : ");
    username=input(320,300);
    outtextxy(100,332, "Enter Password : ");
    pass= inputpass(325, 332);
    if(username=="admin" && pass=="100")
    {
        clearbody();
        settextjustify(1, CENTER_TEXT);
        setcolor(GREEN);
        outtextxy(getmaxwidth()/2,getmaxheight()/2,"Validating..... ");
        delay(2000);
        clearbody();
        outtextxy( getmaxwidth()/2, getmaxheight()/2, "Login successfull! Now you can have access to following function ");
        setcolor(BLACK);
        delay(2000);
    }
    else
    {
        clearbody();
        settextjustify(1, CENTER_TEXT);
        setcolor(GREEN);
        outtextxy(getmaxwidth()/2,getmaxheight()/2,"Validating..... ");
        delay(2000);
        clearbody();
        setcolor(RED);
        outtextxy( getmaxwidth()/2, getmaxheight()/2,"Login Failed !! Try again");
        setcolor(BLACK);
        delay(2000);
        login();
    }
}
void car_rent :: ulogin()                                //defining login() function
{
    cleartitle();
    clearbody();
    clearfooter();
    clearheader();
    settextstyle(9, 0, 4);
    outtextxy(0,145,"---------------------------------USER LOGIN----------------------------------");
    settextstyle(9, 0, 2);
    outtextxy(100,300, "Enter Username : ");
    id = input(320,300);
    outtextxy(100,332, "Enter Password : ");
    pass = inputpass(325, 332);



    ifstream inp("userpass.txt");
    while(inp>>userid>>password)
    {
        if(id==userid  && pass==password )
        {
            count=1;
            clearbody();
        }
    }
    inp.close();
    if(count==1)
    {
        clearbody();
        setcolor(GREEN);
        settextjustify(1, CENTER_TEXT);
        outtextxy(getmaxwidth()/2,getmaxheight()/2,"Validating..... ");
        delay(2000);
        clearbody();
        outtextxy(getmaxwidth()/2,getmaxheight()/2,"WELCOME ");
        outtextxy(getmaxwidth()/2,getmaxheight()/2+32,const_cast<char*>(id.c_str()));
        outtextxy(getmaxwidth()/2,getmaxheight()/2+64,"You are logged in successfully. Now you can have following functions ");
        setcolor(BLACK);
        delay(1000);
    }
    else
    {
        clearbody();
        settextjustify(1, CENTER_TEXT);
        setcolor(GREEN);
        outtextxy(getmaxwidth()/2,getmaxheight()/2,"Validating..... ");
        delay(2000);
        clearbody();
        setcolor(RED);
        outtextxy(getmaxwidth()/2,getmaxheight()/2,"logged in failed,try again");
        setcolor(BLACK);
        getch();
        login();
    }
}
void car_rent :: registration()
{
    string firstname,lastname,dob;
    char a;
    clearbody();
    clearheader();
    settextstyle(9,0,2);
    outtextxy(100,300,"Enter your first name : ");
    firstname=input(380,300);
    if(firstname=="1")
    {
        homepage();
    }
    outtextxy(100,332,"Enter your last name : ");
    lastname=input(380,332);
    outtextxy(100,364,"Enter your date of birth : ");
    dob=input(410,364);
    outtextxy(100,396,"Enter your username : ");
    userid=input(380,396);
    outtextxy(100, 428,"Enter your password : ");
    password=inputpass(380, 428);


    ofstream f1("userpass.txt", ios::app);
    f1<<userid<<' '<<password<<endl;
    f1.close();
    ofstream f2("userinfo.txt", ios::app);
    f2<<firstname<<' '<<lastname<<' '<<dob<<endl;
    f2.close();
    clearbody();
    settextjustify(1,2);
    setcolor(GREEN);
    outtextxy(getmaxwidth()/2, getmaxheight()/2, "Registration is successful!!!  \n");
    settextjustify(0,2);
    setcolor(BLACK);
    delay(1000);
    clearbody();
    homepage();

}
void car_rent :: rent()
{
    char ch;
    int is_update=0;
    string inputbrand, carmodel;
    clearbody();
    cleartitle();
    settextstyle(9, 0, 4);
    outtextxy(0,145,"---------------------------------RENTING PROCESS----------------------------------");
    settextstyle(9, 0, 2);
    outtextxy(100,300,"Enter the brand of car you want to rent in : ");
    inputbrand = input(640,300);
    outtextxy(100,332,"Enter the model of car you want to rent in : ");
    carmodel = input(640, 332);
    ifstream fi("car_details.txt");

    while(fi>>brand>>model>>color>>mileage>>cost>>carnum)
    {
        if(inputbrand == brand && carmodel == model)
        {
            clearbody();
            outtextxy(100,300,"Brand chosen  : ");
            outtextxy(300,300,const_cast<char*>(brand.c_str()));
            outtextxy(100,332,"Model chosen  : ");
            outtextxy(300,332,const_cast<char*>(model.c_str()));
            invoice(brand,model,color,mileage,cost);
            is_update=1;
        }

    }
    fi.close();
    if(is_update)
    {updatecar(inputbrand,carmodel,is_update);}
}
void car_rent :: invoice(string brand, string model, string color, int mileage, int cost)
{
    int days, ad;
    settextstyle(9, 0, 2);
    setcolor(BLACK);
    outtextxy(100,364, "Enter the no of days of renting : ");
    days=stoi(input(550,364));
    outtextxy(100,396, "Enter the advance amount if given : ");
    ad=stoi(input(550,396));
    clearbody();
    cleartitle();
    settextstyle(9,0,2);
    settextjustify(1,2);
    outtextxy(getmaxwidth()/2,getmaxheight()/2," Generating Invoice......");
    settextjustify(0,2);
    delay(1000);
    clearbody();
    cleartitle();
    setcolor(BLACK);
    settextstyle(9,0,2);
    outtextxy(1098,50,"9.HomePage");
    settextstyle(9, 0, 4);
    settextjustify(0,2);
    outtextxy(0,145,"---------------------------------CUSTOMER INVOICE----------------------------------");
    settextstyle(9, 0, 2);
    settextjustify(1,2);
    line(250,220,1100,220);
    outtextxy(637,250,"                 QUICK CAR RENTAL SUPPLIERS PVT LTD           ");
    outtextxy(637,270,"                     Changunarayan-4, Bhaktapur                   ");
    outtextxy(637,290,"                                                                ");
    settextjustify(0,2);
    outtextxy(280,300,"Customer Name : ");
    outtextxy(540,300, const_cast<char *>(id.c_str()));
    outtextxy(300,350,"  Car Details                  Rented days                  Total Cost");
    outtextxy(280,395,"Brand");
    outtextxy(450,395,const_cast<char*>(brand.c_str()));
    outtextxy(280,415,"Mileage");
    outtextxy(450,415,const_cast<char*>(to_string(mileage).c_str()));
    outtextxy(280,435,"Cost/day");
    outtextxy(450,435,const_cast<char*>(to_string(cost).c_str()));
    outtextxy(640,435,const_cast<char*>(to_string(days).c_str()));
    outtextxy(920,435,const_cast<char*>(to_string(days*cost).c_str()));
    outtextxy(280,455,"Model");
    outtextxy(450,455,const_cast<char*>((model).c_str()));
    outtextxy(280,475,"Colour");
    outtextxy(450,475,const_cast<char*>(color.c_str()));
    outtextxy(280,500,"Advance Amount  ");
    outtextxy(920,500,const_cast<char*>(to_string(ad).c_str()));
    outtextxy(280,525,"Total Amount to be paid");
    outtextxy(920,525,const_cast<char*>(to_string(days*cost-ad).c_str()));
    setcolor(GREEN);
    settextstyle(9,0,3);
    outtextxy(637,630,"CAR RENTED SUCCESSFULLY");
    setcolor(BLACK);
    settextstyle(9,0,2);
    line(250,330,1100,330);
    line(250,220,250,560);
    line(1100,220,1100,560);
    line(250,390,1100,390);
    line(250,560,1100,560);
    line(250,330,1100,330);
    line(250,498,1100,498);
    line(250,522,1100,522);
    line(535,330,535,498);
    line(790,330,790,560);
    line(400,390,400,498);
    char ch=getch();
    if(ch='9')
    {
        clearheader();
        homepage();
    }
    ofstream ssave;
    ssave.open("rent_record.txt",ios::app);
    ssave<<userid<<endl<<brand<<"\t\t"<<model<<"\t\t"<<color<<"\t\t"<<mileage<<"\t\t"<<days<<"\t\t"<<cost<<"\t\t"<<(days*cost)<<"\t\t"<<ad<<"\t\t"<<(days*cost-ad)<<endl;
    ssave.close();
    getch();
}

// Defining class car for car operations ( add, delete, view)
class Car
{
    string location,brand,color,model;
    int mileage,cost,carnum;
public:
    void addCarRecord(const Car&);
    void deleteCarRecord(const string&, const string&);
    void viewCarRecords();

    string getmodel()
    {
        return(model);
    }

    void enter()
    {
        cleartitle();
        clearbody();
        clearheader();
        clearfooter();
        settextstyle(9, 0, 4);
        outtextxy(0,145,"---------------------------------ADD CAR DETAILS----------------------------------");
        settextstyle(9, 0, 2);
        outtextxy(100,300,"Enter Car Brand: ");
        brand = input(330,300);
        outtextxy(100,332,"Enter car model : ");
        model = input(330,332);
        outtextxy(100,364,"Enter car color: ");
        color = input(330,364);
        outtextxy(100,396,"Enter mileage : ");
        mileage = stoi(input(330,396));
        outtextxy(100,428,"Enter the cost per day : ");
        cost = stoi(input(500,428));
        outtextxy(100,450,"Enter no of this model available : ");
        carnum=stoi(input(500,450));
    }

};
void car_rent :: updatecar(string brd, string mdl, int trans)
{
    ifstream inputFile("car_details.txt");
    ofstream tempFile("temp.txt");


    while (!inputFile.eof())
    {
        string brand, model,color;
        int mileage,cost,carnum;
        inputFile >> brand >> model >> color >> mileage >> cost >>carnum;
        if (!inputFile.eof())
        {
            if ((brand == brd) && (model == mdl))
            {
               if(trans==1)
                {
                    carnum--;
                    tempFile<<brand<<" " <<model<<" "<<color<<" "<<mileage<<" "<<cost<<" "<<carnum<<" "<<endl;
                }
                else if(trans==2)
                {
                    carnum++;
                    tempFile<<brand<<" " <<model<<" "<<color<<" "<<mileage<<" "<<cost<<" "<<carnum<<" "<<endl;
                }
                else
                {
                    tempFile<<brand<<" " <<model<<" "<<color<<" "<<mileage<<" "<<cost<<" "<<carnum<<" "<<endl;
                }
            }
            else
            {

                 tempFile<<brand<<" " <<model<<" "<<color<<" "<<mileage<<" "<<cost<<" "<<carnum<<" "<<endl;
            }
        }
    }

    inputFile.close();
    tempFile.close();

    remove("car_details.txt");
    rename("temp.txt", "car_details.txt");
}

// Function to add a new car record to the file
void Car :: addCarRecord(const Car& car)
{
    ofstream file("car_details.txt", ios::app);
    if (file.is_open())
    {
        file << car.brand <<" "<< car.model <<" "<< car.color <<" "<< car.mileage <<" "<< car.cost<<" "<<car.carnum<<" "<<endl;//car.location<<endl;
        file.close();
        clearbody();
        settextjustify(1,2);
        settextstyle(9,0,2);
        setcolor(GREEN);
        outtextxy(637,345,"Adding......");
        delay(2000);
        outtextxy(637,380,"Car details added successfully.");
        settextjustify(0,2);
        setcolor(BLACK);
        getch();

    }
    else
    {
        settextstyle(9,0,2);
        outtextxy(getmaxwidth()/2, getmaxheight()/2,"Unable to open the file.");
    }
}

// Function to delete a car record from the file
void Car :: deleteCarRecord(const string& brandToDelete, const string& modeltodelete)
{
    ifstream inputFile("car_details.txt");
    ofstream tempFile("temp.txt");

    if (!inputFile.is_open() || !tempFile.is_open())
    {
        cout << "Unable to open the file(s)." << endl;
        return;
    }

    string line;
    bool found = false;

    while (getline(inputFile, line))
    {
        istringstream iss(line);
        string brand, model,color;
        int mileage,cost;

        if (iss >> brand >> model >> color >> mileage >> cost >>carnum)
        {
            if ((brand != brandToDelete) || (model != modeltodelete))
            {
                tempFile << line << endl;
            }
            else
            {
                found = true;
            }
        }
    }

    inputFile.close();
    tempFile.close();

    if (found)
    {
        remove("car_details.txt");
        rename("temp.txt", "car_details.txt");
        clearbody();
        settextjustify(1,2);
        settextstyle(9,0,2);
        setcolor(GREEN);
        outtextxy(637,345,"Deleting......");
        delay(2000);
        outtextxy(637,380,"Car details deleted successfully.");
        settextjustify(0,2);
        setcolor(BLACK);
        getch();
    }
    else
    {
        remove("temp.txt");
        outtextxy(637,345,"Car not found.");
    }
}

// Function to \ all car records in the file
void Car :: viewCarRecords()
{

    cleartitle();
    clearbody();
    clearheader();
    settextstyle(9, 0, 4);
    outtextxy(0,145,"---------------------------------CAR DETAILS----------------------------------");
    settextstyle(9,0,2);
    int u=0;
    string line1;
    outtextxy(100,220,"Brand");
    outtextxy(300,220,"Model");
    outtextxy(500,220,"Color");
    outtextxy(700,220,"Mileage");
    outtextxy(900,220,"Cost/Day");
    outtextxy(1100,220,"Number");
    line(50,240,1250,240);
    settextstyle(9,0,2);
    outtextxy(1140, 630,"9.Back");

    ifstream fl("car_details.txt");
    while (getline(fl, line1))
    {
        istringstream iss(line1);
        string brand, model,color;
        int mileage,cost;

        if( fl.eof())
        {
            break;
        }
        iss >> brand >> model >> color >> mileage >> cost >>carnum;
        settextstyle(9,0,2);
        outtextxy(100,250+u*30,const_cast<char*>(brand.c_str()));
        outtextxy(300,250+u*30,const_cast<char*>(model.c_str()));
        outtextxy(500,250+u*30,const_cast<char*>(color.c_str()));
        outtextxy(700,250+u*30,const_cast<char*>((to_string(mileage)).c_str()));
        outtextxy(900,250+u*30,const_cast<char*>((to_string(cost)).c_str()));
        outtextxy(1100,250+u*30,const_cast<char*>((to_string(carnum)).c_str()));
        delay(1000);
        u++;

    }
    fl.close();
}

void login()
{
    char ch;
    string brandToDelete,modeltodelete;
    car_rent c1;
    Car car;
    cleartitle();
    clearbody();
    setcolor(BLACK);
    settextstyle(9, 0, 4);
    settextjustify(0,2);
    outtextxy(0,145,"---------------------------------LOGIN PAGE----------------------------------");
    settextstyle(9, 0, 2);
    outtextxy(250, 450, "1.User");
    outtextxy(950, 450, "2.Admin");
    readimagefile("C:/Desktop/finaldefense/photos/user.jpg",190,230, 390,60 );
    readimagefile("C:/Desktop/finaldefense/photos/admin.jpeg",900,230, 1100,60 );
    settextstyle(9,0,2);
    outtextxy(1140, 630,"9.Back");
    ch=getch();
    if(ch=='9')
    {
        homepage();
    }
    else
    {
        switch(ch)
        {
        case '0':
            {
                exit(0);
            }
        case '1':
        {
            c1.ulogin();
uloginlabel:
            clearbody();
            cleartitle();
            settextstyle(9,0,4);
            settextjustify(0,2);
            outtextxy(0,145,"-------------------------------USER FUNCTIONS---------------------------------");
            settextstyle(9,0,2);
            outtextxy(230, 450, "1.View Car");
            outtextxy(930, 450, "2.Rent Car");
            readimagefile("C:/Desktop/finaldefense/photos/carsearch.jpeg",190,230, 390,60 );
            readimagefile("C:/Desktop/finaldefense/photos/rentcar.jpg",850,230, 1140,60 );
            readimagefile("C:/Desktop/finaldefense/photos/exit2.jpg",1110,15, 1250,110 );
            setcolor(BLACK);
            settextstyle(9,0,4);
            outtextxy(1098,50,"0.");
            settextstyle(9,0,2);
            outtextxy(1140, 630,"9.Logout");
            ch=getch();
            if(ch=='9')
            {
                settextstyle(9,0,2);
                settextjustify(1,2);
                clearbody();
                outtextxy(getmaxwidth()/2,getmaxheight()/2, "Logging out........");
                settextjustify(0,2);
                delay(2000);
                clearbody();
                clearfooter();
                login();
            }
            else
            {
                switch(ch)
                {
                case '0':
                    {
                        exit(0);
                    }
                case '1':
                {
                    clearfooter();
                    car.viewCarRecords();
                    getch();
                }
                break;

                case '2':
                {
                    clearheader();
                    clearfooter();
                    c1.rent();
                }
                }
            }
            goto uloginlabel;
        }
        break;
        case '2':
        {
            c1.adminlogin();
label:
            clearbody();
            cleartitle();
            settextstyle(9,0,4);
            settextjustify(0,2);
            outtextxy(0,145,"-------------------------------ADMIN FUNCTIONS----------------------------------");
            readimagefile("C:/Desktop/finaldefense/photos/carsearch.jpeg",140,270, 300,130 );
            readimagefile("C:/Desktop/finaldefense/photos/addcar.jpg",570,250, 770,80  );
            readimagefile("C:/Desktop/finaldefense/photos/deletecar.jpg",970,260, 1150, 430 );
            readimagefile("C:/Desktop/finaldefense/photos/exit2.jpg",1110,15, 1250,110 );
            setcolor(BLACK);
            settextstyle(9,0,4);
            outtextxy(1098,50,"0.");
            setcolor(BLACK);
            outtextxy(110,460,"1.View Cars");
            outtextxy(560,460,"2.Add Cars");
            outtextxy(950,460,"3.Delete Cars");
            settextstyle(9,0,2);
            outtextxy(1140, 630,"9.Logout");
            ch=getch();
            if(ch=='9')
            {
                settextstyle(9,0,2);
                settextjustify(1,2);
                clearbody();
                outtextxy(getmaxwidth()/2,getmaxheight()/2, "Logging out........");
                settextjustify(0,2);
                delay(1000);
                clearfooter();
                clearbody();
                login();
            }
            else
            {

                switch(ch)
                {
                case '0':
                    {
                        exit(0);
                    }
                case '1':
                {
                    clearfooter();
                    car.viewCarRecords();
                    getch();
                    clearbody();
                    goto label;

                }
                case '2':
                {
                    car.enter();
                    clearbody();
                    car.addCarRecord(car);
                    goto label;
                }
                case '3':
                {
                    cleartitle();
                    clearbody();
                    clearheader();
                    clearfooter();
                    setcolor(BLACK);
                    settextstyle(9, 0, 4);
                    settextjustify(0,2);
                    outtextxy(0,145,"---------------------------------DELETION----------------------------------");
                    settextstyle(9, 0, 2);
                    outtextxy(100,300,"Enter brand of the car to delete : ");
                    brandToDelete=input(490,300);
                    outtextxy(100,332,"Enter model of the car to delete : ");
                    modeltodelete = input(490,332);
                    //outtextxy(280,300,const_cast<char*>(brandToDelete.c_str()));
                    car.deleteCarRecord(brandToDelete,modeltodelete);
                    goto label;
                }
                }
                goto label;
            }
        }
        default :
            break;

        }
    }
}



void homepage()
{
    int a;
    car_rent c1;
    Car car;
    char choice;
homelabel:
    string brandToDelete;
    clearbody();
    cleartitle();
    clearfooter();
    clearsuccess();
    setcolor(BLACK);
    settextstyle(9,0,2);
    outtextxy(550,10,"QUICK");
    setcolor(BLACK);
    rectangle(0,121,1500,123);
    settextstyle(9,0,4);
    settextjustify(0,2);
    outtextxy(0,145,"----------------------------------HOME PAGE----------------------------------");
    rectangle(0,200,1500,202);
    readimagefile("C:/Desktop/finaldefense/photos/carrental.jpeg",400,40, 800,120 );
    readimagefile("C:/Desktop/finaldefense/photos/carsearch.jpeg",140,260, 290,120 );
    readimagefile("C:/Desktop/finaldefense/photos/user.jpg",550,230, 750,60 );
    //readimagefile("D:/Pictures/Screenshots/admin.jpeg",680,230, 900 ,80 );
    readimagefile("C:/Desktop/finaldefense/photos/exit2.jpg",1110,15, 1250,110 );
    readimagefile("C:/Desktop/finaldefense/photos/register.jpg",925,210, 1140, 420 );
    setcolor(BLACK);
    outtextxy(110,420,"1.View Cars");
    outtextxy(580,420,"2.Login");
    outtextxy(920,420,"3.Register");
    setcolor(BLACK);
    outtextxy(1098,50,"0.");
    setcolor(BLACK);
    rectangle(0,600,1500,602);
    choice=getch();

    switch(choice)                      // using switch statement for choosing choices
    {
    case '1':
    {

        car.viewCarRecords();
        char ch=getch();
        clearfooter();
    }
    break;
    case '2':
    {
        login();// if success then only goes to next line .
        break;

    }
    case '3':
    {
        clearbody();
        cleartitle();
        settextstyle(9,0,4);
        settextjustify(0,2);
        outtextxy(0,145,"----------------------------------Registration----------------------------------");
        c1.registration();

    }
    break;
    case '0':
    {
        cout<<"Thank you !!";
        exit(0);
    }
    default:
    {

    }

    }
    goto homelabel;
}
int main()
{


    initwindow(getmaxwidth(),getmaxheight(),"HOME");
    setbkcolor(backgroundColor);
    setfillstyle(SOLID_FILL,backgroundColor);
    floodfill(0,0,backgroundColor);
    homepage();

    getch();
    // closegraph();


}
