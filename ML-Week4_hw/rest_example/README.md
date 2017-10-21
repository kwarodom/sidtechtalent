
Rest api of system recommender  

# Requirement
- python3 (Test with python 3.6.3)
- python module(see: requirements.txt)

# Setup
```
pip install -r requirement.txt
cd recommendsystem_project
python manage.py migrate
python manage.py createsuperuser    # test with user/password: 'admin'/'password123'
```

# Start local rest server  
```
python manage.py runserver
```

# App: Car model recommend with K-Nearest Neighbors(K=3)
url: http://127.0.0.1:8000/carrecommend_3nnb/

Try POST with json:  
```
{
    "mpg": 15,
    "disp": 300,
    "hp": 160,
    "wt": 3.2
}
```

Should receive something like:  
```
{
    "result": [
        {
            "car_names": "AMC Javelin",
            "mpg": 15.2,
            "cyl": 8,
            "disp": 304.0,
            "hp": 150,
            "drat": 3.15,
            "wt": 3.435,
            "qsec": 17.3,
            "vs": 0,
            "am": 0,
            "gear": 3,
            "carb": 2
        },
        {
            "car_names": "Dodge Challenger",
            "mpg": 15.5,
            "cyl": 8,
            "disp": 318.0,
            "hp": 150,
            "drat": 2.76,
            "wt": 3.52,
            "qsec": 16.87,
            "vs": 0,
            "am": 0,
            "gear": 3,
            "carb": 2
        },
        {
            "car_names": "Merc 450SLC",
            "mpg": 15.2,
            "cyl": 8,
            "disp": 275.8,
            "hp": 180,
            "drat": 3.07,
            "wt": 3.78,
            "qsec": 18.0,
            "vs": 0,
            "am": 0,
            "gear": 3,
            "carb": 3
        }
    ]
}
```

