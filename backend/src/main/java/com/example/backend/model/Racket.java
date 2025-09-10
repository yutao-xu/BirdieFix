package com.example.backend.model;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;

@Entity
public class Racket {

    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private Long id;
    private int tension;
    private String racketString;
    private String phoneNumber;
    private int lockerNumber;
    private int pickupCode;
    private String status;

    protected Racket() {}

    public Racket(int tension, String racketString, String phoneNumber) {
        this.tension = tension;
        this.racketString = racketString;
        this.phoneNumber = phoneNumber;
        this.lockerNumber = -1;
        this.pickupCode = -1;
        this.status = "dropped_off";
    }

    public Long getId() {
        return id;
    }

    public int getTension() {
        return tension;
    }

    public String getRacketString() {
        return racketString;
    }

    public String getPhoneNumber() {
        return phoneNumber;
    }

    public int getLockerNumber() {
        return lockerNumber;
    }

    public int getPickupCode() {
        return pickupCode;
    }

    public String getStatus() {
        return status;
    }

    public void setLockerNumber(int lockerNumber) {
        this.lockerNumber = lockerNumber;
    }

    public void setPickupCode(int pickupCode) {
        this.pickupCode = pickupCode;
    }

    public void setStatus (String status) {
        this.status = status;
    }
}