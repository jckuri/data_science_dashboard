#from fasthtml.common import *
#import matplotlib.pyplot as plt

## Import QueryBase, Employee, Team from employee_events
##### YOUR CODE HERE

## import the load_model function from the utils.py file
##### YOUR CODE HERE

#"""
#Below, we import the parent classes
#you will use for subclassing
#"""
#from base_components import (
#    Dropdown,
#    BaseComponent,
#    Radio,
#    MatplotlibViz,
#    DataTable
#    )

#from combined_components import FormGroup, CombinedComponent


## Create a subclass of base_components/dropdown
## called `ReportDropdown`
##### YOUR CODE HERE
#    
#    # Overwrite the build_component method
#    # ensuring it has the same parameters
#    # as the Report parent class's method
#    #### YOUR CODE HERE
#        #  Set the `label` attribute so it is set
#        #  to the `name` attribute for the model
#        #### YOUR CODE HERE
#        
#        # Return the output from the
#        # parent class's build_component method
#        #### YOUR CODE HERE
#    
#    # Overwrite the `component_data` method
#    # Ensure the method uses the same parameters
#    # as the parent class method
#    #### YOUR CODE HERE
#        # Using the model argument
#        # call the employee_events method
#        # that returns the user-type's
#        # names and ids


## Create a subclass of base_components/BaseComponent
## called `Header`
##### YOUR CODE HERE

#    # Overwrite the `build_component` method
#    # Ensure the method has the same parameters
#    # as the parent class
#    #### YOUR CODE HERE
#        
#        # Using the model argument for this method
#        # return a fasthtml H1 objects
#        # containing the model's name attribute
#        #### YOUR CODE HERE
#          

## Create a subclass of base_components/MatplotlibViz
## called `LineChart`
##### YOUR CODE HERE
#    
#    # Overwrite the parent class's `visualization`
#    # method. Use the same parameters as the parent
#    #### YOUR CODE HERE
#    

#        # Pass the `asset_id` argument to
#        # the model's `event_counts` method to
#        # receive the x (Day) and y (event count)
#        #### YOUR CODE HERE
#        
#        # Use the pandas .fillna method to fill nulls with 0
#        #### YOUR CODE HERE
#        
#        # User the pandas .set_index method to set
#        # the date column as the index
#        #### YOUR CODE HERE
#        
#        # Sort the index
#        #### YOUR CODE HERE
#        
#        # Use the .cumsum method to change the data
#        # in the dataframe to cumulative counts
#        #### YOUR CODE HERE
#        
#        
#        # Set the dataframe columns to the list
#        # ['Positive', 'Negative']
#        #### YOUR CODE HERE
#        
#        # Initialize a pandas subplot
#        # and assign the figure and axis
#        # to variables
#        #### YOUR CODE HERE
#        
#        # call the .plot method for the
#        # cumulative counts dataframe
#        #### YOUR CODE HERE
#        
#        # pass the axis variable
#        # to the `.set_axis_styling`
#        # method
#        #### YOUR CODE HERE
#        
#        # Set title and labels for x and y axis
#        #### YOUR CODE HERE


## Create a subclass of base_components/MatplotlibViz
## called `BarChart`
##### YOUR CODE HERE

#    # Create a `predictor` class attribute
#    # assign the attribute to the output
#    # of the `load_model` utils function
#    #### YOUR CODE HERE

#    # Overwrite the parent class `visualization` method
#    # Use the same parameters as the parent
#    #### YOUR CODE HERE

#        # Using the model and asset_id arguments
#        # pass the `asset_id` to the `.model_data` method
#        # to receive the data that can be passed to the machine
#        # learning model
#        #### YOUR CODE HERE
#        
#        # Using the predictor class attribute
#        # pass the data to the `predict_proba` method
#        #### YOUR CODE HERE
#        
#        # Index the second column of predict_proba output
#        # The shape should be (<number of records>, 1)
#        #### YOUR CODE HERE
#        
#        
#        # Below, create a `pred` variable set to
#        # the number we want to visualize
#        #
#        # If the model's name attribute is "team"
#        # We want to visualize the mean of the predict_proba output
#        #### YOUR CODE HERE
#            
#        # Otherwise set `pred` to the first value
#        # of the predict_proba output
#        #### YOUR CODE HERE
#        
#        # Initialize a matplotlib subplot
#        #### YOUR CODE HERE
#        
#        # Run the following code unchanged
#        ax.barh([''], [pred])
#        ax.set_xlim(0, 1)
#        ax.set_title('Predicted Recruitment Risk', fontsize=20)
#        
#        # pass the axis variable
#        # to the `.set_axis_styling`
#        # method
#        #### YOUR CODE HERE
# 
## Create a subclass of combined_components/CombinedComponent
## called Visualizations       
##### YOUR CODE HERE

