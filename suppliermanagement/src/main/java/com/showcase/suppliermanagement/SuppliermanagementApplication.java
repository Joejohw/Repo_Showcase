package com.showcase.suppliermanagement;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.autoconfigure.domain.EntityScan;
import org.springframework.context.annotation.ComponentScan;

@SpringBootApplication

// verificação da entidade dos Controllers
@ComponentScan(basePackages = "com.showcase.controllers")

// verificação da entidade T.o.d.o
@EntityScan(basePackages = "com.showcase.models")
public class SuppliermanagementApplication {

    public static void main(String[] args) {
        SpringApplication.run(SuppliermanagementApplication.class, args);
    }

}