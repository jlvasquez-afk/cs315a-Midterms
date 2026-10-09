# Running the project

This is a FastAPI REST API for library books and categories. Start it on Replit
with the configured workflow, or run:

```sh
python -m uvicorn main:app --host 0.0.0.0 --port 8000
```

- API status: `/`
- Interactive API documentation: `/docs`
- OpenAPI schema: `/openapi.json`
- Data is stored in the local `library.db` SQLite file.

The current API declares book listing, detail, update, and delete routes, but
their corresponding CRUD functions are not present in `crud.py`; those routes
will need implementation before they can serve requests successfully.
