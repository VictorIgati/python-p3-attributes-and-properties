#!/usr/bin/env python3
#/python-p3-attributes-and-properties/lib/person.py

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name='Unknown', job='Unemployed'):
        self.name = name
        self.job = job

    def get_name(self):
        return self._name

    def set_name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 25:
            self._name = name.title()
        else:
            print("Name must be string between 1 and 25 characters.")

    name = property(get_name, set_name)        

    def get_job(self):
        return self._job

    def set_job(self, job):
        if job in APPROVED_JOBS:
            self._job = job
        else:
            print("Job must be in list of approved jobs.")

    job = property(get_job, set_job) 

    def __str__(self):
        return f"{self._name} is a {self._job}"
        assert(captured_out.getvalue() == "Name must be string between 1 and 25 characters.\n")

    def test_name_under_25(self):
        '''prints "Name must be string between 1 and 25 characters." if string over 25 characters.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        Person(name="What do Persons do on their day off? Can't lie around - that's their job.",
               job='Sales')
        sys.stdout = sys.__stdout__
        assert(captured_out.getvalue() == "Name must be string between 1 and 25 characters.\n")

    def test_valid_name(self):
        '''saves name if string between 1 and 25 characters.'''
        guido = Person("Guido")
        assert(guido.name == "Guido")

    def test_valid_name_title_case(self):
        '''converts name to title case and saves if between 1 and 25 characters'''
        guido = Person(name="guido van rossum")
        assert(guido.name == "Guido Van Rossum")

    def test_job_not_in_list(self):
        '''prints "Job must be in list of approved jobs." if not in job list.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        Person(job="Benevolent dictator for life")
        sys.stdout = sys.__stdout__
        assert(captured_out.getvalue() == "Job must be in list of approved jobs.\n")

    def test_job_in_list(self):
        '''saves job if in job list.'''
        guido = Person(job="ITC")
        assert(guido.job == "ITC")
