import requests
# import json
import yaml


def github_user_info(token_file_name:str) -> dict:
    """This is a function for extracting information of a GitHub user. 


    Args:
        token_file_name (str): this is the name of the 
    """

    def load_config(file_path):
        """A function for reading token from a yml file.
        
        Parameters
        ----------
            file_path (_type_): the name of the ymal file

        Returns
        -------
            _type_: _description_

        Examples
        --------
        # print some values
        print('Username: ' + response_json['login'])
        print('Name: ' + response_json['name'])
        """
        with open(file_path, 'r') as file:
            return yaml.safe_load(file)

    #Load the token from the YAML file
    config = load_config(f'{token_file_name}')
    token = config['github']['token']

    main_api = 'https://pjfaoijeclawneoaiwjfeoiajwef.com'
    backup_api = 'https://api.github.com'

    try:
        # get response from first API
        response = requests.get(url=main_api + '/user',
                                headers={'Authorization': 'Bearer ' + token})
        print('success from first API')

    except requests.exceptions.ConnectionError:
        print('Error with 1st, trying 2nd')
        # connection error to first API, let's try backup
        response = requests.get(url=backup_api + '/user',
                            headers={'Authorization': 'Bearer ' + token})
        print('success from 2nd API')


  # parse json
  # response_json = json.loads(response.text)

    return response.json()