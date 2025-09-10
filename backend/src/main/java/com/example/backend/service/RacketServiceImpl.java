package com.example.backend.service;

import com.example.backend.model.Racket;
import com.example.backend.model.RacketDTO;
import com.example.backend.repository.RacketRepository;
import org.springframework.stereotype.Service;

import java.util.*;

@Service
public class RacketServiceImpl implements RacketService {
    private final RacketRepository racketRepository;
    private final Random rand;
    private static final int NUM_LOCKERS = 20;

    public RacketServiceImpl(RacketRepository racketRepository) {
        this.racketRepository = racketRepository;
        rand = new Random();
    }

    @Override
    public RacketDTO dropoffRacket(RacketDTO racketDTO) {
        Racket racket = convertToEntity(racketDTO);
        racket.setLockerNumber(getAvailableLocker());
        Racket droppedoffRacket = racketRepository.save(racket);
        return convertToDTO(droppedoffRacket);
    }

    @Override
    public List<RacketDTO> getAllRackets() {
        List<RacketDTO> li = new ArrayList<>();
        for (Racket racket: racketRepository.findAll())
            li.add(convertToDTO(racket));
        return li;
    }

    @Override
    public RacketDTO getRacketById(long id) {
        return racketRepository.findById(id).map(this::convertToDTO).get();
    }

    @Override
    public RacketDTO startRacket(long id) {
        Racket racket = racketRepository.findById(id).get();
        racket.setLockerNumber(-1);
        racket.setStatus("started");
        racketRepository.save(racket);
        return convertToDTO(racket);
    }

    @Override
    public RacketDTO completeRacket(long id) {
        Racket racket = racketRepository.findById(id).get();
        racket.setLockerNumber(getAvailableLocker());
        racket.setStatus("completed");
        racket.setPickupCode(generatePickupCode());
        racketRepository.save(racket);
        return convertToDTO(racket);
    }

    @Override
    public RacketDTO pickupRacket(int pickupCode) {
        for (Racket racket : racketRepository.findAll()) {
            if (racket.getPickupCode() == pickupCode) {
                racket.setStatus("picked_up");
                RacketDTO pickedupRacket = convertToDTO(racket);
                racket.setLockerNumber(-1);
                racketRepository.save(racket);
                return pickedupRacket;
            }
        }
        return null;
    }

    private int getAvailableLocker() {
        HashSet<Integer> s = new HashSet<>();
        int lockerNumber;

        for (Racket racket : racketRepository.findAll()) {
            if (racket.getLockerNumber() != -1)
                s.add(racket.getLockerNumber());
        }

        do {
            lockerNumber = rand.nextInt(NUM_LOCKERS) + 1;
        } while (s.contains(lockerNumber));

        return lockerNumber;
    }

    private int generatePickupCode() {
        HashSet<Integer> s = new HashSet<>();
        int pickupCode;

        for (Racket racket : racketRepository.findAll()) {
            if (racket.getPickupCode() != -1)
                s.add(racket.getPickupCode());
        }

        do {
            pickupCode = rand.nextInt(1000000);
        } while (s.contains(pickupCode));

        return pickupCode;
    }
    private Racket convertToEntity(RacketDTO racketDTO) {
        return new Racket(racketDTO.tension(), racketDTO.racketString(), racketDTO.phoneNumber());
    }

    private RacketDTO convertToDTO(Racket racket) {
        return new RacketDTO(racket.getId(), racket.getTension(), racket.getRacketString(), racket.getPhoneNumber(), racket.getLockerNumber(), racket.getPickupCode(), racket.getStatus());
    }
}
