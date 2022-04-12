                                                                                                    
/**
 * This class represents the company holding employees
 *
 * @author Wayne Thomson
 * @version 05/04/2022, v1
 */
package sample;

import sample.Employee;

import java.lang.reflect.Array;
import java.util.*; // Figure out actualy import location
import java.io.*;
import java.nio.*;
import java.nio.file.Paths;
public class Company
{
    private Set<Employee> employeesInCompany; // A set to hold employees

    /*
     * Constructor inits a TreeSet
     * 
     * TreeSet is selected for two reasons.
     * 1.) It is sorted automaticaly based on the classes compareTo
     * 2.) It does not allow duplicates, as we would only want to employ someone once, this is ideal.
     * 
     */
    public Company()
    {
        employeesInCompany = new TreeSet<>();
    }

    /*
     * Clears all employees out of the set.
     */
    public void clear()
    {
        // MAYBE RESET STATIC EMPLOYEE COUNT TO ZERO OR ADD A METHOD TO RESET IT
        employeesInCompany.clear();
        System.out.println("Database cleared");
    }
    
    /*
     * Reorders the TreeSet after a variable used in sort order is changed
     * 
     * Creates a copy of the company, clears the original and finaly adds old back in. 
     * Not super efficient, but a simple solution.
     * 
     */
    public void reorderCompany(){
        // CREATE COPY
        // CLEAR
        // ADD IN FROM COPY
        
    }
    
    /*
     * Populates the database with several example employees
     * 
     * Future: MAYBE ADD RANDOM NAMES, ETC WITH PROMPT OF QUANITY
     */
    public void populate()
    {
        // Please note, I don't know the rules for NI numbers and used mine as a reference. However, a Sting of letters/numbers
        // should work regardless of posistioning.

        // REUSE OWN METHOD FOOL
        addMember(1, "A", 20000, "Clerk", "Accounting", "Bob", "John Smith");
        addMember(2,"F", 20000, "Clerk", "Accounting", "Bob", "John Smith");
        addMember(3, "I", 20000, "Clerk", "Accounting", "Bob", "John Smith");
        addMember(4,"OP 21 99 G", 20000, "Clerk", "Accounting", "Bob", "John Smith");
        addMember(5,"II 87 22 R", 20000, "Clerk", "Accounting", "Bob", "John Smith");
        System.out.println("Entered");
    }

    /*
     * Prints whole database to a CSV with desired filename.
     * Saved to program root dir
     * 
     * @param filename The name of the outut file
     */
    public void writeCSVFile(String filename)
    {
        // Trys to write with given name to root dir
        try(FileWriter writer = new FileWriter(filename))
        {
            
            for(Employee employee : employeesInCompany)
            {
                writer.write(employee.getNationalInsuranceNumber() + "," + employee.getPayPA() + "," + employee.getRoleAndDepartment()[0] + "," 
                            + employee.getRoleAndDepartment()[1] + "," + employee.getLineManager());
                writer.write('\n');
            }
            
        }
        // FURTHER DEVELOP
        catch(IOException e)
        {
            System.out.println(e);
        }
    }

    /*
     * Reads the selected file and creates employees using the CSV file
     * 
     * @param filename The name of the file in the root dir
     */
    public void readCSVFile(String filename)
    {
        // Trys to read the CSV file and creates a new employee for each line.
        try
        {
            Scanner employeeCSV = new Scanner(Paths.get(filename));
            
            while(employeeCSV.hasNextLine())
            {
                String[] currentEmployee = employeeCSV.nextLine().split(","); // Splits the line and apllies the data to new employee
                employeesInCompany.add(new Employee(Integer.parseInt(currentEmployee[0]),currentEmployee[1], Integer.parseInt(currentEmployee[2]), currentEmployee[3], currentEmployee[4], currentEmployee[5], currentEmployee[6]));
            }
        }
        // FURTHER DEVELOP
        catch(IOException e)
        {
            System.out.println(e);
        }
    }
    
