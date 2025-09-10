package com.example.backend.service;

import com.example.backend.model.RacketDTO;

import java.util.List;
import java.util.Optional;

public interface RacketService {
    RacketDTO dropoffRacket(RacketDTO racketDTO);
    List<RacketDTO> getAllRackets();
    RacketDTO getRacketById(long id);
    RacketDTO startRacket(long id);
    RacketDTO completeRacket(long id);
    RacketDTO pickupRacket(int pickupCode);
}
