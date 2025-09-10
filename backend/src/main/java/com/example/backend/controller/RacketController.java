package com.example.backend.controller;

import com.example.backend.model.RacketDTO;
import com.example.backend.service.RacketService;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("api/racket")
public class RacketController {

    private final RacketService racketService;

    public RacketController(RacketService racketService) {
        this.racketService = racketService;
    }

    @PostMapping("/dropoff")
    public RacketDTO dropoff(@RequestBody RacketDTO racketDTO) {
        return racketService.saveRacket(racketDTO);
    }
}