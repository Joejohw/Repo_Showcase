package com.showcase.controllers;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.servlet.ModelAndView;

@Controller
public class HomeController {

    @GetMapping("/")
    public ModelAndView index() {
        return new ModelAndView("index");
    }

    @GetMapping("/register")
    public ModelAndView showRegistrationForm() {
        return new ModelAndView ("register");
    }

    @GetMapping("/home")
    public ModelAndView home() {
        return new ModelAndView ("home");
    }
}