# <center>Belasting Toegevoegde Waarde</center>

# Value Added Tax with Django

VAT is a simple tax domain to be tested as guniea pig while trying out new applications.

## Domain

Domain is where the Aggregate classes reside. It is the center of the application. It also contains Repository contracts (using Repository pattern).

## Common

This folder holds common pieces that are used thoughout the application. A simple example would be Result objects.

## Infrastructure

This is for contacting third party services.

## APP

Business Layer or App Layer is the mediator between the API and the domain contracts. It also carries out query operations from the dataaccess layer to the API level.

## DataAccess

Repository contract implementations, database operations are carried out here. It serves the connection from database to the application.