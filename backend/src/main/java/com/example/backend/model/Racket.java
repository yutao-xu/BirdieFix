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

    protected Racket() {}

    public Racket(int tension, String racketString, String phoneNumber) {
        this.tension = tension;
        this.racketString = racketString;
        this.phoneNumber = phoneNumber;
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
}