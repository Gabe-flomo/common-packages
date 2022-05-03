import pandas as pd
import numpy as np



class Creator:
    
    def __init__(self, data, creator_id = None):
        self.creator_id = creator_id
        self.imports = data[data['creatorId'] == self.creator_id] if creator_id is not None else data
        self._projects = self.__get_projects(self.creator_data)


    @property
    def projects(self):
        '''
            returns all of the projects created by the creator (Cannot set to this property)
        '''
        return self._projects


    def __get_projects(self) -> dict:
        '''
            returns all of the creators projects as a dictionary of Project objects

            example
            ---
            ```
                {
                    'project_1': Project(),
                    'project_2': Project(),
                    'project_3': Project(),
                              ...
                    'project_N': Project()
                }
            ```
        '''
        pass


    @property
    def project_count(self) -> int:
        '''
            returns the count of the creators projects

            example
            ----
            ```
            count = creator.project_count
            print(count) -> 13
            ```
        '''
        pass
    
    
    @property
    def imported(self) -> pd.DataFrame:
        ''' 
            returns a DataFrame of all the packages this user has ever imported 

            

            Project 1
            --
            ```
            from random import randint
            import numpy
            import pandas as pd
            ```

            Project 2
            --
            ```
            import numpy as np
            from tensorflow import keras
            from tensorflow.keras import layers 
            ```

            Project 3
            --
            ```
            from sklearn import metrics
            import numpy as np
            import pandas as pd
            ```

            Returns: `[randint, numpy, pandas, keras, layers, metrics]`
            --
            
        '''


    @property
    def imports_count(self) -> pd.DataFrame:
        ''' 
            returns a DataFrame of each import and its number of occurences

            Example:
            --------

            ```
            {
                pandas: 444,
                numpy: 111,
                datetime: 222
            }
            ```
        '''
        pass

    
    @property
    def imports_from(self) -> pd.DataFrame:
        ''' returns a DataFrame of all of the packages this user has ever imported using the from keyword

            Example:
            -----------
            ```
            from numpy import random
            from sklearn.metrics import accuracy_score
            from sklearn import metrics
            imoprt pandas as pd

            return [
                {'from': 'numpy', 'import': 'random'},
                {'from': 'sklearn.metrics', 'import': 'accuracy_score'},
                {'from': 'sklearn', 'import': 'metrics'}
            ]
            ```
        '''
        pass

    
    @property
    def imported_from(self):
        ''' returns a Dataframe of all of the unique '''
        pass


    @property
    def packages(self):
        '''
            returns a list of the unique packages this creator has imported

            example
            ----
            ```
            import numpy
            from numpy import reshape
            import pandas as pd
            import sklearn.metrics
            from sklearn.utils import shuffle

            return [numpy, pandas, sklearn]
            ```


        '''


class Project:

    def __init__(self, project_id, data):
        self.project_id = project_id
        self._project_data = data[data['hexId'] == self.project_id]
        self.imports = self.project['import'].unique()


    def get_imports(self):
        pass


    @property
    def project(self):
        return self._project_data


    def generate_import_text(self):
        pass

    
class Dashboard:
    
    def __init__(self, creator: Creator):
        self.creator = creator


    