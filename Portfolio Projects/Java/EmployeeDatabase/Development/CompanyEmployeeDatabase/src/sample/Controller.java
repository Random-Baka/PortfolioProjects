package sample;


import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Node;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.TextField;
import javafx.stage.Stage;

import java.io.IOException;

public class Controller {
    private Stage stage;
    private Scene scene;
    private Parent root;



    @FXML
    public void switchToMainMenu(ActionEvent event) throws IOException {
        Parent root = FXMLLoader.load(getClass().getResource("mainMenu.fxml"));
        stage = (Stage)((Node)event.getSource()).getScene().getWindow();
        scene = new Scene(root);
        stage.setScene(scene);
        stage.show();
    }
    @FXML
    public void switchToAddUser(ActionEvent event) throws IOException {
        Parent root = FXMLLoader.load(getClass().getResource("addEmployee.fxml"));
        stage = (Stage)((Node)event.getSource()).getScene().getWindow();
        scene = new Scene(root);
        stage.setScene(scene);
        stage.show();
    }
    @FXML
    public void switchToRemoveUser(ActionEvent event) throws IOException {
        Parent root = FXMLLoader.load(getClass().getResource("removeEmployee.fxml"));
        stage = (Stage)((Node)event.getSource()).getScene().getWindow();
        scene = new Scene(root);
        stage.setScene(scene);
        stage.show();
    }
    @FXML
    public void switchToUpdateUser(ActionEvent event) throws IOException {
        Parent root = FXMLLoader.load(getClass().getResource("updateEmployee.fxml"));
        stage = (Stage)((Node)event.getSource()).getScene().getWindow();
        scene = new Scene(root);
        stage.setScene(scene);
        stage.show();
    }
    @FXML
    public void switchToViewEmployees(ActionEvent event) throws IOException {
        Parent root = FXMLLoader.load(getClass().getResource("viewEmployees.fxml"));
        stage = (Stage)((Node)event.getSource()).getScene().getWindow();
        scene = new Scene(root);
        stage.setScene(scene);
        stage.show();
    }


    @FXML
    private TextField name;


    @FXML
    public void populateDemoValues() {
        sample.Main.companyX.populate();
        System.out.println("Button Pressed");
    }

    @FXML
    public void printMembers() {
        Main.companyX.printMembers();
    }

    @FXML
    public void testMethod() {
        Main.companyX.addMember(7,"AB 22 23 D", 20000, "Clerk", "Accounting", "Bob", "John Smith");
        System.out.println("Enterered");
    }


}