    /*
     * Manualy add a new member to the database. If the database already contains said person then rejects the creation and informs
     * the user.
     * 
     * @param nationInsuranceNumber The NI of the new employee
     * @param payPA The pay of the new employee per year
     * @param role Role of new employee
     * @param department Department of new employee
     * @param lineManager LM of new employee
     * @param employeeName Employees name
     */
    public boolean addMember(int employeeNumber, String nationalInsuranceNumber, int payPA, String role, String department, String lineManager, String employeeName)
    {
        Employee newEmployee = new Employee(employeeNumber, nationalInsuranceNumber, payPA, role, department, lineManager, employeeName);
        if(employeesInCompany.contains(newEmployee))
        {
            String outputS = String.format("The Employee: %s already appears to exist with NI: %s "
                            + "\nCould not be added to the database.\nAlready exists."
                            , employeeName, nationalInsuranceNumber);
            System.out.println(outputS);
            return false;
        } else {
            employeesInCompany.add(newEmployee);
            String outputS = String.format("The Employee: %s with NI: %s "
                            + "\nHas been added to the database."
                            , employeeName, nationalInsuranceNumber);
            return true;
        }
    }
    
    /*
     * Removes an employee from the database
     * 
     * @param employeeRemove The employee to remove
     * @return If the employee was removed
     */
    public boolean removeMember(int employeeRemove)
    {
        TreeSet<Employee> temp = new TreeSet<>(employeesInCompany);
        for(Employee employee : temp) {
            if(employeeRemove == employee.getEmployeeNumber()){
                employeesInCompany.remove(employee);
                return true;
            }
        }
        return false;
    }
    
    /*
     * Method updateMember Overload One
     * 
     * Updates a data point of an employee, uses employeeNumber to find employee
     * 
     * @param employeeNumber Employee to be changed
     * @param newLineManager The name of the new line manager for this employee
     * @return If the update was a success
     * 
     */
    public boolean updateMember(int employeeNumber, String newLineManager)
    {
        for(Employee employee : employeesInCompany)
        {
            if(employee.getEmployeeNumber() == employeeNumber){
                employee.setLineManager(newLineManager);
                return true;
            }
        }
        return false;
    }
    
    /*
     * Method updateMember Overload Two
     * 
     * Updates a data point of an employee, uses employeeNumber to find employee
     * If ethier of the data point in the list are null then that value is ignored, handled by employee method.
     * 
     * @param employeeNumber Employee to be changed
     * @param newRoleAndDepartment A string list containing new role and/or department
     */
    public boolean updateMember(int employeeNumber, String[] newRoleAndDepartment)
    {
        for(Employee employee : employeesInCompany)
        {
            if(employee.getEmployeeNumber() == employeeNumber){
                employee.setRoleAndDepartment(newRoleAndDepartment[0], newRoleAndDepartment[1]);
                return true;
            }
        }
        return false;
    }
    
    /*
     * Method updateMember Overload Three
     * 
     * Updates a data point of an employee, uses employeeNumber to find employee
     * 
     * @param employeeNumber The employee to change
     * @param payPA The new value of the employees wage
     */
    public boolean updateMember(int employeeNumber, int payPA)
    {
        for(Employee employee : employeesInCompany)
        {
            if(employee.getEmployeeNumber() == employeeNumber){
                employee.setPayPA(payPA);
                return true;
            }
        }
        return false;
    }
    
    /*
     * Method updateMember Overload Four
     * 
     * Updates a data point of an employee, uses employeeNumber to find employee
     * Changes fundamental employee details, could have unexpected results.
     * 
     * @param employeeNumber The employee to change
     * @param newNI New NI number of employee
     * @param newEmployeeNumber The new employee number for the employee
     */
    public boolean updateMember(int employeeNumber, String newNI, Integer newEmployeeNumber)
    {
        for(Employee employee : employeesInCompany) {
            if (employee.getEmployeeNumber() == employeeNumber) {
                // Checks if the NI is being changed
                if (!(employee.getNationalInsuranceNumber().equals(newNI)) && !(newNI == null)) {
                    employee.setNationalInsuranceNumber(newNI);
                    reorderCompany();
                    return true;
                }
                if (!(employee.getEmployeeNumber() == newEmployeeNumber) && !(newEmployeeNumber == null)) {
                    employee.setEmployeeNumber(newEmployeeNumber);
                    reorderCompany();
                    return true;
                }
            }
        }
        return false;
    }
    
