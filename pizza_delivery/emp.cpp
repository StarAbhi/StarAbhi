#include <iostream>
#include <algorithm>
using namespace std;

struct Employee {
    char name[50];
    int salary;
    int employeeID;
    char dept[5];
    double yearlySalary;
};

bool compare( Employee a, Employee b){
    if(a.name < b.name)
        return 1;
    else 
        return 0;
} 
int main() {
    //define array of Employee struct of size 10
    Employee e[10];
    char search[50];
    for(int i=0;i<3;i++)
    {
    cout << "Enter name of employee : ";
    cin.getline(e[i].name, 50);
    cout << "Enter department : ";
    cin.getline(e[i].dept, 5);
    cout << "Enter salary of employee : ";
    cin >> e[i].salary;
    e[i].yearlySalary=e[i].salary*12;
    cout << "Enter employee code : ";
    cin >> e[i].employeeID;
    }
    // Printing employee details 
    cout << "\n*** Employee Details ***" << endl;
    for(int i=0;i<3;i++)
    {
    cout << "Name : " << e[i].name << endl << "Salary : " << e[i].salary << endl<< "Yearly Salary : " << e[i].yearlySalary << endl;
    cout << "Employee Code : " << e[i].employeeID << endl << "Department : " << e[i].dept<<endl;
    }
    sort(e, e+10, compare);
     // After sorting Printing employee details 
     for(int i=0;i<3;i++)
    {
    cout << "Name : " << e[i].name << endl << "Salary : " << e[i].salary << endl<< "Yearly Salary : " << e[i].yearlySalary << endl;
    cout << "Employee Code : " << e[i].employeeID << endl << "Department : " << e[i].dept<<endl;
    }
    
    cout<<"Enter the name you want to search : ";
    cin.getline(search,50);
      for(int i=0;i<3;i++)
    {
        if( e[i].name==search)
        {
            cout << "Name : " << e[i].name << endl << "Salary : " << e[i].salary << endl<< "Yearly Salary : " << e[i].yearlySalary << endl;
            cout << "Employee Code : " << e[i].employeeID << endl << "Department : " << e[i].dept<<endl;
            
        }
        else
        {
            cout <<"Employee not found ";
        }
    }
    
    return 0;
}