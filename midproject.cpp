//    -lbgi -lgdi32 -lcomdlg32 -luuid -loleaut32 -lole32
 // -lwinmm

#include<iostream>
#include<conio.h>
#include<fstream>
#include<string.h>
#include<stdlib.h>
#include<sstream>
using namespace std;
int main();
class car_rent
{
    int count;
    public:
    void login();
    void registration();
    void adminlogin();
    /*void forgot();
    void details();*/
};
void car_rent::adminlogin()
{
    char a;
    string username,pass;
    cout<<"\t\t Enter your username and password : "<<endl;
    cout<<"\t\t USERNAME : ";
    cin>>username;
   cout<<"\t\t PASSWORD : ";
    while(true)
    {
        a=getch();
        if(a =='\r')

            break;
             else if(a=='\b')
            {
                if(pass.length()>0)
                {
                    pass.erase(pass.length()-1,1);
                    cout<<"\b \b";
                }
            }
                else{
                        pass +=a;
                        cout<<"*";
                    }
    }
    if(username=="admin" && pass=="100")
    {
        cout<<"Login successfull!"<<endl;
    }
    else{
        cout<<"Please enter the right username and password!!";

        system("pause");
        system("cls");
        main();
    }


}
void car_rent :: login()                                //defining login() function
{
    string userid,password,id,pass;
    char a;
    system("cls");
    cout<<"\t\t Enter your username and password : "<<endl;
    cout<<"\t\t USERNAME : ";
    cin>>userid;
   cout<<"\t\t PASSWORD : ";
    while(true)
    {
        a=getch();
        if(a =='\r')

            break;
             else if(a=='\b')
            {
if(password.length()>0)
{
    password.erase(password.length()-1,1);
    cout<<"\b \b";
}
            }
            else{
                password +=a;
                cout<<"*";
            }
    }


    ifstream input("record.txt");
    while(input>>id>>pass)
    {
        if(id==userid  && pass==password )
        {
            count=1;
            system("cls");
        }
    }
    input.close();

    if(count==1)
    {
        cout<< userid<<"\n Logged in successfully!! Access Granted \n ";
    }
    else
    {
        cout<<"\t Login Error!! Please enter the correct username and pass ";
        main();
    }
}
void car_rent :: registration()
{
    string userid1,id1,pass1;
    string password1="";
    char a=' ';
    system("cls");
    cout<<"\t\t Enter your username : ";
    cin>>userid1;
    cout<<"\t\t Enter your password : ";

    while(true)
    {
        a=getch();
        if(a =='\r')

            break;
             else if(a=='\b')
            {
if(password1.length()>0)
{
    password1.erase(password1.length()-1,1);
    cout<<"\b \b";
}
            }
            else{
                password1 +=a;
                cout<<"*";
            }
    }
    ofstream f1("record.txt", ios::app);
    f1<<userid1<<' '<<password1<<endl;
    system("cls");
    cout<<"\n\t\t Registration is successful!!!  \n";
}
/*void car_rent :: forgot()
{
    int option;
    system("cls");
    cout<<"\t\t Forgot password ???"<<endl;
    cout<<"\t\t 1.Search id by your username "<<endl;
    cout<<"\t\t 2.Go back to main menu "<<endl;
    cout<<"\n\t\tEnter your choice : ";
    cin>>option;

    switch(option)
    {
        case 1:
            {
                int count=0;
                string userid2,id2,pass2;
                cout<<"\n\t\t Enter the username that you remember : ";
                cin>>userid2;

                ifstream f2("record.txt");
                while(f2>>id2>>pass2)
                {
                    if(id2==userid2)
                    {
                        count=1;
                    }

                }
                f2.close();
                if(count==1)
                {
                    cout<<"\n\n Your account is found! \n";
                    cout<<"Here is your password and username:\n\t"<<pass2<<"\n\t"<<id2;
                    main();
                }
                else
                {
                    cout<<"\n\t Sorry!! Your account is not found! \n";
                    system("cls");
                    main();
                }
                break;
            }
        case 2:
            {
                main();
            }
        default:
        {
            cout<<"\t\t Wrong choice! Please try again "<<endl;
            forgot();
        }


    }

}
void selection(string model,int b,int c,int d,string e,string colour)
{
        int x,ad;
        cout<<endl<<"\tEnter the no of days : ";
        cin>>x;
        cout<<"Enter the advance amount if given : ";
        cin>>ad;
        system("cls");
        cout<<"\n\n\t\t _____________________________________________________"<<endl;
        cout<<"\t\t|             RUTM CAR RENTAL SUPPLIERS PVT LTD           |"<<endl;
        cout<<"\t\t|                Changunarayan-4, Bhaktapur               |"<<endl;
        cout<<"\t\t|                                                         |"<<endl;
        cout<<"\t\t|                  CUSTOMER INVOICE                       | "<<endl;
        cout<<"\t\t|---------------------------------------------------------|"<<endl;
        cout<<"\t\t|       Car Details      |  Rented days  |   Total Cost   |"<<endl;
        cout<<"\t\t|------------------------|---------------|----------------|"<<endl;
        cout<<"\t\t|   Brand   | \t"<<model <<"\t |\t"    <<"\t |\t\t"     <<"  |"<<endl;
        cout<<"\t\t|   Power   | \t"<< b    <<"\t |\t"    <<"\t |\t\t"     <<"  |"<<endl;
        cout<<"\t\t|   Mileage | \t"<< c    <<"\t |\t"    <<"\t |\t\t"     <<"  |"<<endl;
        cout<<"\t\t|  Cost/day | \t" <<d   <<"\t |\t"<<x <<"\t |\t"   <<x*d <<"\t  |"<<endl;
        cout<<"\t\t|   Model   | \t"<< e    <<"\t |\t"    <<"\t |\t\t"      <<"  |"<<endl;
        cout<<"\t\t|   Colour  | \t"<<colour<<"\t |\t"    <<"\t |\t\t"      <<"  |"<<endl;
        cout<<"\t\t|----------------------------------------|----------------|"<<endl;
        cout<<"\t\t| Advance Amount  "<<        "\t  \t"   <<"\t |\t"<<ad <<"\t  |"<<endl;
        cout<<"\t\t|----------------------------------------|----------------|"<<endl;
        cout<<"\t\t| Total Amount to be paid                |\t"<<(x*d-ad)<<"\t  |"<<endl;
        cout<<"\t\t|_________________________________________________________|"<<endl;
}
*/
// Define a structure to represent a car
class Car {
    string make;
    string model;
    int year;
    public:
    void addCarRecord(const Car&);
    void deleteCarRecord(const string&);
    void viewCarRecords();
    void enter()
    {
        cout << "Enter car make: ";
        cin >> make;
        cout << "Enter car model: ";
        cin >> model;
        cout << "Enter car year: ";
        cin >> year;
    }

};
// Function to add a new car record to the file
void Car :: addCarRecord(const Car& car)
{
    ofstream file("car_details.txt", ios::app);
    if (file.is_open()) {
        file << car.make << " " << car.model << " " << car.year << endl;
        file.close();
        cout << "Car details added successfully." << endl;
    } else {
        cout << "Unable to open the file." << endl;
    }
}

