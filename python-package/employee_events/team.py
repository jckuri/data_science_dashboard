# Import the QueryBase class
# YOUR CODE HERE

# Import dependencies for sql execution
#### YOUR CODE HERE

# Create a subclass of QueryBase
# called  `Team`
#### YOUR CODE HERE

    # Set the class attribute `name`
    # to the string "team"
    #### YOUR CODE HERE


    # Define a `names` method
    # that receives no arguments
    # This method should return
    # a list of tuples from an sql execution
    #### YOUR CODE HERE
        
        # Query 5
        # Write an SQL query that selects
        # the team_name and team_id columns
        # from the team table for all teams
        # in the database
        #### YOUR CODE HERE
    

    # Define a `username` method
    # that receives an ID argument
    # This method should return
    # a list of tuples from an sql execution
    #### YOUR CODE HERE

        # Query 6
        # Write an SQL query
        # that selects the team_name column
        # Use f-string formatting and a WHERE filter
        # to only return the team name related to
        # the ID argument
        #### YOUR CODE HERE


    # Below is method with an SQL query
    # This SQL query generates the data needed for
    # the machine learning model.
    # Without editing the query, alter this method
    # so when it is called, a pandas dataframe
    # is returns containing the execution of
    # the sql query
    #### YOUR CODE HERE
#    def model_data(self, id):

#        return f"""
#            SELECT positive_events, negative_events FROM (
#                    SELECT employee_id
#                         , SUM(positive_events) positive_events
#                         , SUM(negative_events) negative_events
#                    FROM {self.name}
#                    JOIN employee_events
#                        USING({self.name}_id)
#                    WHERE {self.name}.{self.name}_id = {id}
#                    GROUP BY employee_id
#                   )
#                """
                
                

# Import the QueryBase class
from employee_events import QueryBase
# from query_base import QueryBase


# Create a subclass of QueryBase
# called  `Team`
class Team(QueryBase):


    # Set the class attribute `name` to the string "team"
    name = "team"


    # Define a `names` method
    # that receives no arguments
    # This method should return
    # a list of tuples from an sql execution
    def names(self):
        
        # Query 5
        # Write an SQL query that selects
        # the team_name and team_id columns
        # from the team table for all teams
        # in the database
        query = f"""
        SELECT team_name, team_id
        FROM {self.name};
        """
        df = self.qm.pandas_query(query)
        return df.to_records(index = False)
    

    # Define a `username` method
    # that receives an ID argument
    # This method should return
    # a list of tuples from an sql execution
    def username(self, id):
        
        # Query 6
        # Write an SQL query
        # that selects the team_name column
        # Use f-string formatting and a WHERE filter
        # to only return the team name related to
        # the ID argument
        query = f"SELECT team_name FROM team WHERE team_id = {id};"
        df = self.qm.pandas_query(query)
        if len(df) > 0: return df.iloc[0]['team_name']
        return None


    # Below is method with an SQL query
    # This SQL query generates the data needed for
    # the machine learning model.
    # Without editing the query, alter this method
    # so when it is called, a pandas dataframe
    # is returns containing the execution of
    # the sql query
    #### YOUR CODE HERE
    def model_data(self, id):
        query = f"""
                SELECT positive_events, negative_events FROM (
                    SELECT employee_id
                         , SUM(positive_events) positive_events
                         , SUM(negative_events) negative_events
                    FROM {self.name}
                    JOIN employee_events
                        USING({self.name}_id)
                    WHERE {self.name}.{self.name}_id = {id}
                    GROUP BY employee_id
                );"""
        return self.qm.pandas_query(query)

                
def main():
 t = Team()
 names = t.names()
 print(names)
 id = 1
 print(t.username(id))
 print("model_data:")
 print(t.model_data(id))


if __name__ == "__main__": main()