    /*
     * Method selectMembers Overload One
     * 
     * Finds employees with selected line manager
     * 
     * @param lineManagerFind The line manager to search for suborbinates of
     * @return A list of employees meeting the search criteria
     */
    public TreeSet<Employee> selectMembers(String lineManagerFind)
    {
        TreeSet<Employee> foundEmployees = new TreeSet<>();
        for(Employee employee : employeesInCompany)
        {
            if(employee.getLineManager().equals(lineManagerFind))
            {
                foundEmployees.add(employee);
            }
        }
        return foundEmployees;
    }
    
    /*
     * Method selectMembers Overload Two
     * 
     * Finds employees with employeeNumber
     * 
     * @param employeeNumber The employee number to search for
     * @return A list of employees meeting the search criteria
     * 
     */
    public TreeSet<Employee> selectMembers(int employeeNumber)
    {
        TreeSet<Employee> foundEmployees = new TreeSet<>();
        for(Employee employee : employeesInCompany)
        {
            if(employee.getEmployeeNumber() == employeeNumber)
            {
                foundEmployees.add(employee);
            }
        }
        return foundEmployees;
    }

    /*
     * Find a single Employee
     *
     * @param employeeID Employee to find
     * @return The toString of the found employee
     */
    public ArrayList<String> findEmployee(int employeeID) {
        ArrayList<String> employeeDetails = new ArrayList<>();
        for(Employee employee : employeesInCompany){
            if(employee.getEmployeeNumber() == employeeID) {
                employeeDetails.add(employee.getEmployeeName());
                employeeDetails.add(employee.getRoleAndDepartment()[1]);
                employeeDetails.add(employee.getRoleAndDepartment()[0]);
                employeeDetails.add(Integer. toString(employee.getPayPA()));
                employeeDetails.add(employee.getLineManager());
                employeeDetails.add(Integer. toString(employee.getEmployeeNumber()));
                return employeeDetails;
            }
        }
        return employeeDetails;
    }
    
    /*
     * Method selectMembers Overload Three
     * 
     * Finds employees with a role, department or both.
     * If one value is null it is ignored and other parameter is used as the selector.
     * 
     * @param role The role to select
     * @param department The department to select
     * @return A list of employees meeting the search criteria
     * 
     */
    public TreeSet<Employee> selectMembers(String role, String department)
    {
        TreeSet<Employee> foundEmployees = new TreeSet<>();
        for(Employee employee : employeesInCompany)
        {
            if(role == null){
                if(employee.getRoleAndDepartment()[1].equals(department)){
                    foundEmployees.add(employee);
                }
            } else if (department == null) {
                if(employee.getRoleAndDepartment()[0].equals(role)){
                    foundEmployees.add(employee);
                }
            } else {
                if(employee.getRoleAndDepartment()[1].equals(department) && employee.getRoleAndDepartment()[0].equals(role)) {
                    foundEmployees.add(employee);
                }
            }
        }
        return foundEmployees;
    }
    
    /*
     * Prints formatted text detailing all employees in the company
     */
    public void printMembers()
    {
        for(Employee employee : employeesInCompany)
        {
           String outputS = String.format("The Employee: %s, The PayPA: %d, Their role and department: %s-%s, Their NI: %s"
                            , employee.getLineManager(),employee.getPayPA(), employee.getRoleAndDepartment()[0]
                            , employee.getRoleAndDepartment()[1], employee.getNationalInsuranceNumber());                
           System.out.println(outputS);
        }
        System.out.println("");
    }
}