// Function to delete a car record from the file
void Car :: deleteCarRecord(const string& makeToDelete) {
    ifstream inputFile("car_details.txt");
    ofstream tempFile("temp.txt");

    if (!inputFile.is_open() || !tempFile.is_open()) {
        cout << "Unable to open the file(s)." << endl;
        return;
    }

    string line;
    bool found = false;

    while (getline(inputFile, line)) {
        istringstream iss(line);
        string make, model;
        int year;

        if (iss >> make >> model >> year) {
            if (make != makeToDelete) {
                tempFile << line << endl;
            } else {
                found = true;
            }
        }
    }

    inputFile.close();
    tempFile.close();

    if (found) {
        remove("car_details.txt");
        rename("temp.txt", "car_details.txt");
        cout << "Car details deleted successfully." << endl;
    } else {
        remove("temp.txt");
        cout << "Car not found." << endl;
    }
}

// Function to view all car records in the file
void Car :: viewCarRecords() {
    ifstream file("car_details.txt");
    if (file.is_open()) {
        string line;
        while (getline(file, line)) {
            cout << line << endl;
        }
        file.close();
    } else {
        cout << "Unable to open the file." << endl;
    }
}




int main()
{
    int a,b;
    car_rent c1;
    Car car;
    cout<<"\n\n\t\t\t----------------------------------------------------------\n\n\n";
    cout<<"\t\t\t-----------RUTM CAR RENTAL SUPPLIERS PVT LTD--------------\n\n";
    cout<<"\t\t\t--------------CAR RENTAL SYSTEM LOGIN PAGE----------------\n\n\n";
    cout<<"\t\t\t|1.ADMIN"<<endl;
    cout<<"\t\t\t|2.USER"<<endl;
    cout<<"\t\t\t|3.EXIT"<<endl;
    cout<<"\n\t\t\t Select the option above : ";
    cin>>a;
    cout<<endl;

    switch(a)                       // using switch statement for choosing choices
    {
        case 1:
        {
            c1.adminlogin();
            label:
            {
            cout<<"1.View Car Details"<<endl;
            cout<<"2.Add Cars"<<endl;
            cout<<"3.Remove Cars"<<endl;
            cout<<"4.Exit"<<endl;
            cout<<"Enter your choice : ";
            cin>>a;
            switch(a)
            {
                case 1:
                {
                    car.viewCarRecords();
                    goto label;
                }
                case 2:
                {
                car.enter();
                car.addCarRecord(car);
                goto label;
                }
                case 3:
                {
                string makeToDelete;
                cout << "Enter make of the car to delete: ";
                cin >> makeToDelete;
                car.deleteCarRecord(makeToDelete);
                goto label;
                }
                case 4:
                {
                    main();
                }
            }
            }
        }
        case 2:
        {
            label2:
            {
            cout<<"1.Register"<<endl;
            cout<<"2.Login"<<endl;
            cout<<"3.Exit"<<endl;
            cout<<"Enter your choice:";
            cin>>a;
            switch(a)
            {
                case 1:
                {
                    c1.registration();
                    goto label2;
                }
                case 2:
                {
                    c1.login();
                    label1:
                    {
                        cout<<"1.View Car Details"<<endl;
                        cout<<"2.Rent Car"<<endl;
                        cout<<"3.Exit"<<endl;
                        cout<<"Enter your choice :";
                        cin>>a;
                        switch(a)
                        {
                            case 1:
                            {
                                car.viewCarRecords();
                                goto label1;
                            }
                            case 2:
                            {

                            }
                            case 3:
                            {
                            main();
                            }
                        }
                    }
                }
                case 3:
                {
                    main();
                }
                default:
                {
                    cout<<"Please enter the correct options!!"<<endl;
                }
            }
        }
    }
}
getch();
}