#    # Set the `children`
#    # class attribute to a list
#    # containing an initialized
#    # instance of `LineChart` and `BarChart`
#    #### YOUR CODE HERE

#    # Leave this line unchanged
#    outer_div_type = Div(cls='grid')
#            
## Create a subclass of base_components/DataTable
## called `NotesTable`
##### YOUR CODE HERE

#    # Overwrite the `component_data` method
#    # using the same parameters as the parent class
#    #### YOUR CODE HERE
#        
#        # Using the model and entity_id arguments
#        # pass the entity_id to the model's .notes 
#        # method. Return the output
#        #### YOUR CODE HERE
#    

#class DashboardFilters(FormGroup):

#    id = "top-filters"
#    action = "/update_data"
#    method="POST"

#    children = [
#        Radio(
#            values=["Employee", "Team"],
#            name='profile_type',
#            hx_get='/update_dropdown',
#            hx_target='#selector'
#            ),
#        ReportDropdown(
#            id="selector",
#            name="user-selection")
#        ]
#    
## Create a subclass of CombinedComponents
## called `Report`
##### YOUR CODE HERE

#    # Set the `children`
#    # class attribute to a list
#    # containing initialized instances 
#    # of the header, dashboard filters,
#    # data visualizations, and notes table
#    #### YOUR CODE HERE

## Initialize a fasthtml app 
##### YOUR CODE HERE

## Initialize the `Report` class
##### YOUR CODE HERE


## Create a route for a get request
## Set the route's path to the root
##### YOUR CODE HERE

#    # Call the initialized report
#    # pass None and an instance
#    # of the QueryBase class as arguments
#    # Return the result
#    #### YOUR CODE HERE

## Create a route for a get request
## Set the route's path to receive a request
## for an employee ID so `/employee/2`
## will return the page for the employee with
## an ID of `2`. 
## parameterize the employee ID 
## to a string datatype
##### YOUR CODE HERE

#    # Call the initialized report
#    # pass the ID and an instance
#    # of the Employee SQL class as arguments
#    # Return the result
#    #### YOUR CODE HERE

## Create a route for a get request
## Set the route's path to receive a request
## for a team ID so `/team/2`
## will return the page for the team with
## an ID of `2`. 
## parameterize the team ID 
## to a string datatype
##### YOUR CODE HERE

#    # Call the initialized report
#    # pass the id and an instance
#    # of the Team SQL class as arguments
#    # Return the result
#    #### YOUR CODE HERE


## Keep the below code unchanged!
#@app.get('/update_dropdown{r}')
#def update_dropdown(r):
#    dropdown = DashboardFilters.children[1]
#    print('PARAM', r.query_params['profile_type'])
#    if r.query_params['profile_type'] == 'Team':
#        return dropdown(None, Team())
#    elif r.query_params['profile_type'] == 'Employee':
#        return dropdown(None, Employee())


#@app.post('/update_data')
#async def update_data(r):
#    from fasthtml.common import RedirectResponse
#    data = await r.form()
#    profile_type = data._dict['profile_type']
#    id = data._dict['user-selection']
#    if profile_type == 'Employee':
#        return RedirectResponse(f"/employee/{id}", status_code=303)
#    elif profile_type == 'Team':
#        return RedirectResponse(f"/team/{id}", status_code=303)
#    


#serve()




from fasthtml.common import *
import matplotlib.pyplot as plt
import numpy as np
import pandas

# Import QueryBase, Employee, Team from employee_events
#### YOUR CODE HERE
from employee_events import Employee, Team

# import the load_model function from the utils.py file
#### YOUR CODE HERE
from utils import load_model

"""
Below, we import the parent classes
you will use for subclassing
"""
from base_components import (
    Dropdown,
    BaseComponent,
    Radio,
    MatplotlibViz,
    DataTable
    )

from combined_components import FormGroup, CombinedComponent


# Create a subclass of base_components/dropdown
# called `ReportDropdown`
#### YOUR CODE HERE
class ReportDropdown(Dropdown):
    # Overwrite the build_component method
    # ensuring it has the same parameters
    # as the Report parent class's method
    #### YOUR CODE HERE
    def build_component(self, entity_id, model, *args, **kwargs):
        #  Set the `label` attribute so it is set
        #  to the `name` attribute for the model
        #### YOUR CODE HERE
        self.label = model.name
        # Return the output from the
        # parent class's build_component method
        #### YOUR CODE HERE
        return super().build_component(entity_id, model, *args, **kwargs)
    
    # Overwrite the `component_data` method
    # Ensure the method uses the same parameters
    # as the parent class method
    #### YOUR CODE HERE
    def component_data(self, entity_id, model, *args, **kwargs):
        # Using the model argument
        # call the employee_events method
        # that returns the user-type's
        # names and ids
        return model.names()


