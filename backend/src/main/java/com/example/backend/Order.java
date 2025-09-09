package com.example.backend;

public class Order {
    private int tension;
    private String racketString;
    private String phoneNumber;

    public Order(int tension, String racketString, String phoneNumber) {
        this.tension = tension;
        this.racketString = racketString;
        this.phoneNumber = phoneNumber;
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
