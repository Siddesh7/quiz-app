from flask import Flask, render_template, request
import random
import copy

s = {
    'Where is Eiffel tower located? ': ['France', 'Germany', 'India', 'China'],
    'Who is the Prime Minister of India?': ['Nehru', 'Modi', 'Siva', 'Donald'],
    'Which planet is closest to Earth?': ['Mercury ', 'Venus', 'Pluto', 'Jupiter'],
    'Which Of These Has Two Zeros Two Fours?': ['0044', '0024', '2024', '2044']
}

ans = ['France', 'Modi', 'Venus', '2024']
questions = copy.deepcopy(s)
key = list(s.keys())
