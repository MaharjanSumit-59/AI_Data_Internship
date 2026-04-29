-- Create database
CREATE DATABASE library_db;
USE library_db;

-- Create table
CREATE TABLE books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    author VARCHAR(255),
    year INT,
    genre VARCHAR(100),
    rating FLOAT
);

-- Insert data
INSERT INTO books (title, author, year, genre, rating) VALUES
('The Hobbit', 'J.R.R. Tolkien', 1937, 'Fantasy', 4.8),
('1984', 'George Orwell', 1949, 'Fiction', 4.7),
('To Kill a Mockingbird', 'Harper Lee', 1960, 'Fiction', 4.6),
('The Da Vinci Code', 'Dan Brown', 2003, 'Mystery', 3.9),
('The Road', 'Cormac McCarthy', 2006, 'Fiction', 4.1),
('Harry Potter and the Sorcerer''s Stone', 'J.K. Rowling', 1997, 'Fantasy', 4.9),
('The Girl with the Dragon Tattoo', 'Stieg Larsson', 2005, 'Thriller', 4.3),
('Sapiens', 'Yuval Noah Harari', 2011, 'Non-fiction', 4.5);