# Create a subclass of base_components/BaseComponent
# called `Header`
#### YOUR CODE HERE
class Header(BaseComponent):
    # Overwrite the `build_component` method
    # Ensure the method has the same parameters
    # as the parent class
    #### YOUR CODE HERE
    def build_component(self, entity_id, model, *args, **kwargs):
        # Using the model argument for this method
        # return a fasthtml H1 objects
        # containing the model's name attribute
        #### YOUR CODE HERE
        title = "Employee Performance" if model.name == 'employee' else "Team Performance"
        return H1(title)
          

# Create a subclass of base_components/MatplotlibViz
# called `LineChart`
#### YOUR CODE HERE
class LineChart(MatplotlibViz):
    
    # Overwrite the parent class's `visualization`
    # method. Use the same parameters as the parent
    #### YOUR CODE HERE
    def visualization(self, entity_id, model):
    
        # Pass the `asset_id` argument to
        # the model's `event_counts` method to
        # receive the x (Day) and y (event count)
        #### YOUR CODE HERE
        events_df = model.event_counts(entity_id)
        
        # Use the pandas .fillna method to fill nulls with 0
        #### YOUR CODE HERE
        events_df.fillna(0, inplace=True)
        
        # User the pandas .set_index method to set
        # the date column as the index
        #### YOUR CODE HERE
        events_df.set_index('event_date')
        
        # Sort the index
        #### YOUR CODE HERE
        events_df.sort_index()
        
        # Use the .cumsum method to change the data
        # in the dataframe to cumulative counts
        #### YOUR CODE HERE
        #events_df = events_df.cumsum(axis = [1, 2])
        #pd.concat([df[['y0', 'y1']].cumsum(axis=1),df['y2']], axis=1)
        sum_df = events_df[['positive_events', 'negative_events']].cumsum(axis = 0)
        date_df = pandas.to_datetime(events_df['event_date'])
        events_df = pandas.concat([date_df, sum_df], axis = 1)
        
        # Set the dataframe columns to the list
        # ['Positive', 'Negative']
        #### YOUR CODE HERE
        events_df.rename(columns={'event_date': 'Date', 'positive_events': 'Positive', 'negative_events': 'Negative'}, inplace=True)
        
        # Initialize a pandas subplot
        # and assign the figure and axis
        # to variables
        #### YOUR CODE HERE
        figure, axis = plt.subplots()
        
        # call the .plot method for the
        # cumulative counts dataframe
        #### YOUR CODE HERE
        plt.plot(events_df['Date'], events_df[['Positive', 'Negative']], label = ['Positive', 'Negative']) 
        axis.xaxis_date()
        figure.autofmt_xdate()
        
        # pass the axis variable
        # to the `.set_axis_styling`
        # method
        #### YOUR CODE HERE
        
        # Set title and labels for x and y axis
        #### YOUR CODE HERE
        plt.title('Positive and negative events through time', fontsize = 16)
        plt.xlabel('Time')
        plt.ylabel('Cumulative number of events')
        plt.legend(title = 'Events:')
        
        return figure


# Create a subclass of base_components/MatplotlibViz
# called `BarChart`
#### YOUR CODE HERE
class BarChart(MatplotlibViz):

    # Create a `predictor` class attribute
    # assign the attribute to the output
    # of the `load_model` utils function
    #### YOUR CODE HERE
    predictor = load_model()

    # Overwrite the parent class `visualization` method
    # Use the same parameters as the parent
    #### YOUR CODE HERE
    def visualization(self, entity_id, model):
    
        # Using the model and asset_id arguments
        # pass the `asset_id` to the `.model_data` method
        # to receive the data that can be passed to the machine
        # learning model
        #### YOUR CODE HERE
        print(f'entity_id={entity_id}')
        df = model.model_data(entity_id)        
        
        # Using the predictor class attribute
        # pass the data to the `predict_proba` method
        #### YOUR CODE HERE
        prediction = BarChart.predictor.predict_proba(df)
        
        # Index the second column of predict_proba output
        # The shape should be (<number of records>, 1)
        #### YOUR CODE HERE
        
        # Below, create a `pred` variable set to
        # the number we want to visualize
        #
        # If the model's name attribute is "team"
        # We want to visualize the mean of the predict_proba output
        #### YOUR CODE HERE
        if model.name == "team":
            prediction = prediction.mean(axis = 0)
        else:
            prediction = prediction[0]
            
        # Otherwise set `pred` to the first value
        # of the predict_proba output
        #### YOUR CODE HERE
        
        # Initialize a matplotlib subplot
        #### YOUR CODE HERE
        figure, axis = plt.subplots()
        titles = ["Risk of being recruited", "Will not be recruited"]
        plt.bar(titles, prediction)
        
        # Run the following code unchanged
        #axis.barh([''], [prediction])
        #axis.set_xlim(0, 1)
        axis.set_title('Predicted Recruitment Risk', fontsize=20)
        plt.ylabel('Probability')
        
        # pass the axis variable
        # to the `.set_axis_styling`
        # method
        #### YOUR CODE HERE
        
        return figure
 
