# >>one time only<<
# step 1: add wouterpotters to channels in anaconda
# Like this: https://docs.anaconda.com/anaconda/navigator/tutorials/manage-channels/
#
# step 2: install package castorapi
# like this: https://docs.anaconda.com/anaconda/navigator/tutorials/manage-packages/#installing-a-package
#
# step 1 and 2 combined:
# right click on the green arrow in environment, click run terminal
# run: `conda install -c wouterpotters castorapi` in the terminal

# store the secret and client files as described here:
# https://github.com/wouterpotters/castorapi/blob/master/README.md#usage

# now use the package
import castorapi

path_to_client_secret = r'C:/path/to/api_secret_a' # FORWARD SLASHES! OR \\ for each backward slash

c = castorapi.CastorApi(path_to_client_secret) # e.g. in user dir outside of GIT repo
    
# get study ID for Parkinson study
c.select_study_by_name('parkinson') # change name to match study name in castor    
    
### STEP 0: collect answer options from optiongroups
    
# get answer option groups for multiple choice questions
df_answeroptions_struct = c.request_study_export_optiongroups()
    
# get the main study structure (i.e. questions)
df_study_structure = c.request_study_export_structure()

# filter unused columns from df_study_structure, sort fields
df_study_structure = df_study_structure \
    .filter(['Form Type', 'Form Collection Name',
        'Form Collection Order', 'Form Name', 'Form Order',
        'Field Variable Name', 'Field Label', 'Field ID', 'Field Type',
        'Field Order', 'Calculation Template',
        'Field Option Group'],axis=1) \
    .sort_values(['Form Order','Form Collection Name','Form Collection Order','Field Order']) # sort on form collection order and field order (this matches how data is filled)

# export data
df_study_data = c.request_study_export_data()