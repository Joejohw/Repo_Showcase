package com.showcase.controllers;

import java.util.List;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.servlet.ModelAndView;

@Controller
public class HomeController {

    @GetMapping("/")
    public ModelAndView index() {
        ModelAndView modelAndView = new ModelAndView("index");
        modelAndView.addObject("nome", "Jonathan");
        var alunos = List.of("Jonathan", "Lucas", "Rafael", "Gabriel");
        modelAndView.addObject("alunos", alunos);
        return modelAndView;
    }
}