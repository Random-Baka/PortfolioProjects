package sample;


import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Node;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.text.Text;
import javafx.stage.Stage;

import java.io.IOException;
import java.lang.reflect.Array;
import java.util.ArrayList;

public class addEmployeeController {
    private Stage stage;
    private Scene scene;
    private Parent root;

    @FXML
    private TextField addEN;
    @FXML
    private TextField addNI;
    @FXML
    private TextField addPPA;
    @FXML
    private TextField addRole;
    @FXML
    private TextField addDep;
    @FXML
    private TextField addLM;
    @FXML
    private TextField addName;
    @FXML
    private Label addSuccess;

    @FXML
    public void switchToMainMenu(ActionEvent event) throws IOException {
        Parent root = FXMLLoader.load(getClass().getResource("mainMenu.fxml"));
        stage = (Stage) ((Node) event.getSource()).getScene().getWindow();
        scene = new Scene(root);
        stage.setScene(scene);
        stage.show();
    }

    @FXML
    public void addUser() {
        boolean success = Main.companyX.addMember(Integer.parseInt(addEN.getText()), addNI.getText(), Integer.parseInt(addPPA.getText()),
                addRole.getText(), addDep.getText(), addLM.getText(), addName.getText());
        if(success){
            addSuccess.setText("Employee: " + addName.getText() + " added successfully");
        } else {
            addSuccess.setText("Employee: " + addName.getText() + " failed to add, check that employee does not already exist!");
        }
        addEN.clear();
        addNI.clear();
        addPPA.clear();
        addPPA.clear();
        addRole.clear();
        addDep.clear();
        addLM.clear();
        addName.clear();
    }
}