# Create a subclass of combined_components/CombinedComponent
# called Visualizations       
#### YOUR CODE HERE
class Visualizations(CombinedComponent):

    # Set the `children`
    # class attribute to a list
    # containing an initialized
    # instance of `LineChart` and `BarChart`
    #### YOUR CODE HERE
    children = [BarChart(), LineChart()]

    # Leave this line unchanged
    outer_div_type = Div(cls='grid')
            
# Create a subclass of base_components/DataTable
# called `NotesTable`
#### YOUR CODE HERE
class NotesTable(DataTable):
    # Overwrite the `component_data` method
    # using the same parameters as the parent class
    #### YOUR CODE HERE
    def component_data(self, entity_id, model, *args, **kwargs):
        # Using the model and entity_id arguments
        # pass the entity_id to the model's .notes 
        # method. Return the output
        #### YOUR CODE HERE
        return model.notes(entity_id)
    

class DashboardFilters(FormGroup):

    id = "top-filters"
    action = "/update_data"
    method="POST"

    children = [
        Radio(
            values=["Employee", "Team"],
            name='profile_type',
            hx_get='/update_dropdown',
            hx_target='#selector'
            ),
        ReportDropdown(
            id="selector",
            name="user-selection")
        ]
    
# Create a subclass of CombinedComponents
# called `Report`
#### YOUR CODE HERE
class Report(CombinedComponent):
    # Set the `children`
    # class attribute to a list
    # containing initialized instances 
    # of the header, dashboard filters,
    # data visualizations, and notes table
    #### YOUR CODE HERE
    children = [Header(), DashboardFilters(), Visualizations(), NotesTable()]

# Initialize a fasthtml app 
#### YOUR CODE HERE
app = FastHTML()

# Initialize the `Report` class
#### YOUR CODE HERE
report = Report()


# Create a route for a get request
# Set the route's path to the root
#### YOUR CODE HERE
@app.get("/")
def home():
    # Call the initialized report
    # pass None and an instance
    # of the QueryBase class as arguments
    # Return the result
    #### YOUR CODE HERE
    # return "Hello world!"
    return report("1", Employee())

# Create a route for a get request
# Set the route's path to receive a request
# for an employee ID so `/employee/2`
# will return the page for the employee with
# an ID of `2`. 
# parameterize the employee ID 
# to a string datatype
#### YOUR CODE HERE
@app.get("/employee/{eid:str}")
def employee(eid:str):
    # Call the initialized report
    # pass the ID and an instance
    # of the Employee SQL class as arguments
    # Return the result
    #### YOUR CODE HERE
    return report(eid, Employee())

# Create a route for a get request
# Set the route's path to receive a request
# for a team ID so `/team/2`
# will return the page for the team with
# an ID of `2`. 
# parameterize the team ID 
# to a string datatype
#### YOUR CODE HERE
@app.get("/team/{tid:str}")
def team(tid:str):
    # Call the initialized report
    # pass the id and an instance
    # of the Team SQL class as arguments
    # Return the result
    #### YOUR CODE HERE
    return report(tid, Team())


# Keep the below code unchanged!
@app.get('/update_dropdown{r}')
def update_dropdown(r):
    dropdown = DashboardFilters.children[1]
    print('PARAM', r.query_params['profile_type'])
    if r.query_params['profile_type'] == 'Team':
        return dropdown(None, Team())
    elif r.query_params['profile_type'] == 'Employee':
        return dropdown(None, Employee())


@app.post('/update_data')
async def update_data(r):
    from fasthtml.common import RedirectResponse
    data = await r.form()
    profile_type = data._dict['profile_type']
    id = data._dict['user-selection']
    if profile_type == 'Employee':
        return RedirectResponse(f"/employee/{id}", status_code=303)
    elif profile_type == 'Team':
        return RedirectResponse(f"/team/{id}", status_code=303)
    

serve()
