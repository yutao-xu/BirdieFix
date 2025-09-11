package com.example.backend.controller;

import com.example.backend.model.RacketDTO;
import com.example.backend.service.RacketService;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@CrossOrigin(origins = "*")
@RequestMapping("api/rackets")
public class RacketController {

    private final RacketService racketService;

    public RacketController(RacketService racketService) {
        this.racketService = racketService;
    }

    @GetMapping
    public List<RacketDTO> getAllRackets() {
        return racketService.getAllRackets();
    }
    @PostMapping("/dropoff")
    public RacketDTO dropoff(@RequestBody RacketDTO racketDTO) {
        return racketService.dropoffRacket(racketDTO);
    }

    @GetMapping("/{id}")
    public RacketDTO getRacketById(@PathVariable long id) {
        return racketService.getRacketById(id);
    }

    @GetMapping("/start/{id}")
    public RacketDTO startRacket(@PathVariable long id) {
        return racketService.startRacket(id);
    }

    @GetMapping("/complete/{id}")
    public RacketDTO completeRacket(@PathVariable long id) {
        return racketService.completeRacket(id);
    }

    @PostMapping("/pickup/{pickupCode}")
    public RacketDTO pickupRacket(@PathVariable int pickupCode) {
        return racketService.pickupRacket(pickupCode);
    }
}