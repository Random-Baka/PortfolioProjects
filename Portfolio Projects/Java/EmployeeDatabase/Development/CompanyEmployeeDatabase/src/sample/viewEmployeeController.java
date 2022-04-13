package sample;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Node;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Label;
import javafx.scene.control.ListView;
import javafx.scene.control.SelectionMode;
import javafx.scene.control.TextField;
import javafx.stage.Stage;

import java.io.IOException;
import java.util.ArrayList;
import java.util.TreeSet;

public class viewEmployeeController {
    private Stage stage;
    private Scene scene;
    private Parent root;

    @FXML
    public Label nameView,departmentView,roleView,salaryView,lineManagerView,employeeNumberView,natInView;

    @FXML
    private ListView employeeView;
    private TreeSet<Employee> employees;

    public void initialize() {
    }

    @FXML
    public void switchToMainMenu(ActionEvent event) throws IOException {
        Parent root = FXMLLoader.load(getClass().getResource("mainMenu.fxml"));
        stage = (Stage) ((Node) event.getSource()).getScene().getWindow();
        scene = new Scene(root);
        stage.setScene(scene);
        stage.show();
    }

    public void populateListWithFresh() {
        employees = Main.companyX.getEmployeesInCompany();
        employeeView.getItems().setAll(employees);
        employeeView.getSelectionModel().setSelectionMode(SelectionMode.SINGLE);
    }

    @FXML
    public void clearView() {
        // Do clear
    }

    @FXML
    public void populateView() {
        employees = Main.companyX.getEmployeesInCompany();
        employeeView.getItems().setAll(employees);
        employeeView.getSelectionModel().setSelectionMode(SelectionMode.SINGLE);
    }

    @FXML
    public void findEmployees() {

    }

    @FXML
    public void handleClickListView() {
        Employee employeeSelected = (Employee) employeeView.getSelectionModel().getSelectedItem();
        nameView.setText("Name: " + employeeSelected.getEmployeeName());
        departmentView.setText("Department: " + employeeSelected.getRoleAndDepartment()[1]);
        roleView.setText("Role: " + employeeSelected.getRoleAndDepartment()[0]);
        salaryView.setText("Salary: " + employeeSelected.getPayPA());
        lineManagerView.setText("Line Manager: " + employeeSelected.getLineManager());
        employeeNumberView.setText("Employee Number: " + employeeSelected.getEmployeeNumber());
        natInView.setText("NI Number: " + employeeSelected.getNationalInsuranceNumber());


    }
}
