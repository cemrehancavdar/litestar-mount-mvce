I manage project with rye,

Steps:

1. Rye sync project

2. Run project with litestar run

3. go localhost:8000/ for see main index file

4. go localhost:8000/second for see index file
   it returns url_for for get handler

Expected:
http://localhost:8000/second
Result:
http://localhost:8000/

It is same result when using url_for inside Jinja Templates
