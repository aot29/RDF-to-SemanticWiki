'''
Created on 17.05.2016

@author: Alvaro.Ortiz
'''
<<<<<<< HEAD
from pyMwImportOWL.repository.AbstractManager import AbstractManager
=======
from pyMwImportOWL.mediawikiDAO.AbstractManager import AbstractManager
>>>>>>> branch 'master' of https://github.com/AlvaroOrtizTroncoso/mwImportOWL.git

class Manager( AbstractManager ):
    _connector = None
    
    def __init__(self, connector ):
        self._connector = connector
    
    
    def commit(self, key, value):
        '''
        Commit the operation in this case using MediaWiki API
        @param key: a string corresponding to a page name
        @param value: a string corresponding to page contents in markdown
        '''
        self._connector.createPage( key, value )
