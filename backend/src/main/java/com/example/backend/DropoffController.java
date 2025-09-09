package com.example.backend;

import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class DropoffController {

    @PostMapping(path = "/dropoff", consumes = "application/json", produces = "application/json")
    public String Dropoff(@RequestBody Order order) {
        return "Tension: " + order.getTension() +
                "\n" + "String: " + order.getRacketString() +
                "\n" + "Phone Number: " + order.getPhoneNumber();
    }
}
