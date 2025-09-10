package com.example.backend.service;

import com.example.backend.model.Racket;
import com.example.backend.model.RacketDTO;
import com.example.backend.repository.RacketRepository;
import org.springframework.stereotype.Service;

@Service
public class RacketServiceImpl implements RacketService {
    private final RacketRepository racketRepository;

    public RacketServiceImpl(RacketRepository racketRepository) {
        this.racketRepository = racketRepository;
    }

    @Override
    public RacketDTO saveRacket(RacketDTO racketDTO) {
        Racket racket = convertToEntity(racketDTO);
        Racket savedRacket = racketRepository.save(racket);
        return convertToDTO(savedRacket);
    }

    private Racket convertToEntity(RacketDTO racketDTO) {
        return new Racket(racketDTO.tension(), racketDTO.racketString(), racketDTO.phoneNumber());
    }

    private RacketDTO convertToDTO(Racket racket) {
        return new RacketDTO(racket.getTension(), racket.getRacketString(), racket.getPhoneNumber());
    }
}
