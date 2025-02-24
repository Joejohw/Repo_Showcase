package com.showcase.repositories;

import org.springframework.data.jpa.repository.JpaRepository;

import com.showcase.models.Todo;

public interface TodoRepository extends JpaRepository<Todo, Long> {
    
}
