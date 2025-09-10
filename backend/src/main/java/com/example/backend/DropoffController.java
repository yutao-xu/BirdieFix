package com.example.backend;

import com.example.backend.model.RacketDTO;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class DropoffController {

    @PostMapping(path = "/api/dropoff", consumes = "application/json", produces = "application/json")
    public String Dropoff(@RequestBody RacketDTO racketDTO) {
        return "Tension: " + racketDTO.tension() +
                "\n" + "String: " + racketDTO.racketString() +
                "\n" + "Phone Number: " + racketDTO.phoneNumber();
    }
}