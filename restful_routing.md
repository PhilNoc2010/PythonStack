RESTful routing
/table_name/id/action
## CRUD
/table_name/new --> display route that displays the form to create a new table row
/table_name/create --> Action Route that processes the form from the new route
/table_name/id --> display route that show the info of that row on the page but not in a form
/table_name/id/edit --> Display route that show the info of that row in a form so that we can edit it
/table_name/id/update --> Action Route that processes the edit form
/table_anme/id/delete --> Action Route that deletes the row in the database