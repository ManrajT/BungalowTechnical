# Bungalow Technical 

This is a small Django app for a technical challenge given by Bungalow.  It consists of two main things, a Django management command for ingesting data 
and an API for retrieving that data.  To produce these two things, a Django model needs to be created for interacting with an SQL backend.  Furthermore, 
to ensure that code I've developed is working correctly I've decided to deploy this onto Google App Engine.  I've never used Google App Engine, but I'm 
excited to learn.    


To access all the property data go to {domain}/getAllData endpoint.  
For example, go to https://bungalowtechnical-231523.appspot.com/getAllData

To ingest new data, please use ingest management command.
For example, python3 manage.py ingest /file/path/to/file.csv
