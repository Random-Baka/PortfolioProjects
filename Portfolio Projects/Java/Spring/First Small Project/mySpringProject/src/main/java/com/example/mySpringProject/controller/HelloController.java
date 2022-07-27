package com.example.mySpringProject.controller;
 
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
 
@RestController
public class HelloController {
 
  @GetMapping("/")
  public String helloWorld() {
    return "<div><h3>Hello World!</h3></div>";
  }
}
