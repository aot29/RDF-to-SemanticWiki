'''
Created on 09.05.2016
A DAO Manager which doesn't persist, for testing.

@author: Alvaro.Ortiz
'''
from pyMwImportOWL.repository.Factory import Factory
from pyMwImportOWL.repository.Manager import Manager

class DummyDAOFactory( Factory ):
    '''
    A factory for testing. Create a normal factory and replace
    the manager object with a dummy manager
    '''

    def __init__(self):
        Factory.__init__( self, None )
        self._manager = DummyManager( None )


class DummyManager( Manager ):

    '''A dummy class for testing
    Values are stored in the value property, not saved to a back-end
    '''
    def commit(self, name, values):
        self.values = values