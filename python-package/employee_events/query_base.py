# Import any dependencies needed to execute sql queries
# YOUR CODE HERE

# Define a class called QueryBase
# that has no parent class
# YOUR CODE HERE

# Create a class attribute called `name`
# set the attribute to an empty string
# YOUR CODE HERE

# Define a `names` method that receives
# no passed arguments
# YOUR CODE HERE

# Return an empty list
# YOUR CODE HERE


# Define an `event_counts` method
# that receives an `id` argument
# This method should return a pandas dataframe
# YOUR CODE HERE

# QUERY 1
# Write an SQL query that groups by `event_date`
# and sums the number of positive and negative events
# Use f-string formatting to set the FROM {table}
# to the `name` class attribute
# Use f-string formatting to set the name
# of id columns used for joining
# order by the event_date column
# YOUR CODE HERE


# Define a `notes` method that receives an id argument
# This function should return a pandas dataframe
# YOUR CODE HERE

# QUERY 2
# Write an SQL query that returns `note_date`, and `note`
# from the `notes` table
# Set the joined table names and id columns
# with f-string formatting
# so the query returns the notes
# for the table name in the `name` class attribute
# YOUR CODE HERE


# Import necessary dependencies
# import sql_execution
from employee_events import QueryMixin


# Define the QueryBase class
class QueryBase:
    # Create a class attribute called `name`
    name = ""

    def __init__(self):
        # self.qm = sql_execution.QueryMixin()
        self.qm = QueryMixin()

    # Define a `names` method that receives no arguments
    def names(self):
        # Return an empty list
        return []

    # Define an `event_counts` method
    def event_counts(self, id):
        if self.name == "employee":
            id_field = "employee_id"
        elif self.name == "team":
            id_field = "team_id"
        else:
            return None
        query = f"""
        SELECT 
            event_date,
            SUM(positive_events) AS positive_events,
            SUM(negative_events) AS negative_events
        FROM employee_events
        WHERE {id_field} = {id}
        GROUP BY event_date
        ORDER BY event_date;
        """
        return self.qm.pandas_query(query)

    # Define a `notes` method
    def notes(self, id):
        if self.name == "employee":
            id_field = "employee_id"
        elif self.name == "team":
            id_field = "team_id"
        else:
            return None
        query = f"""
        SELECT 
            note_date,
            note
        FROM notes
        WHERE {id_field} = {id};
        """
        return self.qm.pandas_query(query)


def main():
    qb = QueryBase()
    # qb.name = "employee"
    qb.name = "team"
    df = qb.event_counts(1)
    print(df)
    print("Hello world.")
    df = qb.notes(1)
    print(df)


if __name__ == "__main__":
    main()
